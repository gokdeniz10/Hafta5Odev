# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 11.10.2026
# Açıklama: Oyunu baştan sona oynatan testler (Hafta 2'den kalan testler).

from uzay_oyunu.oyun import galaksi_yukle, travel


def test_oyunu_kazan(monkeypatch, capsys):
    # input() her çağrıldığında listeden sıradaki cevabı versin
    girdiler = [
        "2",      # sirius'a git
        "2",      # yarışma sorusunu doğru cevapla
        "1",      # orion'a git
        "42",     # pilotun bilmecesi
        "1",      # centauri'ye git
        "evet",   # hiperdrive al
        "2",      # orion'a git
        "2",      # sirius'a git
        "3",      # kara deliğe git
        "evet",   # atla
    ]
    monkeypatch.setattr("builtins.input", lambda yazi="": girdiler.pop(0))
    travel()
    cikti = capsys.readouterr().out
    assert "Kazandın!" in cikti


def test_hazirliksiz_atlayinca_kaybet(monkeypatch, capsys):
    girdiler = ["2", "1", "3", "evet"]
    monkeypatch.setattr("builtins.input", lambda yazi="": girdiler.pop(0))
    travel()
    cikti = capsys.readouterr().out
    assert "Kaybettin." in cikti


def test_gecersiz_secimde_tekrar_sorar(monkeypatch, capsys):
    # "abc", "5" ve "0" geçersiz; oyun çökmemeli, sonra sirius'a gidilip kaybedilir
    girdiler = ["abc", "5", "0", "2", "1", "3", "evet"]
    monkeypatch.setattr("builtins.input", lambda yazi="": girdiler.pop(0))
    travel()
    cikti = capsys.readouterr().out
    assert cikti.count("Geçersiz seçim, tekrar dene.") == 3
    assert "Kaybettin." in cikti
    assert "Oyunu 2 hamlede bitirdin!" in cikti


def test_gecersiz_secim_yakit_harcamaz(monkeypatch, capsys):
    # önce 5 geçersiz seçim, sonra dünya ile sirius arasında gidip gelinir;
    # geçersiz seçimler yakıt harcasaydı 20 yerine 15 hamlede biterdi
    girdiler = ["abc"] * 5 + ["2"] * 22
    monkeypatch.setattr("builtins.input", lambda yazi="": girdiler.pop(0))
    travel()
    cikti = capsys.readouterr().out
    assert "Oyunu 20 hamlede bitirdin!" in cikti


def test_galaksi_baska_klasorden_yuklenir(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    assert galaksi_yukle()["konum"] == "dünya"


def test_komuttan_sonra_menu_tekrar_gosterilir(monkeypatch, capsys):
    # dünya'da "yardim" yaz, sonra sirius'a git ve hazırlıksız atlayıp kaybet
    girdiler = ["yardim", "2", "1", "3", "evet"]
    monkeypatch.setattr("builtins.input", lambda yazi="": girdiler.pop(0))
    travel()
    cikti = capsys.readouterr().out
    menu = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    yardim_cikti = "yardim    komutları listeler"
    assert yardim_cikti in cikti
    # menü komuttan önce bir kez, komuttan sonra bir kez daha gösterilmeli
    assert cikti.count(menu) == 2
    assert cikti.index(yardim_cikti) < cikti.rindex(menu)
    # sonra geçerli bir seçimle sirius'a gidilebilmeli
    assert "Sirius'tasın." in cikti
    assert "Oyunu 2 hamlede bitirdin!" in cikti
