# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 18.10.2026
# Açıklama: Hafta 4 üreteçleri ve önbellekli rota hesabı.

from collections.abc import Iterator


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
