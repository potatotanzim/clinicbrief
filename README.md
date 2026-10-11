# ClinicBrief

Source-based English and Bangla communication drafts for small clinics.

ClinicBrief is a working Python CLI prototype for clinic website maintainers. It
turns approved public administrative information into FAQs, announcements or
website copy using the Claude Messages API, then exports Markdown and a printable
HTML review page. An offline mode packages source text for review without an API
key, translation, generated claims, or network access.

## Run in one minute

Requires Python 3.10 or newer. No third-party packages required.

```bash
python3 clinicbrief.py examples/clinic.md --demo
```

Open the printed `output/draft-.../review.html` path in your browser. Use its
Print / Save PDF button, or edit `draft.md`. Each run creates a new directory.
The bundled clinic is fictional; replace its facts with verified public details.

## Generate with Claude

Set the variables in your terminal. Choose a model ID available in your Claude
Console. The `.env.example` file documents variables but is not loaded automatically.

```bash
export ANTHROPIC_API_KEY='your-api-key'
export ANTHROPIC_MODEL='your-available-model-id'
python3 clinicbrief.py examples/clinic.md --language bn --kind faq
python3 clinicbrief.py examples/clinic.md --language en --kind announcement
```

Live mode sends the supplied source to Anthropic and incurs API charges. Keep
keys out of Git. Use only approved public clinic information, not patient records.
API reference: https://platform.claude.com/docs/en/api/messages/create

## Outputs

- `draft.md`: editable source-based draft (or unchanged source in offline mode).
- `review.html`: responsive, printable review sheet. Output is HTML-escaped.
- `metadata.json`: mode, model, language, requested format and source SHA-256.

Options: `--language en|bn`, `--kind faq|announcement|website`, `--out PATH`,
`--model MODEL`, `--demo`. Maximum input length: 24,000 characters.

## Scope and limitations

This is an administrative writing assistant, not a medical chatbot. It does not
diagnose, recommend treatment, book appointments, or publish automatically.
Claude is instructed to use only provided facts and flag missing details. Those
instructions are not a guarantee: a person must verify every generated draft,
including Bangla translations, before publishing. Offline mode does not translate
or reorganize text into the requested format.

Implemented: CLI, live API adapter, offline source review, English/Bangla language
selection, three draft formats, escaped HTML export, Markdown export, source
fingerprinting, error handling, tests and GitHub Actions configuration.

Not implemented: hosted SaaS, accounts, payments, live clinic integration or a
web editing interface. The live API adapter is covered with mocked tests; a
billable end-to-end request has not been verified in the creation environment.

## Development

```bash
python3 -m unittest discover -s tests -v
```

## Get the project

```bash
git clone https://github.com/potatotanzim/clinicbrief.git
cd clinicbrief
python3 clinicbrief.py examples/clinic.md --demo
```

## Accurate project description

ClinicBrief is an early-stage developer project for drafting English and Bangla
clinic communications from approved public source material. The prototype
integrates the Claude Messages API and exports drafts for human review.

Creating this project does not establish startup-program eligibility or promise
credits. Do not describe it as a deployed service, incorporated company, or
existing customer product unless that becomes true.

## License

MIT. See LICENSE.
