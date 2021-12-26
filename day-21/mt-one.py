pos1 = 8
pos2 = 1

score1 = 0
score2 = 0

turn1 = True
dice = list(range(1,101))
#dice2 = ([x for x in range(1,100)])
print(dice)
#print(dice2)
diceRolls = 0
dicePos = 0

while score1 < 1000 and score2 < 1000:
    # check if dice is over 100
        # if it is, reset 
    if dicePos >= len(dice):
        dicePos = dicePos % 100
    roll1 = dice[dicePos]
    roll2 = dice[dicePos]+1
    roll3 = dice[dicePos]+2

    # special case when a roll contains #s > 99
    if roll1 >= 99:
        if roll1 == 99:
            roll2 = 100
            roll3 = 1
        else:
            roll2 = 1
            roll3 = 2

    rolled = roll1 + roll2 + roll3
	
    if rolled >= 10:
		# made a lap
        # rolled = 17 % 10 = 7
	    rolled = rolled % 10
	
    if turn1:
        # player 1 turn to roll. 
        pos1+= rolled
        if pos1 > 10:
        # pos1 = 15 % 10 = 5
	        pos1 = pos1 % 10
        score1+= pos1
        turn1 = False
		
    else:
        # player 2 turn to roll. 
        pos2+= rolled
        if pos2 > 10:
            pos2 = pos2 % 10
        score2+= pos2
        turn1 = True

    diceRolls+=3
    dicePos+=3

# broke while loop, we have a winner 
print(F"congrats player 1: {score1}") if score1 >= 1000 else print(F"congrats player 2: {score2}" )
print(F"dice was rolled {diceRolls} times")
print('player 1:',score1)
print('player 2:',score2)
# python ternary
print(f"answer is {(score2 if score1 > score2 else score2)  * diceRolls}")
