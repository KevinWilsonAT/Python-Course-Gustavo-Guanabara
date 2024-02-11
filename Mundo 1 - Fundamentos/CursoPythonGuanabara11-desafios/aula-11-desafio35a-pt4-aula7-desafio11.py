colors = {
    'clean': '\033[m',
    'height': '\033[0;31m',
    'width': '\033[0;32m',
    'area': '\033[0;33m',
    'ink': '\033[0;34m'
}

height = float(input("Wall's height (in meters): "))
width = float(input("Wall's width(in meters): "))
area = height * width
ink = area/2

print('Your wall has {}{}{} x {}{}{} in dimension, its area is {}{}{}m² '
      .format(colors['height'], height, colors['clean'], colors['width'], width, colors['clean'],
              colors['area'], area, colors['clean']))

print('To paint the wall, you will need {}{}{}l of ink'.format(colors['ink'], ink, colors['clean']))
