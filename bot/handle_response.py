from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time

def print_letter_by_letter(update, text, delay=0.1):
    for letter in text:
        update.message.reply_text(letter, parse_mode='Markdown')
        time.sleep(delay)

def handle_response(text: str):
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
