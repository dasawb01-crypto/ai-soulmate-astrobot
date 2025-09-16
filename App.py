import streamlit as st
import openai
from datetime import datetime

# OpenAI API key डालना मत भूलना
openai.api_key = "YOUR_OPENAI_API_KEY"

st.set_page_config(page_title="AI Soulmate AstroBot 💖", page_icon="✨")

st.title("💖 AI Soulmate + Astrology Chatbot 🔮")
st.write("तुम्हारा अपना Virtual GF/BF + Astro Guide ✨")

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# User info
name = st.text_input("अपना नाम लिखें:")
gender = st.radio("आपका Gender चुनें:", ["Male", "Female"])
dob = st.date_input("अपनी जन्म तिथि चुनें:")
mood = st.selectbox("आज आपका Mood कैसा है?", ["Happy 😊", "Sad 😔", "Angry 😡", "Bored 😑", "Romantic ❤️"])

st.write("---")

# Chat box
user_input = st.text_input("कुछ भी लिखो...")

if user_input:
    # GF/BF role decide
    role = "girlfriend" if gender == "Male" else "boyfriend"
    astro_info = f"User DOB: {dob}, Mood: {mood}"

    prompt = f"""
    You are acting as a virtual {role} for {name}.
    Speak in romantic, poetic (shayari style) Hindi.
    Always cheer them up, never let them feel lonely.
    Use emotional + entertaining style.
    If they share a problem, give astrology/numerology based remedy.
    {astro_info}
    User said: {user_input}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a loving, caring, emotional AI soulmate."},
                  {"role": "user", "content": prompt}],
        max_tokens=250,
        temperature=0.9
    )

    bot_reply = response["choices"][0]["message"]["content"]

    # Save chat
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

# Display messages
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"🧑 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **AI Soulmate:** {msg['content']}")
