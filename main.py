from telegram.ext import (ApplicationBuilder,
                          MessageHandler, filters)

from config import TELEGRAM_TOKEN
from .handle_received_message import handle_received_message

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters=filters.ALL,
                callback=handle_received_message))
app.run_polling()