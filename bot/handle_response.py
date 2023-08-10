from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import asyncio

async def send_letter_by_letter(update: Update, text: str, delay=0.1):
    message = await update.message.reply_text("")  # Send an empty message to obtain the message object

    for letter in text:
        await message.edit_text(message.text + letter)  # Edit the message by adding one letter at a time
        await asyncio.sleep(delay)

def handle_response(update: Update, text: str):
    processed = text.lower()

    if 'whatsapp' in processed:
        return whatsapp_opt(update)

    reply_text = f"\"{text}\" is not in my database. Try /help to get commands."
    return reply_text, None

async def whatsapp_opt(update: Update):
    user_id = str(update.message.from_user.id)

    keyboard = [
        [InlineKeyboardButton('Whatsapp', callback_data='fmmods_whatsapp')],
        [InlineKeyboardButton('FM Whatsapp', callback_data='fmmods_fmwhatsapp')],
        [InlineKeyboardButton('GB Whatsapp', callback_data='fmmods_gbwhatsapp')],
        [InlineKeyboardButton('Yo Whatsapp', callback_data='fmmods_yowhatsapp')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    reply_text = 'Download Fouad Mod Whatsapp APK files:'
    await send_letter_by_letter(update, reply_text)
    await asyncio.sleep(1)  # Wait for a moment before sending the reply_markup
    await query.message.reply_text('', reply_markup=reply_markup)  # Use query.message to reply

# Example usage (assuming you have a valid Update object and query object)
your_update_object = ...  # Replace this with your actual Update object
your_query_object = ...   # Replace this with your actual query object from the callback
response_text, reply_markup = handle_response(your_update_object, "Hello, how can I help you?")
await send_letter_by_letter(your_update_object, response_text)
