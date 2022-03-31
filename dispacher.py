from maindana import bot, dp

from aiogram.types import Message
from main1703 import my_id

async def send_to_admin(dp):
    await bot.send_message(chat_id=my_id, text="privet!")


@dp.message_handler()
async def echo(message: Message):
    text = f"ты написал:{message.text}"
    await bot.send_message(chat_id=message.from_user.id,
                           text=text)