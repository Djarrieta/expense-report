class ValidateDescriptionResponse:
    description:str=""
    message:str=""

def validate_description(input:str)-> ValidateDescriptionResponse:

    response=ValidateDescriptionResponse()

    if input == "":
        response.message=f'Descripción= {input} no es válida.'
        return

    response.description=input.lstrip().capitalize()

    return response