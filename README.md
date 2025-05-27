# 🤖 OpenRouter Chatbot (Streamlit + Python)

A simple chatbot app built with **Python** and **Streamlit**, powered by **OpenRouter.ai**.  
Users can input their **own API keys** and interact with advanced LLMs like GPT-3.5, Claude, and more.

---

## 🚀 Features

- 🔐 Secure: Users enter their **own OpenRouter API key**
- 🧠 Powered by models like `gpt-3.5-turbo`, `Claude`, `LLaMA`, etc.
- ⚡ Fast, interactive chat UI built with Streamlit
- 🔄 Easily switch models by changing a single line

---

## 🧱 Requirements

- Python 3.9+
- Streamlit
- Requests

---

## 🛠️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/Mutahir-15/openrouter-chatbot.git
cd openrouter-chatbot
```

## 🛠️ Installation

```
uv venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install Dependencies

```
uv pip install -r requirements.txt
```
**Or manually**:
```
uv pip install streamlit requests
```

## 🔑 Get Your OpenRouter API Key

- Go to [https://openrouter.ai](https://openrouter.ai/)
- Sign in with Google
- Navigate to Account → API Keys
- Generate a new API key and copy it

## 🧠 Run the Chatbot
```
streamlit run chatbot.py
```

Happy chatting! 
