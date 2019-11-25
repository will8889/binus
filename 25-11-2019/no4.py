def vowel(characters:str):
    vowels = ["a","i","u","e","o","A","I","U","E","O"]
    for i in range(len(vowels)):
        if vowels[i] == characters:
            return True
    return False

print(vowel("A"))
