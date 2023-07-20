from telegram import Update
from telegram.ext import ContextTypes


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response=update.message.text
    
    await update.message.reply_text(f'{response}')