# sözlük (dictionary ) ve class yapısı kullanarak kütüphane otomasyonu tasarımı

"""
1. kitap ekle 
2. kitap listele
3. kitap ara
4. yönetici ekle 
5. yönetici listele 
6. çıkış 
"""

from symbol import pass_stmt
from time import sleep 
import os
from tkinter import N 

class yonetici :
    yoneticiSozluk = {}

    def yoneticiekleme(self):
        self.yoneticisicil =input ("yonetici sicil no gir :")
        self.yonetiadı = input ("yonetici adı soyadı giriniz :")
        self.yoneticimaas = int(input("yonetici maas giriniz:"))

        self.yoneticiSozluk[self.yoneticisicil]={
            "yoneticiadı":self.yonetiadı,
            "yoneticimaas":self.yoneticimaas
        }

        sleep(1)
        print ("bilgiler başarı ile eklendi")
        sleep(1)
        os.system("cls")

    def yoneticilerilistele (self):
        if (self.yoneticiSozluk== {}):
            print ("yonetici is not found ")
            
        else :
            for yonetici in self.yoneticiSozluk :
                print ("yöneticiler aranıyor ")
                sleep(2)
                print (yonetici,self.yoneticiSozluk[yonetici])
                
                sleep(2)


class myLibrary(yonetici):

    temizle=os.system("cls")
    kitaplar={}

    def __init__(self) :
        while True :
            self.temizle
            print ("library otomasyon ".center(30,"*"))
            print ("""
                    1. kitap ekle 
                    2. kitap listele
                    3. kitap ara
                    4. yönetici ekle 
                    5. yönetici listele 
                    6. çıkış 
                """)

            secim= int(input("işleminizi seçiniz (1-6)"))
            if secim == 1 :
                self.kitapekle()
            elif secim == 2 :
                self.kitaplistele()
            elif secim == 3 :
                self.kitapara()
            elif secim == 4 :
                super().yoneticiekleme()
            elif secim == 5 :
                
                super().yoneticilerilistele()
            elif secim == 6 :
                print ("program sonlandırılıyor.......")
                self.cıkıs()
            
            else :
                print ("hatalı değer girişi")
                continue

            

    def kitapekle(self):
        self.temizle
        tane = int (input ("kaç tane kitap girilecek.:"))

        for adet in range (tane):
            self.kitapID = input ("kitap ID giriniz.:")
            self.kitapadı = input ("kitabın adını giriniz.:")
            self.kitapturu = input ("kitabın türünü giriniz.:")
            self.kitapfiyat = input ("kitabın fiyatını giriniz.:")
            self.kitaplar[self.kitapID] = {
                "kitap_adı" : self.kitapadı ,
                "kitap_turu": self.kitapturu,
                "kitap_fiyat":self.kitapfiyat

            }
            sleep (1)

            print ("bilgiler kaydedildi")


    def kitaplistele(self):
        if self.kitaplar == {} :

            sleep (2)
            print ("library is empty")
        
        
        else :
            for kitap in self.kitaplar :
                print (kitap,self.kitaplar[kitap])

        

    def kitapara(self):
        self.temizle
        self.kitaparama = input ("kitap ID numarasını giriniz.:")

        try :    
            arama = self.kitaplar[self.kitaparama]
            print ("kitaplar listeleniyor ".center(30,"-"))
            print ("""
            
            kitap_adı.......{}
            kitap_türü.......{}
            kitap_fiyat.......{}
            
            """.format(self.kitapadı,self.kitapturu,self.kitapfiyat))
            sleep(2)
            
        except:
            print ("kitap is not foud ")

            sleep(2)

        

    def cıkıs (self):
        exit(0)
        pass 

kutuphane = myLibrary()


         




        