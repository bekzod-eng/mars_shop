from aiogram import types, Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from defalt_keybord import new_bot


token = "6615617282:AAGUN8Ovb-Clyp_bHH1xELY2fuRSAgnDcu8"
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "Salom, testni boshlash uchun pastdagi tugmadan foydalaning."
    await message.answer(text=text, reply_markup=new_bot)


@dp.message_handler(text ="1")
async def start_handler(message: types.Message):
    text = "Salom, siz birni bostingiz."
    await message.answer(text=text)


@dp.message_handler(text ="2")
async def start_handler(message: types.Message):
    text = "Salom, siz ikkini bostingiz."
    await message.answer(text=text)



@dp.message_handler(text ="3")
async def start_handler(message: types.Message):
    text = "Salom, siz uchni bostingiz."
    await message.answer(text=text)


@dp.message_handler(text ="4")
async def start_handler(message: types.Message):
    text = "Salom, siz torni bostingiz."
    await message.answer(text=text)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)




