def okuma(dosya_yolu):
    with open(dosya_yolu, 'rb') as dosya:
        return dosya.read()

if __name__ == "__main__":
    dosya_yolu = input("Dosya yolunu giriniz: ")
    ilk_bytelar = bytes(okuma(dosya_yolu)[:2]).decode('utf-8')
    print(f"İlk iki byte: {ilk_bytelar}")
    input()

