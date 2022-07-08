import random

class RockPaperScissors:
    def play():
        user = input("'r' for rock, 'p' for paper, 's' for scissors \n ")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            return "It's a tie"
        
        if RockPaperScissors.is_win(user, computer):
            return "you won"
        else:
            return "you lost"

    # return true if the player wins
    # r > s, s > p, p>r
    def is_win(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True
        else:
            return False




gameStarted = RockPaperScissors
print(gameStarted.play())