import hashlib
import time
import math

class GelismisRSU:
    def __init__(self, seed):
        # 1. Kriter: Tamamen rastgelelik için güçlü başlangıç (SHA-256)
        self.state = int(hashlib.sha256(str(seed).encode()).hexdigest(), 16)
        self.counter = 0

    def generate_bits(self, length=1000):
        bits = ""
        while len(bits) < length:
            self.counter += 1
            # Hibrit Collatz + Maskeleme
            if self.state % 2 == 0:
                self.state //= 2
            else:
                mask = (self.state ^ 0xABCDEF) & 0xFFFFFFFF
                self.state = (3 * self.state + mask)
            
            if self.state <= 1: # Döngü koruması
                self.state = int(hashlib.sha256(str(self.counter).encode()).hexdigest(), 16)

            # 2. Kriter: 0-1 Eşitliği için Von Neumann Filtresi
            b1 = (self.state >> 3) & 1
            b2 = (self.state >> 7) & 1
            if b1 != b2:
                bits += str(b1)
        return bits[:length]

def kikare_testi(bit_dizisi):
    n = len(bit_dizisi)
    n0 = bit_dizisi.count('0')
    n1 = bit_dizisi.count('1')
    # Kikare Formülü: sum((Gözlenen - Beklenen)^2 / Beklenen)
    beklenen = n / 2
    kikare_degeri = ((n0 - beklenen)**2 / beklenen) + ((n1 - beklenen)**2 / beklenen)
    return n0, n1, kikare_degeri

if __name__ == "__main__":
    seed = input("Seed giriniz: ")
    rsu = GelismisRSU(seed)
    bitler = rsu.generate_bits(1000)
    
    n0, n1, chi = kikare_testi(bitler)
    print(f"\n--- RSÜ ANALİZ SONUÇLARI ---")
    print(f"Üretilen Bit Sayısı: {len(bitler)}")
    print(f"0 Sayısı: {n0}, 1 Sayısı: {n1}")
    print(f"Kikare Değeri: {chi:.4f}")
    print(f"Sonuç: {'BAŞARILI' if chi < 3.84 else 'ZAYIF RASTGELELİK'}") # 3.84 kritik değerdir
