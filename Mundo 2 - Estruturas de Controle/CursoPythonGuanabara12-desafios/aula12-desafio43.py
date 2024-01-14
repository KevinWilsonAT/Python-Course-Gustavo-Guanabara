weight = float(input('How much do you weigh (in Kgs)? '))
height = float(input('How tall are you (in meters)? '))

cmi = weight / (height ** 2)

if cmi < 18.5:
    print('Your Corporeal Mass Index is {:.1f} and is below your ideal weight range'.format(cmi))
elif cmi >= 18.5 and cmi < 25:
    print('Your Corporeal Mass Index is {:.1f} and is in your ideal weight range'.format(cmi))
elif cmi >= 25 and cmi < 30:
    print('Your Corporeal Mass Index is {:.1f} and is slightly above your ideal weight range'.format(cmi))
elif cmi >= 30 and cmi < 40:
    print('Your Corporeal Mass Index is {:.1f} and is above your ideal weight range'.format(cmi))
elif cmi >= 40:
    print('Your Corporeal Mass Index is {:.1f} and is far above your ideal weight range'.format(cmi))