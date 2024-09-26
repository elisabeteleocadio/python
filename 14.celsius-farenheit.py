def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = float(input("digite a temperatura em °C: "))

temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

# Exibir o resultado
print(f"a temperatura em °F é: {temperatura_fahrenheit:.2f} °F")