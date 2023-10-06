# declaramos la funcion
def vueltas_billete(p:int, m:int, h:int, b:int) -> int:
    costo_total = p * 300 + m * 3300 + h * 350
    vueltas = b - costo_total
    return vueltas
if __name__ == "__main__":
    p = int(input("ingrese la cantidad de panes que compró:"))
    m = int(input("ingrese la cantidad de bolsas de leche que compró:"))
    h = int(input("ingrese la cantidad de huevos que compró:"))
    b = int(input("ingrese el valor de billete que dió:"))
    vueltas = vueltas_billete(p, m, h, b)
    valor_absoluto_vueltas = abs(vueltas)
# aqui damos unas condiciones para que se cumplan las instrucciones y se cumplan las condiciones
if vueltas >= 0:
    print("las vueltas fueron:" + str(vueltas))
else:
    print("usted quedo debiendo:" + str(valor_absoluto_vueltas))
    
    