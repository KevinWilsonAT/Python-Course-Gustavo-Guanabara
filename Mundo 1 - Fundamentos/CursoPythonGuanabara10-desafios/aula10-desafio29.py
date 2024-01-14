spd = int(input("Car's current speed: "))
tspd = spd - 80
ticket = 7.00 * tspd

if spd > 80:
    print("You'll be fined in R${:.2f} ({}km above the allowed)" .format(ticket, tspd))
