# .(number)f
# :(number)
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use plus sig if it positive
# := = place sign to left most position
# : = inser the spaces before positive number
# :, = comma seperator

price1 = 300
price2 = 13222222.1414
price3 = 1022.1111111

print(f"{price1:01}")
print(f"{price2:,.04}")
print(f"{price3:.4f}")
