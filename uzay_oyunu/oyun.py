# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 11.10.2026
# Açıklama: Uzay oyunu. Oyuncu gezegenler arasında dolaşır, kredi, hiperdrive
# ve pilot toplar, sonunda kara deliğe atlayarak oyunu kazanmaya çalışır.


def travel() -> None:
    """Oyunu baştan sona oynatır."""
    print("Uzay yolculuğuna hoş geldin! Amacın kara delikten geçmek.")
    planet = "dünya"
    credits = False
    engines = False
    copilot = False
    game_end = False

    while not game_end:
        print("-" * 40)

        # sendeki eşyaları göster
        envanter = ""
        if credits:
            envanter = envanter + "bol kredi"
        if engines:
            if envanter != "":
                envanter = envanter + ", "
            envanter = envanter + "bir hiperdrive"
        if copilot:
            if envanter != "":
                envanter = envanter + ", "
            envanter = envanter + "yetenekli bir pilot"
        if envanter != "":
            print("Sende: " + envanter)

        # gezegende olanlar
        if planet == "dünya":
            print("Dünya'dasın. Buradan uzaya açılıyorsun.")
            destinations = ["centauri", "sirius"]

        if planet == "centauri":
            print("Centauri'desin. Burada bir uzay gemisi pazarı var.")
            destinations = ["dünya", "orion"]
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
            destinations = ["orion", "dünya", "kara_delik"]
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
            destinations = ["centauri", "sirius"]
            if not copilot:
                cevap = input("Pilot bir bilmece soruyor: 6 x 7 kaç eder? ")
                if cevap == "42":
                    print("Pilot seninle gelmeyi kabul etti.")
                    copilot = True
                else:
                    print("Pilot başını sallayıp gidiyor.")

        if planet == "kara_delik":
            print("Kara deliğin kenarındasın.")
            destinations = ["sirius"]
            cevap = input("Kara deliğe atlamak ister misin? (evet/hayır) ")
            if cevap == "evet":
                if engines and copilot:
                    print("Pilotun hiperdrive ile seni kara delikten geçirdi. Kazandın!")
                else:
                    print("Gemin kara deliğe dayanamadı. Kaybettin.")
                game_end = True

        # sonraki gezegeni seç
        if not game_end:
            print("Nereye gitmek istersin?")
            sira = 1
            for hedef in destinations:
                print("[" + str(sira) + "] " + hedef)
                sira = sira + 1
            secim = input()
            planet = destinations[int(secim) - 1]


if __name__ == "__main__":
    travel()
