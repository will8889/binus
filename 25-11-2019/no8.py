def generate_n_chars(number:int,character:str):
    text:str = ""
    for i in range(number):
        text+=character
    return text

print(generate_n_chars(10, "x"))