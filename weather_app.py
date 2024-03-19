from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests;
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser();
config.read(config_file);
apik = config['api_key']['key'];

# function that makes an apicall to get the weather of the given city 
def get_weather(city):
    result = requests.get(url.format(city,apik));
    if result:
        json = result.json();
        cityN = json['name'];
        country = json['sys']['country']
        temp_kel = json['main']['temp']
        temp_cel = temp_kel - 272.15
        temp_far = (temp_kel - 273.15) * 9 / 5 + 32;
        final = (cityN,country,temp_kel,temp_cel,temp_far)
        print(final);
        return final;
    else:
        return None;
app = Tk();
app.title("Weather App");
app.geometry("700x350");


def search():
    city = city_text.get()
    print(city)
    weather = get_weather(city);
    if weather:
        location_lnl['text'] = '{},{}'.format(weather[0],weather[1])
        temp_lbl['text'] = '{:.2f}C, {:.2f}F'.format(weather[2],weather[3]);
        weather_lbl['text'] = weather[4]
    else:
        messagebox.showerror('Error','Cannot find the city {}'.format(city))

city_text = StringVar();
city_entry = Entry(app,textvariable=city_text)
city_entry.pack();

search_btn = Button(app,text="Search Weather",width=12,command=search);
search_btn.pack();

location_lnl = Label(app,text='Location',font=('bold',20))
location_lnl.pack();

image = Label(app,bitmap='');
image.pack();

temp_lbl = Label(app,text='Tempature');
temp_lbl.pack();

weather_lbl = Label(app,text ='Weather');
weather_lbl.pack();

app.mainloop();