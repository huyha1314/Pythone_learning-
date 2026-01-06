count = 0
for number in range(1, 10):
    if (number % 2 == 1):
        print(number, "is an odd")
    else:
        print(number, "is an even")
        count += 1
print(count)