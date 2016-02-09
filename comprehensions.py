print("\n###Part 1 - Remove all vowels from this sentence 'List Comprehensions are the Greatest!' using a list comprehension\n")

def vowel_remover():
    vowels = ["a", "e", "i", "o", "u"]
    sentence = input("Enter a sentence for the vowel remover... ")
    sentence = [letter for letter in sentence if letter not in vowels]
    return "".join(sentence)

print(vowel_remover())

print("\n###Part 2 - Make a list of water temps by day\n")

with open("weather_data.txt") as weather_data_file:
        data = weather_data_file.readlines()

def weather_temp(item):
    return [line.replace("\n","").split(',')[-2:] for line in item]

# old way
    #water_temps = []
    #for line in item:
    #    water_temps.append(line.split(',')[-2:])
    #return water_temps

print(weather_temp(data))


water_temps_and_date = weather_temp(data)


print("\n###Part 3 - Convert the Water Temps from a string to a float\n")


def water(data):
    return [float(_[0]) for _ in data[1:]]

print(water(water_temps_and_date))

#old way....
    # water_list = []
    # for number in water_temps_and_date[1:]:
    #    water_list.append(float(number[0]))
    #    print(float(number[0]))


print("\n###Part 4 - Convert the Water Temps from Celsius to Fahrenheit rounded to an int\n")

water_temp = water(water_temps_and_date)

def c_to_f(info):
    return[int(number * (9/5) + 32) for number in info]

print (c_to_f(water_temp))

#old way...
    #fahrenheit = []
    #for number in water_temp:
    #    fahrenheit.append(int(number * (9/5) + 32))
    #print(fahrenheit)

print("\n###Part 5 - Create a dictionary with Date as the key and Wave Height as the value\n")

date_and_wave_height_dict = {}

def date_and_wave_height(item):
    return [line.replace("\n","").split(',')[-1::-4] for line in item]

print(dict(date_and_wave_height(data)))

print("\n###Part 6 - Create a dictionary with the average wave height for each day\n")

print("Sorry I didn't understand the requirement I'll resubmit at a later date")

print("\n###Part 7 - Create a nested comprehension to get the average of the Homework 1 grades.\n")

d = {'Gale': {'Homework 1': 88, 'Homework 2': 76}, 'Jordan': {'Homework 1': 92, 'Homework 2': 87}, 'Peyton': {'Homework 1': 84, 'Homework 2': 77}, 'River': {'Homework 1': 85, 'Homework 2': 91}}

from statistics import mean
def homework_vals(d):
    return[(d[something]['Homework 1']) for something in d]

print(d)
print("The mean of Homework 1 is..." + str(mean(homework_vals(d))))