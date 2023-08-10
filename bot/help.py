import os 
import asyncio
from telegram import Update
from telegram.ext import CallbackContext
ADMIN_USER_ID = os.environ.get('ADMIN_USER_ID')

options = [
    "/whatsapp - to get WhatsApp mod apks",
    "/count - to get user count",
    "/cast - to send broadcast msg to users",
    "/ccast - to send msg to chanel",
    "/allvar - to get all heroku variables",
    "/edit - to edit heroku variables"
]

async def send_and_edit(update, text_list):
    message = await update.message.reply_text("")
    for text in text_list:
        await message.edit_text(text)
        await asyncio.sleep(0.1)

async def help_command(update: Update, context: CallbackContext):
    message_type: str = update.message.chat.type
    user_id: str = str(update.message.chat.id)
    username: str = update.message.from_user.username
    first_name: str = update.message.from_user.first_name
    last_name: str = update.message.from_user.last_name
    user_id = str(update.message.from_user.id)
    group_chat_id = -707701170
    
    if not username:
        username = f"{first_name} {last_name}" if first_name and last_name else "Anonymous"
    elif user_id == ADMIN_USER_ID:
        username = "@Admin"
        await context.bot.send_message(chat_id=group_chat_id, text=f'{username} in {message_type}: "/help"')
        await context.bot.send_chat_action(chat_id=user_id, action='typing')
        await asyncio.sleep(1)
        await send_and_edit(update, options)
    else:
        username = f"@{username}"
        await context.bot.send_message(chat_id=group_chat_id, text=f'{username} in {message_type}: "/help"')
        await context.bot.send_chat_action(chat_id=user_id, action='typing')
        await asyncio.sleep(1)
        message = await update.message.reply_text(f'⭕️ /whatsapp ')
        await asyncio.sleep(1)
        await context.bot.edit_message_text(chat_id=user_id, message_id=message.message_id, text=f'⭕️ /whatsapp \n -     to get WhatsApp mod apks')
