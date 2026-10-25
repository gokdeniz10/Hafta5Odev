# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 25.10.2026
# Açıklama: Oyundaki komutlar. komut dekoratörü fonksiyonları KOMUTLAR
# sözlüğüne kaydeder, travel() oyuncunun yazdığı komutu buradan bulur.

from collections.abc import Callable

from uzay_oyunu.oyun import envanter_metni

# komut adı -> (fonksiyon, açıklama)
KOMUTLAR: dict[str, tuple[Callable, str]] = {}


def komut(ad: str, aciklama: str = "") -> Callable:
    """Fonksiyonu verilen adla KOMUTLAR sözlüğüne kaydeden dekoratör.

    Fonksiyonu değiştirmez, aynısını geri döndürür. Bu yüzden wraps gerekmez.
    Aynı ad iki kez kullanılırsa tanım anında ValueError fırlatır.
    """
    def kaydet(fonksiyon: Callable) -> Callable:
        """Fonksiyonu kaydeder ve olduğu gibi geri döndürür."""
        if ad in KOMUTLAR:
            raise ValueError("Bu komut adı zaten kullanılıyor: " + ad)
        KOMUTLAR[ad] = (fonksiyon, aciklama)
        return fonksiyon

    return kaydet


@komut("yardim", "komutları listeler")
def yardim(durum: dict) -> str:
    """Bütün komutları açıklamalarıyla, ada göre sıralı listeler."""
    # en uzun komut adını bul, açıklamalar aynı sütundan başlasın
    genislik = 0
    for ad in KOMUTLAR:
        if len(ad) > genislik:
            genislik = len(ad)
    metin = ""
    for ad in sorted(KOMUTLAR):
        if metin != "":
            metin = metin + "\n"
        aciklama = KOMUTLAR[ad][1]
        metin = metin + ad + " " * (genislik - len(ad) + 2) + aciklama
    return metin


@komut("envanter", "eşyalarını gösterir")
def envanter(durum: dict) -> str:
    """Oyuncunun eşyalarını gösterir."""
    return envanter_metni(durum["credits"], durum["engines"], durum["copilot"])


@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum: dict) -> str:
    """Bulunulan gezegenden gidilebilecek gezegenleri virgülle ayırarak gösterir."""
    metin = ""
    for gezegen in durum["baglantilar"][durum["konum"]]:
        if metin != "":
            metin = metin + ", "
        metin = metin + gezegen
    return metin
