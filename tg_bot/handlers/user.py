from aiogram import types, Dispatcher

async def user_start(message: types.Message):
    await message.answer('Привет юзер')

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=['start'])