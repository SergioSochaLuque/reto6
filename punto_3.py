# empezamos declarando la funcion para calcular la cantidad de carne de las aves en kilos
def cantidad_carne_aves(n:int, m:int, k:int) -> int:
    carne_aves = n * 6 + m * 7 + k
    return carne_aves
if __name__ == "__main__":
    n = int(input("ingrese la cantidad de gallinas:"))
    m = int(input("ingrese la cantidad de gallos:"))
    k = int(input("ingrese la cantidadd de pollitos:"))
    carne_aves = cantidad_carne_aves(n, m, k)
    print("la cantidad de aves que tiene es:" + str(carne_aves) + " kilos") 