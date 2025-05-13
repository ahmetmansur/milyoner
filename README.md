
# 🎮 Kim 500 Milyon İster?

**“Kim 500 Milyon İster?”**, popüler bilgi yarışması *“Kim Milyoner Olmak İster?”* formatından esinlenerek Python programlama dili ile geliştirilen, terminal tabanlı bir bilgi yarışması oyunudur. Oyuncuya artan para ödülleri karşılığında 15 çoktan seçmeli soru yöneltilir. Her soruda doğru cevap veren oyuncu daha yüksek bir ödüle ulaşır. Jokerler ve garanti para noktaları ile gerçekçi bir deneyim sunar.

---

## 🧠 Projenin Amacı

Bu projenin temel amacı:
- Python programlama diliyle fonksiyonel ve modüler bir uygulama geliştirmek,
- Kullanıcıya etkileşimli ve eğlenceli bir bilgi yarışması deneyimi sunmak,
- Koşullar, döngüler, kullanıcı girişi ve temel algoritmaları uygulamalı olarak pekiştirmektir.

---

## 🧩 Oyun Özellikleri

- ✅ 15 genel kültür sorusu
- ✅ Yükselen para ödülü sistemi
- ✅ 2 garanti soru (5. ve 10. soru)
- ✅ 3 joker:
  - 🎲 **Yarı Yarıya (J1):** İki yanlış şık elenir
  - 📞 **Telefon (J2):** Arkadaşınız %80 doğrulukla tahminde bulunur
  - 👥 **Seyirci (J3):** Seyirciler oy verir
- ✅ Kullanıcı istediği zaman yarışmadan çekilebilir
- ✅ Yanlış cevapta en son garanti para kazanılır

---

## ⚙️ Kullanılan Teknolojiler

- **Dil:** Python 3.x
- **Kütüphaneler:**  
  - `random` – Jokerlerde rastgelelik sağlar  
  - `time` – Gecikmeli tepkiler için (daha gerçekçi etkileşim)

Herhangi bir harici kütüphane veya kurulum gerekmez.

---

## 💻 Kurulum ve Çalıştırma

### 1. Python yüklü mü kontrol et:
```bash
python --version
```

### 2. Projeyi indir:
```bash
https://github.com/ahmetmansur/milyoner
```

### 3. Oyunu başlat:
```bash
python kim_500_milyon_ister.py
```

---

## 🕹️ Oynanış

- Terminalde size sırayla sorular yöneltilir.
- Aşağıdaki girişleri kullanabilirsiniz:
  - **A, B, C, D:** Seçeneklerden biriyle cevap verirsiniz.
  - **J1:** Yarı Yarıya jokerini kullanır.
  - **J2:** Telefon jokerini kullanır.
  - **J3:** Seyirci jokerini kullanır.
  - **W:** Yarışmadan çekilirsiniz ve mevcut kazancınızı alırsınız.
- Her doğru cevapla bir üst seviyeye geçersiniz.
-  5. ve 10. soruları geçtiğinizde garanti parayı güvenceye alırsınız.
- Yanlış cevaplarsanız, o noktaya kadar ulaştığınız garanti tutar size verilir.

---

## 🧪 Test Süreci

- Tüm jokerlerin bir kez kullanılabildiği kontrol edildi.
- Jokerlerin yalnızca aktif şıklar üzerinde çalıştığı doğrulandı.
- Doğru/yanlış/çekilme senaryoları elle test edilerek tüm oyun akışı sorunsuz hale getirildi.

---

## 🧠 Geliştirme Önerileri

Bu proje geliştirilmeye açıktır. Önerilen bazı geliştirmeler:

- 🔄 Soruların dış dosyadan (`json`, `csv`) okunması
- 🖼️ Grafik arayüz (Tkinter veya PyQt) entegrasyonu
- 🧠 Kullanıcı istatistiklerinin tutulması
- 🌐 Online çok oyunculu mod
- 🎯 Zorluk seviyelerine göre kategori seçimi
- 📂 Daha geniş bir soru havuzu


Teşekkürler ve iyi oyunlar! 🎉

![Ekran [README_Kim_500_Milyon_Ister.md](https://github.com/user-attachments/files/20192942/README_Kim_500_Milyon_Ister.md)
görüntüsü 2025-05-13 194741](https://github.com/user-attachments/assets/f7a88b17-f96e-41c4-a210-8e6f119ab060)
