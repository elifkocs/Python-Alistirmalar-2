###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4,"String",3.2, False]

d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}


t = ("Machine Learning", "Data Science")

s = {"Python", "Machine Learning", "Data Science","Python"}

###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."
words = text.upper().replace(",", " ").replace(".", " ").split()
print(words)

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
eleman_sayisi = len(lst)
print(eleman_sayisi)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
sifirinciIndex = lst[0]
onuncuIndex = lst[10]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.

yeni_liste = lst[:4]
print(yeni_liste)

# Adım 4: Sekizinci index'teki elemanı silin.

del lst[8]
print(lst)

# Adım 5: Yeni bir eleman ekleyin.

lst.append("D")
print(lst)

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.insert(8, "N")
print(lst)

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

anahtarlar = dict.keys()

# Adım 2: Value'lara erişiniz.

for deger in dict.values():
    print(deger)

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict["Daisy"] = 13
print(dict)

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict["Ahmet"] = ["Turkey", 24]
print(dict)

# Adım 5: Antonio'yu dictionary'den siliniz.

del dict["Antonio"]
print(dict)


###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

def tek_cift_ayir(sayi_listesi):
    tekler = []
    ciftler = []

    for sayi in sayi_listesi:
        if sayi % 2 == 0:
            ciftler.append(sayi)
        else:
            tekler.append(sayi)

    return tekler, ciftler

l = [2,13,18,93,22]
tek_sayilar, cift_sayilar = tek_cift_ayir(l)

print("Tek Sayılar:", tek_sayilar)
print("Çift Sayılar:", cift_sayilar)


###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
# Listenin ilk 3 elemanı Mühendislik Fakültesi
muhendislik = ogrenciler[:3]
# Listenin son 3 elemanı Tıp Fakültesi
tip = ogrenciler[3:]

print("MÜHENDİSLİK FAKÜLTESİ DERECELERİ:")
for derece, ogrenci in enumerate(muhendislik, 1):
    print(f"{derece}. {ogrenci}")

print("\nTIP FAKÜLTESİ DERECELERİ:")
for derece, ogrenci in enumerate(tip, 1):
    print(f"{derece}. {ogrenci}")

###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for kod, kr, kont in zip(ders_kodu, kredi, kontenjan):
    print(f"Ders Kodu: {kod} | Kredisi: {kr} | Kontenjanı: {kont}")

###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kume_islemi(kume1, kume2):
    # 1. küme 2. kümeyi kapsıyor mu kontrolü
    if kume1.issuperset(kume2):
        print("1. küme 2. kümeyi kapsıyor.")
        # Ortak elemanları (kesişimi) döndür
        return kume1.intersection(kume2)
    else:
        print("1. küme 2. kümeyi kapsamıyor.")
        # 2. kümenin 1. kümeden farkını döndür
        return kume2.difference(kume1)

print("Senaryo Sonucu:", kume_islemi(kume1, kume2))

