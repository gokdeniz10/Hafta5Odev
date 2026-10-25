# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 25.10.2026
# Açıklama: Hafta 5 dekoratörlerinin testleri.

from functools import lru_cache

import pytest

from uzay_oyunu.dekoratorler import fib_cagri_sayilari, hafiza, log_cagri, say, sure_olc, yakit_harca
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


def test_yakit_harca_adli_argumanla():
    assert yakit_harca(miktar=30) == 70
    with pytest.raises(ValueError):
        yakit_harca(miktar=150)


# --- Bonus: hafiza ---

def test_hafiza_tekrar_cagrida_onbellekten_dondurur():
    @hafiza()
    @say
    def kare(x: int) -> int:
        """Sayının karesini döndürür."""
        return x * x

    assert kare(4) == 16
    assert kare(4) == 16
    assert kare.__wrapped__.cagri == 1
    assert kare.__name__ == "kare"
    assert kare.__doc__ == "Sayının karesini döndürür."


def test_hafiza_farkli_argumanlar():
    @hafiza()
    @say
    def topla_iki(a: int, b: int = 0) -> int:
        """İki sayıyı toplar."""
        return a + b

    assert topla_iki(1, 2) == 3
    assert topla_iki(2, 1) == 3
    assert topla_iki(1, b=5) == 6
    assert topla_iki.__wrapped__.cagri == 3
    assert topla_iki(1, b=5) == 6
    assert topla_iki.__wrapped__.cagri == 3


def test_hafiza_sinirsiz_onbellek():
    @hafiza(maxsize=None)
    @say
    def kare(x: int) -> int:
        """Sayının karesini döndürür."""
        return x * x

    for i in range(200):
        kare(i)
    for i in range(200):
        assert kare(i) == i * i
    assert kare.__wrapped__.cagri == 200


def test_hafiza_dolunca_en_eski_silinir():
    @hafiza(maxsize=2)
    @say
    def kare(x: int) -> int:
        """Sayının karesini döndürür."""
        return x * x

    kare(1)
    kare(2)
    kare(3)
    assert kare.__wrapped__.cagri == 3
    # 2 ve 3 hâlâ önbellekte
    kare(2)
    kare(3)
    assert kare.__wrapped__.cagri == 3
    # 1 en eski olduğu için silindi, yeniden hesaplanır
    assert kare(1) == 1
    assert kare.__wrapped__.cagri == 4


def test_hafiza_lru_cache_ile_ayni_sonuc():
    @hafiza()
    def fib_hafiza(n: int) -> int:
        """Özyinelemeli Fibonacci (hafiza ile)."""
        if n < 2:
            return n
        return fib_hafiza(n - 1) + fib_hafiza(n - 2)

    @hafiza(maxsize=3)
    def fib_kucuk(n: int) -> int:
        """Özyinelemeli Fibonacci (3 girdilik hafiza ile)."""
        if n < 2:
            return n
        return fib_kucuk(n - 1) + fib_kucuk(n - 2)

    @lru_cache
    def fib_lru(n: int) -> int:
        """Özyinelemeli Fibonacci (lru_cache ile)."""
        if n < 2:
            return n
        return fib_lru(n - 1) + fib_lru(n - 2)

    for n in range(40):
        assert fib_hafiza(n) == fib_lru(n)
        assert fib_kucuk(n) == fib_lru(n)
