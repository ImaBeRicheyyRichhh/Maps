import pandas as pd
import plotly.graph_objects as go

# Step 1: GDP data and coordinates for top U.S. metro areas
data = [
    {"Metro": "New York–Newark–Jersey City", "GDP": 2298.9, "Lat": 40.7128, "Lon": -74.0060},
    {"Metro": "Los Angeles–Long Beach–Anaheim", "GDP": 1295.4, "Lat": 34.0522, "Lon": -118.2437},
    {"Metro": "Chicago–Naperville–Elgin", "GDP": 894.9, "Lat": 41.8781, "Lon": -87.6298},
    {"Metro": "San Francisco–Oakland–Berkeley", "GDP": 778.9, "Lat": 37.7749, "Lon": -122.4194},
    {"Metro": "Dallas–Fort Worth–Arlington", "GDP": 744.7, "Lat": 32.7767, "Lon": -96.7970},
    {"Metro": "Washington–Arlington–Alexandria", "GDP": 714.7, "Lat": 38.9072, "Lon": -77.0369},
    {"Metro": "Houston–The Woodlands–Sugar Land", "GDP": 697.0, "Lat": 29.7604, "Lon": -95.3698},
    {"Metro": "Boston–Cambridge–Newton", "GDP": 610.5, "Lat": 42.3601, "Lon": -71.0589},
    {"Metro": "Atlanta–Sandy Springs–Roswell", "GDP": 570.7, "Lat": 33.7490, "Lon": -84.3880},
    {"Metro": "Seattle–Tacoma–Bellevue", "GDP": 566.7, "Lat": 47.6062, "Lon": -122.3321},
    {"Metro": "Philadelphia–Camden–Wilmington", "GDP": 557.6, "Lat": 39.9526, "Lon": -75.1652},
    {"Metro": "Miami–Fort Lauderdale–West Palm Beach", "GDP": 533.7, "Lat": 25.7617, "Lon": -80.1918},
    {"Metro": "Phoenix–Mesa–Scottsdale", "GDP": 398.1, "Lat": 33.4484, "Lon": -112.0740},
    {"Metro": "Detroit–Warren–Dearborn", "GDP": 331.3, "Lat": 42.3314, "Lon": -83.0458},
    {"Metro": "San Diego–Carlsbad", "GDP": 314.9, "Lat": 32.7157, "Lon": -117.1611},
    {"Metro": "Denver–Aurora–Lakewood", "GDP": 311.9, "Lat": 39.7392, "Lon": -104.9903}
]

df = pd.DataFrame(data)

# Step 2: Create base map with metro points
fig = go.Figure()

fig.add_trace(go.Scattergeo(
    locationmode='USA-states',
    lon=df["Lon"],
    lat=df["Lat"],
    text=[f"{row['Metro']}<br>GDP: ${row['GDP']}B" for _, row in df.iterrows()],
    marker=dict(size=10, color='green', line=dict(width=0.5, color='darkgreen')),
    hoverinfo='text'
))

# Step 3: Add GDP bars (vertical lines)
for _, row in df.iterrows():
    fig.add_trace(go.Scattergeo(
        lon=[row["Lon"], row["Lon"]],
        lat=[row["Lat"], row["Lat"]],
        mode='lines',
        line=dict(width=row["GDP"] / 100, color='blue'),
        hoverinfo='skip',
        showlegend=False,
    ))

# Step 4: Layout styling
fig.update_layout(
    title_text='Top U.S. Metropolitan Areas by GDP (2023)',
    showlegend=False,
    geo=dict(
        scope='usa',
        projection_type='albers usa',
        showland=True,
        landcolor='lightgray',
        subunitcolor='white'
    ),
    height=700
)

# Step 5 (Optional): Save to HTML
fig.write_html("us_gdp_map_2023.html")

# Step 6: Show the map
fig.show()