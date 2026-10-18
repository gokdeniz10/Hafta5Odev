# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 18.10.2026
# Açıklama: Bonus. zamanlayici(aralik) üreteciyle 10 saniye boyunca her 2 saniyede
# "tik", her 5 saniyede "tak" yazan program.

import time
from collections.abc import Iterator


def zamanlayici(aralik: float) -> Iterator[bool]:
    """Her next() çağrısında, son tetiklemeden beri aralik saniye geçtiyse True, geçmediyse False üretir."""
    son = time.time()
    while True:
        simdi = time.time()
        if simdi - son >= aralik:
            son = simdi
            yield True
        else:
            yield False


def tiktak(sure: float) -> None:
    """sure saniye boyunca her 2 saniyede 'tik', her 5 saniyede 'tak' yazar."""
    tik = zamanlayici(2)
    tak = zamanlayici(5)
    baslangic = time.time()
    # son tik/tak tam 10. saniyede geliyor, kaçırmamak için yarım saniye pay bırakıldı
    while time.time() - baslangic < sure + 0.5:
        if next(tik):
            print("tik")
        if next(tak):
            print("tak")


# Neden "meşgul bekleme" (busy waiting)?
# while döngüsü hiç durmadan dönüyor ve her turda next() ile "süre doldu mu?" diye soruyor.
# Saniyede milyonlarca kez soruluyor ve cevabın neredeyse hepsi False. Yani program beklerken
# boş durmuyor, işlemciyi sürekli meşgul ediyor (bir çekirdek %100 çalışıyor).
#
# time.sleep ile farkı:
# time.sleep(2) yazınca program 2 saniye boyunca işletim sistemine "beni uyut" diyor ve
# işlemciyi hiç kullanmıyor. Süre dolunca işletim sistemi programı uyandırıyor. Aynı işi
# neredeyse sıfır işlemci harcayarak yapıyor. Meşgul bekleme ise beklerken de enerji ve
# işlemci harcıyor.


if __name__ == "__main__":
    tiktak(10)
