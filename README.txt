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

---

## ⚙️ Kurulum
```bash
git clone https://github.com/hvlsngnr/PE-File-Scanner-Section-Based-Threat-Detection-Tool.git
cd PE-File-Scanner-Section-Based-Threat-Detection-Tool.git
pip install pefile

## 🖼️ Ekran Görüntüleri

### Uygulama 1 – Dosya Okuma
![Uygulama 1](https://github.com/hvlsngnr/PE-File-Scanner-Section-Based-Threat-Detection-Tool/blob/main/screenshots/uygulama1.png)
### Uygulama 2 – Kelime Arama
![Uygulama 2](https://github.com/hvlsngnr/PE-File-Scanner-Section-Based-Threat-Detection-Tool/blob/main/screenshots/uygulama2.png)
### Uygulama 3 – Klasör Taraması
![Uygulama 3](https://github.com/hvlsngnr/PE-File-Scanner-Section-Based-Threat-Detection-Tool/blob/main/screenshots/uygulama3.png)
### Uygulama 4 – PE Analizi
![Uygulama 4](https://github.com/hvlsngnr/PE-File-Scanner-Section-Based-Threat-Detection-Tool/blob/main/screenshots/uygulama4.png)




Not: Uygulama kodlarının incelenmesi veya Visual Studio Code gibi geliştirme ortamlarında çalıştırılması durumunda, .py uzantılı tüm Python dosyalarının aynı dizin yapısı içerisinde bulunmasına dikkat edilmelidir. Bu dosyalar birbirlerine import edilerek bağımlı çalıştıkları için, klasör yapısının bozulması modüllerin düzgün bir şekilde çalışmamasına neden olabilir.
Uygulamanın derlenmiş (executable) sürümleri dist/ dizini içerisinde yer almaktadır. İlgili çalıştırılabilir dosyalar bu klasör altında bulunarak doğrudan kullanılabilir.

