#declaramos la funcion
def calcular_numero_contagios_dia(d:int, c:int) -> int:
    numero_contagios = c * 2** d
    return numero_contagios
#definimos la funcion main
if __name__ == "__main__":
    c = int(input("ingrese el numero de contagiados actual: "))
    d = int(input("ingrese la cantidad de dias: "))
    numero_contagios = calcular_numero_contagios_dia(d, c)
    print("el numero de contagios para el dia " + str(d) + " es de " + str(numero_contagios))
    