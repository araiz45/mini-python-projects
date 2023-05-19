import random

player_score = 0
computer_score = 0
def play():
    player = input('[s] for snake , [g] for gun and [w] for water | What\'s your choice :  ')
    computer = random.choice(['s', 'w', 'g'])
    print(computer)

    if player == computer:
        print('it\'s tie')
        return 0

    if is_wins(player, computer):
        # player_score += 1
        print('You won')
        return 1

    # computer_score += 1
    print('computer won')
    return 2


def is_wins(player, opponent):
    if (player == 's' and opponent == 'w') or (player == 'w' and opponent == 'g') or \
    (player == 'g' and opponent == 's'):
        return True


for x in range(1,10):
    result = play()
    if result == 1:
        player_score += 1
        print(f"Score of Player | {player_score} : Score of Computer {computer_score}")

    if result == 2:
        computer_score += 1
        print(f"Score of Computer | {computer_score} : Score of Player | {player_score}")

    print(f'turn : {x}')

if player_score > computer_score:
    print(f"Hurray! Human Wins this match and player score is {player_score} and computer is {computer_score}")
elif player_score < computer_score:
    print(f"Hurray! Computer Wins this match and computer score {computer_score} and human score is {player_score}")
else:
    print(f"The Match is tie and the score of human is {player_score} and computer is {computer_score}")


input("The Game has been ended. press Enter to exit...")