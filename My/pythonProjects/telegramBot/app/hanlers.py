from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import app.keyboard as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello", reply_markup=kb.main)
    await message.reply("How r u?")


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Do you want help?')


@router.message(F.text == 'qdw')
async def qdw(message: Message):
    await message.answer('That`s fine', reply_markup=kb.qdw)


@router.message(F.text != '.')
async def qdw(message: Message):
    await message.answer('What the hell')
