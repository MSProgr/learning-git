# implementing functions related to feature b
def say_hello():
    print("Hello World")

def get_modulo(a,b):
    return a%b

def get_sum(*argv):
    somme = 0
    for arg in argv:
        somme+=arg
    
    return somme
