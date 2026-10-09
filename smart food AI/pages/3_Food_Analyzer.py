import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

st.set_page_config(page_title="Food Diagnostics", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #FF9800 !important; }
    .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp span, .stApp li, .stApp label { color: #000000 !important; }
    
    [data-testid="stSidebar"] { background-color: #000000 !important; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label { color: #FFFFFF !important; }

    /* 🚨 THE BUTTON FIX 🚨 */
    div[data-testid="stButton"] button { background-color: #000000 !important; border-radius: 8px !important; }
    div[data-testid="stButton"] button * { color: #FFFFFF !important; }
</style>
""", unsafe_allow_html=True)

st.title("Food Diagnostics Analyzer")
st.write("Upload a photo to detect cooking methods and portion sizes.")

api_key = os.environ.get("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

# Fix: Added a label and collapsed it for accessibility
uploaded_file = st.file_uploader("Upload Food Scan", type=["jpg", "png"], label_visibility="collapsed")

if uploaded_file:
    image = Image.open(uploaded_file)
    # Fix: Changed to width="stretch" per latest 2026 update
    st.image(image, width="stretch")
    
    if st.button("Run Deep Scan"):
        with st.spinner("Detecting cooking methods and portions..."):
            prompt = """
            Act as a strict food inspector. Look at this image and output ONLY the following information. 
            You MUST format it as a vertical bulleted list, with each point on a completely new line:
            
            * **Detected Dish:** [Name]
            * **Likely Cooking Method:** [Fried / Grilled / Baked / Raw]
            * **Portion Size:** [Small / Medium / Large]
            * **Verdict:** [Too oily / Balanced / Highly Processed]
            """
            
            response = model.generate_content([prompt, image])
            st.header("Scan Results")
            st.markdown(response.text)