class Kütüphane:
    def __init__(self):
        self.dosya = open("books.txt", "a+")

    def __del__(self):
        self.dosya.close()

    def KitaplarıListele(self):
        kitaplar = self.dosyadan_kitapları_al()
        for kitap in kitaplar:
            self.kitap_bilgilerini_yazdir(kitap)

    def KitapEkle(self):
        kitap_bilgisi = self.kitap_bilgisi_gir()
        self.kitap_bilgisini_kaydet(kitap_bilgisi)
        print("Kitap başarıyla eklendi.")

    def KitapSil(self):
        silinecek_kitap_adı = input("Silmek istediğiniz kitabın adını girin: ")
        self.kitabi_sil(silinecek_kitap_adı)

    def dosyadan_kitapları_al(self):
        self.dosya.seek(0)
        return self.dosya.readlines()

    def kitap_bilgisi_gir(self):
        kitap_adı = self.giris_kontrol("Kitap Adı: ")
        yazar = self.giris_kontrol("Yazar: ")
        yayın_yılı = self.sayi_kontrol("Yayın Yılı: ")
        sayfa_sayısı = self.sayi_kontrol("Sayfa Sayısı: ")
        return f"{kitap_adı},{yazar},{yayın_yılı},{sayfa_sayısı}\n"

    def kitap_bilgisini_kaydet(self, kitap_bilgisi):
        self.dosya.write(kitap_bilgisi)

    def kitap_bilgilerini_yazdir(self, kitap):
        bilgiler = kitap.strip().split(',')
        print("Kitap Adı: {}, Yazar: {}, Yayın Yılı: {}, Sayfa Sayısı: {}".format(bilgiler[0], bilgiler[1], bilgiler[2], bilgiler[3]))

    def kitabi_sil(self, silinecek_kitap_adı):
        kitaplar = self.dosyadan_kitapları_al()
        self.dosya.seek(0)
        self.dosya.truncate()
        silindi = False
        for kitap in kitaplar:
            if not kitap.startswith(silinecek_kitap_adı):
                self.dosya.write(kitap)
            else:
                silindi = True
        if silindi:
            print(f"{silinecek_kitap_adı} adlı kitap başarıyla silindi.")
        else:
            print(f"{silinecek_kitap_adı} adlı kitap bulunamadı.")

    def giris_kontrol(self, mesaj):
        while True:
            deger = input(mesaj)
            if deger.strip():
                return deger
            else:
                print("Boş giriş! Lütfen tekrar deneyin.")

    def sayi_kontrol(self, mesaj):
        while True:
            deger = input(mesaj)
            if deger.strip().isdigit():
                return deger
            else:
                print("Geçersiz giriş! Sayısal bir değer girin.")

lib = Kütüphane()

while True:
    print("\n*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil")
    secim = input("Lütfen bir işlem seçin (Çıkmak için '4'e basın): ")

    if secim == '1':
        lib.KitaplarıListele()
    elif secim == '2':
        lib.KitapEkle()
    elif secim == '3':
        lib.KitapSil()
    elif secim.lower() == '4':
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")