from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import staff



class OrderFSM(StatesGroup):
    article = State()
    size = State()
    quantity = State()
    phone = State()



async def start_order(message: types.Message):
    await OrderFSM.article.set()
    await message.answer("Введите артикул товара:")


async def get_article(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['article'] = message.text
    await OrderFSM.next()
    await message.answer("Введите размер товара:")



async def get_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await OrderFSM.next()
    await message.answer("Введите количество товара:")



async def get_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text
    await OrderFSM.next()


    await message.answer("Введите ваш номер телефона:")


async def get_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text

    await message.answer(f"Заказ принят:\n"
                         f"Артикул: {data['article']}\n"
                         f"Размер: {data['size']}\n"
                         f"Количество: {data['quantity']}\n"
                         f"Телефон: {data['phone']}")

    for user_id in staff:
        try:
            await message.bot.send_message(user_id, f"Новый заказ\n"
                                                    f"Артикул: {data['article']}\n"
                                                    f"Размер: {data['size']}\n"
                                                    f"Количество: {data['quantity']}\n"
                                                    f"Телефон: {data['phone']}")
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")

    await state.finish()


def register_handlers_order(dp: Dispatcher):
    dp.register_message_handler(start_order, commands=['order'], state=None)
    dp.register_message_handler(get_article, state=OrderFSM.article)
    dp.register_message_handler(get_size, state=OrderFSM.size)
    dp.register_message_handler(get_quantity, state=OrderFSM.quantity)
    dp.register_message_handler(get_contact, state=OrderFSM.phone)