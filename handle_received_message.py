from telegram import Update
from telegram.ext import ContextTypes


async def handle_received_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response="""
            Me haz enviado un número, qué quieres hacer? """
    
    await update.message.reply_text(f'{response}')