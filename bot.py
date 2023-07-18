import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher.middlewares import BaseMiddleware

from tg_bot.config import load_config
from tg_bot.filters.admin import AdminFilter
from tg_bot.handlers.echo import register_echo
from tg_bot.handlers.entries_handler import register_entries
from tg_bot.handlers.recording_handler import register_recording
from tg_bot.handlers.stocks_handler import register_stocks
from tg_bot.handlers.user import register_user
from tg_bot.middleware.thottling import ThrottlingMiddleware
from tg_bot.filters.censorship import register_censorship

logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    dp.setup_middleware(ThrottlingMiddleware(BaseMiddleware))


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_user(dp)
    register_stocks(dp)
    register_entries(dp)
    register_recording(dp)
    register_censorship(dp)
    register_echo(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )

    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    bot["config"] = config

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот остановлен!")
