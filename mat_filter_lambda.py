# map -> listenin her elemanına aynı fonksiyonu uygular

def karesini_al(x) :
    return x**2
a = karesini_al(5)
print(a)

sayilar = [*range(1,6)]
print(sayilar)
for index in range(len(sayilar)) :
    sayilar[index] = karesini_al(sayilar[index])
print(sayilar)

sayilar = [*range(1,6)]
print(list(map(karesini_al,sayilar)))

def cift_sayilari_filtrele(x) :
    
    if x%2==0:
        return x
    else :
        return None
    
a = cift_sayilari_filtrele(1)
print(a)


def cift_sayilari_filtrele(x) :
    return x if (x %2 == 0) else None

a = cift_sayilari_filtrele(10)
print(a)

sayilar = [*range(1,6)]
print(list(filter(cift_sayilari_filtrele,sayilar)))

sayilar = [*range(1,6)]
print([*map(lambda sayi : sayi ** 2 , sayilar)])

sayilar = [*range(1,6)]
print([*filter(lambda x: x if x%2 == 0 else None, sayilar )])