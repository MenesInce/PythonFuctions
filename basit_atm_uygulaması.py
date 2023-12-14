print("""\t****BANKAMIZA HOŞ GELDİNİZ. sİZİ GÖRNEKTEN MUTLULUK DUYUYORUZ ****
      \t\t Lütfen Kartınızı Takınız... """)

veritabani = {
    "AhmetHesap" : {
        "ad" : "Ahmet",
        "soyad" : "Candan",
        "kartSifre" : "1357",
        "bakiye" : 5000,
        "borc" : 4200,
        "borcTarihi" : "20/11/2023"
    },

     "MehmetHesap" : {
        "ad" : "Mehmet",
        "soyad" : "Duyar",
        "kartSifre" : "2468",
        "bakiye" : 6000,
        "borc" : 3800,
        "borcTarihi" : "28/11/2023"
    }
}

takilanKart = dict(veritabani["AhmetHesap"])

yanlis_sifre_hakki = 2

for i in range(0,3) :
    sifre = str(input("4 haneli şifrenizi girin: "))
    if sifre == takilanKart.get("kartSifre") :
        print("Hoş geldiniz")
        
    elif sifre != takilanKart.get("kartSifre" ) and yanlis_sifre_hakki != 0 :
        print("Şifreniz Hatalı. Kalan deneme hakkınız : {}".format(yanlis_sifre_hakki))
        yanlis_sifre_hakki -= 1
    elif sifre != takilanKart.get("kartSifre") and yanlis_sifre_hakki == 0 :
        print("İşlem hakkınız kalmamıştır.En yakın şubemize başvurun.")
        exit()

    print(""" Yapabileceğiniz işlemler:
            [1] Bakiye Görüntüle
            [2] Para Yatır
            [3] Para Çek
            [4] Borç tarihini öğren
            [5] Borç öğren
            [6] Borç Öde
            
            """)
    islem = str(input("Yapmak istediğniz işlemi seçiniz"))
    if islem == "1" :
            bakiye = takilanKart.get("bakiye")
            print(bakiye)
    elif islem == "2" :
            tutar = int(input("Yatırmak istediğiniz tutarı girin : "))
            bakiye = takilanKart.get("bakiye")
            bakiye += tutar
            print("İşlem sonrası bakiyeniz {}".format(bakiye))
    elif islem == "3" :
            tutar = int(input("Çekmek istediğiniz tutarı girin : "))
            bakiye = takilanKart.get("bakiye")
            bakiye -= tutar
            print("İşlem sonrası bakiyeniz {}".format(bakiye))
    elif islem == "4" :
            print("Son ödeme tarihi : {} ".format(takilanKart.get("borcTarihi")))
    elif islem == "5" :
            print("Var olan borcunuz : {}".format(takilanKart.get("borc")))
    elif islem == "6" :
            odenecek_tutar = int(input("Ödeyeceğiniz tutarı girin :"))
            borc = takilanKart.get("borc")
            if odenecek_tutar < borc :
                kalan_borc = borc - odenecek_tutar
                print("Kalan borcunuz :{} ".format(kalan_borc))
            elif odenecek_tutar > borc :
                  artan_para = odenecek_tutar - borc
                  print("Borcunuz ödendi.Artan tutar :{}. Artan para bakiyenize eklenecektir. ".format(artan_para))
                  bakiye = takilanKart.get("bakiye")
                  bakiye += artan_para
                  print("İşlem sonrası bakiyeniz : {}".format(bakiye))
               

        
        

        
        





        
