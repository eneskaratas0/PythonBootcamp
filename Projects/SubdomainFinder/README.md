# SubdomainFinder

Basit, hızlı ve tek dosyalık bir CLI subdomain bulucu. Bir wordlist'teki her
kelime için `{word}.{domain}` şeklinde subdomain'ler oluşturur ve DNS çözümü
yapılabilenleri raporlar.

## Özellikler

- Çoklu thread ile paralel DNS taraması (`ThreadPoolExecutor`)
- Harici bağımlılık yok — sadece Python standart kütüphanesi
- Wordlist dosyası bulunamazsa veya bozuk encoding'deyse temiz hata mesajı
- Geçersiz/çözümlenemeyen hostname'ler taramayı çökertmeden atlanır

## Gereksinimler

- Python 3.8+

## Kurulum

```bash
git clone <repo-url>
cd SubdomainFinder
```

Ekstra bağımlılık kurulumu gerekmez.

## Kullanım

```bash
python main.py -d example.com
python main.py -d example.com -w subdomainwordlist.txt -t 20
```

### Argümanlar

| Argüman | Zorunlu | Varsayılan | Açıklama |
|---|---|---|---|
| `-d`, `--domain` | Evet | — | Taranacak hedef domain (örn. `example.com`) |
| `-w`, `--wordlist` | Hayır | `subdomainwordlist.txt` | Kelime listesi dosyası |
| `-t`, `--threads` | Hayır | `20` | Paralel thread sayısı (1-30 arası) |

### Örnek çıktı

```
$ python main.py -d example.com
5000 kelime taranacak
1 subdomain finding
www.example.com -> 172.66.147.243
Tarama tamamlandi !
```

## Proje yapısı

- `main.py` — CLI ve tarama mantığı
- `subdomainwordlist.txt` — varsayılan kelime listesi

## Nasıl çalışır

1. Wordlist dosyası satır satır okunur, boş satırlar atlanır.
2. Her kelime için `{word}.{domain}` hostname'i `socket.gethostbyname` ile
   çözümlenmeye çalışılır; başarılı olursa `host -> ip` çifti sonuç listesine
   eklenir.
3. Tarama, `-t` ile belirtilen thread sayısında paralel yürütülür.
4. Bulunan tüm subdomain'ler konsola yazdırılır.

## Sorumluluk reddi

Bu araç yalnızca **yetkiniz olan** hedefler üzerinde, eğitim ve güvenlik
testi amacıyla kullanılmalıdır. İzinsiz taramalardan doğacak sonuçların
sorumluluğu kullanıcıya aittir.
