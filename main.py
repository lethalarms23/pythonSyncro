import time
import pyautogui
from pynput.mouse import Button, Controller
import itertools


def objeto(i):
    if i == 0:
        pyautogui.moveTo(884, 775)
        pyautogui.click(clicks=1)
    elif i == 1:
        pyautogui.moveTo(971, 775)
        pyautogui.click(clicks=1)
    elif i == 2:
        pyautogui.moveTo(1023, 776)
        pyautogui.click(clicks=1)
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
    for num in each:
        objeto(num)
    for i in range(0, numTotal):
            pyautogui.moveTo(1199, 181)
            pyautogui.click(clicks=1)
