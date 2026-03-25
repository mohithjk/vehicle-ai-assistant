import streamlit as st
import requests
import wikipedia
from news import fetch_news


# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Vehicle AI", layout="wide")

API_KEY = "3133069d3283440caaaca3768228426b"  # 🔑 add your key

# =========================
# CSS (PREMIUM UI)
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

.card {
    padding: 20px;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.1);
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.03);
    box-shadow: 0 0 25px rgba(56,189,248,0.4);
}

.stButton>button {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    border: none;
    font-weight: bold;
}

.chat-box {
    background-color: #020617;
    padding: 12px;
    border-radius: 10px;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🚗 Vehicle AI")
menu = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📰 Updates", "📚 Info", "🤖 AI Chat", "🏁 Motorsports"]
)

# =========================
# HOME
# =========================
if menu == "🏠 Home":
    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.title("🚗 Vehicle AI Assistant")
        st.subheader("Smart Platform for Cars & Bikes")

        st.markdown("""
        <div class="card">
        🚀 Explore the future of vehicles<br><br>
        • Live car & bike updates<br>
        • Search any vehicle info<br>
        • AI assistant (coming soon)
        </div>
        """, unsafe_allow_html=True)

# =========================
# NEWS
# =========================
elif menu == "📰 Updates":
    st.title("📰 Latest Vehicle News")

    news = fetch_news()

    if news:
        for article in news:
            st.markdown(f"""
            <div class="card">
            <h4>{article['title']}</h4>
            <p>{article['desc']}</p>
            <a href="{article['url']}" target="_blank">Read more →</a>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ No news available")

# =========================
# WIKIPEDIA INFO
# =========================
elif menu == "📚 Info":
    st.title("📚 Vehicle Information")

    query = st.text_input("Search any car or bike")

    if query:
        try:
            import wikipedia

            wikipedia.set_lang("en")  # force English

            result = wikipedia.search(query)

            if result:
                page = wikipedia.page(result[0])
                st.write(page.summary[:500])  # first 500 chars
            else:
                st.write("No results found")

        except Exception as e:
            st.write("Error:", e)
# =========================
# CHAT
# =========================
elif menu == "🤖 AI Chat":
    st.title("🤖 Vehicle Chat Assistant")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    user_input = st.text_input("Ask something...")

    if st.button("Send"):
        if user_input:
            st.session_state.chat.append(("You", user_input))
            st.session_state.chat.append(("AI", "AI response coming soon 🚀"))

    for sender, msg in st.session_state.chat:
        st.markdown(f"""
        <div class="chat-box">
        <b>{sender}:</b> {msg}
        </div>
        """, unsafe_allow_html=True)

# =========================
# MOTORSPORTS
# =========================
elif menu == "🏁 Motorsports":
    st.title("🏁 Motorsports Hub")

    sport = st.selectbox(
        "Choose Motorsport",
        ["Formula 1", "MotoGP", "Rally Racing"]
    )

    # =========================
    # FORMULA 1
    # =========================
    if sport == "Formula 1":
        st.header("🏎️ Formula 1")

        st.image("https://images.unsplash.com/photo-1549924231-f129b911e442")

        st.markdown("""
        <div class="card">
        <b>What is Formula 1?</b><br><br>
        Formula 1 is the highest class of international racing for open-wheel single-seater cars.
        It features cutting-edge technology, high-speed tracks, and elite drivers.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <b>Key Facts:</b><br><br>
        • Top speed: ~350 km/h<br>
        • Teams: Ferrari, Mercedes, Red Bull<br>
        • Drivers compete worldwide in circuits<br>
        </div>
        """, unsafe_allow_html=True)

        # NEWS
        st.subheader("📰 Latest Updates")

        url = f"https://newsapi.org/v2/everything?q=Formula 1&apiKey={API_KEY}"
        res = requests.get(url).json()

        if res["status"] == "ok":
            for article in res["articles"][:3]:
                st.markdown(f"""
                <div class="card">
                <b>{article['title']}</b><br>
                {article['description']}<br>
                <a href="{article['url']}">Read more</a>
                </div>
                """, unsafe_allow_html=True)

    # =========================
    # MOTOGP
    # =========================
    elif sport == "MotoGP":
        st.header("🏍️ MotoGP")

        st.image("https://images.unsplash.com/photo-1558981403-c5f9899a28bc")

        st.markdown("""
        <div class="card">
        <b>What is MotoGP?</b><br><br>
        MotoGP is the premier motorcycle racing championship in the world.
        It features high-performance bikes and top riders competing globally.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <b>Key Facts:</b><br><br>
        • Bikes reach speeds over 350 km/h<br>
        • Brands: Yamaha, Ducati, Honda<br>
        • Extreme cornering & racing skills required<br>
        </div>
        """, unsafe_allow_html=True)

        # NEWS
        st.subheader("📰 Latest Updates")

        url = f"https://newsapi.org/v2/everything?q=MotoGP&apiKey={API_KEY}"
        res = requests.get(url).json()

        if res["status"] == "ok":
            for article in res["articles"][:3]:
                st.markdown(f"""
                <div class="card">
                <b>{article['title']}</b><br>
                {article['description']}<br>
                <a href="{article['url']}">Read more</a>
                </div>
                """, unsafe_allow_html=True)

    # =========================
    # RALLY
    # =========================
    elif sport == "Rally Racing":
        st.header("🚙 Rally Racing")

        st.image("https://images.unsplash.com/photo-1503376780353-7e6692767b70")

        st.markdown("""
        <div class="card">
        <b>What is Rally Racing?</b><br><br>
        Rally racing takes place on public or private roads with modified cars.
        It includes dirt, snow, and gravel tracks.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <b>Key Facts:</b><br><br>
        • Drivers race against the clock<br>
        • Extreme terrains<br>
        • Co-driver gives directions<br>
        </div>
        """, unsafe_allow_html=True)

        # NEWS
        st.subheader("📰 Latest Updates")

        url = f"https://newsapi.org/v2/everything?q=rally racing&apiKey={API_KEY}"
        res = requests.get(url).json()

        if res["status"] == "ok":
            for article in res["articles"][:3]:
                st.markdown(f"""
                <div class="card">
                <b>{article['title']}</b><br>
                {article['description']}<br>
                <a href="{article['url']}">Read more</a>
                </div>
                """, unsafe_allow_html=True)

                