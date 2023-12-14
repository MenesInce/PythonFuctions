#  def <fonksiyon_ismi>(<argümanlar>) : #snake_case
#     """
#     bu kod ne işe yarar               #docstring
#     """
#     ...                               #return/print return döndürür/print ekrana yazar,bastırır,
    
#     
 

def bes_bastir() :
    """
    bu fonksiyon ekrana 5 bastırır
    """
    print(5)
bes_bastir()

def bes_dondur() : 
    return 5
a = bes_dondur()
print(a)

def sayi_dondur(sayi1) :
    return sayi1
b = sayi_dondur(78)
print(b) 
     
def sayi_dondur(sayi1 =250) : #default,parametre girmediğimiz zaman döner
    return sayi1
b = sayi_dondur()
print(b) 

def buyuk_sayi_dondur(a , b) :
    if a > b :
        return a
    else : 
        return b

c = buyuk_sayi_dondur(56,358)
print(c)
 
#* fonksiyonların birbirleri ile ilişkisi
def metin_yazdir(a,b) :
    buyuk_sayi = buyuk_sayi_dondur(a,b)
    sablon_metin = "{} daha büyük sayıdır".format(buyuk_sayi)
    print(sablon_metin)
metin_yazdir(5,10)

#* fonksiyonlar birden fazla sonuc döndürebilir
def isim_soyisim_ayirma(isim_soyisim) :
    isim = isim_soyisim.split()[0]
    soyisim = isim_soyisim.split()[1]
    return isim, soyisim

a = isim_soyisim_ayirma("Gökçe Gün")
print(a)

x,y = isim_soyisim_ayirma("Gökçe Gün")
print(x)
print(y)

#* *args argümanı 
#Bilgi ::> " ".join(["",""]) -> join belirttiğimiz simgeyi araya koyarak birleştirme yapar

def isim_soyisim_birlestir(isim, soyisim) :
   return " ".join([isim , soyisim])

a = isim_soyisim_birlestir("Oğuzcan","Bozkurt")
print(a)

def isim_soyisim_birlestir(*args) : # args listeye referans verir
       return " ".join(args) 

a = isim_soyisim_birlestir("Oğuzcan","Selami","Bozkurt")
print(a)

def gobek_adi_yazdir(**kwargs) : # dict olarak tutulur
    if "gobekAdi" in kwargs:
        print(kwargs["gobekAdi"])
    else : 
        print("Göbek adı yok")

gobek_adi_yazdir(adi = "Erol" ,soyadi = "Gün" )











