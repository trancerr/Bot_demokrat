from tg_bot.keyboards.callback_data_factory import stocks_callback
from tg_bot.keyboards.reply import menu
from tg_bot.keyboards.stock_keyboards import osstem_keyboard, brecket_keyboard, all_on_4_keyboard
from tg_bot.misc.main_text import stocks_brecket, stocks_all_on_4
from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

'''
Функции обработки кнопок списка акций
'''


@rate_limit(2)
async def osstem_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Имплантация Osstem от 1200 рублей в месяц", reply_markup=osstem_keyboard)


@rate_limit(2)
async def brecket_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(stocks_brecket, reply_markup=brecket_keyboard)


@rate_limit(2)
async def all_on_4_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(stocks_all_on_4,  reply_markup=all_on_4_keyboard)


@rate_limit(2)
async def cancel_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Главное меню: ", reply_markup=menu)


def register_stocks(dp: Dispatcher):
    dp.register_callback_query_handler(osstem_btn, stocks_callback.filter(stock_name='osstem'))
    dp.register_callback_query_handler(brecket_btn, stocks_callback.filter(stock_name='brecket'))
    dp.register_callback_query_handler(all_on_4_btn, stocks_callback.filter(stock_name='all-on-4'))
    dp.register_callback_query_handler(cancel_btn, Text(equals='cancel'))
