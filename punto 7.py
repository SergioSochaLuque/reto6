# declaramos todas las funciones
def calcular_promedio_1(a:float, b:float, c:float, d:float, e:float) -> float:
    promedio = (a + b + c + d + e) / 5
    return promedio
def calcular_mediana_numeros(a:float, b:float, c:float, d:float, e:float) -> float:
    lista_numeros = (a, b, c, d, e)
    lista_numeros_ordenados = sorted(lista_numeros)
    longitud_lista = len(lista_numeros)
    mediana = lista_numeros_ordenados(longitud_lista // 2)
    return mediana
def calcular_promedio_multiplicativo(a:float, b:float, c:float, d:float, e:float) -> float:
    el_promedio_multiplicativo = ((a+b+c+d+e)**(1/5))
    return el_promedio_multiplicativo
def ordenar_numeros_ascendente(a:float, b:float, c:float, d:float, e:float) -> float:
    lista = (a, b, c, d, e)
    lista_ascendente = sorted(lista)
    return lista_ascendente
def ordenar_numeros_descendente(a:float, b:float, c:float, d:float, e:float) -> float:
    lista_1 = (a, b, c, d, e) 
    lista_descendente = sorted(lista_1, reverse = True)
    return lista_descendente
def calcular_potencia_mayor_numero_elevado_al_menor(a:float, b:float, c:float, d:float, e:float) -> float:
    lista_2 = (a, b, c, d, e)
    mayor : float = max(lista_2)
    menor : float = min(lista_2)
    potencia = mayor ** menor
    return potencia
def calcular_raiz_cubica_menor_numero(a:float, b:float, c:float, d:float, e:float) -> float:
    lista_3 = (a, b, c, d, e)
    menor_1 : float = min(lista_3)  
    raiz = menor_1 ** 1/3
    return raiz
# definimos funcion main
if __name__ == "__main__":
    a = float(input("ingrese el primer numero: "))
    b = float(input("ingrese el segundo numero: "))
    c = float(input("ingrese el tercer numero: "))
    d = float(input("ingrese el cuarto numero: "))
    e = float(input("ingrese el quinto numero: "))
    promedio = calcular_promedio_1(a, b, c, d, e)
    mediana = calcular_mediana_numeros(a, b, c, d, e)
    promedio_multiplicativo = calcular_promedio_multiplicativo(a, b, c, d, e)
    lista_ascendente = ordenar_numeros_ascendente(a, b, c, d, e)
    lista_descendente = ordenar_numeros_descendente(a, b, c, d, e)
    potencia = calcular_potencia_mayor_numero_elevado_al_menor(a, b, c, d, e)
    raiz = calcular_raiz_cubica_menor_numero(a, b, c, d, e)

    print("el promedio de los numeros ingresados es: " + str(promedio))
    print("la mediana es: " + str(mediana))
    print("el promedio multiplicativo de los numeros es: " + str(promedio_multiplicativo))
    print("la lista ordenada de manera ascendente es: " + str(lista_ascendente))
    print("la lista ordenada de manera descendente es: " + str(lista_descendente))
    print("la potencia del numero mayor elevado al menor es: " + str(potencia))
    print("la raiz cubica del menor numero es: " + str(raiz))