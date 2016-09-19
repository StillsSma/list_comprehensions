
from datetime import datetime

def remove_vowls():
    sentence = list("List Comprehensions are the Greatest!")
    vowls = ["a", "e", "i", "o", "u"]
    no_vowl = [letter for letter in sentence if letter not in vowls]
    #print("".join(no_vowl))

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
    #print (water_temps)


list_water_temps()
def water_temps_float():
    water_temps = [lists[4] for lists in data ]
    del water_temps[0]
    temp_float = [float(temps) for temps in water_temps]
    #print (temp_float)

water_temps_float()

def fahrenheit():
    water_temps = [lists[4] for lists in data ]
    del water_temps[0]
    temp_float = [float(temps) for temps in water_temps]
    print (temp_float)
    water_temp_fahrenheit = [int(round(temps * 1.8 + 32)) for temps in temp_float]
    #print (water_temp_fahrenheit)

fahrenheit()

def wave_height_dict():
    wave_dict = {lists[5]: lists[1] for lists in data}
    print (wave_dict)

wave_height_dict()
def average_height():
    del data[0]
    days_of_week = [datetime.strptime( lists[5].replace("-"," "),'%Y %m %d').weekday() for lists in data]


average_height()
