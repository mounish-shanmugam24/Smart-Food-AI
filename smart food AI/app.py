import streamlit as st

st.set_page_config(page_title="Smart Food AI", layout="wide")

custom_css = """
<style>
    /* Main App Background - Green */
    .stApp { background-color: #4CAF50 !important; }
    
    /* Main App Text - Black */
    .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp span, .stApp li, .stApp label { 
        color: #000000 !important; 
        font-family: 'Helvetica Neue', sans-serif; 
    }
    
    /* Sidebar Background - Black */
    [data-testid="stSidebar"] { background-color: #000000 !important; }
    
    /* Sidebar Text - White */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label { 
        color: #FFFFFF !important; 
    }

    /* 🚨 REMOVE KEYBOARD_DOUBLE TEXT 🚨 */
    [data-testid="stSidebarNavSeparator"], [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    header { background-color: transparent !important; }
    header * { color: transparent !important; }

    /* Feature Box Styling */
    .feature-box {
        background-color: #81C784 !important;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #000000;
        margin-bottom: 20px;
    }

    /* Button Styling */
    div[data-testid="stButton"] button {
        background-color: #000000 !important; 
        border-radius: 8px !important;
    }
    div[data-testid="stButton"] button * {
        color: #FFFFFF !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.title("Smart Food AI")
st.write("Select a module from the sidebar to begin.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-box">
        <h3>Nutrition Mode</h3>
        <p>Upload food for instant macro and health analysis.</p>
    </div>
    <div class="feature-box">
        <h3>AI Chef</h3>
        <p>Generate recipes and have them read aloud to you.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h3>Food Analyzer</h3>
        <p>Detect cooking methods and hidden health risks.</p>
    </div>
    <div class="feature-box">
        <h3>Restaurant Finder</h3>
        <p>Locate healthy food options near your location.</p>
    </div>
    """, unsafe_allow_html=True)