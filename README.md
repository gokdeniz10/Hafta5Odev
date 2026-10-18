# Uzay Oyunu – İleri Python Programlama

- **Ad Soyad:** Gökdeniz Demirbağ
- **Öğrenci No:** 20253004005
- **Tarih:** 18.10.2026
- **Açıklama:** Hafta 4 Görev 4 ölçüm sonuçları.

## Hafta 4 – Görev 4: Önbellekli rota sayacı

`rota_sayisi("dünya", 20)` için `time.perf_counter()` ile ölçüldü:

| Sürüm       | Sonuç   | Süre                    |
|-------------|---------|-------------------------|
| Önbelleksiz | 4315343 | yaklaşık 0,66 saniye    |
| Önbellekli  | 4315343 | yaklaşık 0,00005 saniye |

`cache_info()` çıktısı:

```
CacheInfo(hits=47, misses=51, maxsize=128, currsize=51)
```

Önbelleksiz sürüm aynı (gezegen, adım) çiftini tekrar tekrar hesaplıyor. Önbellekli sürüm her
çifti bir kez hesaplıyor (51 miss), sonra aynı çift tekrar sorulunca sonucu önbellekten
alıyor (47 hit). Bu yüzden çok daha hızlı.
