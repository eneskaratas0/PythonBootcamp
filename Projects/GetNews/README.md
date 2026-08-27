# GetNews

`requests` ve `BeautifulSoup` ile [Hacker News](https://news.ycombinator.com/) ana sayfasındaki ilk 30 haberi başlık ve link olarak terminale yazdıran basit bir CLI aracı.

## Özellikler

- Hacker News ana sayfasını `requests` ile çeker
- `BeautifulSoup` ile haber satırlarını (`tr.athing.submission`) parse eder
- İlk 30 haberi sıra numarası, başlık ve link ile terminale yazdırır
- Bağlantı hatası, zaman aşımı ve başarısız HTTP durum kodları için hata kontrolü (`try/except`, `raise_for_status`)

## Çalıştırma

```bash
pip install requests beautifulsoup4
python3 main.py
```

## Örnek Çıktı

```
1. LINK -> https://example.com/article, HEADER -> Örnek Başlık
2. LINK -> https://example.com/article2, HEADER -> Başka Bir Başlık
...
```
