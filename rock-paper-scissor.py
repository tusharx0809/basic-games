import random

def get_computer_move():
    choices = ['r','p','s']
    return random.choice(choices)

def play_game(player_score, computer_score, ties):   #Here passing the values of Player and computer scores
    player_move = input(" --- PICK YOUR MOVE ---  ")
    comp_move = get_computer_move()
    if player_move == 'R' or player_move == 'r':
        if comp_move == 'p':
            print('You Lose! Computer chose Paper!')
            computer_score += 1
        elif comp_move == 's':
            print('You Win! Computer chose Scissor!')
            player_score += 1
        else:
            print('Computer chose Rock! It is a Tie!')
            ties += 1
    elif player_move == 'P' or player_move == 'p':
        if comp_move == 's':
            print('You Lose! Computer chose Scissor!')
            computer_score += 1
        elif comp_move == 'r':
            print('You Win! Computer chose Rock!')
            player_score += 1
        else:
            print("Computer chose Paper! It is a Tie!")
            ties += 1
    elif player_move == 's' or player_move == 'S':
        if comp_move == 'r':
            print('You Lose! Computer chose Rock!')
            computer_score += 1
        elif comp_move == 'p':
            print('You Win! Computer chose Paper!')
            player_score += 1
        else:
            print("Computer chose Scissor! It is a Tie!")
            ties += 1
    return player_score, computer_score, ties #return these values so we can store them later to print
def play_again():
    print("Do you want to Play again?(Y/N)")
    answer = input("Press Y for Yes and N for No: ")
    if answer == 'Y' or answer == 'y':
        return True
    else:
        return False
    
player_score = 0
computer_score = 0
ties = 0
print("Welcome to Rock Paper Scissor!")
print("Press R for rock, P for Paper and S for Scissor")

while True:
    player_score, computer_score, ties = play_game(player_score, computer_score, ties) #call this function to store the value and keep a track of scores
    if not play_again(): #if player chooses not to play, then print the scores and break out of loop
        print("Player Score:", player_score, "Computer Score:", computer_score, "Ties:", ties) 
        break