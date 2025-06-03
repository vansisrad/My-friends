import streamlit as st

# Page config
st.set_page_config(page_title="Hello Kitty Letters 💌", page_icon="🌸", layout="centered")

# Background music toggle
music_toggle = st.checkbox("🎵 Play Hello Kitty Music")

# New music URL (example: some calm piano music)
new_music_url = "https://www.fesliyanstudios.com/play-mp3/6645"  # Change this URL to your preferred music

# Inject background music with HTML (if toggle is on)
if music_toggle:
    st.markdown(
        f"""
        <audio autoplay loop>
            <source src="{new_music_url}" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        """,
        unsafe_allow_html=True
    )

# Cute header with all black text
st.markdown("""
    <div style='text-align: center; color: black;'>
        <h1>🌸 Hello Kitty Letters 💌</h1>
        <p style='font-size: 18px;'>Made with love by Vanshika for her second home 👩‍❤️‍💋‍👩</p>
        <p style='font-size: 30px;'>💖 〜(꒪꒳꒪)〜 💖</p>
    </div>
""", unsafe_allow_html=True)

# Decorative sparkle divider (make it black dashed line)
st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

# Ask user for their name
name = st.text_input("💌 Enter your name to receive your letter:", "")

# Messages for each friend (no color changes here since it's inside a div below)

letters = {
    # ... (same letters dict)
}

name_lower = name.lower().strip()

if name_lower in letters:
    st.markdown(f"""
        <div style='background-color: #ffe6f0; padding: 20px; border-radius: 20px; border: 2px solid black; color: black;'>
            <p style='font-size: 20px;'>{letters[name_lower]}</p>
            <p style='text-align: right;'>💖 Love, Vanshika</p>
        </div>
        <p style='font-size: 25px; text-align: center; color: black;'>🌸✨🌈💖✨🌸</p>
    """, unsafe_allow_html=True)
elif name != "":
    st.warning("Oops! I couldn’t find your name in my special Hello Kitty list 😿")

# Cute footer with black text
st.markdown("<br><center style='color: black;'>🌸 Powered by Streamlit x Hello Kitty ✨</center>", unsafe_allow_html=True)
