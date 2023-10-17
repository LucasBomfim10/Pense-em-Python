
#1 Quadrado
import turtle
import math

bob = turtle.Turtle()


def quadrado(t,tam):
    for i in range(4) :
        print(t)
        t.fd(tam)
        t.lt(90)
        

quadrado(bob,200)

"""Exemplo DOC"""

turtle.mainloop()