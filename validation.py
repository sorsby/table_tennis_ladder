import string


def data_validation(name):
    if name == str(name):
        name = name
    else:
        name = name[0]
    invalid_chars = set(string.punctuation.replace("_", ""))
    if len(name) >= 20:
        print("Input must be less than 20 characters long.")
        return False
    elif any(char in invalid_chars for char in name):
        print("Input must not contain punctuation.")
        return False
    elif " " in name:
        print("Input must not contain spaces.")
        return False
    else:
        return True
    



