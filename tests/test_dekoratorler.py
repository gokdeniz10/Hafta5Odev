# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 25.10.2026
# Açıklama: Hafta 5 dekoratörlerinin testleri.

from uzay_oyunu.dekoratorler import sure_olc


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
