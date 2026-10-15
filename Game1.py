import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)

# ---------------- SESSION STATE ----------------

if "num" not in st.session_state:
    st.session_state.num = random.randint(1, 200)

if "tries" not in st.session_state:
    st.session_state.tries = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "message" not in st.session_state:
    st.session_state.message = "I'm thinking of a number... 🤔"

if "last_guess" not in st.session_state:
    st.session_state.last_guess = 0


# ---------------- CSS ----------------

st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #888;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 18px;
    background-color: #f5f5f5;
    border: 1px solid #ddd;
    text-align: center;
}

.big-number {
    font-size: 40px;
    font-weight: bold;
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
    '<div class="title">🎯 Number Guessing Game</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Guess the secret number between 1 and 200!</div>',
    unsafe_allow_html=True
)


# ---------------- SCORE CARDS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="card">
            <h4>🎯 Range</h4>
            <div class="big-number">1-200</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="card">
            <h4>🔢 Tries</h4>
            <div class="big-number">{st.session_state.tries}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="card">
            <h4>📍 Last Guess</h4>
            <div class="big-number">
                {st.session_state.last_guess if st.session_state.last_guess else "-"}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# ---------------- GAME OVER ----------------

if st.session_state.game_over:

    st.balloons()

    st.success("🎉 CONGRATULATIONS! YOU FOUND THE NUMBER!")

    st.markdown(
        f"""
        <div class="result">
            🏆 You Won!<br><br>
            Secret Number: {st.session_state.num}<br>
            Total Tries: {st.session_state.tries}
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🔄 Play Again", use_container_width=True):

        st.session_state.num = random.randint(1, 200)
        st.session_state.tries = 0
        st.session_state.game_over = False
        st.session_state.message = "I'm thinking of a number... 🤔"
        st.session_state.last_guess = 0

        st.rerun()

    st.stop()


# ---------------- MESSAGE ----------------

st.info(st.session_state.message)


# ---------------- INPUT ----------------

st.subheader("🔢 Enter Your Guess")

guess = st.number_input(
    "Choose a number",
    min_value=1,
    max_value=200,
    value=100,
    step=1
)


# ---------------- GUESS BUTTON ----------------

if st.button("🎯 Check My Guess", use_container_width=True):

    st.session_state.tries += 1
    st.session_state.last_guess = guess

    if guess == st.session_state.num:

        st.session_state.message = "🎉 Perfect! You guessed it!"

        st.session_state.game_over = True

    elif guess > st.session_state.num:

        st.session_state.message = "⬇️ Go a bit LOWER!"

    else:

        st.session_state.message = "⬆️ Go a bit HIGHER!"

    st.rerun()


# ---------------- PROGRESS ----------------

st.write("")

st.subheader("🎮 How to Play")

st.write("""
1. Secret number **1 to 200** ke beech hai.
2. Apna guess enter karo.
3. Game batayega **Higher ⬆️** ya **Lower ⬇️**.
4. Kam se kam tries me number guess karo! 🔥
""")


# ---------------- RESET ----------------

if st.button("🔄 Reset Game", use_container_width=True):

    st.session_state.num = random.randint(1, 200)
    st.session_state.tries = 0
    st.session_state.game_over = False
    st.session_state.message = "I'm thinking of a number... 🤔"
    st.session_state.last_guess = 0

    st.rerun()