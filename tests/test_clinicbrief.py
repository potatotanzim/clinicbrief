import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch, MagicMock
import clinicbrief as app

class Tests(unittest.TestCase):
    def test_escape_untrusted_html(self):
        page = app.render('<script>alert(1)</script>', 'en', 'Demo')
        self.assertNotIn('<script>', page)
        self.assertIn('&lt;script&gt;', page)

    def test_demo_never_calls_network_and_preserves_bangla(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'facts.md'
            source.write_text('বাংলা তথ্য', encoding='utf-8')
            with patch('urllib.request.urlopen', side_effect=AssertionError('Network forbidden')):
                self.assertEqual(app.main([str(source), '--demo', '--out', str(root/'out')]), 0)
            draft = next((root/'out').glob('*/draft.md'))
            self.assertIn('বাংলা তথ্য', draft.read_text())

    def test_api_request_and_response(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = json.dumps({
            'stop_reason': 'end_turn', 'content': [{'type':'text','text':'Draft'}]}).encode()
        with patch('urllib.request.urlopen', return_value=response) as call:
            self.assertEqual(app.generate('facts', 'bn', 'faq', 'test-model', 'test-key'), 'Draft')
            payload = json.loads(call.call_args.args[0].data)
            self.assertEqual(payload['model'], 'test-model')
            self.assertIn('Bangla', payload['messages'][0]['content'])

    def test_missing_configuration(self):
        with patch.dict('os.environ', {}, clear=True):
            self.assertEqual(app.main(['examples/clinic.md']), 1)

if __name__ == '__main__':
    unittest.main()
