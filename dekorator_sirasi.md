# Dekoratör Sırası ve Çağrı Sayısı

- **Ad Soyad:** Gökdeniz Demirbağ
- **Öğrenci No:** 20253004005
- **Tarih:** 25.10.2026
- **Açıklama:** Hafta 5 Görev 2. fib(20) için üç dekoratör sırasında çağrı sayıları ve nedenleri.

Ölçüm `python -m uzay_oyunu.dekoratorler` ile yapıldı (`fib_cagri_sayilari(20)`):

```
Yalnızca @say             : 21891
@say üstte, @lru_cache altta: 39
@lru_cache üstte, @say altta: 21
```

Dekoratörler alttan üste doğru uygulanır. `@a` üstte, `@b` altta ise `fib = a(b(fib))` olur.
Yani üstteki dekoratör en dışta durur ve her çağrı önce ona gelir. Fonksiyonun içindeki
özyinelemeli `fib(n - 1)` çağrıları da `fib` adına, yani en dıştaki sarmalayıcıya gider.

## 1. Yalnızca @say: 21891

Önbellek yok. `fib(20)`, `fib(19)` ve `fib(18)`'i çağırıyor, onlar da kendi alt
çağrılarını yapıyor. Aynı değerler (mesela `fib(5)`) yüzlerce kez yeniden hesaplanıyor.
`say` her çağrıyı saydığı için sayı çok büyük çıkıyor.

## 2. @say üstte, @lru_cache altta: 39

`fib = say(lru_cache(fib))`. `say` en dışta olduğu için önbellekten dönen çağrılar dahil
her çağrıyı sayar. Ama önbellek sayesinde her `n` değeri sadece bir kez gerçekten
hesaplanır. `fib(20)`'den `fib(2)`'ye kadar 19 değer hesaplanır, her biri `fib(n - 1)` ve
`fib(n - 2)` olmak üzere iki çağrı yapar. İlk çağrı da eklenince 1 + 19 × 2 = 39 olur.
Bu çağrıların bir kısmı önbellekten hemen dönse de `say`'den geçtikleri için sayılırlar.

## 3. @lru_cache üstte, @say altta: 21

`fib = lru_cache(say(fib))`. Bu sefer `say` içeride. Önbellekte olan bir değer
istenince `lru_cache` sonucu hemen döndürür ve `say`'e hiç gelinmez. `say` sadece
gerçekten hesaplanan değerleri sayar: `fib(0)`'dan `fib(20)`'ye kadar 21 farklı değer.

Bu durumda sayaca `fib.cagri` ile değil `fib.__wrapped__.cagri` ile ulaşılır. Çünkü
dıştaki `fib` artık `lru_cache`'in sarmalayıcısıdır. `__wrapped__`, `wraps`'in sakladığı
bir içteki fonksiyondur, yani `say`'in sarmalayıcısı. (`wraps`, `cagri` niteliğini de dışa
kopyalar ama kopyalandığı anda değeri 0'dır ve sonra hiç artmaz.)
