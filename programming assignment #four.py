import random
import os
total = 0
from user_inputer import input_integer
output_roll = [0]*13
def get_and_write_file():
    done = True
    while done:
        try:
            file_nam = input("please enter the file name you want to make. if the file exists, the file will be deleted, so be warned: ")
            infile = open(file_nam, "w")
            done = False
        except:
            print("invalid name for a file please try again")
    user_prompt = "please enter a whole number between 100 and 12,000 " 
    users_input = input_integer(input(user_prompt), 100, 12000)
    infile = infile
    for num in range(users_input):
        rolled_nums = random.randint(1, 13)
        infile.write(str(rolled_nums) + "\n")
    infile.close()
    return file_nam, users_input
def reading_and_calc_num(file_nam, users_input):
    infile = open(file_nam, "r")
    for line in range(users_input):
        x = infile.readline()
        number = int(x)
        output_roll[number] += 1
    return output_roll
def writing_stuff(output_roll):
    print("face", "\t", "number of tosses")
    print("----" "\t", "-----------------")
    for position in range(1,13):
        print(position, "\t", output_roll[position])
        total += output_roll[position]
        max_thing = max(output_roll[1:12])
        min_thing = min(output_roll[1:12])
    #what do I do for the avarage to get what you want?
    avarage = float(total/12)
    print("the lowest number rolled is: ", output_roll.index(min_thing), "which was rolled ", min_thing, "times")
    print("the highest number rolled is: ", output_roll.index(max_thing), "which was rolled", max_thing, "times")
    print("the average number rolled is: ", avarage)
    infile.close()
get_and_write_file()
file_nam = file_nam
users_input = users_input
reading_and_calc_num(file_nam, users_input)
otuput_roll = output_roll
writing_stuff(output_roll)




