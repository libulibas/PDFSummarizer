# PDFSummarizer

Reads a PDF and returns a concise summary with key points and takeaways.

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env  # add your ANTHROPIC_API_KEY
```

## Usage

```bash
python pdf_summarizer.py document.pdf
```

## Model

`claude-sonnet-4-20250514` via the Anthropic Python SDK.

## License

MIT
