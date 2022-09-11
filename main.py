import asyncio
from aiogram import Bot, Dispatcher, executor
from settings import API_KEY


TimerBot = Bot(API_KEY)
bot_dispatcher = Dispatcher(TimerBot)


@bot_dispatcher.message_handler()
async def new_time_message(message):
    try:
        timerOfHours = int(message.text)
    except (ValueError,TypeError):
        await TimerBot.send_message(chat_id=message.chat.id, text="Please enter a number")
        return

    new_message = await TimerBot.send_message(chat_id = message.chat.id, text = f"Your timer is at: {timerOfHours}")

    for HoursLeft in range (timerOfHours - 1, -1, -1):
        await asyncio.sleep(1)
        await new_message.edit_text(text = f"Your timer is at: {HoursLeft}")

    await TimerBot.send_message(chat_id = message.chat.id, text = " روز برنامه نویس مبارک =) ")

if __name__ == '__main__':
    executor.start_polling(bot_dispatcher)