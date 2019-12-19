'''
Iterative Prisoner's Dillema Team Submission

In this file, you MUST define the following:

Variables:
  - team_name:            a string with your team's name
  - strategy_name:        a string with your team's strategy name
  - strategy_description: a string with your team's strategy name

Functions:
  - move(my_last_move, their_last_move):
    your team's implementation of your strategy (see move() docstring)
'''

team_name = 'TEAM 3'
team_members = ['Max Vogel', 'Bert', 'David', 'Aidan']
strategy_name = 'Tat for Tit'
strategy_description = 'Tit for Tat, but we always start with betraying'


def move(my_last_move, their_last_move):
    """
    Make my move based on the history with this player.

    my_last_move: a one letter String (c or b) that represents the last move you made
        against your opponent
    their_last_move: a one letter String (c or b) that represents the last move your
        opponent made against you
    Returns 'c' or 'b' for collude or betray.
    """

    if not my_last_move:  # first move of the game
        return 'b'
    return their_last_move


if __name__ == '__main__':
    move()
