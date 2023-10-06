# importar el valor de pi
import math
p = math.pi
def calcular_area(r:float, a:float, b:float) -> float:
    area = (2*(p*(r**2))) + (b*a)
    return area
def calcular_perimetro(r:float, a:float, b:float) -> float:
    perimetro = (2*p*r) + (2+(b+a))
    return perimetro
def calcular_radio(r:float) -> float:
    area_circulo = (p*(r**2))
    rc = math.sqrt(area_circulo/p)
    return rc
def calcular_ab(a:float, b:float) -> float:
    area_rect = (b*a)
    a = area_rect/b
    b = area_rect/a
    return a, b
if __name__ == "__main__":
    r = float(input("Ingrese radio de los circulos:"))
    a = float(input("Ingrese la altura del rectangulo:"))
    b = float(input("Ingrese la base del rectangulo:"))
    area_total = calcular_area(r, a, b)
    perimetro_total = calcular_perimetro(r, a, b)
    rcal = calcular_radio(r)
    abcal = calcular_ab(a, b)
    print("______________________________________________________________")
    print("El area total es " + str(area_total))
    print("El perimetro total es " + str(perimetro_total))
    print("________________________________________________________________")
    print("El valor del radio de la esfera es " + str(rcal))
    print("El valor de radio del cono y su altura es " + str(abcal))

