def increment(number, by):
    return number + by

result = increment(5, by=2)
print(result)

#defaut argument
def increment(number, by=1):
    return number + by

result = increment(5)
print(result)