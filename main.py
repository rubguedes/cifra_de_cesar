from caracteres import lista_caracteres as char
import criptografia as c

str = str(input("Digite uma mensagem "))
rotacao = 2

print(c.cifra_cesar(str=str, rot=rotacao))

