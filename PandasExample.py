import pandas as pd
import numpy as np

# ---------------------- Örnek 1: Basit DataFrame oluşturma ve inceleme ----------------------

# # Örnek satış verisi
# data = {
#     "urun": ["A", "B", "C", "D"],
#     "fiyat": [120, 95, 200, 150],
#     "satis": [10, 15, 7, 20]
# }

# df = pd.DataFrame(data)

# print(df)
# print("\nİlk 3 satır:")
# print(df.head(3))

# print("\nÖzet bilgi:")
# print(df.info())

# print("\nTemel istatistikler:")
# print(df.describe())

# ---------------------- Örnek 1: Basit DataFrame oluşturma ve inceleme ----------------------


# ---------------------- Örnek 2: CSV dosyasından veri okuma ve temel analiz ----------------------

#df = pd.read_csv("satislar.csv")

#print(df.head())          # ilk 5 satır
#print(df.columns)         # sütun isimleri
#print(df.shape)           # (satır sayısı, sütun sayısı)

# Sadece 'fiyat' ve 'satis' sütunları
#print(df[["fiyat", "satis"]].head())

# Fiyatı 150'den yüksek ürünler
#pahalilar = df[df["fiyat"] > 150]
#print(pahalilar)

# Ortalama fiyat ve toplam satış
#print("Ortalama fiyat:", df["fiyat"].mean())
#print("Toplam satış:", df["satis"].sum())

# ---------------------- Örnek 2: CSV dosyasından veri okuma ve temel analiz ----------------------

# ---------------------- Örnek 3: Eksik veri ve veri temizleme ----------------------

# data = {
#     "urun": ["A", "B", "C", "D", "E"],
#     "fiyat": [120, np.nan, 200, 150, 90],
#     "satis": [10, 15, np.nan, 20, 5]
# }

# df = pd.DataFrame(data)

# print("Eksik değer sayısı:")
# print(df.isna().sum())

# # Eksik değerleri ortalama ile doldurma
# df["fiyat"] = df["fiyat"].fillna(df["fiyat"].mean())
# df["satis"] = df["satis"].fillna(df["satis"].mean())

# print("\nTemizlenmiş veri:")
# print(df)

# ---------------------- Örnek 3: Eksik veri ve veri temizleme ----------------------

# ---------------------- Örnek 4: Gruplama ve özet istatistikler ----------------------

# data = {
#     "sehir": ["İstanbul", "İstanbul", "Ankara", "Ankara", "İzmir", "İzmir"],
#     "urun":  ["A", "B", "A", "B", "A", "B"],
#     "satis": [100, 150, 80, 90, 120, 130]
# }

# df = pd.DataFrame(data)

# # Şehirlere göre toplam satış
# sehir_toplam = df.groupby("sehir")["satis"].sum()
# print("Şehirlere göre toplam satış:")
# print(sehir_toplam)

# # Şehir-ürün bazında ortalama satış
# grup_ortalama = df.groupby(["sehir", "urun"])["satis"].mean()
# print("\nŞehir-ürün bazında ortalama satış:")
# print(grup_ortalama)

# ---------------------- Örnek 4: Gruplama ve özet istatistikler ----------------------

# ---------------------- Örnek 5: Yeni sütun ekleme ve dönüşüm ----------------------

# data = {
#     "fiyat": [120, 95, 200, 150],
#     "satis": [10, 15, 7, 20]
# }

# df = pd.DataFrame(data)

# # Ciro = fiyat * satis
# df["ciro"] = df["fiyat"] * df["satis"]

# # İndirimli fiyat (%10 indirim)
# df["indirimli_fiyat"] = df["fiyat"] * 0.9

# print(df)

# ---------------------- Örnek 5: Yeni sütun ekleme ve dönüşüm ----------------------