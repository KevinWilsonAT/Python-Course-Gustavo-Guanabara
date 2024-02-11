# ask the distance of a trip in km

dist = int(input("Trip distance: "))
price = 0
tax = 0

# R$0,50 to trips until 200km

if dist <= 200:
    tax = 0.5
    price = dist * tax
# R$0,45 to trips > 200km
else:
    tax = 0.45
    price = dist * tax

print('Amount to pay: R${:.2f} ({}km with a tax of R${:.2f} per km)' .format(price, dist, tax))
