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
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
    sortpeople(people_list, 'weight', 'desc')
    print(people_list)
    

def sortpeople(people, field, sort_dir):
    reversed = False
    if sort_dir == 'desc':
        reversed = True
    people.sort(key = lambda p : p[field], reverse = reversed)
    return people


def ex2():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
    filtered_list = filter_males(people_list)
    print(filtered_list)


def filter_males(people):
    result = list(filter(lambda m : m['sex'] == 'male', people))
    return result

def ex3():
    people_list = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)


def calc_bmi(people):
    bmi_list = list(map(maptoBMI, people))
    return bmi_list


def maptoBMI(person):
    ret_val = {
        'id': person['id'],
        'name': person['name'],
        'weight_kg': person['weight_kg'],
        'height_meters': person['height_meters'],
        'bmi': round(person['weight_kg'] / person['height_meters'] **2,1) 
    }
    return ret_val
def ex4():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    print(get_people(people_list))


def get_people(people):

    result = [p['name'] for p in people if p['age'] >= 15]
    return result

def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.

def ex6():
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
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