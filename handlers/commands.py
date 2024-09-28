from aiogram import types, Dispatcher
from buttons import start
from config import bot

async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text = f'Hello!, {message.from_user.first_name}',
                           reply_markup=start)

async def info_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="""В этом боте вы можете
    заполнить информацию о любом вашем товаре, информация будет сохранена в базу данных
    и можете продать или найти какой-либо товар по вашему желанию.\n
    Испольуйте для ввода продукта комманду /products""", reply_markup=start)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])