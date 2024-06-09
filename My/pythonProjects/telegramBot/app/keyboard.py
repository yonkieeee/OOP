from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='qdw')],
                                     [KeyboardButton(text='fe')],
                                     [KeyboardButton(text='ed'),
                                     KeyboardButton(text='fe')]],
                           resize_keyboard=True,
                           input_field_placeholder='FWFefwef...')


qdw = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='efef', callback_data='efef')],
    [InlineKeyboardButton(text='wdw',  callback_data='wdw')],
    [InlineKeyboardButton(text='dwq',  callback_data='dwq')],])
