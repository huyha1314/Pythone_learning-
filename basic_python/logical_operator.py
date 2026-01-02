high_income = False 
good_credit = True
student = False 

if (high_income or good_credit) and not student: # short cicuit mean that when move in the logical it stop when the command solve the beginning problem
    print("eligible")
else:
    print("not eligible")
