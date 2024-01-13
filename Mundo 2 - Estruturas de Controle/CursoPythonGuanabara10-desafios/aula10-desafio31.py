# perguntar a distancia de uma viagem em km

dist = int(input("Trip distance: "))
price = 0
tax = 0

# r$ 0,50 para viagens ate 200km

if dist <= 200:
    tax = 0.5
    price = dist * tax
# r$0,45 para viagens > 200km
else:
    tax = 0.45
    price = dist * tax

print('Amount to pay: R${:.2f} ({}km with a tax of R${:.2f} per km)' .format(price, dist, tax))