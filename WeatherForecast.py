import requests
import tkinter as tk
from tkinter import messagebox

def get_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

def extract_weather_info(data):
    if data is None:
        return None

    weather_info = {}

    if 'name' in data:
        weather_info["location"] = data["name"]
    else:
        weather_info["location"] = "Location data not available."

    if 'weather' in data and data['weather']:
        weather_info["description"] = data["weather"][0]["description"].capitalize()
    else:
        weather_info["description"] = "Weather data not available."

    if 'main' in data and 'temp' in data['main']:
        weather_info["temperature"] = data["main"]["temp"]
    else:
        weather_info["temperature"] = "Temperature data not available."

    if 'main' in data and 'humidity' in data['main']:
        weather_info["humidity"] = data["main"]["humidity"]
    else:
        weather_info["humidity"] = "Humidity data not available."

    if 'wind' in data and 'speed' in data['wind']:
        weather_info["wind_speed"] = data["wind"]["speed"]
    else:
        weather_info["wind_speed"] = "Wind speed data not available."

    return weather_info

def display_weather():
    location = location_entry.get()
    if not location:
        messagebox.showerror("Error", "Please enter a city name or zip code.")
        return

    api_key = "1c14cd95652e24f32b024362421b9c0b"  
    data = get_weather_data(api_key, location)
    weather_info = extract_weather_info(data)

    weather_output.config(state=tk.NORMAL)
    weather_output.delete(1.0, tk.END)
    if weather_info:
        weather_output.insert(tk.END, f"Weather Forecast for {weather_info['location']}\n")
        weather_output.insert(tk.END, "-------------------------\n")
        weather_output.insert(tk.END, f"Description: {weather_info['description']}\n")
        weather_output.insert(tk.END, f"Temperature: {weather_info['temperature']} °C\n")
        weather_output.insert(tk.END, f"Humidity: {weather_info['humidity']}%\n")
        weather_output.insert(tk.END, f"Wind Speed: {weather_info['wind_speed']} m/s")
    else:
        weather_output.insert(tk.END, "Failed to retrieve weather data.")
    weather_output.config(state=tk.DISABLED)

app = tk.Tk()
app.title("Weather Forecast")
app.geometry("400x300")

location_label = tk.Label(app, text="Enter city name or zip code:")
location_label.pack(pady=10)

location_entry = tk.Entry(app)
location_entry.pack()

get_weather_btn = tk.Button(app, text="Get Weather", command=display_weather)
get_weather_btn.pack(pady=10)

weather_output = tk.Text(app, wrap=tk.WORD, state=tk.DISABLED)
weather_output.pack(fill=tk.BOTH, expand=True)

app.mainloop()
