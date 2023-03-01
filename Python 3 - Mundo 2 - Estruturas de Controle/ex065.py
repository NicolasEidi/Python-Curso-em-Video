"""     Exercício Python 65: 
    Crie um programa que leia vários números inteiros pelo teclado. 
    No final da execução, mostre a média entre todos os valores e qual 
    foi o maior e o menor valores lidos. O programa deve perguntar ao 
    usuário se ele quer ou não continuar a digitar valores.

    Resolução do exercício:
"""

quant = int(input("Quantos números você quer ler? "))

finalizar = False
soma = total = menor = maior = 0

while not finalizar:
    while quant >= 1:
        num = int(input("Digite um valor: "))
        quant -= 1
        total += 1
        soma += num

        if total == 1:
            menor = maior = num
        elif num > maior:
            maior = num
        elif num < menor:
            menor = num

    fim = str(input("Deseja adicionar mais números? [S/N]")).strip().upper()
    if fim == "N":
        finalizar = True
    elif fim == "S":
        quant = int(input("Mais quantos números você quer ler? "))

media = soma / total

print("===---" * 10)
print(f"Você digitou {total} números, a média deles é {media:.2f}, e a soma é {soma}")
print(f"O maior número é {maior} e o menor número é {menor}")
print("===---" * 10)
