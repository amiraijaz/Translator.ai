import streamlit as st
from translator_utils import translate, get_gTTS_language_code
from gtts import gTTS
import os

st.set_page_config(
    page_title="Translator.AI",
    page_icon="languages.png",
    layout="centered"
)

# Streamlit page title
col3, col4 = st.columns([1, 4])  # Adjust column width ratios for better layout

with col3: 
    st.image("languages.png", width=120) 

with col4: 
    st.title("Translator.ai App - GPT-4o")

col1, col2 = st.columns(2)

with col1:
    input_languages_list = [
        "English", "French", "German", "Latin", "Spanish", "Urdu", "Punjabi", "Sindhi", 
        "Arabic", "Chinese", "Japanese", "Korean", "Italian", "Portuguese", "Russian", 
        "Dutch", "Swedish", "Greek", "Turkish", "Hindi", "Bengali", "Persian", "Tamil", 
        "Telugu", "Gujarati", "Marathi", "Kannada", "Malayalam", "Hebrew", "Polish", 
        "Czech", "Hungarian", "Danish", "Finnish", "Norwegian", "Ukrainian", "Thai", 
        "Vietnamese", "Indonesian", "Malay", "Romanian", "Bulgarian", "Slovak", "Serbian", 
        "Croatian", "Bosnian", "Filipino", "Swahili", "Zulu", "Amharic", "Somali", 
        "Yoruba", "Hausa", "Xhosa", "Kazakh", "Azerbaijani", "Armenian", "Georgian", 
        "Mongolian", "Uzbek", "Tajik", "Kyrgyz", "Pashto", "Tigrinya", "Shona", 
        "Albanian", "Lithuanian", "Latvian", "Estonian", "Icelandic", "Irish", 
        "Welsh", "Basque", "Galician", "Catalan"
    ]
     
    input_language = st.selectbox(label="Input Language", options=input_languages_list)

with col2: 
    output_languages_list = [x for x in input_languages_list if x != input_language]
    output_language = st.selectbox(label="Output Language", options=output_languages_list)

# Text area for user input
input_text = st.text_area("Type the text to be translated")

# Add the Translate button below the text area
if st.button("Translate"):
    translated_text = translate(input_language, output_language, input_text)
    st.success(translated_text)

# Button for generating translated speech
if st.button("Generate Translated Audio"):
    if input_text:
        translated_text = translate(input_language, output_language, input_text)
        gTTS_language_code = get_gTTS_language_code(output_language)  # Get the correct language code for gTTS
        tts = gTTS(text=translated_text, lang=gTTS_language_code)
        tts.save("speech.mp3")
        st.audio("speech.mp3", format="audio/mp3")
    else:
        st.warning("Please enter text to speak.")
