from aiogram import types, Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from defalt_keybord import new_bot
# from environs import env

# env = Env()
# env.read_env()

# BOT_TOKEN = env.str("TOKEN")


token = "6615617282:AAGUN8Ovb-Clyp_bHH1xELY2fuRSAgnDcu8"
storage = MemoryStorage()
bot = Bot(token=Bot_Token, proxy="http.//proxy.server.3128")
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "Salom, testni boshlash uchun pastdagi tugmadan foydalaning."
    await message.answer(text=text, reply_markup=new_bot)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)




