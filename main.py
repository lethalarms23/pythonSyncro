import time
from tabulate import tabulate
from pynput.mouse import Button, Controller
from itertools import product, combinations, permutations
from math import factorial
import itertools
import string

def objeto(i):
    if i == 0:
        mouse.position = (904,780) #Esquerda se for so 2 objetos
        mouse.click(Button.left, 1)
        time.sleep(0.1)
    elif i == 1:
        mouse.position = (980,778) #Direita se for so 2 objetos
        mouse.click(Button.left, 2)
        time.sleep(0.1)
    elif i == 2:
        print("Triangulo")
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
            if (counter != 1):
               #objeto(i)
               counter = counter - 1
            else:
               time.sleep(3)
               for i in range(0, numTotal):
                   mouse.position = (1202, 182)
                   mouse.click(Button.left, 1)
                   time.sleep(0.1)
               counter = numTotal
    else:
        for i in range(k):
            my_list[n - 1]=i
            pr(n-1,k,numTotal)
pr(n,k,numTotal)