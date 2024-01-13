colors = {
    'clean': '\033[m',
    'celsius': '\033[0;33m',
    'fahrenheit': '\033[0;31m'
}

c = float(input('Temperature in °C: '))
f = ((9 * c) / 5) + 32

print('The temperature of {}{}{}°C is equivalent to {}{}{}°F'
      .format(colors['celsius'], c, colors['clean'],
              colors['fahrenheit'], f, colors['clean']))
