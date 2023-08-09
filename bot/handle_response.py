from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from bot.whatsapp import whatsapp_command, send_fouad_mod_options, send_sam_mod_options, send_fmmods_whatsapp_file, send_fmmods_fm_whatsapp_file, send_fmmods_gb_whatsapp_file, send_fmmods_yo_whatsapp_file, send_com_whatsapp_file, send_com_gbwhatsapp_file, send_com_gbwhatsapp2_file, send_com_gbwhatsapp3_file, send_fouad_mod_options_inline, send_sam_mod_options_inline 

def handle_response(text: str):
    processed = text.lower()

    if 'whatsapp' in processed:
    # Send reply message with inline buttons
        keyboard = [
        [InlineKeyboardButton('Fouad Mods', callback_data='fouad')],
        [InlineKeyboardButton('Sam Mods', callback_data='sam')]
         ]    
        reply_markup = InlineKeyboardMarkup(keyboard)
        return 'Please select your Whatsapp:', reply_markup

    return f"\"{text}\" is not in my data basse  \n \n \n  Try /help to get commands", None

