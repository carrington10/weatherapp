from tkinter import *

app = Tk();
app.title("Weather App");
app.geometry("700x350");

def search():
    pass;

city_text = StringVar();
city_entry = Entry(app,textvariable=city_text)
city_entry.pack();

search_btn = Button(app,text="Search Weather",width=12,command=search);
search_btn.pack();

location_lnl = Label(app,text='Location',font=('bold',20))
location_lnl.pack();


app.mainloop();