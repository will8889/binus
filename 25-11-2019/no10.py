def earning(hours:int, rate:int):
    return hours*rate if hours <= 40 else round(hours*rate*1.5)

print(earning(int(input(' Enter number of hours: ')),int(input('Enter the rate: '))))