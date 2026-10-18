# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 18.10.2026
# Açıklama: Galaksi verisi üzerinde aynı üç soruyu iki yolla yanıtlayan fonksiyonlar
# (map/filter/reduce ve liste üreteci/sum) ve partial ile türetilen hizli_yolculuk.

from functools import partial, reduce


# --- 1. soru: gezegen adlarının büyük harfli listesi ---

def buyuk_harfli_adlar_map(galaksi: dict) -> list[str]:
    """Gezegen adlarını map ile büyük harfe çevirir."""
    return list(map(str.upper, galaksi["gezegenler"]))


def buyuk_harfli_adlar_liste(galaksi: dict) -> list[str]:
    """Gezegen adlarını liste üreteci ile büyük harfe çevirir."""
    return [gezegen.upper() for gezegen in galaksi["gezegenler"]]


# --- 2. soru: en az iki bağlantısı olan gezegenler ---

def iki_baglantili_filter(galaksi: dict) -> list[str]:
    """En az iki bağlantısı olan gezegenleri filter ile bulur."""
    baglantilar = galaksi["baglantilar"]
    return list(filter(lambda g: len(baglantilar[g]) >= 2, galaksi["gezegenler"]))


def iki_baglantili_liste(galaksi: dict) -> list[str]:
    """En az iki bağlantısı olan gezegenleri liste üreteci ile bulur."""
    baglantilar = galaksi["baglantilar"]
    return [g for g in galaksi["gezegenler"] if len(baglantilar[g]) >= 2]


# --- 3. soru: toplam bağlantı sayısı ---

def toplam_baglanti_reduce(galaksi: dict) -> int:
    """Bütün gezegenlerin bağlantı sayılarını reduce ile toplar."""
    baglantilar = galaksi["baglantilar"]
    return reduce(lambda toplam, g: toplam + len(baglantilar[g]), galaksi["gezegenler"], 0)


def toplam_baglanti_sum(galaksi: dict) -> int:
    """Bütün gezegenlerin bağlantı sayılarını sum ile toplar."""
    baglantilar = galaksi["baglantilar"]
    return sum(len(baglantilar[g]) for g in galaksi["gezegenler"])


# Hangisi daha okunaklı?
# Liste üreteci ve sum ile yazılanları daha okunaklı buluyorum. Satırı soldan sağa
# okuyunca ne yaptığı direkt anlaşılıyor. map/filter/reduce'da ise lambda'nın içini ayrıca
# çözmek gerekiyor, özellikle reduce'daki (toplam, g) sırası ve başlangıç değeri 0
# ilk bakışta kafa karıştırıyor.


# --- partial ---

def yolculuk(kaynak: str, hedef: str, hiz: int = 1) -> str:
    """Bir yolculuğu kaynak, hedef ve hız bilgisiyle metin olarak döndürür."""
    return kaynak + " -> " + hedef + " (hız: " + str(hiz) + ")"


# hiz=3 sabitlenmiş yeni fonksiyon: hizli_yolculuk("dünya", "sirius") yazmak yeterli
hizli_yolculuk = partial(yolculuk, hiz=3)


if __name__ == "__main__":
    from uzay_oyunu.oyun import galaksi_yukle

    g = galaksi_yukle()

    print("map/filter/reduce ile:")
    print(buyuk_harfli_adlar_map(g))
    print(iki_baglantili_filter(g))
    print(toplam_baglanti_reduce(g))

    print("liste üreteci ve sum ile:")
    print(buyuk_harfli_adlar_liste(g))
    print(iki_baglantili_liste(g))
    print(toplam_baglanti_sum(g))

    print("partial ile:")
    print(yolculuk("dünya", "sirius"))
    print(hizli_yolculuk("dünya", "sirius"))
