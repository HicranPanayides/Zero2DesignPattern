musteriler = {}
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
            if not (kontrol(email)is True):
                print('Lütfen mail adresinizi kontrol ediniz.')
                email = input('e-mail: ')
            else:
                break
            break

