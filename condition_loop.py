# sum = 0
# a = int(input("add a"))
# b = int(input("add b"))
# while a <= b and b < 10000:
#     if a % 2  == 1 :
#         sum += a
#     a += 1
# print(sum)
a = 100
b = 200
print(sum(range(a | 1, b+1, 2)))
