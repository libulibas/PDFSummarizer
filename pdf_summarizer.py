import os, sys
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
MODEL = "claude-sonnet-4-20250514"

def claude(prompt, system="", max_tokens=2000):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("Set ANTHROPIC_API_KEY (copy .env.example to .env).")
    c = Anthropic(api_key=key)
    kw = dict(model=MODEL, max_tokens=max_tokens,
              messages=[{"role": "user", "content": prompt}])
    if system:
        kw["system"] = system
    r = c.messages.create(**kw)
    return "".join(b.text for b in r.content if b.type == "text")



from pypdf import PdfReader

def summarize(pdf_path: str) -> str:
    text = "".join((p.extract_text() or "") for p in PdfReader(pdf_path).pages)
    text = text[:60000]
    sys_p = ("Summarize the document. Output: ## TL;DR, ## Key Points, "
             "## Takeaways.")
    return claude(f"Document text:\n{text}", system=sys_p, max_tokens=2000)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python pdf_summarizer.py <file.pdf>")
    print(summarize(sys.argv[1]))
