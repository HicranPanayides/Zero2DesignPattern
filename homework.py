
"""def musteri_ekle():
    isim = input('Müşterinin İsmi: ')
    soyisim = input('Müşterinin Soyismi: ')
    while True:
        def kontrol(str):
            count = 0
            for ch in str:
                if ch == '@':
                    count = count + 1
            if count == 1:
                return True
            else:
                return False
        while True:
            email = input('e-mail: ')
            if not (kontrol(email)==True):
                print('Lütfen mail adresinizi kontrol ediniz.')
                email = input('e-mail: ')
            else:                
                while True:
                    tel = input('Telefon No: ')
                    if  not len(tel) == 10:
                     print('Lütfen 10 haneli telefon numarası giriniz.')
                    elif not tel.isdigit():
                        print('Tel no hatalı.')
                    else:
                        with open("Musteri_bilgi.txt","a",encoding="utf-8") as file:
                            file.write(isim+' '+ soyisim+ ','+email+ ','+tel+'\n')
                    print('Kayıt oluşturuldu.')
                    break
            break
        break"""
def musteri_sec():
    pass
def musteri_list():
    pass
def siparis_gir():
    urun = input('Ürün adı: ')
    u_miktari= input('Ürün Miktarı: ')
    siparis_tarih = input('Sipariş Tarihi: ')
    with open("Siparis_bilgi.txt","a",encoding="utf-8") as file:
        file.write(urun+' '+ u_miktari+ ','+siparis_tarih+'\n')

def siparis_menu():
    while True:
        siparis = (input('1- Müşteri Seç \n2- Yeni Müşteri ekle\n3- Sipariş Gir \n4- Menüye dön \n'))
        if siparis=='1':
            musteri_sec()
        elif siparis=='2':
            musteri_ekle()
        elif siparis=='3':
            siparis_gir()
        else:
            break

def durum_kontrol():
    pass
def listele():
    pass
while True:
    menu = (input('1- Yeni Müşteri Eklemek için 1 e basınız\n2- Sipariş girmek için 2 ye basınız\n3- Siparişin durumunu kontrol etmek için 3 e basınız\n4- Müşteri Listesi için 4 e basınız\n5- Çıkış\n'))
    if menu == '1':
        musteri_ekle()
    elif menu == '2':
        siparis_menu()
    elif menu == '3':
        durum_kontrol()
    elif menu == '4':
        listele()
    else:
        break
