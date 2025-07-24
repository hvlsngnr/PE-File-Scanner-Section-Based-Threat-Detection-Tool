from uygulama1 import okuma
def ofset(dosya_yolu,aranacak_kelime):
 dosya_icerik = okuma(dosya_yolu)
 ofset = dosya_icerik.find(aranacak_kelime.encode())
 return ofset

def yazdir(ofset):
 if(ofset!=-1):#eger ofset -1'e esit degilse aranan kelime dosyada mevcuttur
  print(""""{}" ifadesi {} adresinde bulundu """.format(aranacak_kelime,ofset))
 else:
  print(""""{}" ifadesi herhangi bir konumda bulunamadi""".format(aranacak_kelime))

if __name__ == "__main__":
 dosya_yolu=input("Dosya yolunu  giriniz: ")
 aranacak_kelime=input("Aramak istediginiz kelimeyi giriniz: ")
 yazdir(ofset(dosya_yolu,aranacak_kelime))
 input()
