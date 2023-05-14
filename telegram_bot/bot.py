from distutils.cmd import Command
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot_tcell import chatbot_response
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


tarif = InlineKeyboardMarkup(row_width=2)
darkor = InlineKeyboardButton(text=' Даркор', callback_data="darkor")
internet = InlineKeyboardButton(text=' +Интернет', callback_data="internet")
socseti = InlineKeyboardButton(text=' Соцсети', callback_data="socseti")
bezlimit = InlineKeyboardButton(text=' +Безлимит', callback_data="bezlimit")
tarif.add(darkor,internet,socseti,bezlimit)


darkor = InlineKeyboardMarkup(row_width=2)
darkor1 = InlineKeyboardButton(text=' Даркор 30', callback_data="darkor 30")
darkor2 = InlineKeyboardButton(text=' Даркор 60', callback_data="darkor 60")
darkor3 = InlineKeyboardButton(text=' Даркор 100', callback_data="darkor 100")
darkor4 = InlineKeyboardButton(text=' Даркор 160', callback_data="darkor 160")
darkor5 = InlineKeyboardButton(text='Даркор 200', callback_data="darkor 200")
darkor.add(darkor1,darkor2,darkor3,darkor4, darkor5)

internet= InlineKeyboardMarkup(row_width=2)
internet1 = InlineKeyboardButton(text='+Интернет 35', callback_data="internet 35")
internet2 = InlineKeyboardButton(text='+Интернет 65', callback_data="internet 65")
internet3 = InlineKeyboardButton(text=' +Интернет 105', callback_data="internet 105")
internet4 = InlineKeyboardButton(text='+Интернет 165', callback_data="internet 165")
internet5 = InlineKeyboardButton(text='+Интернет 205', callback_data="internet 205")
internet.add(internet1,internet2,internet3,internet4,internet5)

bezlimit= InlineKeyboardMarkup(row_width=2)
bezlimit1= InlineKeyboardButton(text='+Безлимит 59', callback_data="bezlimit 59")
bezlimit2= InlineKeyboardButton(text='+Безлимит 99', callback_data="bezlimit 99")
bezlimit3 = InlineKeyboardButton(text='+Безлимит 149', callback_data="bezlimit 149")
bezlimit4 = InlineKeyboardButton(text='+Безлимит199', callback_data="bezlimit 199")
bezlimit5= InlineKeyboardButton(text='+Безлимит 299', callback_data="bezlimit 299")
bezlimit6 = InlineKeyboardButton(text='+Безлимит 499', callback_data="bezlimit 499")
bezlimit7= InlineKeyboardButton(text='+Безлимит 999', callback_data="bezlimit 999")
bezlimit.add(bezlimit1, bezlimit2, bezlimit3, bezlimit4, bezlimit5, bezlimit6, bezlimit7)

socseti = InlineKeyboardMarkup(row_width=2)
socseti1 = InlineKeyboardButton(text='+Соцсети 65', callback_data="socseti 65")
socseti2 = InlineKeyboardButton(text='+Соцсети 105', callback_data="socseti 105")
socseti3 = InlineKeyboardButton(text='+Соцсети 165', callback_data="socseti 165")
socseti4 = InlineKeyboardButton(text='+Соцсети 205', callback_data="socseti 205")
socseti.add(socseti1,socseti2,socseti3,socseti4)

som30 = InlineKeyboardMarkup(row_width=2)
som30.add(darkor1,internet1)

som60 = InlineKeyboardMarkup(row_width=2)
som60.add(darkor2,internet2, socseti1, bezlimit1)

som100 = InlineKeyboardMarkup(row_width=2)
som100.add(darkor3,socseti2,bezlimit2, internet3)

som160 = InlineKeyboardMarkup(row_width=2)
som160.add(darkor4,internet4, socseti3, bezlimit3)

som200 = InlineKeyboardMarkup(row_width=2)
som200.add(darkor5,internet5, socseti4, bezlimit4)

operator_username = '@shan212916' 
operator = types.InlineKeyboardMarkup()
button = types.InlineKeyboardButton("Оператор", url=f"https://t.me/{operator_username}")
operator.add(button)


@dp.message_handler(content_types=['text'])
async def start_command(message: types.Message):
    user_id = message.chat.id
    m = chatbot_response(message.text, user_id)
    if m == "tarif":
        await message.answer(text ='Чанд намуд вариант дастрас аст:', reply_markup=tarif)
    elif m == "darkor":
        await message.answer(text ='Чанд намуд вариант дастрас аст:', reply_markup=darkor)
    elif m == "bezlimit":
        await message.answer(text ='Чанд намуд вариант дастрас аст:', reply_markup=bezlimit)
    elif m == "internet":
        await message.answer(text ='Чанд намуд вариант дастрас аст:', reply_markup=internet)
    elif m == "socseti":
        await message.answer(text ='Чанд намуд вариант дастрас аст:', reply_markup=socseti)
    elif m == "100soma":
        await message.answer(text ='Чанд намуд вариант дастрас аст:', reply_markup=som100)
    elif m == "30soma":
        await message.answer(text ='Чанд намуд вариант дастрас аст:', reply_markup=som30)
    elif m == "60soma":
        await message.answer(text ='Чанд намуд вариант дастрас аст:', reply_markup=som60)
    elif m == "160soma":
        await message.answer(text ='Чанд намуд вариант дастрас аст:', reply_markup=som160)
    elif m == "200soma":
        await message.answer(text ='Чанд намуд вариант дастрас аст:', reply_markup=som200) 
    elif m=="problem":
        await message.answer("Бахшиши зиед шуморо бо оператор тамос мекунем", reply_markup=operator)
    elif m == "operator":
        await message.answer("Мутаасифона, мо дархости шуморо дарк карда натавонистем, шумо метавонед барои ин савол ба оператор муроҷиат кунед", reply_markup=operator)
    else:
        await message.answer(text=m)

