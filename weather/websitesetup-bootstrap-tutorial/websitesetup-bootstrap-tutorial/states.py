from cmath import e
from cmd import PROMPT
import imp
from multiprocessing.connection import answer_challenge


import random
import datetime
from tkinter import W

x = datetime.datetime.now()
print(x.strftime("%B %d, %Y @ %H:%M:%S \n"))

states = {'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'}

def main():
    correct = 0
    wrong = 0
    state, capital, = random.choice(list(states.items()))
    name = input('Enter your name: ')
    answer = input(f"What is the capital of {state}? (enter 0 to quit): ")
    while answer != "0":
        if answer == capital:
            print("That is correct!")
            correct += 1
        elif answer != capital:
            print("That is incorrect!")
            wrong += 1
        state, capital = random.choice(list(states.items()))
        answer = input(f"What is the capital of {state}? (enter 0 to quit): ")

    print(f"You had {correct} correct responces and {wrong} incorrect responces.")

        
main()



IMPORT imp
FROM multiprocessing.connection import answer_challenge


IMPORT random
IMPORT datetime
FROM tkinter IMPORT W

PROMPT for time
DISPLAY current time

states= DISPLAY "state" + "captial"

DEF main():
    correct = 0
    wrong = 0
    state, capital, = random.choice(list(states.items()))
    PROMPT for name 
    DISPLAY "Enter your name: "
    PROMPT for answer
    DISPLAY "What is the capital of {state}? (enter 0 to quit): "
    WHILE answer != "0":
        IF answer == capital:
            DISPLAY "That is correct!"
            correct += 1
        ELIF answer != capital:
            DISPLAY "That is incorrect!"
            wrong += 1
        state, capital = random.choice(list(states.items()))
        PROMPT for answer
        DISPLAY "What is the capital of {state}? (enter 0 to quit): "

    DISPLAY "You had {correct} correct responces and {wrong} incorrect responces."

        
MAIN()
