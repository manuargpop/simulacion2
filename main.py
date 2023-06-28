from numpy import random
from scipy.integrate import quad

def f(x):
    return 3*x**2+2*x

res = quad(f,2,3)
print("el valor matematico es ", res[0])


def carlos():
    itertotal = 1
    porcent=0
    while itertotal <= 10000:
        x1 = round(random.uniform(2.00, 3.00), 2)
        x2 = round(random.uniform(2.00, 3.00), 2)
        if x1 != x2:
            itertotal += 1
            if x1>x2:
                x1f=float(x2)
                x2f=float(x1)
            else:
                x1f = float(x1)
                x2f = float(x2)
            print(x1f)
            print(x2f)
            monte = quad(f, x1f, x2f)
            if porcent == 0:
                porcent = ((abs(monte[0] - res[0]) / res[0]) * 100.0)
            else:
                suma = porcent + ((abs(monte[0] - res[0]) / res[0]) * 100.0)
                porcent = suma/2
            ##print("el valor maonte es ", monte[0])
            print(porcent,"%")


carlos()