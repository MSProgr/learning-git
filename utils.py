# Here we gonna implement the first 12 questions
import random
def count_item(l,item):
    return l.count(item)

def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    return "odd"

def all_element_less_than(l,number):
    return [i  for i in l if i < number]

def list_overlap(a,b):
    return list(set([i for i in a if i in b]))

def is_palyndrome(string):
    return string == ''.join(reversed(string))

def guessing_number():
    num = random.randint(1,9)
    while(True):
        guessing = int(input("please guess the right number : "))
        if guessing < num:
            print("less than the right number")
        elif guessing > num:
            print("greater than the right number")
        else:
            print("Congrats, you found the right number")
            break

