from telegram import InlineKeyboardButton , InlineKeyboardMarkup

def handle_response(text: str):
    processed = text.lower()

    if 'whatsapp' in processed:
        return senwa(query)

    return f"\"{text}\" is not in my data basse  \n \n \n  Try /help to get commands", None


async def senwa(query):
    await query.message.edit_text(text="Download Fouad Mod Whatsapp APK files - Fouad Mods")
    keyboard = [
        [InlineKeyboardButton('Fouad Mods', callback_data='fouad')],
        [InlineKeyboardButton('Sam Mods', callback_data='sam')]
         ]    
    return 'Please select your Whatsapp:', reply_markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_reply_markup(reply_markup=reply_markup)

