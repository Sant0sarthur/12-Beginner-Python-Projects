import random 

def play():
    user = input("[r] for rock, [p] for papper, [s] for scissors. \n->").lower()
    computer = random.choice (['r', 'p', 's'])

    print(f'Your choice {user} \nComputer choices {computer} ')
    if user == computer: 
        return  'tie'
    if is_win(user, computer):
        return 'You won! ;)'
    
    return 'you lost! ;)'
    
def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player ==  'r' and opponent == 's') or \
        (player ==  's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r'):
        return True

print (play())