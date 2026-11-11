def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Invalid integer: '{value}' - Number only allowed")
try:
    result = safe_convert('123') #instead of numbers use alphabets to see the error output
    print(result)
except ValueError as error:
    print(error)