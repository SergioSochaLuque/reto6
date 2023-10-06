# importar con math el valor de pi
import math 
p = math.pi 
# lo siguiente es declarar la funcion para calcular volumenenes y declarar las variables de la funcion
# rad es radio, vol es volumen y alt es altura
def calcular_volumen_figura(rad_circulo:float, rad_cono:float, alt_cono:float) -> float:
    vol_esfera = 4/3 * p * rad_circulo**3
    vol_cono = p * rad_cono**2 * alt_cono
    vol_figura = vol_esfera + vol_cono
    return vol_figura
# lo siguiente es declarar la funcion para calcular el area de la figura y declarar las variables de la funcion
def calcular_area_figura(rad_circulo:float, rad_cono:float, alt_cono:float) -> float:
    generatriz_cono = (alt_cono ** 2 + rad_cono ** 2)**1/2
    area_esfera = 4 * p * rad_circulo**2
    area_cono = p * rad_cono * generatriz_cono + p * rad_cono**2
    area_figura = area_esfera + area_cono
    return area_figura
# lo siguiente es definir la funcion main con las variables y con el resultado que queremos que muestre
if __name__ == "__main__" :
    rad_circulo = float(input("ingrese el radio del circulo:"))
    rad_cono = float(input("ingrese el radio del cono:"))
    alt_cono = float(input("ingrese altura del cono:"))
    vol_figura = calcular_volumen_figura(rad_circulo, rad_cono, alt_cono)
    area_figura = calcular_area_figura(rad_circulo, rad_cono, alt_cono)
    print("el volumen de la figura es: " + str(vol_figura))
    print("el area de la figura es: " + str(area_figura))
