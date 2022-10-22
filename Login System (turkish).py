import json
from random import randint


class Sistem():
    def __init__(self):
        self.durum = True
        self.denemehak = 0
        self.kullaniciadi = ""
        self.sifre = ""
        self.sifrekontrol = ""
        self.email = ""
        self.secim = ""
        self.veriler = {"kullanicilar": []}
        self.kod = ""
        self.aktivasyonkod = ""
        self.kayitsecim = ""
        self.sormail = ""
        self.mailvarmiyokmu = ""
        self.hesapisteme = ""
        self.buldumkullanici = ""
        self.buldumsifre = ""
        print("----- Kadir Ihsan Forum'a Hosgeldiniz! -----")

    def girisyap(self):
        self.kullaniciadi = input("Kullanici adinizi gitin: ")
        self.sifre = input("Sifrenizi girin: ")
        return self.kontrolet(self.kullaniciadi, self.kullaniciadi)

    def kayitol(self):
        self.kullaniciadi = input("Lütfen kendinize bir Kullanici Adi belirleyin: ")
        self.email = input("E-Mail adresinizi girin: ")
        self.sifre = input("Sifrenizi girin: ")
        self.sifrekontrol = input("Sifrenizi tekrar giriniz: ")
        if self.kullaniciadi and self.sifre in self.veriler["kullanicilar"]:
            while True:
                try:
                    self.kayitsecim = int(input(
                        "Böyle bir hesap zaten var, giris yapmak icin 1'e, tekrar ana menüye dönmek icin 2'ye, cikmak icin 3'e basin"))
                    if self.kayitsecim == 1:
                        return self.girisyap()
                    if self.kayitsecim == 2:
                        return self.menugöster()
                    if self.kayitsecim == 3:
                        return self.cikis()
                    break
                except:
                    print("Dogru bir deger girin (1-3): ")
        if self.sifre != self.sifrekontrol:
            print("Sifreniz uyusmuyor, tekrar deneyin!")
            return self.kayitol()
        return self.aktivasyonkoduGönder()

    def sifremiunuttum(self):
        while True:
            try:
                self.mailvarmiyokmu = int(input("Mail adresinizi hatirliyorsaniz 1'e hatirlamiyorsaniz 2'e basin: "))
                break
            except:
                print("Lütfen 1 ile 2 arasinda bir secim yapin!")
        if self.mailvarmiyokmu == 1:
            self.sormail = input("Mail adresinizi buraya girin: ")
            with open("veriler.json","r") as dosya:
                self.veriler = json.load(dosya)
                for kullanici in self.veriler["kullanicilar"]:
                    if kullanici["E-Mail"] == self.sormail:
                        self.buldumkullanici = kullanici["Kullanici adi"]
                        self.buldumsifre = kullanici["Sifre"]
                        self.aktivasyonkod = str(randint(1000, 9999))
                        with open("Aktivasyon_Kodu.txt", "w") as dosya:
                            dosya.write(self.aktivasyonkod)
                        print(
                            "Programin oldugu klasöre bir Aktivasyon Kodu gönderildi, dogrulama icin kodunuzu asagiya girin!")
                        self.kod = str(input("Kodu buraya girin: "))
                        if self.aktivasyonkod == self.kod:
                            print("Kod dogru, kullanici adiniz ve sifreniz:")
                            print("Kullanici adiniz: {}".format(self.buldumkullanici))
                            print("Sifreniz: {}".format(self.buldumsifre))
                        if self.aktivasyonkod != self.kod:
                            print("Kodlar eslesmiyor, tekrar deneyin!")
                            return self.sifremiunuttum()
                    elif kullanici["E-Mail"] != self.sormail:
                        print("Sistemde böyle bir Mail bulunamadi!")
                        self.menugöster()

        elif self.mailvarmiyokmu == 2:
            print("Bu durumda birsey yapamayiz, lütfen yeni bir hesap olursturun!")
            while True:
                try:
                    self.hesapisteme = int(input(
                        "Isterseniz 1'e basarak yeni bir hesap olusturabilirsiniz, yada 2'e basarak sistemden "
                        "cikabilirsiniz!"))
                    break
                except:
                    print("Lütfen 1 ile 2 arasinda bir secim yapin!")
            if self.hesapisteme == 1:
                self.kayitol()
            if self.hesapisteme == 2:
                self.cikis()

    def cikis(self):
        durum = False

    def menugöster(self):
        print("Ne yapmak istiyorsunuz?\n1)Giris Yap\n2)Kayit Ol\n3)Sifremi Unuttum\n4)Cikis")
        return self.secimyapmak()

    def kontrolet(self, kullaniciadi, sifre):
        if kullaniciadi and sifre in self.veriler:
            print("Sitemize tekrardan hosgeldiniz!")
        else:
            print("Kullanici adi veya sifre yanlis, tekrar deneyin!")
            self.denemehak += 1
            if self.denemehak >= 3:
                print("Cok fazla deneme hakki yaptiniz, lütfen daha sonra tekrar deneyin!")
                return self.cikis
            return self.girisyap()

    def calistir(self):
        pass

    def kayitvarmi(self):
        pass

    def aktivasyonkoduGönder(self):
        self.aktivasyonkod = str(randint(1000, 9999))
        with open("Aktivasyon_Kodu.txt", "w") as dosya:
            dosya.write(self.aktivasyonkod)
        print("Programin oldugu klasöre bir Aktivasyon Kodu gönderildi, dogrulama icin kodunuzu asagiya girin!")
        self.kod = str(input("Kodu buraya girin: "))
        return self.aktivasyonkoduKontrol()

    def aktivasyonkoduAl(self):
        pass

    def aktivasyonkoduKontrol(self):
        if self.aktivasyonkod == self.kod:
            print("Kod dogru, hesabiniz basariyla olusturuldu")
            self.veriler["kullanicilar"].append(
                {"Kullanici adi": self.kullaniciadi, "Sifre": self.sifre, "E-Mail": self.email})
            with open("veriler.json", "w") as dosya:
                json.dump(self.veriler, dosya)
        if self.aktivasyonkod != self.kod:
            print("Kodlar eslesmiyor, tekrar deneyin!")
            return self.aktivasyonkoduGönder()

    def fazladenemeVarmi(self):
        pass

    def cikis(self):
        self.durum = False

    def secimyapmak(self):
        while True:
            try:
                self.secim = int(input("Secim yapiniz: "))
                break
            except:
                print("\nLütfen dogru dogru bir secim yapin (1-4): ")


sistem = Sistem()

while sistem.durum:
    sistem.calistir()
    sistem.menugöster()
    if sistem.secim == 1:
        sistem.girisyap()
    if sistem.secim == 2:
        sistem.kayitol()
    if sistem.secim == 3:
        sistem.sifremiunuttum()
    if sistem.secim == 4:
        print("Siteden cikis yaptiniz!")
        sistem.cikis()
