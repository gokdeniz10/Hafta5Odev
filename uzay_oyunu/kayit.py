# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 11.10.2026
# Açıklama: Görev kaydı oluşturan fonksiyon. Değişken sayıda adım (*adimlar),
# sadece adıyla verilen öncelik ve istenildiği kadar ek bilgi (**ekler) alır.


def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str) -> str:
    """Bir görevi başlık, numaralı adımlar ve ek bilgilerle metin olarak döndürür.

    oncelik, *adimlar'dan sonra geldiği için sadece adıyla verilebilir.
    """
    metin = "[" + oncelik.upper() + "] " + baslik
    sira = 1
    for adim in adimlar:
        metin = metin + "\n " + str(sira) + ". " + adim
        sira = sira + 1
    for anahtar in ekler:
        metin = metin + "\n " + anahtar + ": " + ekler[anahtar]
    return metin


if __name__ == "__main__":
    # 1. çağrı biçimi: listeyi * ile, sözlüğü ** ile açarak
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Gökdeniz"}
    print(gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yüksek", **ekler))

    print()

    # 2. çağrı biçimi: argümanları tek tek yazarak
    print(gorev_kaydi("Sirius yarışmasını kazan", "Soruyu oku", "Doğru cevabı seç",
                      sorumlu="Gökdeniz", hobi="bilgisayar oyunları"))
