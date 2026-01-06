principle = 0
rate = 0 
time = 0 

while principle <= 0:
    principle = float(input("pls add your principle "))
    if principle <= 0:
        print("wrong adding principle must > 0")
        principle = float(input("pls add your principle "))
while rate <= 0:
    rate = float(input("pls add your rate "))
    if rate <= 0:
        print("wrong adding rate must > 0")
        rate = float(input("pls add your rate "))
while time <= 0:
    time = int(input("pls add your time "))
    if time <= 0:
        print("wrong adding time must > 0")
        time = int(input("pls add your time "))


interest = principle* pow((1+rate/100),time)

print(f"Your Balance is {interest:.2f}$")