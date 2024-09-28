import logging
from aiogram.utils import executor
from db import db_main
from handlers import commands, fsm_products, fsm_member, send_products
from config import dp, Bot,staff
from buttons import start

async def on_startup(_):
    for i in staff:
        await db_main.sql_create()


commands.register_commands(dp)
fsm_products.register_fsm_reg(dp)
fsm_member.register_handlers_order(dp)
send_products.register_send_products_handler(dp)








if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
