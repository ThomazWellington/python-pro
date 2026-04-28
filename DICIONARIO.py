meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "NOOB": "É uma pessoa que parece ser iniciante em algo, mas naverdade não é",
            "AURA": "É a presença que uma pessoa passa, que baseada em falas ou feitos"
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("INFELIZMENTE está palavra ainda não esta no dicionario")
