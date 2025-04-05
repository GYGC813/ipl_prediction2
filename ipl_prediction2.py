import streamlit as st
import random

def predict_ipl_champion(city, color, vibe, player, time):
    city = city.lower()
    color = color.lower()
    vibe = vibe.lower()
    player = player.lower()
    time = time.lower()

    team = None

    # City-based matching
    if "mumbai" in city:
        team = "Mumbai Indians"
    elif "chennai" in city or "madras" in city:
        team = "Chennai Super Kings"
    elif "kolkata" in city:
        team = "Kolkata Knight Riders"
    elif "bangalore" in city or "bengaluru" in city:
        team = "Royal Challengers Bangalore"
    elif "hyderabad" in city:
        team = "Sunrisers Hyderabad"
    elif "delhi" in city or "new delhi" in city:
        team = "Delhi Capitals"
    elif "punjab" in city or "mohali" in city or "chandigarh" in city:
        team = "Punjab Kings"
    elif "rajasthan" in city or "jaipur" in city:
        team = "Rajasthan Royals"
    elif "lucknow" in city:
        team = "Lucknow Super Giants"
    elif "ahmedabad" in city or "gujarat" in city:
        team = "Gujarat Titans"

    # Color-based fallback
    if not team:
        if "blue" in color:
            team = random.choice(["Mumbai Indians", "Royal Challengers Bangalore", "Delhi Capitals"])
        elif "yellow" in color:
            team = "Chennai Super Kings"
        elif "red" in color:
            team = random.choice(["Sunrisers Hyderabad", "Punjab Kings"])
        elif "purple" in color:
            team = "Kolkata Knight Riders"
        elif "gold" in color:
            team = "Rajasthan Royals"

    # Vibe-based adjustments
    if "aggressive" in vibe:
        if team == "Chennai Super Kings":
            team = "Mumbai Indians"
        elif team == "Sunrisers Hyderabad":
            team = "Punjab Kings"
    elif "defensive" in vibe:
        if team in ["Punjab Kings", "Royal Challengers Bangalore"]:
            team = "Chennai Super Kings"
    elif "unpredictable" in vibe:
        team = random.choice(["Royal Challengers Bangalore", "Punjab Kings", "Rajasthan Royals"])

    # Player preference
    if "batsman" in player and team == "Chennai Super Kings":
        team = "Royal Challengers Bangalore"
    elif "bowler" in player and team == "Royal Challengers Bangalore":
        team = "Mumbai Indians"
    elif "all-rounder" in player:
        team = random.choice(["Chennai Super Kings", "Kolkata Knight Riders"])
    elif "wicket" in player:
        team = random.choice(["Delhi Capitals", "Rajasthan Royals"])

    # Time preference
    if "night" in time and team == "Sunrisers Hyderabad":
        team = "Kolkata Knight Riders"

    if not team:
        team = random.choice([
            "Mumbai Indians", "Chennai Super Kings", "Kolkata Knight Riders",
            "Royal Challengers Bangalore", "Sunrisers Hyderabad", "Delhi Capitals",
            "Punjab Kings", "Rajasthan Royals", "Lucknow Super Giants", "Gujarat Titans"
        ])
    
    return team

# Emojis for team fun
team_emojis = {
    "Mumbai Indians": "🔵",
    "Chennai Super Kings": "🟡",
    "Kolkata Knight Riders": "🟣",
    "Royal Challengers Bangalore": "🔴",
    "Sunrisers Hyderabad": "🧡",
    "Delhi Capitals": "🔷",
    "Punjab Kings": "❤️",
    "Rajasthan Royals": "👑",
    "Lucknow Super Giants": "🌟",
    "Gujarat Titans": "💎"
}

# Streamlit UI
st.set_page_config(page_title="IPL 2025 Champion Predictor", page_icon="🏏")
st.title("🏆 IPL 2025 Champion Predictor")
st.markdown("**Find out who your champion team is based on your vibes!**")

# Sidebar explanation
with st.sidebar:
    st.header("🧠 How it works")
    st.markdown(
        """
        This predictor uses your:
        - City preference
        - Favorite color
        - Current vibe
        - Preferred player type
        - Match time preference  
        
        to **guess** your IPL champion.  
        It's completely fun-based and random. Enjoy! 😄
        """
    )

# Main form
with st.form("predictor_form"):
    city = st.text_input("1. Which Indian city do you feel most connected to?")
    color = st.selectbox("2. What's your favorite color?", ["Blue", "Yellow", "Red", "Purple", "Gold"])
    vibe = st.selectbox("3. What's your current vibe?", ["Aggressive", "Balanced", "Defensive", "Unpredictable"])
    player = st.selectbox("4. What type of player do you prefer?", ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"])
    time = st.radio("5. Do you prefer day or night matches?", ["Day", "Night"])
    submitted = st.form_submit_button("🎯 Predict Champion")

if submitted:
    team = predict_ipl_champion(city, color, vibe, player, time)
    emoji = team_emojis.get(team, "🏏")
    st.success(f"🎉 Based on your vibes, the 2025 IPL Champion is **{team}** {emoji}")
    st.caption("_(Disclaimer: Just for fun and totally random 😄)_")
