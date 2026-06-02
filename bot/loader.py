from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiohttp import ClientTimeout

from core import settings


def create_bot_session() -> AiohttpSession:
    """
    Создаёт оптимизированную сессию для бота.
    """
    
    timeout = ClientTimeout(
        total=30,
        connect=10,
        sock_connect=10,
        sock_read=20
    )
    
    session = AiohttpSession(timeout=timeout)
    
    return session


def create_bot() -> Bot:
    """Создаёт экземпляр бота"""
    session = create_bot_session()
    
    return Bot(
        token=settings.API_TOKEN,
        session=session,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )


def create_dispatcher() -> Dispatcher:
    """Создаёт диспетчер и подключает роутеры"""
    from settings.telegram_routers import (
        user_router
    )
    
    dp = Dispatcher()
    dp.include_router(user_router)
    
    return dp


bot = create_bot()
dp = create_dispatcher()