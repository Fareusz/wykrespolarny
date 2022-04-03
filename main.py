# TODO: znajdz liczby pierwsze w wybranym przedziale a potem umieść je na wykresie polarnym w pliku .png
import numpy as np
import matplotlib.pyplot as plt

startarr = input('Provide start of list: ')
endarr = input('Provide end of list: ')

try:
    startarr = int(startarr)
    endarr = int(endarr)
    a = endarr
except:
    print('You provided something wrong, please try again.')
    exit()

print(type(startarr))

arr = list(range(startarr, endarr))
primearr = list()

for x in arr:
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            print(x, "is prime number")
            primearr.append(x)
print(primearr)

plt.axes(projection='polar')

for rad in primearr:
    r = rad
    plt.polar(rad, r, 'g.')
plt.show()
plt.savefig('polar.png')
