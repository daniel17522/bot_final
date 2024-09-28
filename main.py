import logging
from aiogram.utils import executor
from db import db_main
from handlers import commands, fsm_products, fsm_member
from config import dp, Bot,staff

async def on_startup(_):
    for i in staff:
        await Bot.send_message(chat_id=i, text="Бот включен!")
        await db_main.sql_create()


commands.register_commands(dp)
fsm_products.register_fsm_reg(dp)
fsm_member.register_handlers_order(dp)








if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
