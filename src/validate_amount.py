class ValidateAmountResponse:
    amount:float=0
    message:str=""

    def formatted(self):
        return "${:,.0f} COP".format(self.amount)

def validate_amount(input:str)-> ValidateAmountResponse:

    response=ValidateAmountResponse()

    if not input.isdigit() :
        response.message=f'Monto= {input} no es válido.'
        return response
    
    try:
        amount = float(input) 
        if amount <= 0:
            response.message=f'Monto= {input} no es válido.'
            return response
    except ValueError:
        response.message=f'Monto= {input} no es válido.'
        return response
    

    response.amount=amount
    if(response.amount<1000):
        response.amount*=1000

    return response