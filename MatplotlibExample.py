import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ------------------- Örnek 1: Basit çizgi grafiği (line plot) ------------------- #

# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# plt.plot(x, y)
# plt.xlabel("X ekseni")
# plt.ylabel("Y ekseni")
# plt.title("Basit Çizgi Grafiği")
# plt.show()

# ------------------- Örnek 2: Dağılım grafiği (scatter plot) ------------------- #

# np.random.seed(0)
# x = np.random.rand(50)
# y = np.random.rand(50)

# plt.scatter(x, y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Dağılım Grafiği (Scatter Plot)")
# plt.show()

# ------------------- Örnek 3: Çubuk grafiği (bar plot) ------------------- #

# urunler = ["A", "B", "C", "D"]
# satislar = [120, 95, 200, 150]

# plt.bar(urunler, satislar)
# plt.xlabel("Ürün")
# plt.ylabel("Satış")
# plt.title("Ürün Bazında Satışlar")
# plt.show()

# ------------------- Örnek 4: Histogram (dağılım analizi) ------------------- #

# np.random.seed(0)
# veri = np.random.randn(1000)  # normal dağılımdan rastgele 1000 sayı

# plt.hist(veri, bins=30, edgecolor="black")
# plt.xlabel("Değer")
# plt.ylabel("Frekans")
# plt.title("Histogram")
# plt.show()

# ------------------- Örnek 5: Pasta grafiği (pie chart) ------------------- #

# kategoriler = ["Kira", "Yemek", "Ulaşım", "Eğlence"]
# tutarlar = [3000, 1500, 500, 700]

# plt.pie(tutarlar, labels=kategoriler, autopct="%1.1f%%")
# plt.title("Aylık Harcama Dağılımı")
# plt.show()

# ------------------- Örnek 6: Birden fazla çizgi ve açıklama (legend) ------------------- #

# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, label="sin(x)")
# plt.plot(x, y2, label="cos(x)", linestyle="--")

# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.title("sin(x) ve cos(x) Grafikleri")
# plt.legend()
# plt.grid(True)
# plt.show()

# ------------------- Örnek 7: Pandas DataFrame ile birlikte kullanım ------------------- #

# Örnek veri
data = {
    "ay": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs"],
    "satis": [120, 150, 130, 170, 160]
}
df = pd.DataFrame(data)

plt.plot(df["ay"], df["satis"], marker="o")
plt.xlabel("Ay")
plt.ylabel("Satış")
plt.title("Aylık Satış Grafiği")
plt.grid(True)
plt.show()