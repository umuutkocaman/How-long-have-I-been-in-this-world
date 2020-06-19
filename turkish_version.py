import datetime as dt
kontrol = True
while kontrol:
    dogumTarihi = input("Dogum tarihinizi gün/ay/yıl şeklinde aralarda / olacak şekilde giriniz. Çıkmak için 'q' veya 'ç'. ")
    if dogumTarihi.lower == "q" or dogumTarihi.lower == "ç":
        break
    else:
        tarih = dogumTarihi.split('/') # gün, ay, yıl ayırma
        #kullanıcının girdiği tarihi / ile ayırıp ayırmadığının kontrolü. Farklı bir şey ile ayırırsa split işlemi 1 değer döndürür. ancak doğru girildiyse 3 değer döndürür.
        if len(tarih) == 3: 
            gun = tarih[0]
            ay = tarih[1]
            yıl = tarih[2]

            bugun = dt.datetime.now() # bugünün tarihinin alınması
            bugun2 = str(bugun) #gün,, ay, yıl değerlerinin ayrı ayrı alınabilmesi için string türüne çevrilmesi
            buYıl = bugun2[:4]
            buAy = bugun2[5:7]
            buGun = bugun2[8:10]
 
            if int(yıl) > int(buYıl): # bulunulan yıldan sonraki yıl girilip girilmediğinin kontrolü
                print(f"Yanlış yıl bilgisi girdiniz. Lütfen {buYıl} veya daha küçük bir değer giriniz")
                continue
            elif int(ay) <= 0 or int(ay) > 12 : # 1-12 arası ay kontrolü
                print("Yanlış ay bilgisi girdiniz. Lütfen 1-12 arasında bir ay bilgisi giriniz")
                continue
            elif int(gun) <= 0: #0'dan küçük gün kontrolü
                print("0 veya daha düşük bir gün değeri giremezsiniz.")
                continue

            #ayın günlerine göre gün kontrolü
            elif (int(ay) == 1 or int(ay) == 3 or int(ay) == 5 or int(ay) == 7 or int(ay) == 8 or int(ay) == 10 or int(ay) == 12) and int(gun) > 31:
                print(f"{ay}. ay 31 gündür. Daha yüksek bir değer giremezsiniz.")
                continue
            elif (int(ay) == 4 or int(ay) == 6 or int(ay) == 9 or int(ay) == 11) and int(gun) > 30:
                print(f"{ay}. ay 30 gündür. Daha yüksek bir değer giremezsiniz.")
                continue

            #artık yıla göre şubat ayı gün kontrolü
            elif int(ay) == 2:
                if int(yıl) % 4 == 0:
                    if int(yıl) % 100 == 0:
                        if int(yıl) %400 == 0 :
                            if int(gun) > 29:
                                print(f"{ay}. ay bu yıl 29 gündür. Daha yüksek bir değer giremezsiniz.")
                                continue
                        else:
                            if int(gun) > 28:
                                print(f"{ay}. ay bu yıl 28 gündür. Daha yüksek bir değer giremezsiniz.")
                                continue
                    else:
                        if int(gun) > 29:
                            print(f"{ay}. ay bu yıl 29 gündür. Daha yüksek bir değer giremezsiniz.")
                            continue
                else:
                    if int(gun) > 28:
                        print(f"{ay}. ay bu yıl 28 gündür. Daha yüksek bir değer giremezsiniz.")
                        continue

            #O yılda doğum günü girilmesi durumunda ay kontrolü         
            elif int(yıl) == int(buYıl):
                if int(ay) > int(buAy):
                    print(f"Yanlış Ay bilgisi girdiniz. Şuan {buAy}. aydayız. Lütfen bundan önceki bir tarih giriniz")
                    continue
                
                #o yıl ve o ay doğum tarihi girildiyse gün kontrolü
                elif int(ay) == int(buAy) and int(gun) > int(buGun):
                    print(f"Yanlış gün bilgisi girdiniz. Şuan {buGun}. gündeyiz. Lütfen bundan önceki bir tarih giriniz")
                    continue  
                
            while True:
                try:
                    dogumSaati = int(input("Dogum saatinizi biliyor musunuz? Evet için 1, Hayır için 0'a basınız: "))
                    if dogumSaati == 1:
                        dogumSaati = input("Lütfen doğum saatinizi 00:00 şeklinde arada : olacak şekilde giriniz: ")
                        s = dogumSaati.split(':') # saat ve dakikaya ayırma
                        saat = s[0]
                        dakika = s[1]
                        detaylıDogumTarihi = dt.datetime(int(yıl), int(ay), int(gun), int(saat), int(dakika)) #alt satırda tarih farkını bulabilmek için girilen doğum tarihini datetime türüne çevrilmesi
                        gecenSure = bugun - detaylıDogumTarihi #timedelta türünde hesaplar 
                        
                        #timedelta türündeki sonuç days ve seconds verisi döndürür. bunlara göre saat, dakika ve saniyenin hesaplanması
                        gecenSaat = (gecenSure.days * 24 +  gecenSure.seconds // 3600 ) % 24 
                        gecenDakika = (gecenSure.seconds % 3600) // 60
                        gecenSaniye = gecenSure.seconds % 60
                        
                        #Doğumdan bugüne geçen gün, saat, sakika ve saniye cinsinden ekrana yazdırılması
                        print(f"\n{gecenSure.days} gün, {gecenSaat} saat, {gecenDakika} dakika, {gecenSaniye} saniyedir bu dünyadasınız.")
                        #Doğumdan bu güne geçen zamanı gün türünden, saat türünden, dakika türünden, saniye türünden ayrı ayrdı yazdırılması
                        print(f"\nGun: {gecenSure.days} \nSaat: {(gecenSure.days * 24 +  gecenSure.seconds // 3600 )} \nDakika: {gecenSure.days * 1440 + gecenDakika} \nSaniye: {gecenSure.days * 86400 + gecenSure.seconds}\n")
                        kontrol = False
                        break

                    elif dogumSaati == 0:
                        detaylıDogumTarihi = dt.datetime(int(yıl), int(ay), int(gun), 23, 59)#tarih farkını bulabilmek için girilen doğum tarihini datetime türüne çevrilmesi
                        gecenSure2 = bugun - detaylıDogumTarihi #timedelta türünde hesaplar 
                        
                        #timedelta türündeki sonuç days ve seconds verisi döndürür. bunlara göre saat, dakika ve saniyenin hesaplanması
                        gecenSaat = (gecenSure2.days * 24 +  gecenSure2.seconds // 3600 ) % 24
                        gecenDakika = (gecenSure2.seconds % 3600) // 60
                        gecenSaniye = gecenSure2.seconds % 60
                        
                        #Doğumdan bugüne geçen gün, saat, sakika ve saniye cinsinden ekrana yazdırılması
                        #kullanıcı doğum saatini girmediği için doğum saati doğduğu gün 23:59 olarak kabul edilmiş ve ona göre hesaplanmıştır. Böylece net olmasa dahi yaşadığı en az süre hesaplanmış olur.
                        print(f"\n{gecenSure2.days} gün ve en az {gecenSaat} saat, {gecenDakika} dakika, {gecenSaniye} saniyedir bu dünyadasınız.")
                        print("\nDoğum saatinizi girmediğinizden dolayı saat, dakika ve saniye bilgileri kesin değildir. Doğum saatiniz doğduğunuz günün 23:59'u kabul edilerek en az süre hesaplanmıştır.\n")
                        kontrol = False
                        break

                    else:
                        print("Yanlış bir değer girdiniz.")
                        continue
                except ValueError:
                    print("Yanlış bir değer girdiniz. Sadece 0 veya 1 değerlerini girebilrsiniz")      
        else:
            print("Lütfen doğum tarihinizi 01/01/2020 gibi aralarında / olacak şekilde giriniz.")
            continue       
