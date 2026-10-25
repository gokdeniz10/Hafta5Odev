# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 25.10.2026
# Açıklama: Hafta 5 dekoratörlerinin testleri.

import pytest

from uzay_oyunu.dekoratorler import fib_cagri_sayilari, log_cagri, say, sure_olc, yakit_harca
from uzay_oyunu.komutlar import KOMUTLAR, envanter, harita, komut, yardim


# --- Görev 1: sure_olc ---

@sure_olc
def topla(a: int, b: int = 0) -> int:
    """İki sayıyı toplar."""
    return a + b


def test_sure_olc_sonuc_degismiyor(capsys):
    assert topla(2, 3) == 5
    cikti = capsys.readouterr().out
    assert "topla: " in cikti
    assert " sn" in cikti


def test_sure_olc_adli_argumanla():
    assert topla(2, b=10) == 12
    assert topla(a=1, b=1) == 2


def test_sure_olc_ad_ve_belge_korunuyor():
    assert topla.__name__ == "topla"
    assert topla.__doc__ == "İki sayıyı toplar."


# --- Görev 2: say ve dekoratör sırası ---

def test_say_cagrilari_sayiyor():
    @say
    def selam(ad: str) -> str:
        """Selam verir."""
        return "Merhaba " + ad

    assert selam.cagri == 0
    assert selam("Gökdeniz") == "Merhaba Gökdeniz"
    selam(ad="Gökdeniz")
    assert selam.cagri == 2
    assert selam.__name__ == "selam"
    assert selam.__doc__ == "Selam verir."


def test_fib_20_dekorator_sirasi():
    assert fib_cagri_sayilari(20) == (21891, 39, 21)



# --- Görev 3: log_cagri ---

def test_log_cagri_ornek_cikti(capsys):
    # ödevdeki örnek çıktıyı veren küçük bir yolculuk fonksiyonu
    @log_cagri
    def yolculuk(hedef: str, hiz: int = 1) -> str:
        """Hedefi ve hızı metin olarak döndürür."""
        return hedef + " hiz=" + str(hiz)

    assert yolculuk("orion", hiz=3) == "orion hiz=3"
    cikti = capsys.readouterr().out
    assert cikti == "-> yolculuk('orion', hiz=3)\n<- yolculuk = 'orion hiz=3'\n"
    assert yolculuk.__name__ == "yolculuk"




# --- Görev 4: komut sistemi ---

def ornek_durum() -> dict:
    """Testlerde kullanılan, sirius'ta duran bir oyun durumu."""
    return {
        "konum": "sirius",
        "baglantilar": {"sirius": ["orion", "dünya", "kara_delik"], "orion": ["sirius"]},
        "credits": True,
        "engines": False,
        "copilot": True,
    }


def test_komut_fonksiyonu_degistirmeden_kaydeder():
    def deneme(durum: dict) -> str:
        """Deneme komutu."""
        return "deneme"

    kayitli = komut("deneme_komutu", "sadece test için")(deneme)
    assert kayitli == deneme
    assert KOMUTLAR["deneme_komutu"] == (deneme, "sadece test için")
    del KOMUTLAR["deneme_komutu"]


def test_ayni_komut_adi_iki_kez_hata_verir():
    with pytest.raises(ValueError):
        @komut("yardim")
        def ikinci_yardim(durum: dict) -> str:
            """Aynı adlı ikinci komut."""
            return ""
    # eski kayıt bozulmamalı
    assert KOMUTLAR["yardim"][0] == yardim


def test_yardim_komutu():
    beklenen = ("envanter  eşyalarını gösterir\n"
                "harita    gidebileceğin gezegenleri gösterir\n"
                "yardim    komutları listeler")
    assert yardim(ornek_durum()) == beklenen


def test_envanter_komutu():
    assert envanter(ornek_durum()) == "Sende: bol kredi, yetenekli bir pilot"


def test_harita_komutu():
    assert harita(ornek_durum()) == "orion, dünya, kara_delik"
    durum = ornek_durum()
    durum["konum"] = "orion"
    assert harita(durum) == "sirius"



# --- Görev 5: sinirla ---

def test_yakit_harca_ornek():
    assert yakit_harca(30) == 70


def test_yakit_harca_sinir_degerleri():
    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0


def test_yakit_harca_ust_sinir_disi():
    with pytest.raises(ValueError, match="yakit_harca: 150 değeri 0-100 aralığında değil"):
        yakit_harca(150)


def test_yakit_harca_alt_sinir_disi():
    with pytest.raises(ValueError, match="yakit_harca: -1 değeri 0-100 aralığında değil"):
        yakit_harca(-1)
