# Hibrit Collatz-XOR Rastgele Sayı Üreteci (RSÜ)

Bu proje Bilgi Sistemleri Güvenliği dersi için hazırlanmıştır.

## Algoritma Mantığı
Algoritma, matematiksel kaos teorisinin bir örneği olan **Collatz Sanısı** üzerine kurulmuştur. Ancak klasik Collatz'ın istatistiksel zayıflıklarını gidermek için şu eklemeler yapılmıştır:

1. **Dinamik Maskeleme:** Her adımda durum değeri bir XOR maskesi ile karıştırılarak deterministik yapı bozulmuştur.
2. **Von Neumann Whitening:** Ardışık bit çiftleri (01, 10) analiz edilerek 0 ve 1 sayılarının mutlak eşitliği (%50-%50) sağlanmıştır.

## İstatistiksel Testler
Algoritmanın başarısı **Kikare (Chi-Square)** testi ile doğrulanmıştır. 
- **Beklenen Dağılım:** %50 Sıfır, %50 Bir.
- **Kritik Değer:** 3.84 (Serbestlik derecesi 1, p < 0.05 için).
- **Sonuç:** Algoritma tüm testlerde kritik değerin altında kalarak "İstatistiksel Kalite" kriterini geçmiştir.
