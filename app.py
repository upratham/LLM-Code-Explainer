import os
import re
import gradio as gr
from openai import OpenAI
from  dotenv import load_dotenv
import time

load_dotenv(override=True)
# Hugging Face Inference Router (OpenAI-compatible)
# Docs show OpenAI SDK + base_url=https://router.huggingface.co/v1 + HF_TOKEN
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],  # set this as a Space Secret
)

# Pick a chat-completion capable model from the HF playground/docs.
# Example from HF docs:
DEFAULT_MODEL = os.environ.get("HF_MODEL", "meta-llama/Llama-3.2-3B-Instruct")

system_prompt = """You are a technical explainer and problem-solver.
Your job is to answer the user’s technical question with a clear, accurate explanation that matches their skill level.

Guidelines:
- Start with a short direct answer.
- Then explain the concept step-by-step in plain language.
- Use a small example when helpful (code, command, or pseudo-code).
- Call out assumptions and edge cases.
"""

def get_question_user_prompt(question: str) -> str:
    return "Please explain what this code does and why:\n\n" + question

def looks_like_code(s: str) -> bool:
    s = s.strip()
    if not s:
        return False

    patterns = [
        r"```",                          # fenced code blocks
        r"^\s{4,}\S",                    # indented lines (4+ spaces)
        r"\b(def|class|import|from|if|elif|else|for|while|try|except|with|return|print)\b",
        r"[(){}\[\];]",                  # code punctuation
        r"==|!=|<=|>=|:=|\+=|-=|\*=|/=|//=|\*\*",
        r":\s*$",                        # line ending with colon (Python blocks)
        r"#",                            # comment
    ]

    score = sum(bool(re.search(p, s, re.MULTILINE)) for p in patterns)
    if score >= 2:
        likely_code=True
    else:
        likely_code=False

    return likely_code

def generate_code_explainer(message,history):
    history=[{"role":h['role'],"content":h['content']}for h in history]
    if looks_like_code(message)==True:
        relative_system_promt=system_prompt
        relative_user_prompt=get_question_user_prompt(message)
    else:
        relative_system_promt='You are an polite helpful Technical assistant to help learners'
        relative_user_prompt=message
        
    
    stream = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[{"role": "system", "content": relative_system_promt}] +history+
          [{"role": "user", "content": relative_user_prompt}],
        stream=True  # streanms one by one in chunks (parts)
    )    
    response = ""

    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
     
        yield response
        time.sleep(0.05)
   

demo = gr.ChatInterface(fn=generate_code_explainer, title="Code Explainer")

if __name__ == "__main__":
    demo.launch(share=True)
