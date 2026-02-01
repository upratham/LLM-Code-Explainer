Here’s a **shorter README.md** you can paste into GitHub that also **shows your deployed Hugging Face Space** via a badge (and a clear demo link).

````md
# Code Explainer (Local LLM + Ollama) 🚀

AI-powered **code explainer for students** that can run **locally** using **Ollama** (OpenAI-compatible `/v1` endpoint) + the **OpenAI Python SDK**, with **streaming output** and a **Gradio chat UI**.

## Live Demo (Hugging Face Space)

[Open in Spaces]👉[//huggingface.co/spaces/upratham/code_explainer](https://aistudio.google.com/)

🔗 https://huggingface.co/spaces/upratham/code_explainer

## Features

- Student-friendly explanations for code snippets (via a dedicated system prompt)
- **Streaming** responses (live typing effect)
- Works with **Ollama’s OpenAI-compatible API** (`http://localhost:11434/v1`)
- **Gradio UI** that detects if the message looks like code and switches prompts automatically

## Repository Structure

- `app.py` — Hugging Face Space / Gradio app entrypoint
- `notebooks/` — original development notebook(s)

## Run Locally (Ollama)

### 1) Install + start Ollama
```bash
ollama serve
# in another terminal
ollama pull llama3.2
````

### 2) Create env + install deps

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install openai gradio requests python-dotenv
```

### 3) Configure model + endpoint (example)

Use these values in your code:

```python
OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL_LLAMA = "llama3.2"   # or "llama3.2:3b"
```

### 4) Run the app

```bash
python app.py
```

## Troubleshooting

* **Connection refused (localhost:11434):** Ollama isn’t running → start `ollama serve`
* **Model not found:** `ollama pull llama3.2`
* **Slow / high RAM:** try a smaller model, e.g. `llama3.2:3b`

## Author

**Prathamesh Uravane**
📧 [upratham2002@gmail.com](mailto:upratham2002@gmail.com)


