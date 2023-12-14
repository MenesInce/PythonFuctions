sayi = input("Bir sayı girin : ")
print(sayi)

def uygulama() :
    sayi = int(input("Bir sayı girin : "))
    islem = str(input("Tek mi? Çift mi? Sorgula : "))

    if islem == "çift":
        if sayi %2 == 0:
            return "{} sayisi bir çift sayıdır".format(sayi)
        else : 
            return "{} sayisi bir çift sayı değildir".format(sayi)
    elif islem == "tek":
        if sayi %2 == 1:
            return "{} sayisi bir tek sayıdır".format(sayi)
        else : 
            return "{} sayisi bir tek sayı değildir".format(sayi)
print(uygulama())


def sayi_girdisi_control() :
    girdi = input("Bir sayı girin : ")
    if girdi.isdigit() :
        print("Tebrikler sayı tipi değer girdiniz")
    else : 
        print("Bu bir sayı tipi değer değildir")
sayi_girdisi_control()


def sayi_girdisi_control_dongu() :
     girdi = input("Bir sayı girin : ")
     while not girdi.isdigit() :
             print("Bu bir sayı tipi değer değildir")
             girdi = input("Bir sayı girin : ")
     else :
            print("Tebrikler sayı tipi değer girdiniz")
sayi_girdisi_control_dongu()

            
def eposta_control() :
          girdi = input("geçerli bir eposta adresi giriniz : ")

          while not (("." in girdi) and ("@" in girdi)):
                print("Bu geçerli bir eposta adresi değildir")
                girdi = input("geçerli bir eposta adresi giriniz : ")
          else :
                print("Tebrikler başarılı giriş")
eposta_control()
                

            


