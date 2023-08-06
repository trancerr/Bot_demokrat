from aiogram.dispatcher import FSMContext

from api_amo.add_contat import add_contact
from tg_bot.keyboards.reply import menu
from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from tg_bot.misc.states_online_recording import OnlineRecording


@rate_limit(2)
async def enter_name(call: types.CallbackQuery):
    await call.message.answer('Введите имя:')
    await OnlineRecording.NAME.set()


@rate_limit(2)
async def enter_phone(message: types.Message, state: FSMContext):
    answer_name = message.text
    await state.update_data(answer_name=answer_name)
    await message.answer('Введите номер телефона:')
    await OnlineRecording.PHONE.set()


@rate_limit(2)
async def end_enter(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get('answer_name')
    phone = message.text
    await message.answer(f'Спасибо {name} {phone}\n'
                         f'Администратор свяжется с вами в течении 10 минут.', reply_markup=menu)
    # add_contact(name=name, phone=phone)
    await state.finish()


def register_states_recording(dp: Dispatcher):
    dp.register_callback_query_handler(enter_name, Text(equals='rec_online'), state=None)
    dp.register_message_handler(enter_phone, state=OnlineRecording.NAME)
    dp.register_message_handler(end_enter, state=OnlineRecording.PHONE)
