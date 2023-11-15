# define your methods here.
# ex1() - ex10()
from src.WordCounter import WordCounter
from src.TaxMan import TaxMan
from src.Calculator import Calculator
from src.CarCollector import CarCollector
from pprint import pprint
from src.Dwarf import Dwarf
from src.Fighter import Fighter
from src.Invoice import Invoice

def ex1():

    # Given list
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
    # call sortpeople on people list with field weight, descending order
    sortpeople(people_list, 'weight', 'desc')
    # print result of sort
    print(people_list)
    

def sortpeople(people, field, sort_dir):
    '''
    This method sorts a given list with a field and sort direction
    '''
    reversed = False # initialize reversed as False for asecending order

    if sort_dir == 'desc':  # if sort_dir is desc
        reversed = True     # set reversed as True
    
    # use lambda to sort on a field in ascending order by default unless flag is False
    people.sort(key = lambda p : p[field], reverse = reversed) 

    return people


def ex2():
    # Given list
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
    # Initialize filtered_list to store result of filter_males func
    filtered_list = filter_males(people_list)

    # Print filtered_list
    print(filtered_list)


def filter_males(people):
    '''
    This method accepts a list of people (people) and returns only the males in the list.
    '''
    # use lambda to loop through each person and checks if sex == male, then puts it in list
    result = list(filter(lambda m : m['sex'] == 'male', people))

    # return filtered result
    return result

def ex3():
    # Given list
    people_list = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]
    # Initialize new_people_list to store the result of calc_bmi
    new_people_list = calc_bmi(people_list)

    # print result new_people_list
    print(new_people_list)


def calc_bmi(people):
    '''
    This method accepts a list (people) and calculates the BMI for each person.
    '''

    # Maps each person in people to result of maptoBMI
    bmi_list = list(map(maptoBMI, people))

    # Return list bmi_list
    return bmi_list


def maptoBMI(person):

    # Initialize ret_val as a dict with edited columns and bmi calculation
    ret_val = {
        'id': person['id'],
        'name': person['name'],
        'weight_kg': person['weight_kg'],
        'height_meters': person['height_meters'],
        'bmi': round(person['weight_kg'] / person['height_meters'] **2,1) 
    }

    return ret_val

def ex4():

    # Given list
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    print(get_people(people_list))


def get_people(people):

    '''
    This method accepts a list of people (people) and uses list comphrension
    to return the names of people that are equal to or greater than 15 years old.
    '''
    
    # Initialize result to store the names of people over 15 in list
    result = [p['name'] for p in people if p['age'] >= 15]

    # Return list result
    return result

def ex5():

    # Given sentence
    sentence = "This is a test of the emergency broadcast system"

    # Initialize word_counter to hold WordCounter object
    word_counter = WordCounter(sentence)

    # Call count_words method to count words in sentence
    word_counter.count_words()

    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.

def ex6():

    # Given list
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]

    # Initialize tm to store TaxMan object
    tm = TaxMan(items, "10%")

    # Call calc_total method 
    tm.calc_total()

    # Print calculated total
    print(tm.get_total())

def ex7():
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())

def ex8():
    pprint(CarCollector.get_data())

def ex9():
    f = Fighter(18)
    d = Dwarf(15)
    print(f)
    print(d)
    f.fight(d)
    d.fight(f)
    print(f)
    print(d)

def ex10():
    data = [
    "1, 2322, 10.00, False",
    "2, 5435, 60.30, True",
    "3, 3433, 15.63, False",
    "4, 8439, 12.77, False",
    "5, 3424, 11.34, False",
    ]
    arr = []
    for i in data:
        print(i)
        arr2 = i.split(", ")
        invoice = Invoice(int(arr2[0]), int(arr2[1]), float(arr2[2]), str(arr2[3]))
        arr.append(invoice)

    print(arr)