
import random
random_number = random.randint(1,30)

while True:
    user_input = int(input('맞춰보세요'))
    if user_input == random_number :
        print('정답')
        break
    elif user_input < random_number :
        print('up')
    elif user_input > random_number :
        print('down')
        