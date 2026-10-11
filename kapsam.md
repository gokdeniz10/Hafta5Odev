# Kapsam (Scope) Örnekleri

- **Ad Soyad:** Gökdeniz Demirbağ
- **Öğrenci No:** 20253004005
- **Tarih:** 11.10.2026
- **Açıklama:** Dersteki kapsam örneklerinin tahmini, gerçek çıktısı ve nedeni.

## Örnek 1 – Fonksiyon içinde aynı isimli değişken

```python
yakit = 100

def yolculuk():
    yakit = 30
    print("içeride:", yakit)

yolculuk()
print("dışarıda:", yakit)
```

**Tahminim:** `içeride: 30`, sonra `dışarıda: 30`.

**Gerçek sonuç:**

```
içeride: 30
dışarıda: 100
```

**Neden:** Fonksiyonun içinde `yakit = 30` yazınca Python yeni bir **yerel** değişken
oluşturuyor. Bu, dışarıdaki `yakit` değişkenini değiştirmiyor, sadece fonksiyonun
içinde onu gölgeliyor. Fonksiyon bitince yerel `yakit` siliniyor, dışarıdaki hâlâ 100.

## Örnek 2 – Fonksiyon dışarıdaki değişkeni okuyor

```python
gezegen = "dünya"

def nerede():
    print("şu an:", gezegen)

nerede()
gezegen = "mars"
nerede()
```

**Tahminim:** İki kere `şu an: dünya`.

**Gerçek sonuç:**

```
şu an: dünya
şu an: mars
```

**Neden:** `nerede()` içinde `gezegen` diye bir yerel değişken yok, o yüzden Python
dışarıdaki (global) `gezegen`e bakıyor. Bu bakma işi fonksiyon **tanımlanırken** değil
**çalışırken** oluyor. İkinci çağrıdan önce değer `"mars"` olduğu için `mars` yazdı.

## Örnek 3 – İç içe fonksiyonlar

```python
def dis():
    sayi = 1
    def ic():
        sayi = 2
        print("ic:", sayi)
    ic()
    print("dis:", sayi)

dis()
```

**Tahminim:** `ic: 2`, `dis: 2`.

**Gerçek sonuç:**

```
ic: 2
dis: 1
```

**Neden:** `ic()` içindeki `sayi = 2` yine `ic`'e ait yeni bir yerel değişken.
`dis`'teki `sayi` değişmiyor. Eğer `ic` içinde `nonlocal sayi` yazsaydık o zaman
`dis`'teki değişken değişirdi ve `dis: 2` çıkardı (Görev 5'teki sayaç böyle çalışıyor).

## UnboundLocalError örneği

```python
puan = 10

def puan_ekle():
    print(puan)
    puan = puan + 5

puan_ekle()
```

**Tahminim:** Önce `10` yazar, sonra puan 15 olur.

**Gerçek sonuç:**

```
UnboundLocalError: cannot access local variable 'puan' where it is not associated with a value
```

**Neden:** Python fonksiyonu çalıştırmadan önce bütün gövdesine bakıyor. İçeride
`puan = ...` diye bir atama gördüğü için `puan`ı fonksiyonun **tamamında** yerel değişken
sayıyor. Böylece `print(puan)` satırı dışarıdaki 10'u değil, henüz değer verilmemiş yerel
`puan`ı okumaya çalışıyor ve hata veriyor. Çözüm: değeri parametre olarak alıp yeni
değeri `return` ile döndürmek (`global` kullanmak bu ödevde yasak).
