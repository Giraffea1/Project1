choiceString = input(
    'Hi, what kind of sandwich would you like to order today?\n')
choices = choiceString.split()

if 'choices' in choices:
    print(True)
