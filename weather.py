import tkinter as tk
from tkinter import messagebox
import requests
import json

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast")
        self.root.geometry("400x300")
        self.root.configure(bg="lightblue")
         # promt to enter the city  name
        self.city_label = tk.Label(root, text="Enter city name:", font=("Helvetica", 14), bg="lightblue")
        self.city_label.place(x=50, y=50)
        self.city_entry = tk.Entry(root, font=("Helvetica", 12))
        self.city_entry.place(x=200, y=50, width=150)
        
        # When we click this it is redirected to method get weather to receive the weather
        self.get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=self.get_weather, relief="raised")
        self.get_weather_button.place(x=150, y=100, width=100)
        
        self.weather_label = tk.Label(root, text="", font=("Helvetica", 12), bg="lightblue", wraplength=350)
        self.weather_label.place(x=25, y=150)
        
        self.api_key = "Use ur API key"
        
    def get_weather(self):
        city = self.city_entry.get()
        if city:
            try:
                # syntax for checking weather 
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
                response = requests.get(url)
                data = response.json()

                '''If the response code ("cod") is 200, indicating successful data retrieval, 
                it calls parse_weather_data to process the data and updates the weather label with the information.'''
                if data.get("cod") == 200:
                    weather_info = self.parse_weather_data(data) # if cod is 
                    self.weather_label.config(text=weather_info)
                else:
                    self.weather_label.config(text="Weather data not found for this city.")
            except Exception as e:
                messagebox.showerror("Error", "An error occurred while fetching weather data.")
        else:
            messagebox.showwarning("Warning", "Please enter a city name.")
    

    '''takes the JSON data from the API response and processes it to create a formatted weather information string.
    It extracts temperature-related information from the "main" section and weather description from the "weather" section'''
    def parse_weather_data(self, data):
        main_info = data["main"]
        temp = main_info["temp"]
        temp_min = main_info["temp_min"]
        temp_max = main_info["temp_max"]
            
        weather_info = data["weather"][0]["description"]
            
        result = f"Weather: {weather_info}\n"
        result += f"Temperature: {temp}°C\n"
        result += f"Min Temperature: {temp_min}°C\n"
        result += f"Max Temperature: {temp_max}°C"
            
        return result

root = tk.Tk()
app = WeatherApp(root)
root.mainloop()
