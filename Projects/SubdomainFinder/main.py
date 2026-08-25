import argparse
import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from functools import partial


def scan_word(word, domain):
    target = f"{word}.{domain}"
    try:
        ip = socket.gethostbyname(target)
        return {"host": target, "ip": ip}
    except (socket.gaierror, UnicodeError):
        return None


def thread_count(value):
    ivalue = int(value)
    if not 1 <= ivalue <= 30:
        raise argparse.ArgumentTypeError("threads 1 ile 30 arasinda olmali")
    return ivalue


def parse_args():
    parser = argparse.ArgumentParser(description="Subdomain Bulucu")
    parser.add_argument("-d", "--domain", required=True, help="hedef domain, orn. example.com")
    parser.add_argument("-w", "--wordlist", default="subdomainwordlist.txt", help="kelime listesi dosyasi")
    parser.add_argument("-t", "--threads", type=thread_count, default=20, help="paralel thread sayisi (1-30)")
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        with open(args.wordlist, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        sys.exit(f"Hata: wordlist dosyasi bulunamadi: {args.wordlist}")
    except UnicodeDecodeError:
        sys.exit(f"Hata: wordlist dosyasi okunamadi (gecersiz encoding, UTF-8 bekleniyor): {args.wordlist}")

    print(f"{len(words)} kelime taranacak")

    scan = partial(scan_word, domain=args.domain)
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        results = list(executor.map(scan, words))
        finding = [r for r in results if r]
        print(f"{len(finding)} subdomain finding")
        for r in finding:
            print(r["host"], "->", r["ip"])

    print("Tarama tamamlandi !")


if __name__ == "__main__":
    main()
