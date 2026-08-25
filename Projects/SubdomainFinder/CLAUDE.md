# SubdomainFinder

Basit bir CLI subdomain bulucu.

## Yapı

- `main.py` — CLI ve tarama mantığı
- `subdomainwordlist.txt` — default kelime listesi

## Çalıştırma

```
python main.py -d example.com
python main.py -d example.com -w subdomainwordlist.txt -t 20
```

### Argümanlar

- `-d, --domain` (zorunlu): taranacak hedef domain
- `-w, --wordlist` (default: `subdomainwordlist.txt`): kelime listesi dosyası
- `-t, --threads` (default: `20`, 1-30 arası): paralel thread sayısı

## Mevcut davranış

- Wordlist dosyasındaki her kelime için `{word}.{domain}` şeklinde bir subdomain denenir.
- `socket.gethostbyname` ile çözümlenebilen host'lar bulunmuş sayılır (host, ip çifti olarak).
- Tarama `ThreadPoolExecutor` ile belirtilen thread sayısında paralel çalışır.
- Bulunan subdomain'ler `host -> ip` formatında konsola yazdırılır.
- Wordlist dosyası bulunamazsa ya da UTF-8 olarak okunamazsa temiz bir hata mesajıyla çıkılır (traceback yerine).
- Geçersiz/çözümlenemeyen bir hostname (`socket.gaierror` ya da IDNA encode hatası veren `UnicodeError`) sessizce atlanır; tek bir kötü kelime tüm taramayı çökertmez.
