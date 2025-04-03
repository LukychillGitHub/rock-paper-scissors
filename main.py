import random


print ('===================\nRock Paper Scissors\n===================')
print('')
print ('1) ✊\n2) ✋\n3) ✌️')


player = int(input('Option: '))
while(player<1 or player>3):
    player = int(input('wrong choice, try again: '))

computer = random.randint(1,3)

choice = 'null'

if (player == 1):
    choice = 'rock'
elif (player == 2):
    choice = 'paper'
elif (player == 3):
    choice = "scissors"

if (computer == 1):
    compchoice = 'rock'
elif (computer == 2):
    compchoice = 'paper'
elif (computer == 3):
    compchoice = "scissors"

if (player == computer):
    print ('draw // your choice: ' + choice + ' / ' + 'computer choice: ' + compchoice)
elif ((player==1 and computer==3)or(player==2 and computer==1)or(player==3 and computer==2)):
    print('Player is the winner! your choice: ' + choice + ' / ' + 'computer choice: ' + compchoice)
else:
    print('Computer is the winner! your choice: ' + choice + ' / ' + 'computer choice: ' + compchoice)