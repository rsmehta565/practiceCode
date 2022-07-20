# Print Even Odd using thread.

import time
from threading import *

def printEven(limit):
    global num

    while num <= limit:
        if(num%2==0):
            print("Even ", num)
            num = num + 1

def printOdd():
    global num

    while num < limit:
        if num % 2 != 0:
            print("Odd  ",num)
            num = num + 1

if __name__ == "__main__":
    num = 0
    limit = 10
    t1 = Thread (target = printEven, args=(limit,))
    t2 = Thread (target = printOdd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()