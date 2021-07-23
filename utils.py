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
        
def fibonacci(n):
    fib = [1,1]
    for i in range(n):
        fib[i] = fib[i-2] + fib[i-1]
    return fib
def find_minimum_and_max(l):
    min_val = l[0]
    max_val = l[0]
    for value in l[1:]:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return range(min_val,max_val+1)

def sort_list(l):
    my_gen = find_minimum_and_max(l)
    return [[i]*l.count(i) for i in my_gen if i in l]

