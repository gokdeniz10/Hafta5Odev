# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 18.10.2026
# Açıklama: Hafta 4 üreteçlerinin ve fonksiyonlarının testleri.

from itertools import islice, takewhile

import pytest

from uzay_oyunu.akis import fibonacci, yakit_gostergesi
from uzay_oyunu.oyun import travel


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


# --- Görev 2: yakıt göstergesi ---

def test_yakit_gostergesi_ornek():
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]


def test_yakit_bitince_stopiteration():
    g = yakit_gostergesi(10, 5)
    assert next(g) == 5
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)


def test_oyunda_yakit_biter(monkeypatch, capsys):
    # dünya ile sirius arasında gidip gel: ilk "2" sirius, ikinci "2" yarışma sorusu,
    # sonra hep "2" (sirius'ta 2 = dünya, dünya'da 2 = sirius)
    # 100 yakıt, yolculuk başı 5 -> 20 yolculuk yapılır, 21. yolculukta yakıt biter
    girdiler = ["2"] * 22
    monkeypatch.setattr("builtins.input", lambda yazi="": girdiler.pop(0))
    travel()
    cikti = capsys.readouterr().out
    assert "Yakıtın bitti, uzayda sürükleniyorsun…" in cikti
    assert "Oyunu 20 hamlede bitirdin!" in cikti
