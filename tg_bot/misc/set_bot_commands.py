from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запустить бота'
        ),
        BotCommand(
            command='help',
            description='Что умеет этот бот'
        ),
        BotCommand(
            command='support',
            description='Связаться с администратором'
        ),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
