successful = True
for number in range(1, 10, 2):
    print("Attempt", number, (number + 1) * '.')
    if successful:
        print("successfull")
        break
else:
    print("attemp fail")
