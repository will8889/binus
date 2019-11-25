def pig_latin(text:str):
    if len(text) >= 2:
        first_char = text[0:1]
        return text[1:len(text)] + first_char + "ay"
    else:
        return "error"

print(pig_latin("python"))