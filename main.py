import time
from tabulate import tabulate
from pynput.mouse import Button, Controller
from itertools import product, combinations, permutations
from math import factorial
import itertools
import string

def objeto(i):
    if i == 0:
        mouse.position = (874,773)
        mouse.click(Button.left, 1)
        time.sleep(0.07)
    elif i == 1:
        mouse.position = (952,777)
        mouse.click(Button.left, 1)
        time.sleep(0.07)
    elif i == 2:
        mouse.position = (1023, 776)
        mouse.click(Button.left, 1)
        time.sleep(0.07)
    else:
        print("Nenhum")
mouse = Controller()
numTotal = int(input("Total de movimentos: "))
numObjetos = int(input("Total de objetos: "))
counter = numTotal
my_list = [0] * numTotal
time.sleep(2)



print(my_list)
n = len(my_list)
k = numObjetos
def pr(n,k,numTotal):
    counter = numTotal
    if n < 1:
        for i in my_list:
            #print(i, end="")
            #print()
            objeto(i)
        time.sleep(0.1)
        for i in range(0, numTotal):
            mouse.position = (1438, 185)
            mouse.click(Button.left, 1)
            time.sleep(0.07)

    else:
        for i in range(k):
            my_list[n - 1]=i
            pr(n-1,k,numTotal)
pr(n,k,numTotal)