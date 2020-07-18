# Peyton Thomas
# username and password generator


import string
from random import *
# counter for the loop
x = 1
while x <= 5:
    # username generator
    base_name = 'user'
    characters_user = string.ascii_letters
    # Will be between 10-15 characters, randomly generated
    username_join = "".join(choice(characters_user) for x in range(randint(10, 15)))
    # password generator
    characters_pass = string.ascii_letters+string.punctuation+string.digits
    # Will be between 25-30 characters, randomly generated
    password = "".join(choice(characters_pass) for x in range(randint(25, 30)))

    # Output
    print('username: ' + (base_name + username_join))
    print('password: ' + password)
    print(' ')
    x += 1
