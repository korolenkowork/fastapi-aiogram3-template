from aiogram import Dispatcher

from src.bot.handlers.start import router as start_routes


def register_bot_routes(dp: Dispatcher):
    dp.include_router(start_routes)
