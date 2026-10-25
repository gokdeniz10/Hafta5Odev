# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 25.10.2026
# Açıklama: Hafta 5 dekoratörleri. Süre ölçen, çağrı sayan, loglayan ve
# argüman alan dekoratörler.

import time
from collections.abc import Callable
from functools import lru_cache, wraps


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


def say(fonksiyon: Callable) -> Callable:
    """Fonksiyonun kaç kez çağrıldığını sarmalayıcının 'cagri' niteliğinde sayar."""
    @wraps(fonksiyon)
    def sarmalayici(*args: object, **kwargs: object) -> object:
        """Sayacı bir artırır ve asıl fonksiyonun sonucunu döndürür."""
        sarmalayici.cagri = sarmalayici.cagri + 1
        return fonksiyon(*args, **kwargs)

    sarmalayici.cagri = 0
    return sarmalayici


def fib_cagri_sayilari(n: int) -> tuple[int, int, int]:
    """fib(n) için üç farklı dekoratör sırasında çağrı sayılarını döndürür.

    Sıra: yalnızca @say, @say üstte @lru_cache altta, @lru_cache üstte @say altta.
    Fonksiyonlar her seferinde burada yeniden tanımlandığı için sayaçlar sıfırdan başlar.
    """
    @say
    def fib(n: int) -> int:
        """Özyinelemeli Fibonacci (sadece say)."""
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    @say
    @lru_cache
    def fib_say_ustte(n: int) -> int:
        """Özyinelemeli Fibonacci (say dışta, önbellek içte)."""
        if n < 2:
            return n
        return fib_say_ustte(n - 1) + fib_say_ustte(n - 2)

    @lru_cache
    @say
    def fib_cache_ustte(n: int) -> int:
        """Özyinelemeli Fibonacci (önbellek dışta, say içte)."""
        if n < 2:
            return n
        return fib_cache_ustte(n - 1) + fib_cache_ustte(n - 2)

    fib(n)
    fib_say_ustte(n)
    fib_cache_ustte(n)
    return fib.cagri, fib_say_ustte.cagri, fib_cache_ustte.__wrapped__.cagri


if __name__ == "__main__":
    from uzay_oyunu.akis import rota_sayaci_onbelleksiz
    from uzay_oyunu.oyun import galaksi_yukle

    baglantilar = galaksi_yukle()["baglantilar"]

    # Görev 1: Hafta 4'teki önbelleksiz rota sayacının adim=20 için süresi
    rota_sayisi = sure_olc(rota_sayaci_onbelleksiz(baglantilar))
    rota_sayisi("dünya", 20)

    # Görev 2: fib(20) için dekoratör sırasına göre çağrı sayıları
    sayilar = fib_cagri_sayilari(20)
    print("Yalnızca @say             : " + str(sayilar[0]))
    print("@say üstte, @lru_cache altta: " + str(sayilar[1]))
    print("@lru_cache üstte, @say altta: " + str(sayilar[2]))
