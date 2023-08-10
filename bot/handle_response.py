from telegram import InlineKeyboardButton , InlineKeyboardMarkup

def handle_response(text: str):
    processed = text.lower()

    if 'whatsapp' in processed:
        whatsapp_opt()

    return f"\"{text}\" is not in my data basse  \n \n \n  Try /help to get commands", None


async def whatsapp_opt(update: Update):
    user_id = str(update.message.from_user.id)

    # Create an inline keyboard with the options
    keyboard = [
        [InlineKeyboardButton('Whatsapp', callback_data='fmmods_whatsapp')],
        [InlineKeyboardButton('FM Whatsapp', callback_data='fmmods_fmwhatsapp')],
        [InlineKeyboardButton('GB Whatsapp', callback_data='fmmods_gbwhatsapp')],
        [InlineKeyboardButton('Yo Whatsapp', callback_data='fmmods_yowhatsapp')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message to the user
    await update.message.reply_text('Download Fouad Mod Whatsapp APK files:', reply_markup=reply_markup)
