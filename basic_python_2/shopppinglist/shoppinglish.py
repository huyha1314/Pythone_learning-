
list = []
listp =[]
total = 0

while True:
    food = input("Pls input the item for shopping ")
    if food.upper() == "Q":
        break
    else:
        price = float(input("Pls input the price for shopping "))
        print("type q to quit")
    list.append(food)
    listp.append(price)
print("THE SHOPPING LIST \n _________________________")
for name in list:
    print(name , end=" ")
for i in listp:
    total +=i
print()
print(f"total price {total}VND")