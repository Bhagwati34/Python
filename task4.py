good_Credit = False
price =  int(1000000)
if good_Credit:
    down_payment= 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment : ${down_payment}")
