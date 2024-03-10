
def get_input_from_user(request, input_type, greater_than=None):
    """
    Getting input in a correct format from a user
    :param request: question to the user
    :param input_type: required type of the input
    :param greater_than: optional condition that the input should be greater than a given number
    :return: user input in the given input type
    """
    allowed_types = {str, int, float}

    if input_type not in allowed_types:
        raise ValueError("Invalid input_type")
    while True:
        try:
            user_input = input(f"{request}\n")
            converted_input = input_type(user_input)
            if greater_than is not None:
                if converted_input > greater_than:
                    return converted_input
                else:
                    print(f"Your number {user_input} is lower than {greater_than}")
            else:
                return converted_input
        except ValueError as ve:
            print(f"Invalid input. Please provide a valid {input_type}.")

