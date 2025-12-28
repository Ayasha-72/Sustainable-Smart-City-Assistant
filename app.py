import streamlit as st
from chatbot import urban_chatbot
from summarizer import summarize_text
from eco_advisor import eco_tips
from dashboard import show_dashboard

st.set_page_config(
    page_title="Smart City Assistant",
    page_icon="🌿",
    layout="wide"
)

# -------------------- ADAPTIVE CSS --------------------
st.markdown("""
<style>
/* Light theme */
@media (prefers-color-scheme: light) {
    .stApp {
        background: linear-gradient(120deg, #e8f5e9, #c8e6c9, #f1f8e9);
        background-size: 300% 300%;
        animation: gradientBG 12s ease infinite;
        color: #1b5e20;
    }
    h1, h2, h3 {
        color: #1b5e20;
    }
    .glass {
        background: rgba(255, 255, 255, 0.65);
        color: #1b5e20;
        backdrop-filter: blur(12px);
        border-radius: 22px;
        padding: 35px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
        margin-bottom: 25px;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(#c8e6c9, #a5d6a7);
    }
    .stButton > button {
        background: linear-gradient(135deg, #2e7d32, #66bb6a);
        color: white;
    }
}

/* Dark theme */
@media (prefers-color-scheme: dark) {
    .stApp {
        background: linear-gradient(120deg, #1b2f23, #2e4d36, #1a3a29);
        background-size: 300% 300%;
        animation: gradientBG 12s ease infinite;
        color: #a5d6a7;
    }
    h1, h2, h3 {
        color: #a5d6a7;
    }
    .glass {
        background: rgba(30, 50, 40, 0.7);
        color: #c8e6c9;
        backdrop-filter: blur(12px);
        border-radius: 22px;
        padding: 35px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        margin-bottom: 25px;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(#2e4d36, #1b2f23);
    }
    .stButton > button {
        background: linear-gradient(135deg, #66bb6a, #2e7d32);
        color: white;
    }
}

/* Shared styles */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

input, textarea {
    border-radius: 12px !important;
}

.stButton > button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# -------------------- SESSION --------------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# -------------------- WELCOME PAGE --------------------
if st.session_state.page == "welcome":
    st.markdown("""
    <div class="glass">
        <h1>🌿 Sustainable Smart City Assistant</h1>
        <h3>AI-Powered Urban Intelligence Platform</h3>
        <p style="font-size:18px;">
            ✔ Solve urban problems using AI<br>
            ✔ Analyze city datasets visually<br>
            ✔ Summarize reports instantly<br>
            ✔ Get eco-friendly recommendations
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3,1,3])
    with col2:
        if st.button("🚀 Get Started"):
            st.session_state.page = "main"
            st.rerun()

# -------------------- MAIN APP --------------------
else:
    st.sidebar.title("🌱 Smart City Menu")

    option = st.sidebar.radio(
        "Select a module",
        ["Urban Chatbot", "Dashboard", "Summarizer", "Eco Tip Adviser"]
    )

    # -------- CHATBOT --------
    if option == "Urban Chatbot":
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.header("🤖 Urban Issue Chatbot")
        issue = st.text_input("Enter an urban problem (e.g., water pollution):")
        if st.button("Get Solutions") and issue:
            with st.spinner("Thinking like a city planner..."):
                st.success(urban_chatbot(issue))
        st.markdown('</div>', unsafe_allow_html=True)

    # -------- DASHBOARD --------
    elif option == "Dashboard":
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        show_dashboard()
        st.markdown('</div>', unsafe_allow_html=True)

    # -------- SUMMARIZER --------
    elif option == "Summarizer":
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.header("📝 Smart Summarizer")
        text = st.text_area("Paste content to summarize:", height=220)
        if st.button("Summarize") and text:
            with st.spinner("Creating concise summary..."):
                st.info(summarize_text(text))
        st.markdown('</div>', unsafe_allow_html=True)

    # -------- ECO ADVISOR --------
    elif option == "Eco Tip Adviser":
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.header("🌍 Eco Tip Adviser")
        topic = st.text_input("Enter topic (e.g., plastic waste):")
        if st.button("Get Eco Tips") and topic:
            with st.spinner("Generating eco-friendly tips..."):
                st.warning(eco_tips(topic))
        st.markdown('</div>', unsafe_allow_html=True)




