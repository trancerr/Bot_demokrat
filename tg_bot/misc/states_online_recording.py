from aiogram.dispatcher.filters.state import StatesGroup, State


class OnlineRecording(StatesGroup):
    NAME = State()
    PHONE = State()
