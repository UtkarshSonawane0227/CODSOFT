from tkinter import *
import requests
import json
from datetime import datetime
 
#Initialize Window
 
root =Tk()
root.geometry("600x600+400+500")
root.title("Weather App")
root.configure(bg="#17161b") 
root.resizable(0,0) 

 
 
# ----------------------Functions to fetch and display weather info
city_value = StringVar()
 
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
 
city_value = StringVar()
 
def showWeather():
   
    api_key = "afcb0d35166677788bb5f0242d240603"  
 
    
    city_name=city_value.get()
 
    
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
   
    response = requests.get(weather_url)
 
     
    weather_info = response.json()
 
 
    tfield.delete("1.0", "end")   
 

 
 
    if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin
 

        temp = int(weather_info['main']['temp'] - kelvin)                                   
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 

         
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
 
    tfield.insert(INSERT, weather)   
    
 
 

 
 
city_head= Label(root, text = 'Enter City Name', font = 'Century 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Century 12 bold').pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Century 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).place(x=450,y=45)
 


weather_now = Label(root, text = "The Weather is:", font = 'Century 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()
 
root.mainloop()