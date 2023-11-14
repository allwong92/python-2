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


if __name__ == '__main__':
    ex1()