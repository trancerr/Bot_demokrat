from asyncio import sleep
from typing import Union

from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import current_handler
from aiogram import types, Dispatcher
from aiogram.utils.exceptions import Throttled

"""Анти флуд класс Middleware"""


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix="antiflood_"):
        self.limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def throttle(self, target: Union[types.Message, types.CallbackQuery]):
        handler = current_handler.get()
        if not handler:
            return
        dp = Dispatcher.get_current()
        limit = getattr(handler, "throttling_rate_limit", self.limit)
        key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        try:
            await dp.throttle(key, rate=limit)
        except Throttled as t:
            await self.target_throttled(target, t, dp, key)

    @staticmethod
    async def target_throttled(
        target: Union[types.Message, types.CallbackQuery],
        throttled: Throttled,
        dispatcher: Dispatcher,
        key: str,
    ):
        msg = target.message if isinstance(target, types.CallbackQuery) else target
        delta = throttled.rate - throttled.delta
        if throttled.exceeded_count == 2:
            await msg.reply(
                "❗❗❗Не отправляйте запросы часто это может привести \
            к кратковременной блокировке❗❗❗"
            )
            return
        elif throttled.exceeded_count == 3:
            await msg.reply(f"Чат заблокирован на {round(delta, 0)} секунд!")
            return
        await sleep(delta)

        thr = await dispatcher.check_key(key)
        if thr.exceeded_count == thr.exceeded_count:
            await msg.reply("Чат разблокирован!")

    async def on_process_message(self, message, data):
        await self.throttle(message)

    async def on_process_callback_query(self, call, data):
        await self.throttle(call)
