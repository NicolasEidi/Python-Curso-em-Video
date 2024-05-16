"""     Exercício Python 77:
    Crie um programa que tenha uma tupla com várias palavras 
    (não usar acentos). Depois disso, você deve mostrar, 
    para cada palavra, quais são as suas vogais.

    Resolução do exercício:
"""

conjunto = ("imprescindivel", "condescendente", "caracteristica", "idiossincrasia", "concupiscencia", "extraordinario", "demasiadamente", "sadomasoquismo",
            "intercorrencia", "irrepreensuvel", "consubstanciar", "incomensuravel", "preponderancia", "arbitrariedade", "discricionario", "especificidade", 
            "posteriormente", "imprescritivel", "intransponivel", "contextualizar")
for palavra in conjunto:
    print(f"\nA palavra {palavra.upper()} tem ", end="")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra, end=" ")