# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 25.10.2026
# Açıklama: Hafta 5 dekoratörleri. Süre ölçen, çağrı sayan, loglayan ve
# argüman alan dekoratörler.

import time
from collections.abc import Callable
from functools import wraps


def sure_olc(fonksiyon: Callable) -> Callable:
    """Fonksiyonun çalışma süresini 'ad: 0.0123 sn' biçiminde yazan dekoratör.

    Fonksiyonun sonucunu değiştirmeden geri döndürür.
    """
    @wraps(fonksiyon)
    def sarmalayici(*args: object, **kwargs: object) -> object:
        """Asıl fonksiyonu çağırır, geçen süreyi yazar ve sonucu döndürür."""
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        print(fonksiyon.__name__ + ": " + str(round(bitis - baslangic, 4)) + " sn")
        return sonuc

    return sarmalayici


if __name__ == "__main__":
    from uzay_oyunu.akis import rota_sayaci_onbelleksiz
    from uzay_oyunu.oyun import galaksi_yukle

    baglantilar = galaksi_yukle()["baglantilar"]

    # Görev 1: Hafta 4'teki önbelleksiz rota sayacının adim=20 için süresi
    rota_sayisi = sure_olc(rota_sayaci_onbelleksiz(baglantilar))
    rota_sayisi("dünya", 20)
