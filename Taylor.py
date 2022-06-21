from scipy import integrate
import math
import matplotlib.pyplot as plt
from sympy import *
x = Symbol('x')
funkcja = input("Type function:")
a = int(input('Input a:'))
y = eval(funkcja)
summa = y
n=0


while True:
    n += 1
    y = y.diff(x)
    d = (y*((x-a)**n)/math.factorial(n))
    if d ==0:
        break
    if n==50:
        break
    summa += d


bruh=str(summa)
print(bruh)

xarray=[]
yarray=[]
farray=[]
for x in range(-100,100):
    if x == 0:
        x=1
    xarray.append(x)
    yarray.append(eval(funkcja))
    farray.append(eval(bruh))

plt.plot(xarray, yarray,label='x' )
plt.plot(xarray, farray,label='teilor(x)')
plt.axis([-100, 100, -100, 100])
plt.show()






