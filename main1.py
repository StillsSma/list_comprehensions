
from datetime import datetime

def remove_vowls():
    sentence = list("List Comprehensions are the Greatest!")
    vowls = ["a", "e", "i", "o", "u"]
    no_vowl = [letter for letter in sentence if letter not in vowls]
    # print("".join(no_vowl))

remove_vowls()
# id,Wave Height,Wave Period,Avg Waves Per Second,Water Temp,Date
import csv

with open('data.csv', 'rt') as f:
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)
    f.close()


def list_water_temps():
    water_temps = [lists[4] for lists in data ]
    del water_temps[0]
    # print (water_temps)


list_water_temps()
def water_temps_float():
    water_temps = [lists[4] for lists in data ]
    del water_temps[0]
    temp_float = [float(temps) for temps in water_temps]
    # print (temp_float)

water_temps_float()

def fahrenheit():
    water_temps = [lists[4] for lists in data ]
    del water_temps[0]
    temp_float = [float(temps) for temps in water_temps]
    # print (temp_float)
    water_temp_fahrenheit = [int(round(temps * 1.8 + 32)) for temps in temp_float]
    # print (water_temp_fahrenheit)

fahrenheit()

def wave_height_dict():
    wave_dict = {lists[5]: lists[1] for lists in data}
    # print (wave_dict)

wave_height_dict()
def average_height():
    week = []
    del data[0]
    days_of_week = [0,1,2,3,4,5,6]
    for days in days_of_week:
        day = [float(lists[1]) for lists in data if datetime.strptime(lists[5].replace("-"," "),'%Y %m %d').weekday() == days]
        week.append(day)
    avesum = [sum(height)/len(height) for height in week]
    aveheight = dict(zip(days_of_week, avesum))
    # print (aveheight)
average_height()

def nested():
    my_dictionary = {'Gale': {'Homework 1': 88, 'Homework 2': 76}, 'Jordan': {'Homework 1': 92,
    'Homework 2': 87}, 'Peyton': {'Homework 1': 84, 'Homework 2': 77},
    'River': {'Homework 1': 85, 'Homework 2': 91}}

    avescore = { names : (my_dictionary[names]["Homework 1"] + my_dictionary[names]["Homework 2"])/2
               for names in my_dictionary
               for values in my_dictionary[names]}


    print (avescore)


nested()
