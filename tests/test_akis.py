# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 18.10.2026
# Açıklama: Hafta 4 üreteçlerinin ve fonksiyonlarının testleri.

from itertools import islice, takewhile

from uzay_oyunu.akis import fibonacci


# --- Görev 1: fibonacci ---

def test_fibonacci_next_ile_ilk_uc():
    g = fibonacci()
    assert (next(g), next(g), next(g)) == (0, 1, 1)


def test_fibonacci_islice_ilk_12():
    assert list(islice(fibonacci(), 12)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_fibonacci_takewhile_100_den_kucukler():
    sonuc = list(takewhile(lambda x: x < 100, fibonacci()))
    assert sonuc == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_fibonacci_tek_kullanimlik():
    g = fibonacci()
    birinci = list(islice(g, 5))
    ikinci = list(islice(g, 5))
    # aynı üreteç kaldığı yerden devam eder, baştan başlamaz
    assert birinci == [0, 1, 1, 2, 3]
    assert ikinci == [5, 8, 13, 21, 34]
    assert birinci != ikinci
