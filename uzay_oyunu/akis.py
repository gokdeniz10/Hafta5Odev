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
