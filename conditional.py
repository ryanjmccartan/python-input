price = 1000000

good_credit = True

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

name = "Ryan"


if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be less than 50 characters")
else:
    print("Name looks good")
