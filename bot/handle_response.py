from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import time

def send_letter_by_letter(update: Update, text: str, delay=0.1):
    message = update.message.reply_text("")  # Send an empty message to obtain the message object

    for letter in text:
        message.edit_text(message.text + letter)  # Edit the message by adding one letter at a time
        time.sleep(delay)

def handle_response(update: Update, text: str):
    processed = text.lower()

    if 'whatsapp' in processed:
        keyboard = [
            [InlineKeyboardButton('Fouad Mods', callback_data='fouad')],
            [InlineKeyboardButton('Sam Mods', callback_data='sam')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        text = 'Please select your Whatsapp:'
        return send_letter_by_letter(text) ,reply_markup

    reply_text = f"\"{text}\" is not in my database. Try /help to get commands."
    return reply_text, None

# Example usage (assuming you have the update object from the Telegram API)
