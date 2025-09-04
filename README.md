# 🔍 PE Dosya ve İçerik Analiz Aracı

Bu proje, **dosya okuma, içerik arama, klasör tarama ve PE (Portable Executable) dosya analizi** için geliştirilmiş Python tabanlı bir araçtır. Amaç, özellikle **Windows çalıştırılabilir dosyalarının (EXE, DLL)** iç yapısını inceleyerek belirli bir kelimenin hangi offset’te ve hangi section içinde bulunduğunu tespit etmektir.

---

## 🚀 Özellikler
- 📂 Dosya okuma (ilk byte’ları görüntüleme)  
- 🔎 Dosya içeriğinde kelime arama ve offset bulma  
- 📁 Klasör bazlı tarama ile toplu analiz  
- 🏷️ PE dosyalarının doğrulanması (x86/x64 mimari kontrolü)  
- 📌 Aranan kelimenin bulunduğu **section** bilgisinin raporlanması  

---

## 📂 Proje Yapısı
├── uygulama1.py # Dosya okuma ve ilk byte'ların kontrolü

├── uygulama2.py # Kelime arama ve offset bulma

├── uygulama3.py # Klasör tarama ve çoklu dosya analizi

├── uygulama4.py # PE dosyası kontrolü ve section bazlı analiz

└── screenshots/ # Ekran görüntüleri


---

## ⚙️ Kurulum
```bash
git clone https://github.com/hvlsngnr/PE-File-Scanner-Section-Based-Threat-Detection-Tool.git
cd PE-File-Scanner-Section-Based-Threat-Detection-Tool/dist/uygulama1
./uygulama1.exe
```

## 🖼️ Ekran Görüntüleri

###Uygulama1.exe
![Uygulama 1](https://github.com/hvlsngnr/PE-File-Scanner-Section-Based-Threat-Detection-Tool/blob/main/screenshots/uygulama1.png)

###Uygulama2.exe
![Uygulama 2](https://github.com/hvlsngnr/PE-File-Scanner-Section-Based-Threat-Detection-Tool/blob/main/screenshots/uygulama2.png)

###Uygulama3.exe
![Uygulama 3](https://github.com/hvlsngnr/PE-File-Scanner-Section-Based-Threat-Detection-Tool/blob/main/screenshots/uygulama3.png)

###Uygulama4.exe
![Uygulama 4](https://github.com/hvlsngnr/PE-File-Scanner-Section-Based-Threat-Detection-Tool/blob/main/screenshots/uygulama4.png)

