# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 18.10.2026
# Açıklama: Hafta 4 üreteçleri ve önbellekli rota hesabı.

import time
from collections.abc import Callable, Iterator
from functools import lru_cache


def fibonacci() -> Iterator[int]:
    """Fibonacci sayılarını sonsuza kadar sırayla üretir: 0, 1, 1, 2, 3, ..."""
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]:
    """Her adımda yakıtı tuketim kadar azaltıp kalan yakıtı üretir.

    Yakıt 0'a inince durur. Yakıt eksiye düşerse 0 olarak üretilir.
    """
    while yakit > 0:
        yakit = yakit - tuketim
        if yakit < 0:
            yakit = 0
        yield yakit


def satirlari_oku(yol: str) -> Iterator[str]:
    """Dosyayı satır satır okur; boş satırları ve # ile başlayanları atlar.

    Dosyanın tamamı belleğe alınmaz, her seferinde bir satır üretilir.
    """
    dosya = open(yol, encoding="utf-8")
    for satir in dosya:
        satir = satir.strip()
        if satir == "" or satir.startswith("#"):
            continue
        yield satir
    dosya.close()


def ayristir(satirlar: Iterator[str]) -> Iterator[tuple[str, str, int]]:
    """'dünya -> sirius 12' gibi her satırdan (kaynak, hedef, yakit) demeti üretir."""
    for satir in satirlar:
        parcalar = satir.split()
        # parcalar: ["dünya", "->", "sirius", "12"]
        yield (parcalar[0], parcalar[2], int(parcalar[3]))


def uzun_yolculuklar(kayitlar: Iterator[tuple[str, str, int]], esik: int) -> Iterator[tuple[str, str, int]]:
    """Yakıtı esik değerinden büyük olan yolculukları üretir."""
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit


def rota_sayaci(baglantilar: dict) -> Callable[[str, int], int]:
    """Önbellekli rota_sayisi fonksiyonunu kurup döndürür."""

    @lru_cache
    def rota_sayisi(gezegen: str, adim: int) -> int:
        """gezegen'den başlayıp tam adim yolculuk yapan farklı rotaların sayısı."""
        if adim == 0:
            return 1
        toplam = 0
        for komsu in baglantilar[gezegen]:
            toplam = toplam + rota_sayisi(komsu, adim - 1)
        return toplam

    return rota_sayisi


def rota_sayaci_onbelleksiz(baglantilar: dict) -> Callable[[str, int], int]:
    """Aynı hesabı önbelleksiz yapan sürüm (sadece süre karşılaştırması için)."""

    def rota_sayisi(gezegen: str, adim: int) -> int:
        """gezegen'den başlayıp tam adim yolculuk yapan farklı rotaların sayısı."""
        if adim == 0:
            return 1
        toplam = 0
        for komsu in baglantilar[gezegen]:
            toplam = toplam + rota_sayisi(komsu, adim - 1)
        return toplam

    return rota_sayisi


if __name__ == "__main__":
    # Görev 4: önbelleksiz ve önbellekli sürümün adim=20 için süre karşılaştırması
    from uzay_oyunu.oyun import galaksi_yukle

    baglantilar = galaksi_yukle()["baglantilar"]

    yavas = rota_sayaci_onbelleksiz(baglantilar)
    baslangic = time.perf_counter()
    sonuc = yavas("dünya", 20)
    bitis = time.perf_counter()
    print("Önbelleksiz: " + str(sonuc) + " rota, " + str(bitis - baslangic) + " saniye")

    hizli = rota_sayaci(baglantilar)
    baslangic = time.perf_counter()
    sonuc = hizli("dünya", 20)
    bitis = time.perf_counter()
    print("Önbellekli:  " + str(sonuc) + " rota, " + str(bitis - baslangic) + " saniye")
    print(hizli.cache_info())
