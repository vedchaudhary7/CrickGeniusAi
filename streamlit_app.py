import streamlit as st

st.set_page_config(page_title="CrickGenius AI", layout="wide")

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("🏏 CrickGenius AI")
menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "IPL Analytics",
        "International Analytics",
        "Player Rankings",
        "Head-to-Head",
        "Win Probability Simulator"
    ]
)

# ----------------------------
# Home Page
# ----------------------------
if menu == "Home":
    st.title("🏏 CrickGenius AI")
    st.subheader("Advanced Cricket Analytics Platform")

    st.write("Welcome to CrickGenius AI.")
    st.write("This platform provides cricket statistics, player analysis, and performance insights.")

    st.markdown("---")

    st.header("Project Overview")
    st.write("""
    CrickGenius AI is a data-driven cricket analytics application.
    It analyzes structured datasets to provide player rankings,
    team comparisons, and predictive simulations.
    """)

# ----------------------------
# IPL Section
# ----------------------------
elif menu == "IPL Analytics":
    st.header("📊 IPL Analytics")
    st.info("IPL data analytics will appear here.")

# ----------------------------
# International Section
# ----------------------------
elif menu == "International Analytics":
    st.header("🌍 International Cricket Analytics")
    st.info("International cricket statistics will appear here.")

# ----------------------------
# Player Ranking
# ----------------------------
elif menu == "Player Rankings":
    st.header("🥇 Player Ranking System")
    st.info("Player ranking algorithm will appear here.")

# ----------------------------
# Head to Head
# ----------------------------
elif menu == "Head-to-Head":
    st.header("🤝 Head-to-Head Comparison")
    st.info("Head-to-head team comparison will appear here.")

# ----------------------------
# Win Probability
# ----------------------------
elif menu == "Win Probability Simulator":
    st.header("🎯 Win Probability Simulator")

    team1 = st.text_input("Enter Team 1")
    team2 = st.text_input("Enter Team 2")

    if st.button("Simulate"):
        import random
        p1 = random.randint(40, 60)
        p2 = 100 - p1

        st.success(f"{team1}: {p1}% chance of winning")
        st.success(f"{team2}: {p2}% chance of winning")
