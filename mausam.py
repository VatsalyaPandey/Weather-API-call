
import tkinter as tk
import time
import requests

def getdata(canvas):
    city=textfield.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=2e163add277eda6a34585d1d93490566"
    jsondata=requests.get(api).json()
    haze=(jsondata["weather"][0]["main"]) 
    temp=int((jsondata["main"]["temp"]-273.5))
    humidity=(jsondata["main"]["humidity"]) 
    mintemp=int(jsondata['main']['temp_min']-273.15)
    maxtemp=int(jsondata['main']['temp_max']-273.15)
    sunrise=time.strftime("%I:%M:%S",time.gmtime(jsondata['sys']['sunrise']-21500))
    info= haze+"\n"+str(temp)+"°C"
    finalinfo="\n"+"max temp"+str(maxtemp)+"\n"+"min temp"+str(mintemp)+"\n"+"humidity:"+str(humidity)+"\n"+"Temperature:"+str(temp)+"\n"+"Sunrise:"+str(sunrise)
    
    label1.config(text=info)
    label2.config(text=finalinfo)



canvas=tk.Tk()
canvas.geometry=("600x500")
canvas.title("Weather info")
s1=("calibri",15,"bold")
s2=("calibri",25,"bold")

textfield=tk.Entry(canvas,font=s2)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getdata)
label1=tk.Label(canvas,font=s2)
label1.pack()
label2=tk.Label(canvas,font=s1)
label2.pack()


canvas.mainloop()



