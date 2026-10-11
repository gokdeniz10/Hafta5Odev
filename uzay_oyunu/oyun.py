# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 11.10.2026
# Açıklama: Uzay oyunu. Oyuncu gezegenler arasında dolaşır, kredi, hiperdrive
# ve pilot toplar, sonunda kara deliğe atlayarak oyunu kazanmaya çalışır.
# Oyun haritası galaksi.json dosyasından okunur.

import json

from uzay_oyunu.araclar import hamle_sayaci


def galaksi_kur(gezegenler: list[str], baglantilar: dict, baslangic: str, **kwargs: int) -> dict:
    """Gezegenler ve bağlantılardan bir galaksi sözlüğü kurar.

    Başlangıç gezegeni listede yoksa ValueError fırlatır.
    yakit verilmezse 50 olur.
    """
    if baslangic not in gezegenler:
        raise ValueError("Başlangıç gezegeni listede yok: " + baslangic)
    yakit = kwargs.get("yakit", 50)
    galaksi = {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }
    return galaksi


def galaksi_yukle() -> dict:
    """galaksi.json dosyasını okur ve galaksiyi kurar."""
    dosya = open("uzay_oyunu/galaksi.json", encoding="utf-8")
    veri = json.load(dosya)
    dosya.close()
    return galaksi_kur(**veri)


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Oyuncunun eşyalarını 'Sende: ...' metni olarak döndürür.

    Hiç eşya yoksa boş metin döndürür.
    """
    metin = ""
    if credits:
        metin = metin + "bol kredi"
    if engines:
        if metin != "":
            metin = metin + ", "
        metin = metin + "bir hiperdrive"
    if copilot:
        if metin != "":
            metin = metin + ", "
        metin = metin + "yetenekli bir pilot"
    if metin == "":
        return ""
    return "Sende: " + metin


def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek yerleri numaralı bir menü metni olarak döndürür."""
    metin = "Nereye gitmek istersin?"
    sira = 1
    for hedef in hedefler:
        metin = metin + "\n[" + str(sira) + "] " + hedef
        sira = sira + 1
    return metin


def travel() -> None:
    """Oyunu baştan sona oynatır."""
    print("Uzay yolculuğuna hoş geldin! Amacın kara delikten geçmek.")
    galaksi = galaksi_yukle()
    planet = galaksi["konum"]
    sayac = hamle_sayaci()
    toplam_hamle = 0
    credits = False
    engines = False
    copilot = False
    game_end = False

    while not game_end:
        print("-" * 40)

        # sendeki eşyaları göster
        envanter = envanter_metni(credits, engines, copilot)
        if envanter != "":
            print(envanter)

        # gezegende olanlar
        if planet == "dünya":
            print("Dünya'dasın. Buradan uzaya açılıyorsun.")

        if planet == "centauri":
            print("Centauri'desin. Burada bir uzay gemisi pazarı var.")
            if not engines:
                cevap = input("Hiperdrive almak ister misin? (evet/hayır) ")
                if cevap == "evet":
                    if credits:
                        print("Hiperdrive gemine takıldı.")
                        engines = True
                    else:
                        print("Hiperdrive için yeterli kredin yok.")

        if planet == "sirius":
            print("Sirius'tasın. Bir yarışma programına katıldın.")
            if not credits:
                print("Soru: Python'da listenin ilk elemanının indeksi kaçtır?")
                print("[1] 1   [2] 0   [3] -1")
                cevap = input()
                if cevap == "2":
                    print("Doğru! Bol kredi kazandın.")
                    credits = True
                else:
                    print("Yanlış cevap, ödül yok.")

        if planet == "orion":
            print("Orion'dasın. Barda bir pilot oturuyor.")
            if not copilot:
                cevap = input("Pilot bir bilmece soruyor: 6 x 7 kaç eder? ")
                if cevap == "42":
                    print("Pilot seninle gelmeyi kabul etti.")
                    copilot = True
                else:
                    print("Pilot başını sallayıp gidiyor.")

        if planet == "kara_delik":
            print("Kara deliğin kenarındasın.")
            cevap = input("Kara deliğe atlamak ister misin? (evet/hayır) ")
            if cevap == "evet":
                if engines and copilot:
                    print("Pilotun hiperdrive ile seni kara delikten geçirdi. Kazandın!")
                else:
                    print("Gemin kara deliğe dayanamadı. Kaybettin.")
                game_end = True

        # sonraki gezegeni seç
        if not game_end:
            destinations = galaksi["baglantilar"][planet]
            print(hedef_menusu(destinations))
            secim = input()
            planet = destinations[int(secim) - 1]
            toplam_hamle = sayac()

    print("Oyunu " + str(toplam_hamle) + " hamlede bitirdin!")


if __name__ == "__main__":
    travel()
