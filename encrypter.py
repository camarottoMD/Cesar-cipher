#ord(caractere) + base - variancia

class CesarCipher:

    def __init__(self):
        pass

    def encrypter(self, texto: str, variance: int) -> str:
        lista = []
        for caractere in texto:
            if caractere.islower():
                response = self.__encriptar_cesar_lower(caractere, variance)

            elif caractere.isupper():
                response = self.__encriptar_cesar_upper(caractere, variance)

            elif caractere == " ":
                response = self.__if_space_encrypted(caractere=caractere, variance=variance)

            lista.append(response)
        return "".join(lista)

    def decrypter(self, texto: str, variance: int) -> str:
        lista = []
        for caractere in texto:
            if caractere.islower():
                response = self.__decriptar_cesar_lower(caractere, variance)

            elif caractere.isupper():
                response = self.__decriptar_cesar_upper(caractere, variance)

            elif caractere == '#':
                response = self.__if_space_decrypted(caractere=caractere, variance=variance)

            lista.append(response)
        return "".join(lista)

    def __encriptar_cesar_upper(self, caractere: str, variance: int) -> str:
        carac_encrypted = chr((ord(caractere) - ord("A") + variance) % 26 + ord('A'))
        return carac_encrypted


    def __encriptar_cesar_lower(self, caractere: str, variance: int) -> str:
        carac_encrypted = chr((ord(caractere) - ord("a") + variance) % 26 + ord('a'))
        return carac_encrypted
    
    def __decriptar_cesar_lower(self, caractere: str, variance: int) -> str:
        carac_decrypted = chr((ord(caractere) - ord('a') - variance) % 26 + ord('a'))
        return carac_decrypted

    def __decriptar_cesar_upper(self, caractere: str, variance: int) -> str:
        carac_decrypted = chr((ord(caractere) - ord('A') - variance) % 26 + ord('A'))
        return carac_decrypted

    def __if_space_encrypted(self, caractere: str, variance: int) -> str:
        space_decrypted = chr((ord(caractere) - ord(' ') + variance) % 26 + ord(' '))
        return space_decrypted
    
    def __if_space_decrypted(self, caractere: str, variance: int) -> str:
        space_decrypted = chr((ord(caractere) - ord(' ') - variance) % 26 + ord(' '))
        return space_decrypted
    
cripta = CesarCypher()
encriptado = cripta.encrypter('Me ajuda yoda, me ajuda, mata o kazhix pelo menos', 3)
print(encriptado)
decriptado = cripta.decrypter(encriptado, 3) #tem que saber a variancia para poder acertar a casa certa
print(decriptado)

