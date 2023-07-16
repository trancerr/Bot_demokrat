from tg_bot.keyboards.callback_data_factory import stocks_callback
from tg_bot.misc.main_text import stocks_brecket
from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher


@rate_limit(2)
async def osstem_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Имплантация Osstem от 1200 рублей в месяц")


@rate_limit(2)
async def brecket_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(stocks_brecket)


def register_stocks(dp: Dispatcher):
    dp.register_callback_query_handler(osstem_btn, stocks_callback.filter(stock_name='osstem'))
    dp.register_callback_query_handler(brecket_btn, stocks_callback.filter(stock_name='brecket'))
