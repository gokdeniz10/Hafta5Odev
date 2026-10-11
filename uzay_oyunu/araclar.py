# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 11.10.2026
# Açıklama: Oyunda kullanılan yardımcı fonksiyonlar.


def yakit_ekle(miktar: int, depo: list | None = None) -> list:
    """Verilen miktarı depoya ekler ve depoyu döndürür.

    Depo verilmezse her çağrıda yeni boş bir liste kullanılır.
    (Varsayılan değer [] olsaydı aynı liste bütün çağrılarda paylaşılırdı.)
    """
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo
