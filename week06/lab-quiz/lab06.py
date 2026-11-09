branslar = ("Yazılım", "Tasarım", "Pazarlama")
tum_ogrenciler = []
ogrenci1 =["Hilal".strip(), ["Yazılım","Tasarım"]]
ogrenci2 =["Ahmet".strip(), ["Tasarım", "Pazarlama"]]
ogrenci3 =["Hazal".strip(), ["Yazılım", "Pazarlama"]]
tum_ogrenciler.append(ogrenci1)
tum_ogrenciler.append(ogrenci2)
tum_ogrenciler.append(ogrenci3)
baskan = ["Mehmet".strip(), ["Yazılım"]]
tum_ogrenciler.insert(0, baskan)
len(tum_ogrenciler)
print(f"Toplam Kayıtlı Öğrenci Sayısı: {len(tum_ogrenciler)}")
tum_ogrenciler.remove(ogrenci2)
son_ogrenci = tum_ogrenciler.pop()
print(f"Son Kayıtlı Öğrenci: {son_ogrenci[0]}")
yeni_ogrenci = ["Burak Tan".strip(), ["Tasarım"]]
tum_ogrenciler.append(yeni_ogrenci)
print("Geçici Sıralı Liste:", sorted(tum_ogrenciler))
print("Orijinal Liste:", tum_ogrenciler)
tum_ogrenciler.sort()
print("Kalıcı Sıralı Liste:", tum_ogrenciler)
