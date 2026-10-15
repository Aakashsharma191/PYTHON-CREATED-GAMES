import streamlit as st
import random

# Page configuration
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

# ---------------- SESSION STATE ----------------

if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "com_score" not in st.session_state:
    st.session_state.com_score = 0

if "result" not in st.session_state:
    st.session_state.result = "Choose your move!"

if "user_choice" not in st.session_state:
    st.session_state.user_choice = ""

if "com_choice" not in st.session_state:
    st.session_state.com_choice = ""


# ---------------- CSS ----------------

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #888;
    margin-bottom: 30px;
}

.score-box {
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    background-color: #f5f5f5;
    border: 1px solid #ddd;
}

.score {
    font-size: 40px;
    font-weight: bold;
}

.choice-box {
    text-align: center;
    font-size: 22px;
    padding: 15px;
}

.result {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.markdown(
    '<div class="main-title">🎮 Rock Paper Scissors</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">First player to reach 5 points wins!</div>',
    unsafe_allow_html=True
)


# ---------------- SCORE ----------------

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div class="score-box">
            <h3>👤 YOU</h3>
            <div class="score">{st.session_state.user_score}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="score-box">
            <h3>🤖 COMPUTER</h3>
            <div class="score">{st.session_state.com_score}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# ---------------- GAME OVER ----------------

if st.session_state.user_score >= 5:

    st.success("🎉 CONGRATULATIONS! YOU WON THE GAME! 🏆")

    st.markdown(
        f"""
        <div class="result">
            👤 You {st.session_state.user_score}
            &nbsp;&nbsp; - &nbsp;&nbsp;
            🤖 Computer {st.session_state.com_score}
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🔄 Play Again", use_container_width=True):
        st.session_state.user_score = 0
        st.session_state.com_score = 0
        st.session_state.result = "Choose your move!"
        st.session_state.user_choice = ""
        st.session_state.com_choice = ""
        st.rerun()

    st.stop()


elif st.session_state.com_score >= 5:

    st.error("🤖 COMPUTER WON THE GAME! 😢")

    st.markdown(
        f"""
        <div class="result">
            👤 You {st.session_state.user_score}
            &nbsp;&nbsp; - &nbsp;&nbsp;
            🤖 Computer {st.session_state.com_score}
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🔄 Play Again", use_container_width=True):
        st.session_state.user_score = 0
        st.session_state.com_score = 0
        st.session_state.result = "Choose your move!"
        st.session_state.user_choice = ""
        st.session_state.com_choice = ""
        st.rerun()

    st.stop()


# ---------------- CHOICES ----------------

st.subheader("Choose your move 👇")

col1, col2, col3 = st.columns(3)

with col1:
    rock = st.button("🪨 Rock", use_container_width=True)

with col2:
    paper = st.button("📄 Paper", use_container_width=True)

with col3:
    scissors = st.button("✂️ Scissors", use_container_width=True)


# ---------------- GAME LOGIC ----------------

user = 0

if rock:
    user = 1

elif paper:
    user = 2

elif scissors:
    user = 3


if user != 0:

    com = random.randint(1, 3)

    choices = {
        1: "🪨 Rock",
        2: "📄 Paper",
        3: "✂️ Scissors"
    }

    st.session_state.user_choice = choices[user]
    st.session_state.com_choice = choices[com]

    if user == com:

        st.session_state.result = "🤝 It's a Draw!"

    elif (
        (user == 1 and com == 3) or
        (user == 2 and com == 1) or
        (user == 3 and com == 2)
    ):

        st.session_state.user_score += 1
        st.session_state.result = "🎉 You Won This Round!"

    else:

        st.session_state.com_score += 1
        st.session_state.result = "🤖 Computer Won This Round!"


# ---------------- ROUND RESULT ----------------

if st.session_state.user_choice:

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="choice-box">
                👤 <b>Your Choice</b><br>
                {st.session_state.user_choice}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="choice-box">
                🤖 <b>Computer Choice</b><br>
                {st.session_state.com_choice}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="result">
            {st.session_state.result}
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------- RESET ----------------

st.write("")

if st.button("🔄 Reset Game", use_container_width=True):

    st.session_state.user_score = 0
    st.session_state.com_score = 0
    st.session_state.result = "Choose your move!"
    st.session_state.user_choice = ""
    st.session_state.com_choice = ""

    st.rerun()