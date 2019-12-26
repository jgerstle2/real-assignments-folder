import random
from user_input import input_integer
done = False
total = 0  
wager = 0
wins = 0
rounds = 0
while not done:
    print("you will be putting in a wager of an INTEGER from 1 - 10 for this")
    print("game if you want to stop the game please enter")
    wager = input("anything higher than a number between 1 - 10 ")
    try:
        wager = int(wager)
        if wager <= 10:	
            print(wager)
		# the following three lines should be moved to a function, say get_user_choice
		# you should split that long prompt into several prints statements there
		#instead of answer, call this something like user_choice
            def get_user_choice():
                print("please enter one of the following numbers which represent these words")
                answer = input(" for rock paper scissors, 1 = rock, 2 = paper, 3 or higher = scissors ")
                answer = input_integer(answer, 1, 3)     # input_integer does not expect a number in this spot
                return answer



		
		# the following green code should also be exported into a function.  In fact, perhaps two functions:
		# one to generate computer choice, another to declare this round’s winner
            def computer_choice():
                comp_choice = random.randint(1, 3)
                if comp_choice == 1:
                    comp_word = "rock"
                elif comp_choice == 2:
                    comp_word = "paper"
                else:
                    comp_word = "scissors"
                print(comp_word)
                return comp_choice
            computer_choice()
            if comp_choice == 1:
                if answer == 1:
                    print("its a tie")
                elif answer == 2:
                    print("you win")
                    total += wager
                    wins += 1

                else:
                    print("you lose")
                    total -= wager
            elif comp_choice == 2:
                if answer == 1:
                    print("you lose")
                    total -= wager
                elif answer == 2:
                    print("its a tie")
                else:
                    print("you win")
                    total += wager
                    wins += 1
            else:
                if answer == 1:
                    print("you win")
                    total += wager
                    wins +=1
                elif answer == 2:
                    print("you lose")
                    total -= wager
                else:
                    print("its a tie")
            rounds += 1
        else:
            print(total)
            print(wins)
            print(rounds)	# full report should be given here (via a function call)
            done = True
    except:
        continue
