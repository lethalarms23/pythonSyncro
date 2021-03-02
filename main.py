import time
from pynput.mouse import Button, Controller
import itertools


def objeto(i):
    print("Objeto: ", num)
    print("\n")
    if i == 0:
        mouse.position = (884, 775)
        mouse.click(Button.left, 1)
    elif i == 1:
        mouse.position = (989, 778)
        mouse.click(Button.left, 1)
    elif i == 2:
        mouse.position = (1023, 776)
        mouse.click(Button.left, 1)
    else:
        print("Nenhum")


mouse = Controller()
numTotal = int(input("Total de movimentos: "))
numObjetos = int(input("Total de objetos: "))
counter = numTotal
my_list = [0] * numTotal
listNum = [0] * numObjetos
time.sleep(2)
for i in range(0, numObjetos):
    listNum[i] = i

comb = list(itertools.product(listNum, repeat=numTotal))
result = itertools.chain(comb)
print(comb)
for each in result:
    time.sleep(0.1)
    for num in each:
        time.sleep(0.1)
        print(num)
        objeto(num)
    print("\n")
    time.sleep(0.5)
    for i in range(0, numTotal):
            mouse.position = (1304, 182)
            mouse.click(Button.left, 1)
            time.sleep(0.1)
