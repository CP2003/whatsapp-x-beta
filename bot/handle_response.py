from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time

def send_letter_by_letter(update, text, delay=0.1):
    message = update.message.reply_text("")

    for letter in text:
        message.edit_text(message.text + letter)
        time.sleep(delay)

def handle_response(update, text: str):
    processed = text.lower()

    if 'whatsapp' in processed:
        keyboard = [
            [InlineKeyboardButton('Fouad Mods', callback_data='fouad')],
            [InlineKeyboardButton('Sam Mods', callback_data='sam')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        reply_text = 'Please select your Whatsapp:'
        return reply_text, reply_markup

    reply_text = f"\"{text}\" is not in my database. Try /help to get commands."
    return reply_text, None

# Example usage (assuming you have the update object from the Telegram API)
response_text, reply_markup = handle_response(update, "Hello, how can I help you?")
send_letter_by_letter(update, response_text)
