import logging
import requests
from aiogram import types,executor,Dispatcher,Bot
from keyboard import button

from datetime import datetime as dt

bot = Bot(token="6218515361:AAE3pkqNppvNFQm5Q-rHzo581Sg92LL5YWQ")
dp=Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Obi havo haqida malumot beruvchi bot hisoblanadi")
    await message.answer('Shahar yoki davlat  nomini kiriting')



@dp.message_handler()
async def get_message(message: types.Message):
     
   try:

        City_API_endpoint = "http://api.openweathermap.org/data/2.5/weather?q="
        City = message.text
        Country = ",KE,"
        join_key = "&appid=" + "ed842fbad1362d2455d752d84b031c23"
        units = "&units=metric"

        current_city_weather = City_API_endpoint + City + Country + join_key + units
        request = requests.get(url=current_city_weather).json()
        
        temperatura = request['main']['temp']
        pressure = request['main']['pressure']
        humidity = request['main']['humidity']
        wind_speed = request['wind']['speed']
        sunrise = dt.utcfromtimestamp(request['sys']['sunrise']+ request['timezone'])
        sunset = dt.utcfromtimestamp(request['sys']['sunset']+ request['timezone'])
        lon = request['coord']['lon']
        lat = request['coord']['lat']
        name = request['name']
        
        caption = f"{name} \n\n\n🌡  Hozirgi temperatura: {temperatura} C\n\n🧬  Bosim kuchi: {pressure} hPa\n\n💧  Namligi: {humidity} %\n\n💨  Shamol tezligi: {wind_speed}m/s\n\n🌅  Quyosh chiqishi: {sunrise}\n\n🌇  Quyosh botishi: {sunset}"
        await message.answer_location(latitude=lat,longitude=lon)
        await message.answer(caption)
   except:
    await message.answer("Xatolik sodir bo'ldi qayta urinib ko'ring")
    await message.answer('Agar umuman ishlamasa inglizcha variantdagi shahar yoki davlatni  kiriting') 
   








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)