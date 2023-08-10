from telegram import InlineKeyboardButton , InlineKeyboardMarkup , Update

def handle_response(text: str):
    processed = text.lower()

    if 'whatsapp' in processed:
        return text_wha(query)

    return f"\"{text}\" is not in my data basse  \n \n \n  Try /help to get commands", None


async def text_wha(query):
    await query.message.edit_text(text="Download Fouad Mod Whatsapp APK files - Fouad Mods")
    keyboard = [
        [InlineKeyboardButton('Whatsapp', callback_data='fmmods_whatsapp')],
        [InlineKeyboardButton('FM Whatsapp', callback_data='fmmods_fmwhatsapp')],
        [InlineKeyboardButton('GB Whatsapp', callback_data='fmmods_gbwhatsapp')],
        [InlineKeyboardButton('Yo Whatsapp', callback_data='fmmods_yowhatsapp')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_reply_markup(reply_markup=reply_markup)

