from telegram.ext import (ApplicationBuilder,
                          MessageHandler, filters)

from message_handler  import message_handler
from config import TELEGRAM_TOKEN

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters=filters.ALL,
                callback=message_handler))
app.run_polling()
