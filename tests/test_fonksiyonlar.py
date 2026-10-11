# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 11.10.2026
# Açıklama: Oyundan çıkarılan fonksiyonların testleri.

import pytest

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
