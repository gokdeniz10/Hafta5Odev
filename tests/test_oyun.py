# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 11.10.2026
# Açıklama: Oyunu baştan sona oynatan testler (Hafta 2'den kalan testler).

from uzay_oyunu.oyun import travel


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
