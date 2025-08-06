import streamlit as st
from googletrans import Translator

st.set_page_config(page_title="AI Translator", layout="centered")

st.title("🌐 Real-Time AI Translator App")

text_input = st.text_area("Enter Text to Translate:", "")

target_language = st.selectbox(
    "Select Target Language:",
    ('bn', 'en', 'hi', 'fr', 'de', 'es', 'ja', 'zh-cn', 'ar', 'ru')
)

translator = Translator()

if st.button("Translate"):
    if text_input.strip() != "":
        translated = translator.translate(text_input, dest=target_language)
        st.success(f"Translated Text:\n{translated.text}")
    else:
        st.warning("Please enter some text to translate.")
