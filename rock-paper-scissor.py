import random

def get_computer_move():
    choices = ['r','p','s']
    return random.choice(choices)

def play_game():
    player_move = input(" --- PICK YOUR MOVE ---  ")
    comp_move = get_computer_move()
    if player_move == 'R' or player_move == 'r':
        if comp_move == 'p':
            print('You Lose!, Computer chose Paper!')
        elif comp_move == 's':
            print('You Win! Computer chose Scissor!')
        else:
            print('It is a Tie!')
    elif player_move == 'P' or player_move == 'p':
        if comp_move == 's':
            print('You Lose! Computer chose Scissor!')
        elif comp_move == 'r':
            print('You Win! Computer chose Rock!')
        else:
            print("It is a Tie!")
    elif player_move == 's' or player_move == 'S':
        if comp_move == 'r':
            print('You Lose! Computer chose Rock!')
        elif comp_move == 'p':
            print('You Win! Computer chose Paper!')
        else:
            print("It is a Tie!")
def play_again():
    print("Do you want to Play again?(Y/N)")
    answer = input("Press Y for Yes and N for No: ")
    if answer == 'Y' or answer == 'y':
        return True
    else:
        return False
    
print("Welcome to Rock Paper Scissor!")
print("Press R for rock, P for Paper and S for Scissor")

while True:
    play_game()
    if not play_again():
        break