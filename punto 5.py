# empezamos definiendo la funcion para despues declarar la variable
def calculo_prestamo(c:float, i:float, m:float) -> float:
    interes_mes = i/12
    total = c*((1+interes_mes)**m)
    return total
if __name__ == "__main__":
    c = float(input("ingrese el valor del prestamo inicial:"))
    i = float(input("ingrese el interes anual:"))
    m = float(input("ingrese la cantidad de meses:"))
    total_x = calculo_prestamo(c, i, m)
    print("el interes compuesto es:" + str(total_x))
