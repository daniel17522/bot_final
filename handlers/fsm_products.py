from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from config import staff
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from db import db_main
import buttons


class FsmProduct(StatesGroup):
    fullname = State()
    category = State()
    size_product = State()
    price = State()
    product_id = State()
    photo = State()


async def start_fsm(message: types.Message):
    if message.from_user.id not in staff:
        await message.answer('У вас нет доступа к этой комманде!')
        return

    await message.answer('Укажите название или бренд товара: ')
    await FsmProduct.fullname.set()


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await message.answer('Введите категорию товара: ')
    await FsmProduct.next()


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await message.answer('Введите размер товара: ')
    await FsmProduct.next()


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size_product'] = message.text

    await message.answer('Введите цену товара: ')
    await FsmProduct.next()


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await message.answer('Введите артикул товара: ')
    await FsmProduct.next()

async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await message.answer('Отправьте фото: ')
    await FsmProduct.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data['photo'],
                                   caption='Ваш товар\n\n'
                                           f'Название товара: {data["fullname"]}\n'
                                           f'категория товара: {data["category"]}\n'
                                           f'размер товара: {data["size_product"]}\n'
                                           f'Стоимость: {data["price"]}\n'
                                           f'Артикул товара: {data["product_id"]}\n')

    async with state.proxy() as data:
        await message.answer('Отлично, Данные в базе!')
        await db_main.sql_insert_products(
            fullname=data['fullname'],
            category=data['category'],
            size_product=data['size_product'],
            price=data['price'],
            product_id=data['product_id'],
            photo=data['photo']
        )


def register_fsm_reg(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands=['product_add'], state=None)
    dp.register_message_handler(load_name, state= FsmProduct.fullname)
    dp.register_message_handler(load_category, state=FsmProduct.category)
    dp.register_message_handler(load_size, state=FsmProduct.size_product)
    dp.register_message_handler(load_price, state=FsmProduct.price)
    dp.register_message_handler(load_product_id, state=FsmProduct.product_id)
    dp.register_message_handler(load_photo, state=FsmProduct.photo,
                                content_types=['photo'])