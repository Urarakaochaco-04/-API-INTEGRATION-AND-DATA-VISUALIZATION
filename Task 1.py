import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Set API key and city
API_KEY = '6af3c7c129c69ad48d4d38eb916992ad'  # Your OpenWeatherMap API key
CITY = 'Delhi'  # Use a valid city name, not country
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# 2. Fetch data from OpenWeatherMap
response = requests.get(URL)

# 3. Check if request was successful
if response.status_code != 200:
    print("Failed to fetch data from OpenWeatherMap API.")
    print("Error:", response.json())
else:
    data = response.json()

    # 4. Extract forecast data
    forecast_list = data['list']
    df = pd.DataFrame([{
        'datetime': entry['dt_txt'],
        'temperature': entry['main']['temp'],
        'humidity': entry['main']['humidity'],
        'weather': entry['weather'][0]['main']
    } for entry in forecast_list])

    # 5. Convert string to datetime object
    df['datetime'] = pd.to_datetime(df['datetime'])

    # 6. Plotting
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='datetime', y='temperature', label='Temperature (°C)')
    sns.lineplot(data=df, x='datetime', y='humidity', label='Humidity (%)')
    plt.title(f'5-Day Weather Forecast for {CITY}')
    plt.xlabel('Date and Time')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.show()
