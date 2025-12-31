import hashlib
import time

class UltraRSU:
    def __init__(self, seed):
        # SHA-256 ile devasa bir başlangıç sayısı (Seed) oluşturur
        self.state = int(hashlib.sha256(str(seed).encode()).hexdigest(), 16)
        self.counter = 0

    def generate_bits(self, length=1000):
        bits = ""
        while len(bits) < length:
            self.counter += 1
            # 1. TEMEL: Collatz Adımı (Hocanın istediği kural)
            if self.state % 2 == 0:
                self.state //= 2
            else:
                # 2. GÜVENLİK: XOR Maskeleme ile yörüngeyi gizle
                mask = (self.state ^ 0x5555555555555555) & 0xFFFFFFFFFFFFFFFF
                self.state = (3 * self.state + mask)
            
            # 3. KORUMA: Sayı çok küçülürse tekrar entropi yükle
            if self.state < 10**20:
                self.state |= int(hashlib.sha256(str(self.counter).encode()).hexdigest(), 16)

            # 4. GÜÇLÜ BİT ÇIKARMA: Durumu hashleyip bit alıyoruz (Zayıflığı bitiren kısım)
            step_hash = hashlib.md5(str(self.state).encode()).digest()
            b1 = step_hash[0] % 2 # İlk byte'ın paritesi
            b2 = step_hash[1] % 2 # İkinci byte'ın paritesi
            
            # 5. DENGELEME: Von Neumann Whitening
            if b1 != b2:
                bits += str(b1)
        
        return bits[:length]

def kikare_testi(bit_dizisi):
    n = len(bit_dizisi)
    n0 = bit_dizisi.count('0')
    n1 = bit_dizisi.count('1')
    beklenen = n / 2
    # Formül: sum((Gözlenen - Beklenen)^2 / Beklenen)
    chi = ((n0 - beklenen)**2 / beklenen) + ((n1 - beklenen)**2 / beklenen)
    return n0, n1, chi

if __name__ == "__main__":
    u_seed = input("Yeni Seed giriniz: ")
    rsu = UltraRSU(u_seed)
    final_bits = rsu.generate_bits(1000)
    
    n0, n1, chi = kikare_testi(final_bits)
    print(f"\n--- RSÜ ANALİZ SONUÇLARI (V2) ---")
    print(f"Üretilen Bit Sayısı: {len(final_bits)}")
    print(f"0 Sayısı: {n0}, 1 Sayısı: {n1}")
    print(f"Kikare Değeri: {chi:.4f}")
    print(f"Sonuç: {'BAŞARILI' if chi < 3.84 else 'ZAYIF RASTGELELİK'}")
