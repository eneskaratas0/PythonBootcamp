import numpy as np

# ------------ Temel dizi işlemleri ve istatistik ------------

# # Rastgele satış verisi (örnek: 10 gün)
# satislar = np.random.randint(100, 1000, size=10)

# print("Satışlar:", satislar)
# print("Toplam satış:", satislar.sum())
# print("Ortalama satış:", satislar.mean())
# print("Medyan:", np.median(satislar))
# print("Standart sapma:", satislar.std())
# print("Minimum:", satislar.min())
# print("Maksimum:", satislar.max())

# ------------ Filtreleme ve koşullu seçim ------------

# fiyatlar = np.array([120, 95, 200, 150, 80, 300, 170])

# # 150'den yüksek fiyatlar
# pahalilar = fiyatlar[fiyatlar > 150]
# print("150'den pahalı ürünler:", pahalilar)

# # 100 ile 200 arasında olanlar
# orta_seviye = fiyatlar[(fiyatlar >= 100) & (fiyatlar <= 200)] # 2 boytulu dizi olusturur.
# print("100-200 arası fiyatlar:", orta_seviye)

# ------------ Eksik veri ve aykiri deger (outlier) analizi ------------

# # Örnek fiyat verisi (bir aykırı değer var: 2000)
# fiyatlar = np.array([100, 120, 130, 115, 2000, 125, 110])

# ortalama = fiyatlar.mean()
# std = fiyatlar.std()

# # Z-skoru ile aykırı değer tespiti
# z_scores = (fiyatlar - ortalama) / std
# aykiri_degerler = fiyatlar[np.abs(z_scores) > 2]

# print("Ortalama:", ortalama)
# print("Standart sapma:", std)
# print("Aykırı değerler (Z-skoru > 2):", aykiri_degerler)

# ------------ İki veri seti üzerinde işlem (örnek: gelir–gider) ------------

# gelir = np.array([5000, 6000, 5500, 7000, 6200])
# gider = np.array([3000, 3200, 2900, 3500, 3100])

# net = gelir - gider
# kar_orani = net / gelir  # net kâr oranı

# print("Net kâr:", net)
# print("Kâr oranı:", kar_orani)
# print("Ortalama kâr oranı:", kar_orani.mean())

# ------------ Matrislerle analiz (örnek: çarpım ve özet istatistik) ------------

# # Ürün bazlı aylık satış matrisi (3 ürün x 4 ay)
# satis_matrisi = np.array([
#     [10, 15, 20, 25],   # Ürün A
#     [5,  8, 12, 10],    # Ürün B
#     [20, 22, 18, 30]    # Ürün C
# ])

# # Her ürünün toplam satışı
# urun_toplam = satis_matrisi.sum(axis=1)
# # Her ayın toplam satışı
# ay_toplam = satis_matrisi.sum(axis=0)

# print("Ürün bazlı toplam satış:", urun_toplam)
# print("Ay bazlı toplam satış:", ay_toplam)

# # Ortalama aylık satış (tüm ürünler için)
# print("Genel ortalama aylık satış:", satis_matrisi.mean())

# ------------ Basit bir “veri ön işleme” örneği (normalizasyon) ------------

# Örnek: farklı ölçeklerde özellikler (yaş, gelir)
yas = np.array([20, 25, 30, 35, 40], dtype=float)
gelir = np.array([5000, 7000, 9000, 12000, 15000], dtype=float)

# Min-max normalizasyon (0-1 aralığına çekme)
def min_max_normalize(x):
    return (x - x.min()) / (x.max() - x.min())

yas_norm = min_max_normalize(yas)
gelir_norm = min_max_normalize(gelir)

print("Normalize edilmiş yaş:", yas_norm)
print("Normalize edilmiş gelir:", gelir_norm)