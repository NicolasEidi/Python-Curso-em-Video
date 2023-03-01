"""     Exercício Python 14: 
    Escreva um programa que converta uma temperatura 
    digitando em graus Celsius e converta para graus Fahrenheit.

    Resolução do exercício:
"""

temp = float(input('Temperatura em °C: '))
fahr = (temp * 1.8) +32
kelvin = (temp + 273.15)
print('Temperatura em graus Celsius: {:.1f}°C \nTemperatura em graus Fahrenheit: {:.1f}°F \nTemperatura em graus Kelvin: {:.2f}K'.format(temp, fahr, kelvin)) 
