import streamlit as st
import random
import os

# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="Avengers: Civil War",
    page_icon="⚔️",
    layout="wide"
)


# =========================
# CSS - GAME UI
# =========================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top, #252525 0%, #090909 45%, #000000 100%);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: 900;
    color: #ffcc00;
    text-shadow: 0px 0px 25px #ff6600;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    color: #bbbbbb;
    font-size: 20px;
    margin-bottom: 25px;
}

.team-card {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    min-height: 250px;
    box-shadow: 0px 0px 25px rgba(255,255,255,0.12);
}

.iron-card {
    background: linear-gradient(135deg, #7a0000, #d71919);
    border: 2px solid #ff4444;
}

.cap-card {
    background: linear-gradient(135deg, #00235c, #0757c9);
    border: 2px solid #3399ff;
}

.team-name {
    font-size: 30px;
    font-weight: 900;
}

.score {
    font-size: 45px;
    font-weight: 900;
}

.vs {
    text-align: center;
    font-size: 55px;
    font-weight: 1000;
    color: #ffcc00;
    text-shadow: 0px 0px 20px red;
    padding-top: 80px;
}

.battle-card {
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    min-height: 330px;
    box-shadow: 0px 0px 35px rgba(255,255,255,0.15);
}

.player-battle {
    background: linear-gradient(145deg, #520000, #d00000);
    border: 3px solid #ff3333;
}

.computer-battle {
    background: linear-gradient(145deg, #001d52, #0066cc);
    border: 3px solid #3399ff;
}

.character {
    font-size: 40px;
    font-weight: 900;
    margin-top: 15px;
}

.power {
    font-size: 65px;
    font-weight: 1000;
    color: #ffdd00;
    text-shadow: 0px 0px 15px #ff8800;
}

.power-label {
    color: #dddddd;
    font-size: 17px;
}

.ability {
    font-size: 18px;
    color: #ffffff;
    margin-top: 10px;
}

.result-win {
    background: linear-gradient(90deg, #003d00, #008000, #003d00);
    border: 2px solid #00ff55;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    font-size: 35px;
    font-weight: 900;
    box-shadow: 0px 0px 30px rgba(0,255,80,0.35);
}

.result-lose {
    background: linear-gradient(90deg, #420000, #990000, #420000);
    border: 2px solid #ff4444;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    font-size: 35px;
    font-weight: 900;
    box-shadow: 0px 0px 30px rgba(255,0,0,0.35);
}

.result-draw {
    background: linear-gradient(90deg, #3c3000, #806900, #3c3000);
    border: 2px solid #ffcc00;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    font-size: 35px;
    font-weight: 900;
}

.round-title {
    text-align: center;
    font-size: 28px;
    color: #ffffff;
    font-weight: 800;
}

.status-box {
    background: #111111;
    padding: 12px;
    border-radius: 12px;
    margin: 5px 0;
    border: 1px solid #333333;
}

</style>
""", unsafe_allow_html=True)


# =========================
# TEAMS
# =========================

iron_man_team = {
    "Iron Man": {"main": 5, "ability": 4, "emoji": "🤖"},
    "Vision": {"main": 5, "ability": 5, "emoji": "🔴"},
    "Black Panther": {"main": 4, "ability": 2, "emoji": "🐾"},
    "Spider-Man": {"main": 4, "ability": 2, "emoji": "🕷️"},
    "War Machine": {"main": 4, "ability": 3, "emoji": "⚙️"},
    "Black Widow": {"main": 3, "ability": 3, "emoji": "🕷️"}
}

captain_team = {
    "Captain America": {"main": 5, "ability": 4, "emoji": "🛡️"},
    "Scarlet Witch": {"main": 5, "ability": 5, "emoji": "🔮"},
    "Winter Soldier": {"main": 4, "ability": 2, "emoji": "❄️"},
    "Ant-Man": {"main": 4, "ability": 4, "emoji": "🐜"},
    "Falcon": {"main": 3, "ability": 3, "emoji": "🦅"},
    "Hawkeye": {"main": 3, "ability": 2, "emoji": "🏹"}
}


# =========================
# AUDIO FUNCTION
# =========================

def play_audio(file_name):
    if os.path.exists(file_name):

        with open(file_name, "rb") as audio_file:
            audio_bytes = audio_file.read()

        st.audio(
            audio_bytes,
            format="audio/mp3",
            autoplay=True
        )


# =========================
# SESSION STATE
# =========================

defaults = {
    "started": False,
    "game_over": False,
    "round": 1,

    "user_team_name": "",
    "computer_team_name": "",

    "user_score": 0,
    "computer_score": 0,

    "user_usage": {},
    "computer_usage": {},

    "user_ability": {},
    "computer_ability": {},

    "battle": None,
    "battle_finished": False,
    "last_sound": ""
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# =========================
# FUNCTIONS
# =========================

def reset_game():

    st.session_state.started = False
    st.session_state.game_over = False

    st.session_state.round = 1

    st.session_state.user_team_name = ""
    st.session_state.computer_team_name = ""

    st.session_state.user_score = 0
    st.session_state.computer_score = 0

    st.session_state.user_usage = {}
    st.session_state.computer_usage = {}

    st.session_state.user_ability = {}
    st.session_state.computer_ability = {}

    st.session_state.battle = None
    st.session_state.battle_finished = False
    st.session_state.last_sound = ""


def get_points(difference):

    if difference == 0:
        return 0

    elif difference == 1:
        return 4

    elif difference == 2:
        return 6

    elif difference == 3:
        return 8

    else:
        return 10


def get_available_characters(team, usage):

    available = []

    for character in team:

        if usage.get(character, 0) < 2:
            available.append(character)

    return available


# =========================
# TITLE
# =========================

st.markdown(
    '<div class="main-title">⚔️ AVENGERS: CIVIL WAR ⚔️</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Choose your side • Build your battle • Reach 100 points</div>',
    unsafe_allow_html=True
)


# =====================================================
# TEAM SELECTION
# =====================================================

if not st.session_state.started:

    st.markdown(
        "<h2 style='text-align:center;'>CHOOSE YOUR TEAM</h2>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="team-card iron-card">

        <div class="team-name">🔴 TEAM IRON MAN</div>

        <br>

        🤖 Iron Man<br>
        🔴 Vision<br>
        🐾 Black Panther<br>
        🕷️ Spider-Man<br>
        ⚙️ War Machine<br>
        🕷️ Black Widow

        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🔴 PLAY AS IRON MAN",
            use_container_width=True
        ):

            st.session_state.started = True
            st.session_state.user_team_name = "Iron Man"
            st.session_state.computer_team_name = "Captain America"

            st.rerun()

    with col2:

        st.markdown("""
        <div class="team-card cap-card">

        <div class="team-name">🔵 TEAM CAPTAIN AMERICA</div>

        <br>

        🛡️ Captain America<br>
        🔮 Scarlet Witch<br>
        ❄️ Winter Soldier<br>
        🐜 Ant-Man<br>
        🦅 Falcon<br>
        🏹 Hawkeye

        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🔵 PLAY AS CAPTAIN AMERICA",
            use_container_width=True
        ):

            st.session_state.started = True
            st.session_state.user_team_name = "Captain America"
            st.session_state.computer_team_name = "Iron Man"

            st.rerun()

    st.stop()


# =========================
# TEAM DATA
# =========================

if st.session_state.user_team_name == "Iron Man":

    user_team = iron_man_team
    computer_team = captain_team

    user_color = "🔴"
    computer_color = "🔵"

else:

    user_team = captain_team
    computer_team = iron_man_team

    user_color = "🔵"
    computer_color = "🔴"


# =========================
# SCORE BOARD
# =========================

st.markdown(
    f'<div class="round-title">⚔️ ROUND {st.session_state.round} / 12 ⚔️</div>',
    unsafe_allow_html=True
)

score1, vs_score, score2 = st.columns([4, 2, 4])

with score1:

    st.markdown(
        f"""
        <div class="team-card iron-card">

        <div class="team-name">
        {user_color} {st.session_state.user_team_name}
        </div>

        <div class="score">
        {st.session_state.user_score}
        </div>

        POINTS

        </div>
        """,
        unsafe_allow_html=True
    )

with vs_score:

    st.markdown(
        """
        <div class="vs">
        VS
        </div>
        """,
        unsafe_allow_html=True
    )

with score2:

    st.markdown(
        f"""
        <div class="team-card cap-card">

        <div class="team-name">
        {computer_color} {st.session_state.computer_team_name}
        </div>

        <div class="score">
        {st.session_state.computer_score}
        </div>

        POINTS

        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# GAME OVER
# =====================================================

if st.session_state.game_over:

    if st.session_state.user_score > st.session_state.computer_score:

        st.markdown(
            """
            <div class="result-win">
            🏆 YOU WON THE CIVIL WAR! 🏆
            </div>
            """,
            unsafe_allow_html=True
        )

        play_audio("win.mp3")

    elif st.session_state.user_score < st.session_state.computer_score:

        st.markdown(
            """
            <div class="result-lose">
            💥 COMPUTER WON THE CIVIL WAR 💥
            </div>
            """,
            unsafe_allow_html=True
        )

        play_audio("lose.mp3")

    else:

        st.markdown(
            """
            <div class="result-draw">
            🤝 THE CIVIL WAR ENDED IN A DRAW
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    final1, final2 = st.columns(2)

    with final1:

        st.metric(
            st.session_state.user_team_name,
            st.session_state.user_score
        )

    with final2:

        st.metric(
            st.session_state.computer_team_name,
            st.session_state.computer_score
        )

    st.write("")

    if st.button(
        "🔄 PLAY AGAIN",
        use_container_width=True
    ):

        reset_game()
        st.rerun()

    st.stop()


# =====================================================
# BATTLE RESULT SCREEN
# =====================================================

if st.session_state.battle_finished:

    battle = st.session_state.battle

    user_char = battle["user_char"]
    computer_char = battle["computer_char"]

    user_data = user_team[user_char]
    computer_data = computer_team[computer_char]

    user_power = battle["user_power"]
    computer_power = battle["computer_power"]

    points = battle["points"]

    st.markdown(
        "<h2 style='text-align:center;'>🔥 BATTLE RESULT 🔥</h2>",
        unsafe_allow_html=True
    )

    left, middle, right = st.columns([4, 2, 4])

    with left:

        ability_text = ""

        if battle["user_used_ability"]:
            ability_text = "⚡ SPECIAL ABILITY USED"

        st.markdown(
            f"""
            <div class="battle-card player-battle">

            <div class="power-label">
            {user_color} YOUR FIGHTER
            </div>

            <div class="character">
            {user_data["emoji"]}<br>
            {user_char}
            </div>

            <div class="power">
            {user_power}
            </div>

            <div class="power-label">
            BATTLE POWER
            </div>

            <div class="ability">
            {ability_text}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with middle:

        st.markdown(
            """
            <div class="vs">
            ⚡<br>
            VS<br>
            ⚡
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        ability_text = ""

        if battle["computer_used_ability"]:
            ability_text = "⚡ SPECIAL ABILITY USED"

        st.markdown(
            f"""
            <div class="battle-card computer-battle">

            <div class="power-label">
            {computer_color} COMPUTER FIGHTER
            </div>

            <div class="character">
            {computer_data["emoji"]}<br>
            {computer_char}
            </div>

            <div class="power">
            {computer_power}
            </div>

            <div class="power-label">
            BATTLE POWER
            </div>

            <div class="ability">
            {ability_text}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # RESULT

    if user_power > computer_power:

        st.markdown(
            f"""
            <div class="result-win">
            🏆 {user_char} WINS!<br>
            +{points} POINTS
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.session_state.last_sound != "win":

            play_audio("win.mp3")
            st.session_state.last_sound = "win"

    elif computer_power > user_power:

        st.markdown(
            f"""
            <div class="result-lose">
            💥 {computer_char} WINS!<br>
            +{points} POINTS
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.session_state.last_sound != "lose":

            play_audio("lose.mp3")
            st.session_state.last_sound = "lose"

    else:

        st.markdown(
            """
            <div class="result-draw">
            🤝 DRAW!<br>
            0 POINTS
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # CHECK GAME END

    if (
        st.session_state.user_score >= 100
        or st.session_state.computer_score >= 100
        or st.session_state.round >= 12
    ):

        st.session_state.game_over = True

        st.write("")

        if st.button(
            "🏆 SHOW FINAL RESULT",
            use_container_width=True
        ):

            st.rerun()

    else:

        if st.button(
            "⚔️ NEXT ROUND",
            use_container_width=True
        ):

            st.session_state.round += 1
            st.session_state.battle = None
            st.session_state.battle_finished = False
            st.session_state.last_sound = ""

            st.rerun()

    st.stop()


# =====================================================
# CHARACTER SELECTION
# =====================================================

st.markdown(
    "<h2 style='text-align:center;'>SELECT YOUR FIGHTER</h2>",
    unsafe_allow_html=True
)

available_user = get_available_characters(
    user_team,
    st.session_state.user_usage
)

if len(available_user) == 0:

    st.session_state.game_over = True
    st.rerun()


character = st.selectbox(
    "Choose Character",
    available_user,
    key=f"character_{st.session_state.round}"
)


# =========================
# CHARACTER INFO
# =========================

data = user_team[character]

usage = st.session_state.user_usage.get(character, 0)
ability_used = st.session_state.user_ability.get(character, False)

info1, info2, info3 = st.columns(3)

with info1:

    st.metric(
        "Main Power",
        data["main"]
    )

with info2:

    st.metric(
        "Ability Power",
        "+" + str(data["ability"])
    )

with info3:

    st.metric(
        "Used",
        f"{usage}/2"
    )


# =========================
# ABILITY
# =========================

use_ability = False

if ability_used:

    st.warning(
        f"⚠️ {character} ki special ability already use ho chuki hai."
    )

else:

    use_ability = st.checkbox(
        f"⚡ Use {character}'s Special Ability (+{data['ability']})",
        key=f"ability_{st.session_state.round}_{character}"
    )


# =========================
# CHARACTER STATUS
# =========================

with st.expander("📋 Character Status"):

    for char in user_team:

        used = st.session_state.user_usage.get(char, 0)
        ability = st.session_state.user_ability.get(char, False)

        if used >= 2:

            status = "❌ 2/2"

        else:

            status = f"🟢 {used}/2"

        ability_status = "❌ Used" if ability else "⚡ Ready"

        st.markdown(
            f"""
            <div class="status-box">
            <b>{user_team[char]["emoji"]} {char}</b>
            &nbsp;&nbsp; {status}
            &nbsp;&nbsp; Ability: {ability_status}
            </div>
            """,
            unsafe_allow_html=True
        )


# =====================================================
# START BATTLE
# =====================================================

if st.button(
    "⚔️ START BATTLE",
    use_container_width=True
):

    # COMPUTER CHARACTER

    available_computer = get_available_characters(
        computer_team,
        st.session_state.computer_usage
    )

    computer_char = random.choice(available_computer)

    computer_data = computer_team[computer_char]

    # COMPUTER ABILITY

    computer_used_ability = False

    computer_ability_ready = not st.session_state.computer_ability.get(
        computer_char,
        False
    )

    if computer_ability_ready:

        computer_used_ability = random.choice(
            [True, False]
        )

    # USER POWER

    user_power = data["main"]

    if use_ability and not ability_used:

        user_power += data["ability"]

    # COMPUTER POWER

    computer_power = computer_data["main"]

    if computer_used_ability:

        computer_power += computer_data["ability"]

    # DIFFERENCE

    difference = abs(
        user_power - computer_power
    )

    points = get_points(difference)

    # WINNER SCORE

    if user_power > computer_power:

        st.session_state.user_score += points

    elif computer_power > user_power:

        st.session_state.computer_score += points

    # USAGE UPDATE

    st.session_state.user_usage[character] = (
        st.session_state.user_usage.get(character, 0) + 1
    )

    st.session_state.computer_usage[computer_char] = (
        st.session_state.computer_usage.get(computer_char, 0) + 1
    )

    # ABILITY UPDATE

    if use_ability and not ability_used:

        st.session_state.user_ability[character] = True

    if computer_used_ability:

        st.session_state.computer_ability[computer_char] = True

    # SAVE BATTLE

    st.session_state.battle = {
        "user_char": character,
        "computer_char": computer_char,

        "user_power": user_power,
        "computer_power": computer_power,

        "points": points,

        "user_used_ability": use_ability,
        "computer_used_ability": computer_used_ability
    }

    st.session_state.battle_finished = True

    st.session_state.last_sound = ""

    st.rerun()


# =========================
# BACKGROUND MUSIC
# =========================

if os.path.exists("background.mp3"):

    with open("background.mp3", "rb") as music:

        st.audio(
            music.read(),
            format="audio/mp3",
            autoplay=True
        )