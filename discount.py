price = int(input("Enter the buying price: "))
if price < 100:
  discount = price * 0
elif price <= 1000:
  discount = price * 0.1
else:
  discount = price * 0.20

#discount = price * 0.20
total = price - discount

print(f"The buying price is {price} and the total discount is {discount}. Therefore the buying price is: {total}")