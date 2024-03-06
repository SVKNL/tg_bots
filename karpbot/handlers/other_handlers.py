from aiogram.types import Message
from aiogram import Router
from lexicons.lexicons import LEXICON_RU

# Создание объекта класса роутер чтобы зарегистрировать хэндлеры в диспетчере

router=Router()

# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])