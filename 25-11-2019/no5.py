def reverse(text:str):
    reversed_text:str = " "               #
    for i in range(len(text)-1,-1,-1):    #
        reversed_text += text[i]          #
    #return text [::-1]
    return reversed_text

print(reverse("I am testing"))