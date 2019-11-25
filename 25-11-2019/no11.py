def distance_from_zero(number):
    if(type(number) == type(0) or type(number) == type(1.0)):
        return abs(number)
    else:
        return "Nope"

print(distance_from_zero(-5.6))
print(distance_from_zero('what?'))