import turtle as t
import numpy as np
from operator import add
from time import time # För mätning av körtid

# Några konstanter
ORIGO = (0, 0)
t_i = 0.2   # Tidpunkten då sköldpaddan börjar röra på sig
t_f = 20    # Tidpunkten då sköldpaddan slutar röra på sig
dt  = 0.025 # Tidsintervall


def get_coords(t):
    """
    Parameter:  Ett tal
    Returnerar: En koordinat
    Kommentar:  Returkoordinaterna ligger på en rät linje
    """

    # Beräkningsalgoritm för läget
    x = 20/t
    y = 20/t

    # Exempel på hur returen fungerar:
    # Om x = 100, y = 200 och ORIGO = (30, -50)
    # så returneras (130, 150)
    return tuple(map(add, (x, y), ORIGO))


def plot_line():
    """
    Kommentar: Funktionen ritar linjen, koordinater beräknas i
    funktionen get_coords.
    Parametrar: Inga
    Returvärde: Inget
    """
    tim.color("red")
    tim.penup()
    tim.goto(get_coords(t_i))  # Gå till första punkten på linjen
    tim.pendown()

    # Skapar en lista med tal fr.o.m t_i till t_f med intervallet dt
    t = np.arange(t_i, t_f, dt)

    for i in t:  # Flyttar sköldpaddan
        tim.goto(get_coords(i))


### Huvudprogram ###
tim = t.Turtle() # Den vandrande sköldpaddan
tom = t.Turtle() # Målmarkering

tim.pensize(6)
tim.shape("turtle")
tim.tilt(225) # Sköldpaddan vänds rätt
tim.speed(0)  # 0 - 10, 1 - 10 ökad hastighet, 0 snabbast

tom.color("yellow")
tom.penup()
tom.goto(ORIGO) # Målet markeras
tom.tilt(45)

screen = t.Screen()
screen.bgcolor("Black")
screen.setup(600, 400)
screen.title("Fartminskning")

start = time() # Starttid
plot_line()    # Plottar linjen
end = time()   # Sluttid

print(f"Tidsåtgång: {(end - start):.2f} sek.")
screen.exitonclick()