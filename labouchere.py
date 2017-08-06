'''labouchere.py

PURPOSE:    This script runs the Labouchere gambling method in American
            Roulette. This script just allows for keeping a constant bet on
            RED, and does not allow for betting on black, evens, or odds.

FURTHER
READING:    For information on how this method works, see the following:
            https://en.wikipedia.org/wiki/Labouch%C3%A8re_system

            The gamble() function is based off of the code given in the
            aforementioned website.

AUTHOR:     Nicholas P. Taliceo
            ntaliceo@gmail.com  |  www.NicholasTaliceo.com

DATE:       August 06, 2017
'''

import random


def spins():
    slots = {'00': 'green', '0': 'green', '1': 'red', '2': 'black',
             '3': 'red', '4': 'black', '5': 'red', '6': 'black', '7': 'red',
             '8': 'black', '9': 'red', '10': 'black', '11': 'red',
             '12': 'black', '13': 'red', '14': 'black', '15': 'red',
             '16': 'black', '17': 'red', '18': 'black', '19': 'red',
             '20': 'black', '21': 'red', '22': 'black', '23': 'red',
             '24': 'black', '25': 'red', '26': 'black', '27': 'red',
             '28': 'black', '29': 'red', '30': 'black', '31': 'red',
             '32': 'black', '33': 'red', '34': 'black', '35': 'red',
             '36': 'black'}

    global winning_number
    winning_number = int(random.choice(list(slots.keys())))
    return winning_number


def win_loss(winning_number):
    if (winning_number % 2 == 0) and (winning_number != 0):
        win = True
    else:
        win = False
    return win


def gamble(sequence, balance):
    global adj_bankroll

    # Won
    if len(sequence) < 1:
        prompt =  "You won with an ending balance of $%s" % balance
        adj_bankroll = balance
        return(prompt, adj_bankroll)

    # If the sequence is of length 1, the bet is the number in the sequence.
    # Otherwise, it is the first number added to the last number.
    if len(sequence) is 1:
        bet = sequence[0]
    else:
        bet = sequence[0] + sequence[-1]

    # Lost the entire round
    if bet > balance:
        prompt =  "You have insufficient funds at $%s" % balance
        adj_bankroll = balance
        return(prompt, adj_bankroll)

    spins()

    if win_loss(winning_number):
        # Won
        return gamble(sequence[1:-1], balance+bet)
    else:
        # Lost bet
        return gamble(sequence+[bet], balance-bet)


sequence = [5, 5, 5]
bankroll = int(input("What is your starting balance (in whole $$): "))
while bankroll > 0:
    (prompt, balance) = gamble(sequence, bankroll)
    print(prompt)
    bankroll = balance
    sequence = [5, 5, 5]
