price = float(input("Enter the price: "))
if price < 500:
    discount = 0.2
    final_price = price - (price * discount)
elif price <= 200 and price >=500:
    discount = 0.1
    final_price = price - (price * discount)
else:
    final_price = price
print("The final price is:", final_price)