import streamlit as st
import pandas as pd
import requests
import os

st.set_page_config(page_title="Restaurant Finder", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #F44336 !important; }
    .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp span, .stApp li, .stApp label { color: #000000 !important; }
    
    [data-testid="stSidebar"] { background-color: #000000 !important; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label { color: #FFFFFF !important; }
    
    /* Text Input Background Fix */
    .stTextInput>div>div>input { background-color: #FFFFFF !important; color: #000000 !important; border: 1px solid #000000 !important; }

    /* Restaurant Card Styling */
    .restaurant-card { background-color: #FFCDD2 !important; padding: 15px; border-radius: 10px; border-left: 5px solid #000000; margin-bottom: 15px; }
    .restaurant-title { color: #000000; font-size: 1.2rem; font-weight: bold; margin-bottom: 5px; }
    .restaurant-rating { color: #D32F2F; font-weight: bold; }
    .restaurant-address { color: #000000; font-size: 0.9rem; margin-bottom: 10px; }
    
    /* Map Directions Button */
    .directions-btn { background-color: #000000; color: #FFFFFF !important; padding: 8px 15px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; }
    .directions-btn:hover { background-color: #333333; }

    /* 🚨 THE BUTTON FIX 🚨 */
    div[data-testid="stButton"] button { background-color: #000000 !important; border-radius: 8px !important; }
    div[data-testid="stButton"] button * { color: #FFFFFF !important; }
</style>
""", unsafe_allow_html=True)

st.title("Smart Restaurant Finder")
st.write("Locate specific food options and get instant directions.")

gcp_key = os.environ.get("GCP_API_KEY")

if not gcp_key:
    st.warning("Please start the app with your GCP_API_KEY in the terminal to enable live maps.")
    st.stop()

col1, col2 = st.columns(2)
with col1:
    location = st.text_input("Enter area (e.g., Edgbaston, Birmingham)", value="Edgbaston")
with col2:
    craving = st.text_input("What are you craving?", value="South Indian restaurant")

if st.button("Search Live Map"):
    if location and craving:
        with st.spinner("Searching Google Places..."):
            search_query = f"{craving} in {location}"
            url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={search_query}&key={gcp_key}"
            
            response = requests.get(url)
            data = response.json()
            
            if data.get('status') == 'OK':
                results = data.get('results', [])
                
                map_points = []
                for place in results:
                    lat = place['geometry']['location']['lat']
                    lng = place['geometry']['location']['lng']
                    map_points.append({'lat': lat, 'lon': lng})
                
                df_map = pd.DataFrame(map_points)
                
                st.markdown("---")
                
                map_col, list_col = st.columns([1.2, 1])
                
                with map_col:
                    st.header("Area Map")
                    st.map(df_map, zoom=13, width="stretch")
                
                with list_col:
                    st.header("Top Results")
                    for place in results[:5]:
                        name = place.get('name', 'Unknown Name')
                        rating = place.get('rating', 'No rating')
                        address = place.get('formatted_address', 'No address provided')
                        
                        encoded_address = address.replace(" ", "+").replace(",", "")
                        directions_url = f"https://www.google.com/maps/dir/?api=1&destination={encoded_address}"
                        
                        card_html = f"""
                        <div class="restaurant-card">
                            <div class="restaurant-title">{name}</div>
                            <div class="restaurant-rating">⭐ Rating: {rating} / 5.0</div>
                            <div class="restaurant-address">{address}</div>
                            <a href="{directions_url}" target="_blank" class="directions-btn">Get Directions -></a>
                        </div>
                        """
                        st.markdown(card_html, unsafe_allow_html=True)
            else:
                st.error("Could not find any results. Try adjusting your search terms.")