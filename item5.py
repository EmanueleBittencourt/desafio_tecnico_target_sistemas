# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(string):
    resultado = ""
    for i in range(len(string) - 1, -1, -1):

        resultado += string[i]
    
    return resultado

string = str(input("Informe uma palavra ou frase: "))
string_invertida = inverter_string(string)
print(string_invertida)