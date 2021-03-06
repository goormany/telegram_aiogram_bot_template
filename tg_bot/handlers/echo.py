from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext


async def bot_echo(message: types.Message):

    text = [
        'Неизвестная команда.',
        message.text
    ]

    await message.answer('\n'.join(text))

async def bot_echo_all(message: types.Message, state: FSMContext):

    state_name = await state.get_state()

    text = [
        f'Команда в состоянии {state_name}.',
        message.text
    ]

    await message.answer('\n'.join(text))

def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo, state=None)
    dp.register_message_handler(bot_echo_all, state='*', content_types=types.ContentTypes.ANY)