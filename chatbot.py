# AI Chat Hub with OpenRouter and Streamlit
import requests
import streamlit as st
import json

# Set page configuration with dark theme
st.set_page_config(
    page_title="AI Chat Hub",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown(
    """
    <style>
    .stApp { background-color: #1a1a1a; color: #e0e0e0; }
    .stTextInput > div > div > input { background-color: #2a2a2a; color: #e0e0e0; }
    .stSelectbox > div > div > select { background-color: #2a2a2a; color: #e0e0e0; }
    .stButton>button { background-color: #333; color: #e0e0e0; border: none; }
    .stButton>button:hover { background-color: #444; }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar layout
st.sidebar.title("AI Chat Hub")
st.sidebar.write("Powered by **OpenRouter**")

# API Key input
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""
api_key = st.sidebar.text_input("OpenRouter API Key", type="password", value=st.session_state["api_key"])
if api_key:
    st.session_state["api_key"] = api_key

# Model selection (using only free, confirmed models)
model_options = {
    "Llama 3.1 8B (Free, Fast)": "meta-llama/llama-3.1-8b-instruct:free",
    "Mistral 7B (Free, Lightweight)": "mistralai/mixtral-8x7b-instruct:free",
    "Llama 4 Scout (Free, Long Context)": "meta-llama/llama-4-scout:free",
    "NVIDIA Nemotron Nano 8B (Free, Efficient)": "nvidia/llama-3.1-nemotron-nano-8b-v1:free",
    "DeepSeek V3 Base (Free, Technical)": "deepseek/deepseek-v3-base:free",
    "Mistral Small 3.1 24B (Free, Instruct)": "mistralai/mistral-small-3.1-24b-instruct:free"
}
selected_model = st.sidebar.selectbox("Select Model", options=list(model_options.keys()))
model_id = model_options[selected_model]

# Clear conversation button
if st.sidebar.button("Clear Conversation"):
    st.session_state.chat_history = []
    st.rerun()

# Main chat area
st.title("AI Chat Hub")
st.write("Connect to **OpenRouter** for diverse AI models.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
question = st.chat_input("Ask AI Chat Hub...")

# Process API request
if api_key and question:
    st.session_state.chat_history.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter-chatbot.streamlit.app/"
    }
    data = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": "You are an autonomous, helpful AI agent that provides concise, accurate, and natural responses to user queries about Agentic AI and related technologies."},
            *st.session_state.chat_history
        ],
        "max_tokens": 500  # Optional: Limit response length
    }

    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()  # Raises an HTTPError for bad responses
            reply = response.json()["choices"][0]["message"]["content"]
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)
        except requests.exceptions.HTTPError as e:
            error_detail = response.json() if "json" in dir(response) else str(e)
            st.error(f"API Error: {e}\nDetails: {json.dumps(error_detail, indent=2)}")
        except requests.exceptions.RequestException as e:
            st.error(f"Connection Error: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected Error: {str(e)}")
elif not api_key:
    st.info("Please enter your OpenRouter API key to start.")
elif not question:
    st.info("Type a message to start chatting.")