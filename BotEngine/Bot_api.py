from Config import Config
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = Config.BOT_TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def send_to_chat(message: types.Message):

    await bot.send_photo(chat_id=Config.programmers_chat_id, photo=message.photo[-1].file_id, caption=message.caption)
    await bot.send_message(chat_id=message.chat.id, text='Ошибка отправлена и скоро будет исправлена')

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def text_messages(message: types.Message):

    await bot.send_message(chat_id=message.chat.id, text='Отправьте картинку ошибки сюда (желательно с описанием)')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)