from aiogram import Dispatcher
from aiogram.types import Message
from tg_bot.misc.throttling import rate_limit

import json, string


@rate_limit(2)
async def censorship(message: Message):
    if {
        i.lower().translate(str.maketrans("", "", string.punctuation))
        for i in message.text.split(" ")
    }.intersection(set(json.load(open("tg_bot/filters/censorship.json")))) != set():
        await message.reply("🤬Маты запрещены")
        await message.delete()


def register_censorship(dp: Dispatcher):
    dp.register_message_handler(censorship)