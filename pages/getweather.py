import streamlit as st
import pandas as pd
import requests
import json
import plotly.express as px
import streamlit.components.v1 as components

def get_weather_data(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=imperial"
    res = requests.get(url)
    data = res.json()
    return {
        "Temperature (°F)": round(data["main"]["temp"], 2),
        "Weather": data["weather"][0]["description"].title(),
        "UV Index": "Check local UV forecast"
    }

def get_tide_data(station_id="9410840"):
    """Fetch hourly tide predictions from NOAA and ensure rounding to 2 decimals."""
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
    """Find and summarize high and low tides for the day (rounded to 2 decimals)."""
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
# Beach Data
# ---------------------------
beaches = {
    "Santa Monica Pier": {"lat": 34.0100, "lon": -118.4950, "station": "9410840"},
    "Venice Beach": {"lat": 33.9850, "lon": -118.4695, "station": "9410840"},
    "Malibu Surfrider Beach": {"lat": 34.0360, "lon": -118.6880, "station": "9410840"},
    "Huntington Beach": {"lat": 33.6595, "lon": -117.9988, "station": "9411270"},
    "Newport Beach": {"lat": 33.6189, "lon": -117.9290, "station": "9411340"},
    "Laguna Beach": {"lat": 33.5427, "lon": -117.7854, "station": "9411340"},
}

# ---------------------------
# Streamlit Setup
# ---------------------------
st.set_page_config(page_title="OceanSafe", layout="wide", page_icon="🌊")

if "hazard_reports" not in st.session_state:
    st.session_state["hazard_reports"] = []

# ---------------------------
# Sidebar Navigation
# ---------------------------
page = st.sidebar.radio("Navigation", ["🏠 Home", "🌊 Beaches"])

# ---------------------------
# Home Page
# ---------------------------
if page == "🏠 Home":
    st.markdown("<h1 style='text-align: center; color: #0077b6;'>🌊 Welcome to OceanSafe</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #00b4d8;'>Stay safe, report hazards, and enjoy California beaches!</h3>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1500&q=80", use_column_width=True)

# ---------------------------
# Beaches Page
# ---------------------------
if page == "🌊 Beaches":
    st.title("🌊 California Beach Safety Dashboard")

    selected_beach = st.selectbox("Select Beach:", list(beaches.keys()))
    beach_coords = beaches[selected_beach]

    # Weather metrics
    st.subheader(f"🏖️ {selected_beach} Overview")
    weather = get_weather_data(beach_coords["lat"], beach_coords["lon"])
    cols = st.columns(3)
    cols[0].metric("🌡 Temperature", f"{weather['Temperature (°F)']} °F")
    cols[1].metric("☀ Weather", weather["Weather"])
    cols[2].metric("🕶 UV Index", weather["UV Index"])

    # Tide summary and chart
    st.subheader("🌊 Tide Forecast (Next 24 Hours)")
    tide_df = get_tide_data(beach_coords["station"])
    if not tide_df.empty:
        tide_summary = summarize_tides(tide_df)
        if not tide_summary.empty:
            st.markdown("**🕒 Upcoming High and Low Tides**")
            st.table(tide_summary)
        else:
            st.info("No high/low tide points found for today.")
        
        # Round for chart clarity
        tide_df['Tide (ft)'] = tide_df['Tide (ft)'].round(2)
        
        # Collapsible chart section
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

    # Hazard reporting
    st.subheader("📢 Report a Hazard")
    hazard_type = st.selectbox(
        "Select Hazard Type",
        ["Jellyfish", "Broken glass", "High surf", "Trash"],
        key=f"{selected_beach}_hazard_type"
    )

    # ---------------------------
    # Mapbox GL JS Map
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
                setupMap([{beach_coords['lon']}, {beach_coords['lat']}])
            }}

            function setupMap(center) {{
                const map = new mapboxgl.Map({{
                    container: 'map',
                    style: 'mapbox://styles/mapbox/streets-v11',
                    center: center,
                    zoom: 14
                }});

                const nav = new mapboxgl.NavigationControl();
                map.addControl(nav);

                // Live user marker
                const userMarker = new mapboxgl.Marker({{color:'blue'}})
                    .setLngLat(center)
                    .addTo(map);

                navigator.geolocation.watchPosition(function(pos){{
                    const lon = pos.coords.longitude;
                    const lat = pos.coords.latitude;
                    userMarker.setLngLat([lon, lat]);
                    if(window.directions) {{
                        window.directions.setOrigin([lon, lat]);
                    }}
                }}, function(err){{ console.error(err); }}, {{ enableHighAccuracy:true }});

                // Add hazard markers
                const hazards = {hazard_data_json};
                hazards.forEach(h => {{
                    if(h.beach == "{selected_beach}") {{
                        new mapboxgl.Marker({{color:'orange'}})
                            .setLngLat([h.lon, h.lat])
                            .setPopup(new mapboxgl.Popup().setText(h.hazard))
                            .addTo(map);
                    }}
                }});

                // Click-to-add hazard
                map.on('click', function(e) {{
                    const lat = e.lngLat.lat;
                    const lon = e.lngLat.lng;
                    const hazard = prompt("Enter hazard type (e.g., Jellyfish, Trash, High surf):");
                    if(hazard) {{
                        fetch("", {{
                            method: "POST",
                            headers: {{ "Content-Type": "application/json" }},
                            body: JSON.stringify({{lat:lat, lon:lon, hazard: hazard, beach: "{selected_beach}"}})
                        }});
                        new mapboxgl.Marker({{color:'orange'}})
                            .setLngLat([lon, lat])
                            .setPopup(new mapboxgl.Popup().setText(hazard))
                            .addTo(map);
                    }}
                }});

                // Directions toggle
                {"window.directions = new MapboxDirections({accessToken: mapboxgl.accessToken, unit:'imperial', profile:'mapbox/walking'}); map.addControl(window.directions, 'top-left'); window.directions.setDestination([" + str(beach_coords['lon']) + "," + str(beach_coords['lat']) + "]);" if show_directions else ""}
            }}
        </script>
    </body>
    """, height=650)

    st.write("🟢 Your location updates live (blue marker). Click the map to report hazards. If 'Show Directions' is toggled on, navigation automatically starts.")



