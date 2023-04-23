import random
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from dotenv import load_dotenv
#from test import *
from random import randint




load_dotenv()

TOKEN=os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
ADMINS = [5888056812]


async def set_default_commands(dp):
    await bot.set_my_commands(
        [
        types.BotCommand("start"),
        types.BotCommand("country_info"),
        types.BotCommand("help"),
        ]
    )





country = {
    "Pakistan":{
    "Region":"South Asia",
    "Capital": "Islamabad",
    "Population": "220,892,340 (5th Rank)",
    "Size":"881,912 km² (34th Largest)",
    "Language":"Urdu, English",
    "Density":"287 per Km²",
    "Currency":"Pakistani rupee",
    "National flower":"Jasmine",
    "National dish": "Pakistani Nihari"
    },

    "Slovakia":{
    "Region":"Central Europe",
    "Capital":"Bratislava",
    "Population":"5,459,642 (118th Rank)",
    "Size":"49,037 km² (130th Largest)",
    "Language":"Slovak",
    "Density":"114 per km²",
    "Currency":"Euro",
    "National flower":"Rose",
    "National dish":"Bryndzové Halušky",
    },
    "India":{
    "Region":"South Asia",
    "Capital":"New Delhi",
    "Population":"1,380,004,385 (2th Rank)",
    "Size":"3,287,590 km² (7th Largest)",
    "Language":"Hindi, English",
    "Density":"464 per km²",
    "Currency":"Indian rupee",
    "National flower":"Lotus",
    "National dish":"No official national food",
    },
    "Sweden":{
    "Religion":"Northern Europe",
    "Capital":"Stockholm",
    "Population":"10,099,265 (91th Rank)",
    "Size":"450,295 km² (56th Largest)",
    "Language":"Swedish",
    "Density":"25 per km²",
    "Currency":"Swedish krona",
    "National flower":"Campanula rotundifolia",
    "National dish":"Meatballs",
    },
    "Palestine state":{
    "Region":"Western Asia",
    "Capital":"Jerusalem, Ramallah",
    "Population":"5,101,414 (121th Rank)",
    "Size":"6,220 km² (170th Largest)",
    "Language":"Arabic",
    "Density":"847 per Km²",
    "Currency":"Israeli Shekel, Egyptian pound, Jordanian dinar, Palestine pound",
    "National flower":"Faqqua iris",
    "National dish":"Musakhan",
    },
    "Latvia":{
    "Region" :  "Northeastern Europe",
    "Capital": "Riga",
    "Population": "21,886,198",
    "Size": "64,559 km²",
    "Language": "Latvian",
    "Density": "30 per Km2",
    "Currency": "Euro",
    "National flower" :"Daisy",
    "National dish": "Pelēkie zirņi ar speķi ",
    },
    "Cabo Verde":{
    "Region":"Central Atlantic Ocean",
    "Capital":"Praia",
    "Population":"555,987",
    "Size":"4,033 km²",
    "Language":"Spanish",
    "Density":"138 per Km2",
    "Currency":"Cape Verdean escudo",
    "National flower":"Gerbera daisy",
    "National dish":"Cachupa",
    }, 
   "Tunisia":{
    "Region":"North Africa",
    "Capital":"Tunis",
    "Population":"11,818,619",
    "Size":"163,610 km²",
    "Language":"Arabic",
    "Density":"76 per Km2",
    "Currency":"Tunisian dinar",
    "National flower":"Jasmine",
    "National dish": "Couscous",
    },
    "Uzbekistan":{
    "Region":"Central Asia",
    "Capital":"Tashkent",
    "Population":"33,469,203",
    "Size":"447,400 km² ",
    "Language":"Uzbek",
    "Density":"79 per Km2",
    "Currency":"Uzbekistani so'm",
    "National flower":"Cotton Flower",
    "National dish":  "	Plov" ,
    },
    "Dominica":{
    "Region":"Caribbean Sea",
    "Capital":"Roseau",
    "Population":"71,986",
    "Size":"751 km²",
    "Language":"English",
    "Density":"96 per Km2",
    "Currency":"Eastern Caribbean dollar",
    "National flower":"Sabinea carinalis",
    "National dish":"Mountain Chicken",
    },
    "Japan":{
    "Region":"East Asia",
    "Capital":"Tokyo",
    "Population":"126,476,461",
    "Size":"377,930 km² ",
    "Language":"Japanese",
    "Density":"340.8 per Km2",
    "Currency":"Japanese yen",
    "National flower":"Cherry Blossoms",
    "National dish":"Curry-rice",
    },
    "Solomon Islands":{
    "Region":"South Pacific",
    "Capital":"Honiara",
    "Population":"686,884 ",
    "Size":"28,896 km²",
    "Language":"English",
    "Density":"25 per Km2",
    "Currency":"Solomon Islands dollar",
    "National flower":"Hibiscus",
    "National dish":"Poi",
    }, 
    "Chile":{
    "Region":"South America",
    "Capital":"Santiago",
    "Population":"19,116,201",
    "Size":"756,102 km²",
    "Language":"Spanish",
    "Density":"26 per Km2",
    "Currency":"Chilean peso",
    "National flower":"	Lapageria",
    "National dish":"Pastel de Choclo",
    },
    "Algeria":{
    "Region":"North Africa",
    "Capital":"Algiers",
    "Population":"43,851,044",
    "Size":"2,381,741 km²",
    "Language":"Arabic and Tamazight",
    "Density":"18 per Km2",
    "Currency":"Algerian dinar",
    "National flower":"	Iris Tectorum",
    "National dish":"Couscous",
    },
    "South Korea":{
    "Region":"Southern half of the Korean Peninsula",
    "Capital":"Seoul",
    "Population":"51,269,185",
    "Size":"100,210 km²",
    "Language":"Korean",
    "Density":"527 per Km2",
    "Currency":"South Korean won",
    "National flower":"Rose of Sharon",
    "National dish":"Kimchi",
    },
    "Botswana":{
    "Region":"Southern Africa",
    "Capital":"Gaborone",
    "Population":"2,351,627",
    "Size":"582,000 km²",
    "Language":"English",
    "Density":"4 per Km2",
    "Currency":"Botswana pula",
    "National flower":"Kalahari Devil's Claw",
    "National dish":"Seswaa",
    },
    "Vanuatu":{
    "Region":"	South Pacific Ocean",
    "Capital":"Port Vila",
    "Population":"307,145",
    "Size":"12,189 km²",
    "Language":"French, Bislama, English",
    "Density":"25 per Km2",
    "Currency":"Vanuatu vatu",
    "National flower":"Hibiscus Plant",
    "National dish":"Lap lap",
    },
}




@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f"Hi I'm bot!")

@dp.message_handler(commands='help')
async def country_info(message: types.Message):
    await message.answer(f"For  have some information of country, print command-country_info\n\
                           for read some information print command-information about bot ")




@dp.message_handler(commands='countr_info')
async def country_info(message: types.Message):
    await bot.send_message(message, "Eneter the country")    
    if message in country.keys():
        name = country[message.data]["Region"],
        capital = country[message.data]["Capital"],
        population = country[message.data]["Population"],
        size = country[message.data]["Size"],
        language = country[message.data]["Language"],
        desity = country[message.data]["Density"],
        national_flower = country[message.data]["National flower"],
        national_dish = country[message.data]["National dish"],
    else:
        await bot.send_message(message, "Not found!!!")


if __name__ == '__main__':
    set_default_commands(dp)
    executor.start_polling(dp)
