import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os
import re  # <-- We import this to clean the text!

st.set_page_config(page_title="AI Chef", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #FFEB3B !important; }
    .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp span, .stApp li, .stApp label { color: #000000 !important; }
    
    [data-testid="stSidebar"] { background-color: #000000 !important; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label { color: #FFFFFF !important; }

    /* Text Input Background Fix */
    .stTextInput>div>div>input { background-color: #FFFFFF !important; color: #000000 !important; border: 1px solid #000000 !important; }

    /* 🚨 THE BUTTON FIX 🚨 */
    div[data-testid="stButton"] button { background-color: #000000 !important; border-radius: 8px !important; }
    div[data-testid="stButton"] button * { color: #FFFFFF !important; }
</style>
""", unsafe_allow_html=True)

st.title("Voice-Activated AI Chef")
st.write("Type what you want to cook and get an audio recipe.")

api_key = os.environ.get("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

dish = st.text_input("What do you want to cook? (e.g., Healthy Chicken Curry)")
preference = st.selectbox("Dietary Preferences", ["None", "Vegetarian", "High Protein", "Low Carb"])

if st.button("Generate Recipe and Audio"):
    if dish and api_key:
        with st.spinner("Chef is writing your recipe..."):
            prompt = f"Write a short, step-by-step recipe for {dish}. Preference: {preference}. Keep the steps concise and easy to hear. Do not use complex symbols."
            response = model.generate_content(prompt)
            recipe_text = response.text
            
            # 1. Print the nicely formatted text to the screen
            st.header("Your Recipe")
            st.markdown(recipe_text)
            
            with st.spinner("Generating Voice Audio..."):
                # 2. Clean the text strictly for the audio engine
                # This removes asterisks, hashes, underscores, and colons.
                audio_text = re.sub(r'[*#_:]', '', recipe_text)
                
                # We replace hyphens with a space so it doesn't say "dash"
                audio_text = audio_text.replace('-', ' ')
                
                # 3. Generate the audio using the cleaned text
                tts = gTTS(text=audio_text, lang='en', tld='co.uk')
                tts.save("recipe.mp3")
                
                st.header("Listen to Instructions")
                st.audio("recipe.mp3", format="audio/mp3")