colors = {
    'clean': '\033[m',
    'fine': '\033[0;32m',
    'km': '\033[0;36m'
}

spd = int(input("Car's current speed: "))
tspd = spd - 80
ticket = 7.00 * tspd


if spd > 80:
    print("You'll be fined in {}R${:.2f}{} ({}{}km{} above the allowed)"
          .format(colors['fine'], ticket, colors['clean'], colors['km'], tspd, colors['clean']))