def format_number(number):
    if number < 0:
        return None
    number = str(number)
    if len(number) < 3:
        return number