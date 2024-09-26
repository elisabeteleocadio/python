
def calcular_perda_de_vida(cigarros_por_dia, anos_fumando):
    minutos_perdidos_por_cigarro = 10
    total_cigarros = cigarros_por_dia * 365 * anos_fumando  
    total_minutos_perdidos = total_cigarros * minutos_perdidos_por_cigarro 
    dias_perdidos = total_minutos_perdidos / (1440) 
    return dias_perdidos

cigarros_por_dia = int(input("digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("digite a quantidade de anos que você fumou: "))

dias_perdidos = calcular_perda_de_vida(cigarros_por_dia, anos_fumando)

print(f"você perderá aproximadamente {dias_perdidos:.2f} dias de vida.)")