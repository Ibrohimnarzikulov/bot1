import asyncio
import logging
from loader import bot, dp
from aiogram import Router
from heanler import set_up


async def main()->None:
   main_router=set_up()
   dp.include_router(main_router)
   logging.info("Bot ishladi")
   await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)    
    asyncio.run(main())
    