# define your methods here.
# ex1() - ex10()

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

