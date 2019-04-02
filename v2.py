from functools import reduce
from tkinter import Tk, Canvas
import time
dimensiune = 20

class punct:
    def __init__(self, coord):
        self.coord = coord
        self.x, self.y = coord

def GrahamScan(puncte):
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0) #st = 1 ; dr = -1; coliniare = 0;

    def cmp(a, b):
        return (a > b) - (a < b) # 3 if-uri condensate : sa stiu TURN-ul dintre 2 puncte

    def orientare(p, q, r):        # 3 puncte
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0) #determinantul celor 3 puncte

    def stanga(acoperire, r):
        while len(acoperire) > 1 and orientare(acoperire[-2], acoperire[-1], r) != TURN_LEFT:#acoperire[-2]= antepenultimul punct adaugat in acoperire, [-1]= penultimul
            acoperire.pop()  #acoperirea mea ramane aceeasi (punctul curent nu e bun si il scot din stiva)
        if not len(acoperire) or acoperire[-1] != r:
            acoperire.append(r) # punctul e bun si il adaug in acoperire
        return acoperire

    puncte = sorted(puncte) #sortez punctele
    l = reduce(stanga, puncte, [])  # imi aplica functia stanga pe toate punctele => acoperirea rezultata pana cand ajung la un punct care e in dreapta
    u = reduce(stanga, reversed(puncte), []) #imi aplica functia stanga pe toate punctele => acoperirea rezultata pana cand ajung la un punct care e in stanga
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l    #unesc l-ul cu u-ul ca sa imi dea acoperirea totala

conv = GrahamScan([[5,8],[6,6],[8,8],[10,10],[6,6],[7,8],[9,7],[9,9]])  # returneaza acoperirea convexa a acestor puncte
print(conv) #afiseaza acoperirea convexa

#initial
window = Tk()  #importate de la inceput pt exemplificarea grafica
canvas = Canvas(window) #importate de la inceput pt exemplificarea grafica
for i in range(len(conv)-1):
    canvas.create_line(conv[i][0]*dimensiune, conv[i][1]*dimensiune, conv[i+1][0]*dimensiune, conv[i+1][1]*dimensiune, fill='blue', width=3)
    #coord a doua puncte consecutive,unesc punctele consecutive din acoperirea initiala

canvas.create_line(conv[0][0]*dimensiune, conv[0][1]*dimensiune, conv[-1][0]*dimensiune, conv[-1][1]*dimensiune, fill='blue', width=3)
    #unesc si ultimele 2 puncte din acoperirea convexa
canvas.pack()
window.mainloop()
time.sleep(1)
window = Tk()
canvas = Canvas(window)
ultim = [10,9] # punctul pe care trebuie sa il adaugam la acoperirea convexa
conv = GrahamScan(conv+[ultim]) #adaugam punctul la acoperire
print(conv)
if ultim in conv:
    for i in range(len(conv)-1):
        if conv[i+1] == ultim:
            canvas.create_line(conv[i][0] * dimensiune, conv[i][1] * dimensiune, conv[i + 1][0] * dimensiune, conv[i + 1][1] * dimensiune,
                               fill='red', width=3)
        elif conv[i] == ultim:
            canvas.create_line(conv[i][0] * dimensiune, conv[i][1] * dimensiune, conv[i + 1][0] * dimensiune, conv[i + 1][1] * dimensiune,
                               fill='red', width=3)
        else:
            canvas.create_line(conv[i][0]*dimensiune, conv[i][1]*dimensiune, conv[i+1][0]*dimensiune, conv[i+1][1]*dimensiune, fill='blue', width=3)
else:
    print('Acoperirea este identica')
    for i in range(len(conv)-1):
        canvas.create_line(conv[i][0] * dimensiune, conv[i][1] * dimensiune, conv[i + 1][0] * dimensiune, conv[i + 1][1] * dimensiune,
                               fill='blue', width=3)
    canvas.create_line(conv[i][0]*dimensiune, conv[i][1]*dimensiune, conv[i+1][0]*dimensiune, conv[i+1][1]*dimensiune, fill='blue', width=3)

canvas.create_line(conv[0][0]*dimensiune, conv[0][1]*dimensiune, conv[-1][0]*dimensiune, conv[-1][1]*dimensiune, fill='blue', width=3)
canvas.pack()
window.mainloop()
