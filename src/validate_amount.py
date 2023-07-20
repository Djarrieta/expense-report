class ValidateAmountResponse:
    amount: float = 0
    message: str = ""

    def formatted(self):
        return "${:,.0f} COP".format(self.amount)


def validate_amount(amount_as_string: str) -> ValidateAmountResponse:

    response = ValidateAmountResponse()

    try:
        amount = float(amount_as_string)
        if amount <= 0:
            raise
    except ValueError:
        response.message = f'Monto= {amount_as_string} no es válido.'
        return response

    response.amount = amount
    if (response.amount < 1000):
        response.amount *= 1000

    return response
