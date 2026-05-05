import random
senha = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamanho = int(input("qual o tamnho da senha"))
senha_nova = ""
for i in range(tamanho):
    senha_nova = senha_nova + random.choice(senha)
print(senha_nova)