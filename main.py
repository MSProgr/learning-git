def is_prime(n):
    numbers = range(2, int(n/2)+2)
    stop_num = 1
    for i in numbers:
        stop_num = i
        if n%i == 0:
            break
    if stop_num == int(n/2)+1:
        return True
    return False



