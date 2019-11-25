def max_of_three(number_1:int,number_2:int,number_3:int):
    if number_1 > number_2 and number_1 > number_3:
        return number_1
    
    elif number_2 > number_1 and number_2 > number_3:
        return number_2

    else:
        return number_3

print(max_of_three(10, 20, 30))