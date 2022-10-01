import random

running = True

while running:
    dice_n = input ('Do you want to roll [One] or [Two] dices?\n')

    # Rolling one dice
    if dice_n == 'One':
        rand_O = random.randint (1, 6)
        print ('You rolled the number', rand_O)

    # Rolling two dices
    elif dice_n == 'Two':
        rand_T1 = random.randint (1, 6)
        rand_T2 = random.randint (1, 6)
        print ('You rolled the number', rand_T1 + rand_T2)
    
    # Invalid option
    else:
        print ('Insert a valid option\n')

    # Doing it again
    redo = input ('Do you want to roll again? [Yes] or [No]?\n')

    if redo == 'Yes':
        running = True

    elif redo == 'No':
        running = False

    else:
        print ('Insert a valid option\n')