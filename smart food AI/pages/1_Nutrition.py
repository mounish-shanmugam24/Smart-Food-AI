import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

st.set_page_config(page_title="Nutrition Analyzer", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #2196F3 !important; }
    .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp span, .stApp li, .stApp label { color: #000000 !important; }
    
    [data-testid="stSidebar"] { background-color: #000000 !important; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label { color: #FFFFFF !important; }

    /* 🚨 THE BUTTON FIX 🚨 */
    div[data-testid="stButton"] button { background-color: #000000 !important; border-radius: 8px !important; }
    div[data-testid="stButton"] button * { color: #FFFFFF !important; }
</style>
""", unsafe_allow_html=True)

st.title("Nutrition Analyzer")
st.write("Upload a photo of your food or a nutrition label.")

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    st.warning("Please set your GOOGLE_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-pro')

# Fix: Added a label and collapsed it for accessibility
uploaded_file = st.file_uploader("Upload Food", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # Fix: Changed to width="stretch" per latest 2026 update
    st.image(image, caption="Uploaded Image", width="stretch")
    
    if st.button("Analyze Nutrition"):
        with st.spinner("Analyzing macros and health rating..."):
            prompt = """
            Analyze this food image. Provide:
            1. Estimated Calories
            2. Macro Breakdown (Protein, Carbs, Fats)
            3. Health Rating (Good, Moderate, Poor)
            4. Hidden Risks (e.g., High oil, High sugar)
            5. A healthier alternative swap.
            Format as a clean markdown list.
            """
            response = model.generate_content([prompt, image])
            st.header("Analysis Results")
            st.markdown(response.text)