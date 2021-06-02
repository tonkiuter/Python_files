import math as m
import numpy as np
from matplotlib import pyplot

print ("Función 1")
a=float(input("ingrese el valor de (a):\n"))
b=float(input("ingrese el valor de (b):\n"))

print ("Función 2")
c=float(input("ingrese el valor de (a):\n"))
d=float(input("ingrese el valor de (b):\n"))


resultado=(-b)/a
print ("valor de la funcion 1",resultado)

resultado1=(-d)/c
print ("valor de la funcion 2",resultado1)



def f(x):
    return a*(x)+b

x = np.linspace(-100,50+np.pi,100)


pyplot.plot(x,[f(i)for i in x])


def f(x1):
    return c*(x1)+d
x1 = np.linspace(-100,50+np.pi,100)
pyplot.plot(x1,[f(i)for i in x1])


pyplot.axhline(0, color= "black")
pyplot.axvline(0, color= "black")

pyplot.xlim(-50,50)
pyplot.ylim(-50,50)
pyplot.savefig("output.png")
pyplot.show()