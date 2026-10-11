# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 11.10.2026
# Açıklama: Oyunda kullanılan yardımcı fonksiyonlar.

import time
from collections.abc import Callable


def yakit_ekle(miktar: int, depo: list | None = None) -> list:
    """Verilen miktarı depoya ekler ve depoyu döndürür.

    Depo verilmezse her çağrıda yeni boş bir liste kullanılır.
    (Varsayılan değer [] olsaydı aynı liste bütün çağrılarda paylaşılırdı.)
    """
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıldığında bir artan bir sayaç fonksiyonu döndürür."""
    sayi = 0

    def say() -> int:
        """Sayacı bir artırır ve yeni değeri döndürür."""
        nonlocal sayi
        sayi = sayi + 1
        return sayi

    return say


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre çoktan aza sıralar.

    Bağlantı sayısı eşit olanlar alfabetik sıraya konur.
    """
    baglantilar = galaksi["baglantilar"]
    return sorted(galaksi["gezegenler"], key=lambda g: (-len(baglantilar[g]), g))


def sure_olc(fonksiyon: Callable) -> Callable:
    """Verilen fonksiyonun ne kadar sürdüğünü yazan bir sarmalayıcı döndürür."""
    def sarmalayici(*args: object, **kwargs: object) -> object:
        """Asıl fonksiyonu çağırır, geçen süreyi yazar ve sonucu döndürür."""
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print("Geçen süre: " + str(bitis - baslangic) + " saniye")
        return sonuc

    return sarmalayici


if __name__ == "__main__":
    # oyun.py zaten bu dosyayı import ettiği için burada, en altta import ediyoruz
    from uzay_oyunu.oyun import galaksi_yukle

    g = galaksi_yukle()
    print(en_bagli_gezegenler(g))

    # bonus: süre ölçme
    en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
    print(en_bagli_gezegenler(g))
