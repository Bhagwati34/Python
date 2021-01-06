high_income = True
good_credit = True
# AND operation
if high_income and good_credit:
    print("Eligible for lone (with logical AND operation)")
else:
    print("Not Eligible for lone")

# Or operation
high_income = True
good_credit = False
if high_income or good_credit:
    print("Eligible for lone (with logical OR operation)")
else:
    print("Not Eligible for lone")

# NOT operator
good_credit = True
criminal_record = False
if good_credit and not criminal_record:
    print("Eligible for lone (with logical NOT operation)")
else:
    print("Not Eligible for lone")




