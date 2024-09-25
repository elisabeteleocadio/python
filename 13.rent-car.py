km_percorridos = float(input ("digite a quantidade de km percorridos: "))
dias_alugados = float(input ("digite os dias em que o carro foi utilizado: "))

custo_por_dia = 60.0
custo_por_km = 0.15

preco_total = (custo_por_dia * dias_alugados + custo_por_km * km_percorridos)

print(f"o total a pagar é: R${preco_total:.2f}")