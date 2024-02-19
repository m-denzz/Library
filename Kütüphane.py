class Kütüphane:
    def __init__(self):
        self.dosya = open("books.txt", "a+")

    def __del__(self):
        self.dosya.close()

    def KitaplarıListele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        for kitap in kitaplar:
            bilgiler = kitap.strip().split(',')
            print("Kitap Adı: {}, Yazar: {}, Yayın Yılı: {}, Sayfa Sayısı: {}".format(bilgiler[0], bilgiler[1], bilgiler[2], bilgiler[3]))

    def KitapEkle(self):
        kitap_adı = self.giris_kontrol("Kitap Adı: ")
        yazar = self.giris_kontrol("Yazar: ")
        yayın_yılı = self.sayi_kontrol("Yayın Yılı: ")
        sayfa_sayısı = self.sayi_kontrol("Sayfa Sayısı: ")
        kitap_bilgisi = f"{kitap_adı},{yazar},{yayın_yılı},{sayfa_sayısı}\n"
        self.dosya.write(kitap_bilgisi)
        print("Kitap başarıyla eklendi.")

    def KitapSil(self):
        silinecek_kitap_adı = input("Silmek istediğiniz kitabın adını girin: ")
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
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
                print("Geçersiz giriş! Lütfen tekrar deneyin.")

    def sayi_kontrol(self, mesaj):
        while True:
            deger = input(mesaj)
            if deger.strip().isdigit():
                return deger
            else:
                print("Geçersiz giriş! Lütfen sayısal bir değer girin.")

lib = Kütüphane()

while True:
    print("\n--- MENÜ ---")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil")
    secim = input("Lütfen Geçerli bir işlem seçin!(Çıkmak için '4'e basın.): ")

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
