from telegram import Update
from telegram.ext import ContextTypes
from Repository import Repository

spends = Repository()
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    text_message = update.message.text

    amount = int(text_message.split(",")[0])
    description = text_message.split(",")[1]

    if amount <= 0:
        await update.message.reply_text(f'Monto= {amount} no es válido.')
        return

    if description == "":
        await update.message.reply_text(f'Descripción= {description} no es válida.')
        return

    if amount < 1000:
        amount = amount*1000

    description = description.lstrip()

    spends.create_one(amount, description)
    print(spends.get_all())

    await update.message.reply_text(f'amount= {amount}; description= {description}')
