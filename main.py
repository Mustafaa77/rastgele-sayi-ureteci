import hashlib
import time

class RNG:
    def __init__(self, seed):
        self.state = int(hashlib.sha256(str(seed).encode()).hexdigest(), 16)
        self.counter = 0

    
    def next_bit(self):
        while True:
            self.counter += 1
            if self.state % 2 == 0:
                self.state //= 2
            else:
                mask = (self.state ^ 0xABCDEF) & 0xFFFFFFFF
                self.state = (3 * self.state + mask)
            
            # 1 döngüsüne girerse state'i tazele
            if self.state <= 1:
                self.state = int(hashlib.sha256(str(self.counter).encode()).hexdigest(), 16)

            # İstatistiksel dengeleme (arkadaşının eksik bıraktığı yer burasıydı)
            b1 = (self.state >> 2) & 1
            b2 = (self.state >> 5) & 1
            if b1 != b2:
                return b1

    def generate_sequence(self, length=64):
        return "".join(str(self.next_bit()) for _ in range(length))

# Test Kısmı
if __name__ == "__main__":
    seed_val = input("Seed girin (Örn: Okul No): ")
    rng = KralRNG(seed_val)
    print(f"\nÜretilen 64-bit Dizi: {rng.generate_sequence(64)}")
