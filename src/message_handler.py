from telegram import Update
from telegram.ext import ContextTypes
from Repository import Repository
from validate_amount import validate_amount
from validate_description import validate_description

spends = Repository()


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    text_message = update.message.text
    splitted_text = text_message.split(",")

    if (len(splitted_text) < 2):
        await update.message.reply_text(f'No comprendo lo que me envías. Coloca "50, restaurante" para registrar $50.000 COP con la descripción "Restaurante"')
        return

    amount_string = splitted_text[0]
    unformatted_description = splitted_text[1]

    validated_amount = validate_amount(amount_string)
    if not validated_amount.message == "":
        await update.message.reply_text(validated_amount.message)
        return

    validated_description = validate_description(unformatted_description)
    if not validated_description.message == "":
        await update.message.reply_text(validated_description.message)
        return

    spends.create_one(validated_amount.amount,
                      validated_description.description)
    print(spends.get_all())

    await update.message.reply_text(f'He registrado {validated_amount.formatted()} bajo el concepto de "{validated_description.description}"')
