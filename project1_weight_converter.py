weight = input("enter the weight: ")
L_or_K = input("(L)bs or (K)kg: ")
if L_or_K.upper() == "L":
    kg = 0.454 * int(weight)
    print(f"weight : {kg} kg")
else:
    pd = int(weight)/0.454
    print(f"you weight is : {pd} pounds")
