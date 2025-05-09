import streamlit as st
from agent_utils import get_search_results

# Page config
st.set_page_config(
    page_title="GenAI Search Agent",
    page_icon="🔎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS for modern look
st.markdown("""
    <style>
    body {
        background-color: #0f0f0f;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        padding: 3rem 2rem;
        background-color: #121212;
        border-radius: 1rem;
        box-shadow: 0 0 15px rgba(0,0,0,0.5);
    }
    input {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
        border: 1px solid #444 !important;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #00b894;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        margin-top: 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #00cec9;
        transform: scale(1.02);
    }
    .stMarkdown, .stSuccess, .stWarning {
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Main UI
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("## 🤖 Ask GenAI Search Agent")
st.markdown("Type your query below and get instant intelligent results using Tavily AI search:")

query = st.text_input(" ", placeholder="e.g. What are the latest trends in Generative AI?")

if st.button("🔍 Search"):
    if query.strip():
        with st.spinner("🧠 Thinking... Searching the web..."):
            response = get_search_results(query)
        st.success("✅ Here's what I found:")
        st.markdown(f"<div style='padding:1rem;background-color:#1e1e1e;border-radius:10px;'>{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a query before searching.")
        
st.markdown("</div>", unsafe_allow_html=True)
