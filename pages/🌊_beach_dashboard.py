import streamlit as st
import pandas as pd
import requests
import json
import plotly.express as px
import streamlit.components.v1 as components

# ---------------------------
# API Keys from Secrets
# ---------------------------
OPENWEATHER_API_KEY = st.secrets["OPENWEATHER_API_KEY"]
MAPBOX_TOKEN = st.secrets["MAPBOX_TOKEN"]

# ---------------------------
# Weather Data
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
# Tide Data
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

# ---------------------------
# Tide Summary
# ---------------------------
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
# Beach Data with Images, Description, Fun Facts, Visitor Info
# ---------------------------
beaches = {
    "Santa Monica Pier": {
        "lat": 34.0100, "lon": -118.4950, "station": "9410840",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
        "description": "Iconic pier with amusement park, aquarium, and stunning views of the Pacific Ocean.",
        "fun_facts": ["Home to Pacific Park amusement park.", "Featured in numerous movies and TV shows."],
        "visitor_info": {"Dogs Allowed": "No", "Parking": "Paid parking lot", "Beach Hours": "6:00 AM - 10:00 PM"}
    },
    "Venice Beach": {
        "lat": 33.9850, "lon": -118.4695, "station": "9410840",
        "image": "https://images.unsplash.com/photo-1544215729-3e0ee4c2d3b6?w=1200&h=400&fit=crop",
        "description": "Famous for its bohemian spirit, street performers, and skate park.",
        "fun_facts": ["Venice Boardwalk is 2 miles long.", "Known for Muscle Beach outdoor gym."],
        "visitor_info": {"Dogs Allowed": "Yes, on leash", "Parking": "Street and paid lots", "Beach Hours": "6:00 AM - 10:00 PM"}
    },
    "Malibu Surfrider Beach": {
        "lat": 34.0360, "lon": -118.6880, "station": "9410840",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
        "description": "World-renowned surf spot with historic pier and mellow waves.",
        "fun_facts": ["Home to the Surfrider Foundation.", "Perfect for beginner and intermediate surfers."],
        "visitor_info": {"Dogs Allowed": "No", "Parking": "Limited street parking", "Beach Hours": "6:00 AM - Sunset"}
    },
    "Huntington Beach": {
        "lat": 33.6595, "lon": -117.9988, "station": "9411270",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
        "description": "Known as 'Surf City USA' with long sandy beaches and surf culture.",
        "fun_facts": ["Hosts the US Open of Surfing.", "The pier is 1,850 feet long."],
        "visitor_info": {"Dogs Allowed": "No", "Parking": "Paid lots & street", "Beach Hours": "6:00 AM - 10:00 PM"}
    },
    "Newport Beach": {
        "lat": 33.6189, "lon": -117.9290, "station": "9411340",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
        "description": "Popular destination for boating, beaches, and the Balboa Fun Zone.",
        "fun_facts": ["Balboa Pier and Fun Zone are main attractions.", "Harbor is one of the largest recreational harbors."],
        "visitor_info": {"Dogs Allowed": "Yes, on leash", "Parking": "Paid lots", "Beach Hours": "6:00 AM - 10:00 PM"}
    },
    "Laguna Beach": {
        "lat": 33.5427, "lon": -117.7854, "station": "9411340",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&h=400&fit=crop",
        "description": "Artistic beach town with tide pools, coves, and galleries.",
        "fun_facts": ["Famous for Pageant of the Masters.", "Many tide pools to explore at low tide."],
        "visitor_info": {"Dogs Allowed": "Yes, on leash", "Parking": "Paid lots & street", "Beach Hours": "6:00 AM - Sunset"}
    }
}

# ---------------------------
# Streamlit Page Setup
# ---------------------------
st.title("🌊 California Beach Safety Dashboard")

if "hazard_reports" not in st.session_state:
    st.session_state["hazard_reports"] = []

# ---------------------------
# Beach Selection
# ---------------------------
selected_beach = st.selectbox("Select Beach:", list(beaches.keys()))
beach_coords = beaches[selected_beach]

# ---------------------------
# Beach Image and Info
# ---------------------------
st.image(beach_coords["image"], use_container_width=True, caption=selected_beach)
st.subheader(f"About {selected_beach}")
st.write(beach_coords["description"])

with st.expander("🌟 Fun Facts"):
    for fact in beach_coords["fun_facts"]:
        st.markdown(f"- {fact}")

with st.expander("📍 Visitor Information"):
    for key, value in beach_coords["visitor_info"].items():
        st.markdown(f"**{key}:** {value}")

# ---------------------------
# Weather Metrics (fixed truncation)
# ---------------------------
st.subheader(f"🏖️ {selected_beach} Overview")
weather = get_weather_data(beach_coords["lat"], beach_coords["lon"])
cols = st.columns(3)
cols[0].metric(label="🌡 Temperature", value=f"{weather['Temperature (°F)']} °F")
cols[1].metric(label="☀ Weather", value=weather["Weather"])
cols[2].metric(label="🕶 UV Index", value=weather["UV Index"])

# ---------------------------
# Tide Summary and Chart
# ---------------------------
st.subheader("🌊 Tide Forecast (Next 24 Hours)")
tide_df = get_tide_data(beach_coords["station"])
if not tide_df.empty:
    tide_summary = summarize_tides(tide_df)
    if not tide_summary.empty:
        st.markdown("**🕒 Upcoming High and Low Tides**")
        st.table(tide_summary)
    else:
        st.info("No high/low tide points found for today.")
    
    tide_df['Tide (ft)'] = tide_df['Tide (ft)'].round(2)
    with st.expander("📈 Show Tide Graph"):
        fig = px.line(
            tide_df.head(24),
            x='t',
            y='Tide (ft)',
            title="Tide Levels - Next 24 Hours",
            markers=True
        )
        fig.update_layout(
            xaxis_title="Time",
            yaxis_title="Tide Height (ft)",
            xaxis_tickformat="%I:%M %p",
            template="plotly_white",
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No tide data available for this beach.")

# ---------------------------
# Hazard Reporting
# ---------------------------
st.subheader("📢 Report a Hazard")
st.markdown(
    "Click anywhere on the map to report a hazard directly. "
    "You can enter types like Jellyfish, Broken glass, High surf, or Trash."
)

# ---------------------------
# Map Section
# ---------------------------
hazard_data_json = json.dumps(st.session_state["hazard_reports"])
show_directions = st.checkbox("Show Directions", key="directions_toggle")

components.html(f"""
<head>
    <link href='https://api.mapbox.com/mapbox-gl-js/v1.12.0/mapbox-gl.css' rel='stylesheet' />
    <script src='https://api.mapbox.com/mapbox-gl-js/v1.12.0/mapbox-gl.js'></script>
    <script src='https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-directions/v4.1.0/mapbox-gl-directions.js'></script>
    <link rel='stylesheet' href='https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-directions/v4.1.0/mapbox-gl-directions.css' />
</head>
<body>
    <div id='map' style='width:100%; height:650px;'></div>
    <script>
        mapboxgl.accessToken = '{MAPBOX_TOKEN}';

        navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {{
            enableHighAccuracy: true
        }});

        function successLocation(position) {{
            setupMap([position.coords.longitude, position.coords.latitude])
        }}

        function errorLocation() {{
            setupMap([{
