# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 11.10.2026
# Açıklama: Varsayılan değer olarak liste kullanma tuzağının testi.

from uzay_oyunu.araclar import yakit_ekle


def test_her_cagrida_yeni_depo():
    yakit_ekle(10)
    # ikinci çağrıda depo boş başlamalı, önceki 10 içinde olmamalı
    assert yakit_ekle(20) == [20]


def test_verilen_depoya_ekler():
    depom = [5]
    assert yakit_ekle(15, depom) == [5, 15]
