# Roulette Simulator
Python simulation games for roulette.  Includes scripts to simulate strategic roulette betting techniques.

## About
This repository contains Python 3 scripts that not only simulate the game of American Roulette, but also take into account the simulation of roulette betting techniques.

Despite some sort term sucesses, it seems as though the [risk of ruin](https://en.wikipedia.org/wiki/Risk_of_ruin) is generally too great, and the result is an ultimate bust.

## Author Information
*Author*: Nicholas P. Taliceo

*Date Created*: August 06, 2017

## Files 

- general.py
  - A script that simulates a manual game of roulette. Asks the user for the type of bet, the starting bankroll, and the bid. 
- labouchere.py
  - Simulates the Labouchere method of stragetic roulette betting.
  - The idea behind this method is to create a sequence of bets. 
    - I often use a constant bet which is the table's minimum (often $5).
    - This method can only be used when betting on all evens, odds, red, or black (I usually choose red).
    - A sequence of bets is made: $5-$5-$5-$5, and the sum of the first and last bet is used as each bet in the sequence (the first bet would be $5 + $5 = $10).
    - If successful, then we would remove the first and last bet (~~$5~~-$5-$5-~~$5~~).
    - If unsuccessful, then the the current bet would be added to this sequence ($5-$5-$5-$5-$10), and the process begins again.
    - The total amount of money won is the sum of the original sequence of numbers: $5 + $5 + $5 + $5 = $20.
  - **Example:**
    - Initial bankroll = $50
    - Sequence = $5-$5-$5-$5
    - Projected amount won = $20
    - **Bet 1:** $10 -- Won 
      - Balance: $50 + $10 = $60
      - Revised Sequence: $5-$5
    - **Bet 2:** $10 -- Loss
      - Balance: $60 - $10 = $50
      - Revised Sequence: $5-$5-$10
    - **Bet 3:** $15 -- Won
      - Balance: $50 + 15 = $65
      - Revised Sequence: $5
    - **Bet 4:** $5 -- Won
      - Balance: $65 + $5 = $70
      - Revised Sequence: N/A
    - **Total Amount Won: $20**
