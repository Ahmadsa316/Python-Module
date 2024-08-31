zander_lenght = int(input('please enter your zander length in centimeters'))
if zander_lenght > 41:
    print('great catch')
elif zander_lenght <41:
    lenght_needed = 42 - zander_lenght
    print(f'please release the fish back into the sea because it is smaller by {lenght_needed}cm')