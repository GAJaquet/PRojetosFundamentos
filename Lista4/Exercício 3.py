#Algumas correções foram feitas com ajuda do ChatGPT (espero que tenha consertado...)

cesar = CifraCesar(3)
xor = CifraXor(42)

texto_original = "Está muito quente"
texto_cifrado_cesar = cesar.cifrar(texto_original)
texto_decifrado_cesar = cesar.decifrar(texto_cifrado_cesar)

texto_cifrado_xor = xor.cifrar(texto_original)
texto_decifrado_xor = xor.decifrar(texto_cifrado_xor)

class Criptografia:
    def cifrar(self, texto):
        pass

    def decifrar(self, texto_cifrado):
        pass

class CifraCesar(Criptografia):
    def __init__(self, deslocamento):
        self.deslocamento = deslocamento

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                novo_char = chr((ord(char) - ascii_offset + self.deslocamento) % 26 + ascii_offset)
                texto_cifrado += novo_char
            else:
                texto_cifrado += char
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        return self.cifrar(texto_cifrado)

class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            texto_cifrado += chr(ord(char) ^ self.chave)
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        return self.cifrar(texto_cifrado)

print("Cifra de César:")
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado_cesar)
print("Texto decifrado:", texto_decifrado_cesar)

print("\nCifra XOR:")
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado_xor)
print("Texto decifrado:", texto_decifrado_xor)