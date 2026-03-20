import streamlit as st

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Vehicle AI Assistant",
    page_icon="🚗",
    layout="wide"
)

# -------------------------
# CUSTOM CSS (for styling)
# -------------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}

h1, h2, h3 {
    color: #00adb5;
}

.stButton>button {
    background-color: #00adb5;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #1f2937;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("🚗 Vehicle AI")
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📰 Updates", "🤖 AI Assistant", "🏁 Motorsports", "🔍 Explore"]
)

# -------------------------
# HOME
# -------------------------
if menu == "🏠 Home":
    st.title("🚗 Vehicle AI Assistant")
    st.subheader("Your smart companion for Cars & Bikes")

    st.markdown("""
    <div class="card">
    Welcome to your Vehicle AI platform 🚀<br><br>
    - Get latest updates 📰<br>
    - Ask anything 🤖<br>
    - Explore motorsports 🏁<br>
    - Discover vehicles 🔍
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# UPDATES
# -------------------------
elif menu == "📰 Updates":
    st.title("📰 Latest Updates")

    tab1, tab2 = st.tabs(["🚗 Cars", "🏍️ Bikes"])

    with tab1:
        st.markdown('<div class="card">🚗 New EV models launching soon</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">🚗 AI features in modern cars</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="card">🏍️ Electric bikes trending</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">🏍️ New sports bikes release</div>', unsafe_allow_html=True)

# -------------------------
# AI ASSISTANT
# -------------------------
elif menu == "🤖 AI Assistant":
    st.title("🤖 Ask Anything")

    user_input = st.text_input("Ask about cars or bikes:")

    if st.button("Get Answer"):
        st.info("⚡ AI response will appear here (connect backend later)")

# -------------------------
# MOTORSPORTS
# -------------------------
elif menu == "🏁 Motorsports":
    st.title("🏁 Motorsports World")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">🏎️ Formula Racing</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">🏍️ MotoGP</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">🚙 Rally Racing</div>', unsafe_allow_html=True)

# -------------------------
# EXPLORE (COOL SECTION)
# -------------------------
elif menu == "🔍 Explore":
    st.title("🔍 Explore Vehicles")

    option = st.selectbox(
        "Choose category",
        ["Best Mileage", "High Performance", "Budget Friendly"]
    )

    st.markdown(f"""
    <div class="card">
    Showing results for: <b>{option}</b><br><br>
    Data will be connected soon 🚀
    </div>
    """, unsafe_allow_html=True)