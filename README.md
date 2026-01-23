# Code-Explainer (Local LLM with Ollama)

AI-powered **code explainer for students** that runs **locally** using **Ollama** (OpenAI-compatible endpoint) + the **OpenAI Python SDK** — with **streaming output** and an optional **Gradio chat UI**.

> ✅ No paid API required — inference runs on your machine.

---

## What this project does

- Explains code snippets in a clear, student-friendly way (via a dedicated *code-explainer* system prompt)
- Streams responses token-by-token (nice “live typing” effect)
- Uses Ollama’s **OpenAI-compatible** API (`/v1`) so the same OpenAI SDK code works locally
- Optional: launches a **Gradio ChatInterface** web UI that:
  - detects whether the user message “looks like code”
  - uses the code-explainer prompt for code, and a normal assistant prompt otherwise

---

## Prerequisites

- **Python 3.11+**
- **Ollama** installed and running
- Recommended: VS Code + Jupyter extension (or install Jupyter)

---

## 1) Install Ollama

### macOS
1. Download the `.dmg` from Ollama
2. Drag **Ollama.app** into **Applications**
3. Launch Ollama (it runs in the background)

### Windows
1. Download and install Ollama
2. Ollama runs in the background and exposes the API on `http://localhost:11434`

### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## 2) Start Ollama

On **macOS/Windows**, starting the Ollama app is usually enough.

On **Linux** (or if you want to run manually):

```bash
ollama serve
```

Verify the server is up (the notebook also does this check):

```bash
curl http://localhost:11434
```

---

## 3) Download (pull) a model

The notebook is configured for **Llama 3.2** by default:

```bash
ollama pull llama3.2
```

You can also pick a specific size/tag (example):

```bash
ollama pull llama3.2:3b
# ollama pull llama3.2:8b
```

List downloaded models:

```bash
ollama ls
```

---

## 4) Python setup

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

pip install openai gradio requests python-dotenv ipython
```

Optional (if you want Jupyter from terminal):

```bash
pip install jupyter
```

---

## 5) Run the notebook (core demo)

Open and run:

- `code_explainer.ipynb`

If you start Jupyter manually:

```bash
jupyter notebook
```

The notebook contains:
- a streaming “code explainer” function (renders incremental Markdown in the output cell)
- an optional Gradio UI section (see next step)

---

## 6) Configure Ollama endpoint + model (in the notebook)

In the notebook, set:

```python
OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL_LLAMA = "llama3.2"
```

> If you use a tagged model name (like `llama3.2:8b`), put that exact string in `MODEL_LLAMA`.

---

## 7) (Optional) Launch the Gradio Chat UI

The notebook includes a **“Adding UI using gradio”** section that launches a chat app:

```python
chat = gr.ChatInterface(fn=generate_code_explainer_ollama, title="Code Explainer")
chat.launch(share=True)
```

Notes:
- `share=True` creates a public Gradio link. If you want local-only, change to `share=False`.
- The UI streams model output using `yield` so you see responses as they are generated.

---

## Troubleshooting

### `Connection refused` / `Failed to connect to localhost:11434`

- Ollama isn’t running → start it (or run `ollama serve`)
- Port is different → update `OLLAMA_BASE_URL`

### `model not found`

- Download it first:

  ```bash
  ollama pull llama3.2
  ```

### Slow responses / high RAM usage

- Use a smaller model:

  ```bash
  ollama pull llama3.2:3b
  ```

---

## Notes

This project uses the OpenAI Python SDK pointed at Ollama’s local OpenAI-compatible endpoint (`http://localhost:11434/v1`) and enables streaming responses.

---

## Author

**Prathamesh Uravane**  
📧 [upratham2002@gmail.com](mailto:upratham2002@gmail.com)
