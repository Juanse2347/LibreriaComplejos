import math
def sumacplx(a,b):
    # Suma de numeros complejos
    real = a[0]+b[0]
    img = a[1]+b[1]
    return real,img
#
def multcplx(a,b):
    # Multiplicacion de numeros complejos
    real = (a[0]*b[0])-(a[1]*b[1])
    img = (a[0]*b[1])+(b[0]*a[1])
    return real,img
#
def restacplx(a,b):
    # Resta de numeros complejos
    real = a[0]-b[0]
    img = a[1]-b[1]
    return real,img
#
def divisioncplx(a,b):
    # Division de numeros complejos
    try:
        div = b[0] ** 2 + b[1] ** 2
        real = (a[0] * b[0] + a[1] * b[1]) / div
        img = (a[1] * b[0] - a[0] * b[1]) / div
        return (real, img)
    except:
        return 'Imposible hacer la division.'

#
def modcplx(c):
    # Modulacion de numeros complejos
    modulo = (c[0] ** 2 + c[1] ** 2)
    return round(math.sqrt(modulo),2)

#
def conjcplx(c):
    # Conjugado de numeros Complejos
    real = c[0]
    img = c[1] * -1
    return real, img
#
def conv_polar_carte(c):
    # Conversion de polar a cartesiano
    real = round(c[0] * math.cos(c[1]))
    img = round(c[0] * math.sin(c[1]))
    return real,img
#
def fasecplx(c):
    # Retornar la fase de un numero complejo
    if c[0] < 0 and c[1] < 0:
        phase = round(2 * math.pi - (-1 * (math.atan2(c[1], c[0]))), 2)
        return phase
    elif c[0] > 0 > c[1]:
        phase = round((2 * math.pi + math.atan2(c[1], c[0])), 2)
        return phase
    else:
        phase = round((math.atan2(c[1], c[0])), 2)
        return phase
#
def prettyprinting(c):
    print(str(c[0]) + "+" + str(c[1]) + "i")

if __name__ == "__main__":
    c = (2,5)
    prettyprinting(sumacplx((2,3),(4,7)))
    prettyprinting(multcplx((2,3),(4,7)))
    prettyprinting(restacplx((2,3),(4,7)))
    prettyprinting(divisioncplx((2,3),(4,7)))
    print((modcplx(c)))
    prettyprinting(conjcplx((c)))
    print(conv_polar_carte((c)))
    print(fasecplx(c))





