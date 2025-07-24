import os
from uygulama2 import ofset
def klasor_tarama(klasor_yolu):
    sonuclar=[]
    for suanki_klasor, icindeki_klasor, icindeki_dosyalar in os.walk(klasor_yolu):#Klasorun icinde gezme islemi yapiliyor
        for dosya in icindeki_dosyalar:
          dosya_yolu=suanki_klasor+"\\"+dosya
          """ust taraftaki(7.kod satirindaki) atama isleminin amaci,oldugu andaki klasorun ve icindeki dosyanin 
          backslah(\) ile birlestirilmesi sonucu dosyanin yolunu elde etmek"""
          sonuclar.append(dosya_yolu) #alinan dosya yollari sonuclar lisltenine eklendi
    return sonuclar 

def yazdir(aranacak_kelime,sonuclar):
    for dosya_yolu in sonuclar:
     kontrol = ofset(dosya_yolu, aranacak_kelime)
     if (kontrol != -1):
        print("""{}:\tBULUNDU ({} adresinde) """.format(dosya_yolu, kontrol))
     else:
        print("{}:\tBULUNAMADI".format(dosya_yolu))

if __name__ == "__main__":
 klasor_yolu=input("Klasor yolunu giriniz: ")
 aranacak_kelime=input("Aramak istediginiz kelimeyi giriniz: ")
 sonuclar = klasor_tarama(klasor_yolu)
 yazdir(aranacak_kelime,sonuclar)
 input()