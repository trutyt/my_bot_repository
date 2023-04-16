from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from films import FILMS

film_choise = InlineKeyboardMarkup()
for film in FILMS:
    button = InlineKeyboardButton(text=film, callback_data=film)
    film_choise.add(button)