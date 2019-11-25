def length(text:str):
    length:int = 0
    for i in text:
        length+=1
    return length

print(length([1,2,3]))
print(length("hello"))