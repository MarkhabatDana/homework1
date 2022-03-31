import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

TOKEN = '2036987065:AAEbvh13IxU6WU-ZoNo-DZlauPaGDI4ds9I'
my_id = 1060901941

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
async def send_to_admin(dp):
    await bot.send_message(chat_id=my_id, text="privet!")

@dp.message_handler()
async def echo(message: Message):
    if message.text == "Hi, how are ":
        await bot.send_message(chat_id=message.from_user.id, text="Hello. Eto Dana, Have a nice day!")
    elif message.text == "Dollor":
        await bot.send_message(chat_id=message.from_user.id, text="qazirgi yaqytta dollor bagasy 510.00 tg")
    elif message.text == "Euro":
        await bot.send_message(chat_id=message.from_user.id, text="qazirgi yaqytta euro bagasy 559.27 tg")
    elif message.text == "Rubl":
        await bot.send_message(chat_id=message.from_user.id, text="qazirgi yaqytta euro bagasy 3.98 tg")
    else:
        await bot.send_message(chat_id=message.from_user.id, text="kazfin saytynan alyngan aqparattar")

    async def sent_to_admin(dp):
        await bot.send_message(chat_id=my_id, text="Good bue")
if __name__ == "__main__":
    from dispacher import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)