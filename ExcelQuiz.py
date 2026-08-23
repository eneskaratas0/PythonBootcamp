import pandas as pd
import numpy as np

df = pd.read_excel("27-SalarySheet.xlsx")
print("Data Base")
print(df)

#1) Toplamda kaç satır veri vardır?

print("1. soru",len(df))
# cevap

#2) Bu firma ortalama ne kadar maaş vermektedir?
ortalama_maas = df["Salary"].mean()
print("2. soru",ortalama_maas)
# cevap

#3) Bu firmada departmanlara göre ortalama maaş karşılaştırması nasıldır?
ortalama_maas_karsilastirmasi = df.groupby("Department")["Salary"].mean()
print("3. soru",ortalama_maas_karsilastirmasi)
# cevap)

#4) Bu firmada title (senior - junior) durumuna göre ortalama maaş karşılaştırması nasıldır?
ortalama_senior_junior_karsilastirmasi = df[df["Title"].isin(["Senior", "Junior"])].groupby("Title")["Salary"].mean()
print("4. soru",ortalama_senior_junior_karsilastirmasi)
# cevap

#5) Senior bir kişinin junior bir kişiye göre maaşı ortalama yüzde kaç fazladır?
senior_ort = df[df["Title"] == "Senior"]["Salary"].mean()
junior_ort = df[df["Title"] == "Junior"]["Salary"].mean()
senior_junior_yuzde = (senior_ort - junior_ort) / junior_ort * 100
print("5. soru",round(senior_junior_yuzde, 2))
# cevap

#6) Software development departmanında senior bir kişinin junior bir kişiye göre maaşı ortalama ne kadar fazladır?
sw_df = df[df["Department"] == "Software Development"]
sw_senior_ort = sw_df[sw_df["Title"] == "Senior"]["Salary"].mean()
sw_junior_ort = sw_df[sw_df["Title"] == "Junior"]["Salary"].mean()
print("6. soru",round(sw_senior_ort - sw_junior_ort, 2))
# cevap

#7) Finance departmanında c-level bir kişinin mid-senior bir kişiye göre maaşı ortalama ne kadar fazladır?
finance_df = df[df["Department"] == "Finance"]
finance_clevel_ort = finance_df[finance_df["Title"] == "C-level"]["Salary"].mean()
finance_midsenior_ort = finance_df[finance_df["Title"] == "Mid-Senior"]["Salary"].mean()
print("7. soru",round(finance_clevel_ort - finance_midsenior_ort, 2))
# cevap

#8) Software development departmanında c-level çalışan sayısı marketing departmanında çalışana oranla kaç kat fazladır?
sw_clevel_sayisi = len(df[(df["Department"] == "Software Development") & (df["Title"] == "C-level")])
marketing_sayisi = len(df[df["Department"] == "Marketing"])
oran = sw_clevel_sayisi / marketing_sayisi
print("8. soru",round(oran, 2))
# cevap