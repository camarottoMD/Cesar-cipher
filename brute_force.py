from encrypter import CesarCipher

decriptador = CesarCipher()

# frase = input("Digite algo: ")
frase = "Whyhiluz, klzjviypb h tluzhnlt l apyvb 87"


for num in range(26):
    print(f'Frase num {num}: {decriptador.decrypter(frase, num)}')