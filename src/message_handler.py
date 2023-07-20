from telegram import Update
from telegram.ext import ContextTypes
from Repository import Repository

spends = Repository()


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    text_message = update.message.text
    splitted_text=text_message.split(",")

    if(len(splitted_text)<2):
        await update.message.reply_text(f'No comprendo lo que me envías. Coloca "50, restaurante" para registrar $50.000 COP con la descripción "Restaurante"')
        return

    amount_string = text_message.split(",")[0]
    description = text_message.split(",")[1]

    if not amount_string.isdigit() :
        await update.message.reply_text(f'Monto= {amount_string} no es válido.')
        return
    
    amount=0
    try:
        amount = float(amount_string)  # Intentar convertir la cadena a un número flotante
        if amount <= 0:
            await update.message.reply_text(f'Monto= {amount_string} no es válido.')
            return
    except ValueError:
        pass

    if description == "":
        await update.message.reply_text(f'Descripción= {description} no es válida.')
        return

    if amount < 1000:
        amount = amount*1000

    description = description.lstrip().capitalize()

    spends.create_one(amount, description)
    print(spends.get_all())

    await update.message.reply_text(f'He registrado {amount} bajo el concepto de "{description}"')
