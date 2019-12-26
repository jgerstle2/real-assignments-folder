import random
from user_input import input_integer
done = False
bad = True
wager = 0
num = 0
total = 0
comp_ans = 0
user_answer = 0
def users_ans():
    print("please enter one of the following numbers which represent these words for rock paper scissors,")
    ans = input(" 1 = rock, 2 = paper, 3 or higher = scissors ")
    user_answer = input_integer(ans, 1, 3)
    return user_answer
def computer_answer():
    comp_ans = random.randint(1,3)
    if comp_ans == 1:
        comp_word = "rock"
    elif comp_ans == 2:
        comp_word = "paper"
    else:
        comp_word = "scissors"
    print(comp_word)
    return comp_ans, comp_word
def winner(comp_ans, user_answer):
    if comp_ans == 1:
        if user_answer == 1:
            print("its a tie")
        elif user_answer == 2:
            print("you win")
            games += 1
            points += 1
            total += wager
        else:
             print("you lose")
                    
    elif comp_ans == 2:
         if user_answer == 1:
            print("you lose")
         elif user_answer == 2:
            print("its a tie")
         else:
            print("you win")
            games += 1
            points +=1
                    
    else:
        if user_answer == 1:
            print("you win")
            games += 1
            points += wages
        elif user_answer == 2:
            print("you lose")
        else:
            print("its a tie")
    rounds += 1
    return points, games, rounds
try:
    while not done:
        print("you will be putting in a wager from 1 - 10 for this game if you want to stop the game please enter")
        value = input("anything other than a number two times 1 - 10 ")
        try:
            wager = int(value)
            while bad:
                if value <= 10:
                    done = True
                    bad = False
                else:
                    value("that was not what was asked please try again")
        except:
            print("REALLY?!!?!?!?")
        users_ans()
        computer_answer()
        rounds = 0
        winner(comp_ans, user_answer)
        print("the total wages gained is: ", points)
        print("the amounts of games played is: ", games)
        print("the amount of rounds in the game was: ", rounds)
        '''answer = int(input("please enter one of the following numbers which represent these words for rock paper scissors, 1 = rock, 2 = paper, 3 or higher = scissors "))
            answer = input_integer(answer, 1, 3)
            
            comp_choice = random.randint(1,3)
            if comp_choice == 1:
                    comp_word = "rock"
            elif comp_choice == 2:
                comp_word = "paper"
            else:
                comp_word = "scissors"
            print(comp_word)
            
            if comp_choice == 1:
                if answer == 1:
                    print("its a tie")
                elif answer == 2:
                    print("you win")
                    total += 1
                else:
                    print("you lose")
                    
            elif comp_choice == 2:
                if answer == 1:
                    print("you lose")
                elif answer == 2:
                    print("its a tie")
                else:
                    print("you win")
                    total += 1
                    
            else:
                if answer == 1:
                    print("you win")
                    total += 1
                elif answer == 2:
                    print("you lose")
                else:
                    print("its a tie")
            rounds += 1
            print("either you have ended it or something went wront on my account, good bye")'''
     
except Exception as e:
    print(e)
    



    
