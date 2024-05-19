"""     Exercício Python 114:

    Crie um código em Python que teste se o site 
    pudim está acessível pelo computador usado.

    Resolução do exercício:
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://www.pudim.com.br")

except:
    print("Deu erro")

else:
    print("Tudo ok")