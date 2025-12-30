# Gelişmiş Collatz-XOR Rastgele Sayı Üreteci

Bu proje, **Bilgi Sistemleri Güvenliği** dersi final ödevi için geliştirilmiştir. 
Klasik **Collatz Teoremi (3n+1)** algoritması, kriptografik maskeleme yöntemleri ile hibritlenerek daha güvenli bir hale getirilmiştir.

## Algoritma Mantığı
Sıradan Collatz dizileri deterministik olduğu için kolayca tahmin edilebilir. Bu projede:
1. **Dinamik Maskeleme:** Tek sayı adımlarında sadece `3n+1` değil, sistemden türetilen bir `maske` değeri eklenir.
2. **Bit Dengeleme (Whitening):** Üretilen sayıların 0/1 dağılımını eşitlemek için Von Neumann düzeltme algoritması kullanılmıştır.

## Güvenlik Analizi
- **Direnç:** Klasik Collatz'a göre tersine mühendislik yapılması çok daha zordur.
- **Denge:** Çıktı dizisindeki 0 ve 1 sayıları birbirine yakındır (%50-%50 dağılım hedeflenmiştir).
