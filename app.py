import streamlit as st
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(page_title="Tirumalarao Kilari | AI Portfolio", page_icon="🤖", layout="wide")

# Custom CSS for Terminal Aesthetic
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ff41; font-family: 'Courier New', Courier, monospace; }
    .stMarkdown { color: #00ff41; }
    .css-10trblm { color: #00ff41; } /* Titles */
    section[data-testid="stSidebar"] { background-color: #000000; }
    .stButton>button { background-color: #00ff41; color: black; border-radius: 0px; border: none; }
    .stButton>button:hover { background-color: #008f11; color: white; }
    /* Horizontal Rule color */
    hr { border: 1px solid #00ff41; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("root@tirumala:~#")
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Skills", "Contact"],
        icons=["terminal", "code-slash", "cpu", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#000"},
            "icon": {"color": "#00ff41", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#111", "color": "#00ff41"},
            "nav-link-selected": {"background-color": "#222"},
        }
    )

# --- HOME SECTION ---
if selected == "Home":
    st.title("> INITIALIZING BIOGRAPHY...")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Tirumalarao Kilari")
        st.subheader("AI Agent Developer · Backend Engineer · LLM Systems Builder [cite: 1, 2]")
        st.write("""
        AI Engineer with hands-on experience designing and evaluating production-grade agentic systems. 
        I specialize in multi-stage pipelines, modular backend architectures, and autonomous RAG agents 
        featuring prompt injection safeguards[cite: 5, 6, 33].
        """)
        st.write("**Current Location:** Pflugerville, TX [cite: 3]")
        st.write("**Availability:** Immediate / Open to Remote [cite: 44]")
    
    with col2:
        st.code("""
        {
          "status": "Active",
          "focus": "Agentic Workflows",
          "learning": "LangGraph",
          "location": "USA"
        }
        """)

# --- PROJECTS SECTION ---
elif selected == "Projects":
    st.title("> EXECUTING PROJECTS.EXE")
    
    # Project 1: ResumeAI
    with st.expander("🚀 ResumeAI — Live Web Application", expanded=True):
        st.write("**Tech:** Python, Streamlit, Groq, BeautifulSoup, Render [cite: 23]")
        st.write("""
        - Built a multi-stage pipeline: URL scraping → job text extraction → skill gap analysis → resume rewriting → cover letter generation[cite: 25].
        - Features zero manual input after URL paste; handles PDF/DOCX resume parsing[cite: 25, 26].
        """)
        st.link_button("View Live App", "https://resumeai-v2.onrender.com")

    # Project 2: RAG PDF Chat Agent
    with st.expander("🧠 RAG PDF Chat Agent", expanded=False):
        st.write("**Tech:** Python, FAISS, Claude, FastAPI, pytest [cite: 31]")
        st.write("""
        - Developed an autonomous RAG agent with modular separation for ingestion, vector indexing, and retrieval[cite: 32].
        - Implemented **RAGAS-style evaluation** to measure citation rate and faithfulness[cite: 35].
        - Engineered prompt injection defenses to prevent authority escalation[cite: 33].
        """)
        st.link_button("View Source Code", "https://github.com/bizygoodz-web/rag-pdf-chat")

    # Project 3: Client Content Pipeline
    with st.expander("🏢 Multi-Stage AI Pipeline (Contract)", expanded=False):
        st.write("**Client:** Austinite Market [cite: 16]")
        st.write("""
        - Designed a pipeline: brief ingestion → prompt engineering → image generation → iterative refinement[cite: 17].
        - Validated real-world AI output quality in a live, non-mocked environment for storefront assets[cite: 20].
        """)

# --- SKILLS SECTION ---
elif selected == "Skills":
    st.title("> SCANNING SYSTEM_RESOURCES...")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### **AI & LLM Logic**")
        st.write("- LangGraph & LangChain [cite: 10]")
        st.write("- Multi-turn Interaction Design [cite: 5]")
        st.write("- Advanced Prompt Engineering (Claude, GPT-4, Gemini) [cite: 10, 42]")
        st.write("- RAGAS-style Eval Harnesses [cite: 14, 35]")

    with col_b:
        st.markdown("### **Backend & Retrieval**")
        st.write("- FastAPI & REST APIs [cite: 11, 34]")
        st.write("- Pydantic & Python (Primary) [cite: 11]")
        st.write("- FAISS & Vector Embedding Pipelines [cite: 12, 33]")
        st.write("- GitHub Actions (CI/CD) [cite: 13, 34]")

# --- CONTACT SECTION ---
elif selected == "Contact":
    st.title("> ESTABLISHING CONNECTION...")
    st.write("📫 **Email:** kilaritirumalarao@gmail.com [cite: 3]")
    st.write("🔗 **LinkedIn:** [linkedin.com/in/tirumalaraokilari-803829273](https://linkedin.com/in/tirumalaraokilari-803829273) [cite: 3]")
    st.write("🐙 **GitHub:** [github.com/bizygoodz-web](https://github.com/bizygoodz-web) [cite: 3, 44]")
    
    st.text_input("Enter your message to send to the terminal:")
    if st.button("Submit"):
        st.success("Message 'logged' to system console (Demo only).")

st.markdown("---")
st.caption("© 2026 Tirumalarao Kilari | Compiled with Streamlit & AI")