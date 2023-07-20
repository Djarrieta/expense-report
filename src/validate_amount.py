class ValidateAmountResponse:
    amount: float = 0
    message: str = ""

    def formatted(self):
        return "${:,.0f} COP".format(self.amount)


def validate_amount(input: str) -> ValidateAmountResponse:

    response = ValidateAmountResponse()

    try:
        amount = float(input)
        if amount <= 0:
            raise "No valid"
    except ValueError:
        response.message = f'Monto= {input} no es válido.'
        return response

    response.amount = amount
    if (response.amount < 1000):
        response.amount *= 1000

    return response
