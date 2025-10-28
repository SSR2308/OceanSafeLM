import streamlit as st
import pandas as pd
import requests
import json
import plotly.express as px
import streamlit.components.v1 as components

# ---------------------------
# API Keys
# ---------------------------
OPENWEATHER_API_KEY = st.secrets["OPENWEATHER_API_KEY"]
MAPBOX_TOKEN = st.secrets["MAPBOX_TOKEN"]

# ---------------------------
# Weather Function
# ---------------------------
def get_weather_data(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=imperial"
    res = requests.get(url)
    data = res.json()
    return {
        "Temperature (°F)": round(data["main"]["temp"], 2),
        "Weather": data["weather"][0]["description"].title(),
        "UV Index": "Check local UV forecast"
    }

# ---------------------------
# Tide Functions
# ---------------------------
def get_tide_data(station_id="9410840"):
    url = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
    params = {
        "station": station_id,
        "product": "predictions",
        "datum": "MLLW",
        "time_zone": "lst_ldt",
        "units": "english",
        "interval": "h",
        "format": "json",
        "date": "today"
    }
    try:
        res = requests.get(url, params=params, timeout=10)
        data = res.json()
        if "predictions" in data:
            df = pd.DataFrame(data['predictions'])
            df['t'] = pd.to_datetime(df['t'])
            df.rename(columns={'v': 'Tide (ft)'}, inplace=True)
            df['Tide (ft)'] = pd.to_numeric(df['Tide (ft)'], errors='coerce').round(2)
            return df
        else:
            st.warning(f"⚠ NOAA API returned no predictions for station {station_id}.")
            return pd.DataFrame(columns=['t', 'Tide (ft)'])
    except Exception as e:
        st.error(f"Failed to fetch tide data: {e}")
        return pd.DataFrame(columns=['t', 'Tide (ft)'])

def summarize_tides(tide_df):
    if tide_df.empty:
        return pd.DataFrame()
    df = tide_df.copy()
    df['diff'] = df['Tide (ft)'].diff().fillna(0)
    
    high_tides = df[(df['diff'] > 0) & (df['diff'].shift(-1) < 0)]
    low_tides = df[(df['diff'] < 0) & (df['diff'].shift(-1) > 0)]
    
    summary = pd.concat([
        pd.DataFrame({"Time": high_tides['t'], "Tide (ft)": high_tides['Tide (ft)'], "Type": "High Tide"}),
        pd.DataFrame({"Time": low_tides['t'], "Tide (ft)": low_tides['Tide (ft)'], "Type": "Low Tide"})
    ]).sort_values("Time")
    
    summary['Time'] = summary['Time'].dt.strftime("%I:%M %p")
    summary['Tide (ft)'] = summary['Tide (ft)'].round(2)
    return summary

# ---------------------------
# Beach Data (full)
# ---------------------------
beaches = {
    "Santa Monica Pier": {
        "lat": 34.0100, "lon": -118.4950, "station": "9410840",
        "image": "https://images.squarespace-cdn.com/content/v1/5e0e65adcd39ed279a0402fd/1627422658456-7QKPXTNQ34W2OMBTESCJ/1.jpg?format=2500w",
        "description": "An iconic landmark offering stunning ocean views, amusement rides, and family-friendly attractions.",
        "fun_facts": ["Opened in 1909.", "Home to Pacific Park.", "Featured in films & TV."],
        "visitor_info": {"Dogs Allowed": "No", "Parking": "Paid; free 8 PM–6 AM", "Beach Hours": "6 AM – 10 PM", "Nearby Amenities": "Restrooms, Food, Lifeguard Station"}
    },
    "Venice Beach": {
        "lat": 33.9850, "lon": -118.4695, "station": "9410840",
        "image": "https://drupal-prod.visitcalifornia.com/sites/default/files/styles/fluid_1920/public/VC_California101_VeniceBeach_Stock_RF_638340372_1280x640.jpg.webp?itok=emtWYsp9",
        "description": "Known for its bohemian spirit, street performers, and bustling boardwalk.",
        "fun_facts": ["Home to Muscle Beach.", "Venice Canals inspired by Italy.", "Popular filming location."],
        "visitor_info": {"Dogs Allowed": "Yes, on leash", "Parking": "Paid; free before 8 AM", "Beach Hours": "6 AM – 10 PM", "Nearby Amenities": "Skate Park, Food, Restrooms"}
    },
    "Malibu Surfrider Beach": {
        "lat": 34.0360, "lon": -118.6880, "station": "9410840",
        "image": "https://www.worldbeachguide.com/photos/large/malibu-beach-pier-lagoon.jpg",
        "description": "Famous for perfect waves and surf culture.",
        "fun_facts": ["Known as 'The First Point'.", "Part of Malibu Lagoon State Beach.", "Hosts surf competitions."],
        "visitor_info": {"Dogs Allowed": "No", "Parking": "Free, first-come-first-serve", "Beach Hours": "Sunrise to Sunset", "Nearby Amenities": "Lifeguard Station, Restrooms"}
    },
    "Huntington Beach": {
        "lat": 33.6595, "lon": -117.9988, "station": "9411270",
        "image": "https://www.redfin.com/blog/wp-content/uploads/2023/12/GettyImages-1812336731.jpg",
        "description": "World-famous for surfing.",
        "fun_facts": ["Hosts the US Open of Surfing.", "Pier extends 1,850 feet.", "Great for volleyball & events."],
        "visitor_info": {"Dogs Allowed": "No", "Parking": "Paid, free 8 PM–6 AM", "Beach Hours": "6 AM – 10 PM", "Nearby Amenities": "Lifeguard Station, Food, Restrooms"}
    },
    "Newport Beach": {
        "lat": 33.6189, "lon": -117.9290, "station": "9411340",
        "image": "https://static.independent.co.uk/2023/07/27/12/iStock-1210240213%20%281%29.jpg",
        "description": "Offers wide sandy beaches and a bustling harbor.",
        "fun_facts": ["Famous for Newport Harbor boating.", "Home to Balboa Fun Zone.", "Popular for whale watching."],
        "visitor_info": {"Dogs Allowed": "Yes, on leash", "Parking": "Paid", "Beach Hours": "6 AM – 10 PM", "Nearby Amenities": "Lifeguard Station, Food, Restrooms"}
    },
    "Laguna Beach": {
        "lat": 33.5427, "lon": -117.7854, "station": "9411340",
        "image": "https://cdn.britannica.com/37/189937-050-478BECD3/Night-view-Laguna-Beach-California.jpg",
        "description": "Known for art galleries, tide pools, and dramatic cliffs.",
        "fun_facts": ["Annual Pageant of the Masters.", "Famous for tide pools.", "Scenic coastal cliffs."],
        "visitor_info": {"Dogs Allowed": "Yes, on leash", "Parking": "Paid", "Beach Hours": "6 AM – 10 PM", "Nearby Amenities": "Restrooms, Food, Lifeguard Station"}
    }
}

# ---------------------------
# Page Setup & Sidebar
# ---------------------------
st.set_page_config(page_title="🌊 Ocean Safe", layout="wide")
if "hazard_reports" not in st.session_state:
    st.session_state["hazard_reports"] = []

# Sidebar
with st.sidebar:
    st.title("🌊 Ocean Safe Controls")
    selected_beach = st.selectbox("Select Beach:", list(beaches.keys()))
    show_directions = st.checkbox("Show Directions", key="directions_toggle")

beach_coords = beaches[selected_beach]

# ---------------------------
# Beach Info Card
# ---------------------------
st.markdown(f"""
<div style='background-color:#E0F7FA; padding:15px; border-radius:12px; margin-bottom:15px;'>
<h2 style='color:#0B3D91;'>About {selected_beach}</h2>
<img src="{beach_coords['image']}" width="100%" style="border-radius:10px; margin-bottom:10px;">
<p>{beach_coords['description']}</p>
</div>
""", unsafe_allow_html=True)

with st.expander("🌟 Fun Facts"):
    for fact in beach_coords["fun_facts"]:
        st.markdown(f"✅ {fact}")

with st.expander("📍 Visitor Information"):
    icons = {"Dogs Allowed":"🐶","Parking":"🅿️","Beach Hours":"⏰","Nearby Amenities":"🏖️"}
    for key, value in beach_coords["visitor_info"].items():
        st.markdown(f"{icons.get(key,'')} **{key}:** {value}")

# ---------------------------
# Weather Metrics
# ---------------------------
st.subheader(f"🏖️ {selected_beach} Weather & Conditions")
weather = get_weather_data(beach_coords["lat"], beach_coords["lon"])
cols = st.columns(3)
cols[0].metric("🌡 Temperature", f"{weather['Temperature (°F)']} °F")
cols[1].metric("☀ Weather", weather["Weather"])
cols[2].metric("🕶 UV Index", weather["UV Index"])

# ---------------------------
# Tide Summary & Chart
# ---------------------------
st.subheader("🌊 Tide Forecast (Next 24 Hours)")
tide_df = get_tide_data(beach_coords["station"])
if not tide_df.empty:
    tide_summary = summarize_tides(tide_df)
    if not tide_summary.empty:
        st.markdown("**🕒 Upcoming High and Low Tides**")
        st.table(tide_summary)

    with st.expander("📈 Show Tide Graph"):
        fig = px.line(tide_df.head(24), x='t', y='Tide (ft)', markers=True)
        fig.update_layout(template="plotly_white", xaxis_tickformat="%I:%M %p", yaxis_title="Tide Height (ft)")
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No tide data available.")

# ---------------------------
# Hazard Reporting & Map
# ---------------------------
st.subheader("📢 Report a Hazard")
st.markdown("Click on the map to add hazards (Jellyfish, Trash, High surf, etc.)")

hazard_data_json = json.dumps(st.session_state["hazard_reports"])
components.html(f"""
<div id='map' style='width:100%; height:650px; border-radius:12px;'></div>
<script src='https://api.mapbox.com/mapbox-gl-js/v1.12.0/mapbox-gl.js'></script>
<link href='https://api.mapbox.com/mapbox-gl-js/v1.12.0/mapbox-gl.css' rel='stylesheet' />
<script>
mapboxgl.accessToken = '{MAPBOX_TOKEN}';
navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {{ enableHighAccuracy: true }});

function successLocation(position) {{
    setupMap([position.coords.longitude, position.coords.latitude])
}}
function errorLocation() {{
    setupMap([{beach_coords['lon']}, {beach_coords['lat']}])
}}
function setupMap(center) {{
    const map = new mapboxgl.Map({{container:'map', style:'mapbox://styles/mapbox/streets-v11', center:center, zoom:14}});
    map.addControl(new mapboxgl.NavigationControl());
    const userMarker = new mapboxgl.Marker({{color:'blue'}}).setLngLat(center).addTo(map);

    navigator.geolocation.watchPosition(function(pos){{
        const lon=pos.coords.longitude; const lat=pos.coords.latitude;
        userMarker.setLngLat([lon, lat]);
        if(window.directions) {{ window.directions.setOrigin([lon, lat]); }}
    }}, function(err){{ console.error(err); }}, {{ enableHighAccuracy:true }});

    const hazards = {hazard_data_json};
    hazards.forEach(h => {{
        if(h.beach=="{selected_beach}") {{
            new mapboxgl.Marker({{color:'orange', opacity:0.8}})
                .setLngLat([h.lon,h.lat])
                .setPopup(new mapboxgl.Popup({{closeButton:true}}).setText(h.hazard))
                .addTo(map);
        }}
    }});

    map.on('click', function(e) {{
        const lat=e.lngLat.lat; const lon=e.lngLat.lng;
        const hazard=prompt("Enter hazard type:");
        if(hazard){{
            fetch("", {{method:"POST", headers:{{"Content-Type":"application/json"}}, body:JSON.stringify({{lat:lat, lon:lon, hazard:hazard, beach:"{selected_beach}"}})}});
            new mapboxgl.Marker({{color:'orange', opacity:0.8}}).setLngLat([lon, lat]).setPopup(new mapboxgl.Popup({{closeButton:true}}).setText(hazard)).addTo(map);
        }}
    }});

    {"window.directions = new MapboxDirections({accessToken: mapboxgl.accessToken, unit:'imperial', profile:'mapbox/walking'}); map.addControl(window.directions,'top-left'); window.directions.setDestination([" + str(beach_coords['lon']) + "," + str(beach_coords['lat']) + "]);" if show_directions else ""}
}}
</script>
""", height=650)

st.write("🟢 Blue marker = your live location. Click map to report hazards. Toggle 'Show Directions' for navigation.")
