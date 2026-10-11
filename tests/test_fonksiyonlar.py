# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 11.10.2026
# Açıklama: Oyundan çıkarılan fonksiyonların testleri.

import pytest

from uzay_oyunu.araclar import en_bagli_gezegenler, hamle_sayaci
from uzay_oyunu.oyun import envanter_metni, galaksi_kur, galaksi_yukle, hedef_menusu


def test_envanter_iki_esya():
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"


def test_envanter_bos():
    assert envanter_metni(False, False, False) == ""


def test_envanter_hepsi_var():
    sonuc = envanter_metni(True, True, True)
    assert sonuc == "Sende: bol kredi, bir hiperdrive, yetenekli bir pilot"


def test_envanter_sadece_hiperdrive():
    assert envanter_metni(False, True, False) == "Sende: bir hiperdrive"


def test_hedef_menusu_iki_hedef():
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(["centauri", "sirius"]) == beklenen


def test_hedef_menusu_tek_hedef():
    beklenen = "Nereye gitmek istersin?\n[1] sirius"
    assert hedef_menusu(["sirius"]) == beklenen


def test_galaksi_dosyadan_kurulur():
    g = galaksi_yukle()
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100


def test_yakit_verilmezse_50():
    assert galaksi_kur(["mars"], {"mars": []}, "mars")["yakit"] == 50


def test_baslangic_listede_yoksa_hata():
    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "venüs")


def test_hamle_sayaci_birer_artar():
    sayac = hamle_sayaci()
    assert sayac() == 1
    assert sayac() == 2
    assert sayac() == 3


def test_iki_sayac_birbirini_etkilemez():
    birinci = hamle_sayaci()
    ikinci = hamle_sayaci()
    birinci()
    birinci()
    assert ikinci() == 1


def test_en_bagli_gezegenler():
    g = galaksi_yukle()
    assert en_bagli_gezegenler(g) == ["sirius", "centauri", "dünya", "orion", "kara_delik"]


def test_esitlikte_alfabetik():
    g = galaksi_kur(["c", "a", "b"], {"a": ["b"], "b": ["a"], "c": ["a", "b"]}, "a")
    assert en_bagli_gezegenler(g) == ["c", "a", "b"]
