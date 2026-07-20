# Standard WMO Weather Interpretation Codes Map
WEATHER_CODES = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Depositing Rime Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Dense Drizzle",
    61: "Slight Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    71: "Slight Snowfall",
    73: "Moderate Snowfall",
    75: "Heavy Snowfall",
    80: "Slight Rain Showers",
    81: "Moderate Rain Showers",
    82: "Violent Rain Showers",
    95: "Thunderstorm",
    96: "Thunderstorm with Slight Hail",
    99: "Thunderstorm with Heavy Hail"
}

def get_weather_status(code):
    """Retrieves standard text description and an anchor emoji matching the weather ID."""
    description = WEATHER_CODES.get(code, "Unknown Weather Condition")
    
    # Map conditions to scannable visual status anchors
    if code == 0:
        emoji = "☀️"
    elif code in [1, 2]:
        emoji = "⛅"
    elif code == 3:
        emoji = "☁️"
    elif code in [45, 48]:
        emoji = "🌫️"
    elif code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
        emoji = "🌧️"
    elif code in [71, 73, 75]:
        emoji = "❄️"
    elif code in [95, 96, 99]:
        emoji = "⛈️"
    else:
        emoji = "🌍"
        
    return f"{emoji} {description}"

# Simulated incoming live forecast code
incoming_api_code = 95 
current_condition = get_weather_status(incoming_api_code)

print(f"API Weather Status: {current_condition}")
# Output: ⛈️ Thunderstorm
