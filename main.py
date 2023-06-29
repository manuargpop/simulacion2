from numpy import random
from scipy.integrate import quad

def f(x):
    return 3*x**2+2*x

res = quad(f,2,3)
print("el valor matematico es ", res[0])

def carlos():
    itertotal = 1
    suma=0
    i=int(input("numero de iteraciones"))
    while itertotal <= i:
        x1 = round(random.uniform(2.00, 3.00), 2)
        itertotal += 1
        ##print(x1)
        monte = round(f(x1),2)
        if suma == 0:
            suma = monte
        else:
            suma += monte

        ##print("el valor maonte es ", monte[0])
    suma = suma/i

    def dif(current, previous):
        if current == previous:
            print("la presicion final es: 100%")
        try:
            final= (current/previous[0])*100
            print("la presicion final es: ",final, "%")
        except ZeroDivisionError:
            return 0

    print("el valor montecarlos es ", suma)
    dif(suma,res)

carlos()