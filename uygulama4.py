import pefile
from uygulama1 import okuma
from uygulama2 import ofset
from uygulama3 import klasor_tarama


def son(klasor_yolu,aranacak_kelime):
 dosyalar=klasor_tarama(klasor_yolu)
 for dosya_yolu in dosyalar:
  dene(dosya_yolu)


def dene(dosya_yolu):
 with open(dosya_yolu, 'rb') as file:
  dos_header = file.read(64)
  dos_signature = dos_header[:2]
  if dos_signature == b'MZ': #signature alaninin doğrulanmasi
     if (karsilastir(dosya_yolu)):
      offset=ofset(dosya_yolu,aranacak_kelime)
      if(offset!=-1):
       section_name=sectionlar(dosya_yolu,offset)
       #print(section_name)
       print(dosya_yolu, ":\t BULUNDU ({} adresinde ve '{}' section içersinde)".format(offset,section_name))
      else:
       print(dosya_yolu,":\t BULUNAMADİ")
  else:
   print(dosya_yolu,": Gecerli PE dosyasi degil")


def karsilastir(dosya_yolu):
  pe = pefile.PE(dosya_yolu)
  if pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_I386'] or pe.FILE_HEADER.Machine == pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_AMD64']:
   """IMAGE_FILE_HEADER alaninin okunarak Machine alaninin
   IMAGE_FILE_MACHINE_I386 veya IMAGE_FILE_MACHINE_AMD64 değerine eşit olmasi durumu kontrol ediliyor"""
   return True
  else:
   return False


def sectionlar(dosya_yolu,offset):
    pe = pefile.PE(dosya_yolu)
    for section in pe.sections:
        section_name = section.Name.decode().strip('\x00')#o andaki section'nin ismini
        file_offset = section.PointerToRawData# gosterdigi offset degerini aliyoruz
        if offset in range(file_offset, file_offset + section.SizeOfRawData):
            """Aranan kelimenin bulundugu offset degerinin, dosyadaki file_offset değeri
             ile dosyadanin boyutu araliginda olup olmadigini kontrol ediyor ve aranan kelimeninin bulundugu
             offset degeri bu araligin icindeyse bize section'nin ismini return ediyor. """
            return section_name



        


if __name__ == "__main__":
 klasor_yolu=input("Klasor yolunu giriniz: ")
 aranacak_kelime=input("Aramak istediginiz kelimeyi giriniz: ")
 son(klasor_yolu,aranacak_kelime)
 input()
