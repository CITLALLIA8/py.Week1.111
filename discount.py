DISCOUNT_RATE = -1
TAXI_RATE=.06
subtotal=float(input("Enter the subtotal: "))
print(f"Total order{subtotal}")
discount=subtotal * DISCOUNT_RATE
print(f"Discount {discount}")
subtotal-=discount
tax=subtotal * TAXI_RATE
total=subtotal + tax
print(f"Tax {tax}")
print(f"Total Due {total}")