"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):

        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):
        self.total_items[item] = price

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, discount):
        self.discount = discount
        self.total_price -= discount
        return f"New total: £{self.total_price}"


    def get_total(self):
        self.total_price = sum(self.total_items.values())
        return f"Total: £{self.total_price}"

    def show_items(self):
        return f"All items: {list(self.total_items.keys())}"

    def reset_register(self):
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0
        return 'Register has successfully reset ✅'


# EXAMPLE code run:

# ADD
cash = CashRegister()
cash.add_item('pear', 5)
cash.add_item('apple', 8)
cash.add_item('melon', 18)

print(cash.show_items())
print(cash.get_total())
print(cash.apply_discount(30))
print(cash.remove_item('pear'))
print(cash.show_items())
print(cash.get_total())
print(cash.reset_register())


"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()


class CFGStudent(Student):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
        self.tot_mark = 0

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade
        print(self.subjects)
        return f"{subject} successfully added"

    def remove_subject(self, subject):
        self.subjects.pop(subject)
        return f'{subject} successfully removed'

    def overall_mark(self):
        self.tot_mark = sum(self.subjects.values()) / len(self.subjects.values())
        return f"Average mark: {self.tot_mark}"

    def all_subjects(self):
        return list(self.subjects.keys())




marta = CFGStudent('Marta', 23, 1)
print(marta.add_subject('math', 3))
print(marta.add_subject('science', 1))
print(marta.add_subject('coding', 9))
print(marta.add_subject('analytics', 5))
print(marta.overall_mark())
print(marta.remove_subject('science'))
print(marta.all_subjects())
print(marta.overall_mark())




# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)