@dp.callback_query_handler(lambda query: query.data == 'internet')
async def internet_callback(callback_query: types.CallbackQuery):
    internet_markup = InlineKeyboardMarkup(row_width=2)
    internet_markup.add(internet1, internet2, internet3, internet4, internet5)
    await bot.send_message(chat_id=callback_query.message.chat.id, text='Чанд намуд вариант дастрас аст:', reply_markup=internet_markup)

@dp.callback_query_handler(lambda query: query.data == 'socseti')
async def socseti_callback(callback_query: types.CallbackQuery):
    socseti_markup = InlineKeyboardMarkup(row_width=2)
    socseti_markup.add(socseti1, socseti2, socseti3, socseti4)
    await bot.send_message(chat_id=callback_query.message.chat.id, text='Чанд намуд вариант дастрас аст:', reply_markup=socseti_markup)

@dp.callback_query_handler(lambda query: query.data == 'darkor')
async def socseti_callback(callback_query: types.CallbackQuery):
    darkor_markup = InlineKeyboardMarkup(row_width=2)
    darkor_markup.add(darkor1, darkor2, darkor3, darkor4, darkor5)
    await bot.send_message(chat_id=callback_query.message.chat.id, text='Чанд намуд вариант дастрас аст:', reply_markup=darkor_markup)

@dp.callback_query_handler(lambda query: query.data == 'bezlimit')
async def socseti_callback(callback_query: types.CallbackQuery):
    bezlimit_markup = InlineKeyboardMarkup(row_width=2)
    bezlimit_markup.add(bezlimit1, bezlimit2, bezlimit3, bezlimit4, bezlimit5, bezlimit6, bezlimit7)
    await bot.send_message(chat_id=callback_query.message.chat.id, text='Чанд намуд вариант дастрас аст:', reply_markup=bezlimit_markup)



@dp.callback_query_handler()
async def choose(callback: types.CallbackQuery):
    user_id = callback.message.chat.id
    if callback.data == 'darkor':
        await callback.message.answer(text=chatbot_response("darkor", user_id))
    elif callback.data=='internet':
        await callback.message.answer(text=chatbot_response("internet", user_id))
    elif callback.data=='bezlimit':
        await callback.message.answer(text=chatbot_response("bezlimit", user_id))
    elif callback.data=='socseti':
        await callback.message.answer(text=chatbot_response("socseti", user_id))
    elif callback.data=='darkor 30':
        await callback.message.answer(text=chatbot_response("Даркор 30", user_id))
    elif callback.data=='darkor 60':
        await callback.message.answer(text=chatbot_response("Даркор 60", user_id))
    elif callback.data=='darkor 100':
        await callback.message.answer(text=chatbot_response("Даркор 100", user_id))
    elif callback.data=='darkor 160':
        await callback.message.answer(text=chatbot_response("Даркор 160", user_id))
    elif callback.data=='darkor 200':
        await callback.message.answer(text=chatbot_response("Даркор 200", user_id))
    elif callback.data=='internet 35':
        await callback.message.answer(text=chatbot_response("Интернет 35", user_id))
    elif callback.data=='internet 65':
        await callback.message.answer(text=chatbot_response("Интернет 65", user_id))
    elif callback.data=='internet 105':
        await callback.message.answer(text=chatbot_response("Интернет 105", user_id))
    elif callback.data=='internet 165':
        await callback.message.answer(text=chatbot_response("Интернет 165", user_id))
    elif callback.data=='internet 205':
        await callback.message.answer(text=chatbot_response("Интернет 205", user_id))
    elif callback.data=='socseti 65':
        await callback.message.answer(text=chatbot_response("Соцсети 65", user_id))
    elif callback.data=='socseti 105':
        await callback.message.answer(text=chatbot_response("Соцсети 105", user_id))
    elif callback.data=='socseti 165':
        await callback.message.answer(text=chatbot_response("Соцсети 165", user_id))
    elif callback.data=='socseti 205':
        await callback.message.answer(text=chatbot_response("Соцсети 205", user_id))
    elif callback.data=='bezlimit 59':
        await callback.message.answer(text=chatbot_response("Безлимит 59", user_id))
    elif callback.data=='bezlimit 99':
        await callback.message.answer(text=chatbot_response("Безлимит 99", user_id))
    elif callback.data=='bezlimit 149':
        await callback.message.answer(text=chatbot_response("Безлимит 149", user_id))
    elif callback.data=='bezlimit 199':
        await callback.message.answer(text=chatbot_response("Безлимит 199", user_id))
    elif callback.data=='bezlimit 299':
        await callback.message.answer(text=chatbot_response("Безлимит 299", user_id))
    elif callback.data=='bezlimit 499':
        await callback.message.answer(text=chatbot_response("Безлимит 499", user_id))
    elif callback.data=='bezlimit 999':
        await callback.message.answer(text=chatbot_response("Безлимит 999", user_id))
    
    await callback.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)






