from random import choice

class MP3calar():
    def __init__(self,sarkiListesi = []):
        self.suancalansarki = ""
        self.ses = 100
        self.sarkiListesi = sarkiListesi
        self.durum = True


    def sarkisec(self):
        sayac = 1
        for sarki in self.sarkiListesi:
            print("{}){}".format(sayac, sarki))
            sayac += 1

        secileceksarki = int(input("Secmek istediginiz sarkiyi secin: "))

        while secileceksarki < 1 or silineceksarki > len(self.sarkiListesi):
            secileceksarki = int(
                input("Secmek istediginiz sarkinin numarasini dogru girin(1-{}): ".format(self.sarkiListesi)))

            self.suancalansarki = self.sarkiListesi[secileceksarki-1]


    def sesazalt(self):
        if self.ses == 100:
            pass
        else:
            self.ses += 10

    def sesarttir(self):
        if self.ses == 0:
            pass
        else:
            self.ses -= 10

    def rasgelesarkisec(self):
        randomsarki = choice(self.sarkiListesi)
        self.suancalansarki = randomsarki

    def sarkiekle(self):
        sarkiadi = input("Sarkinin adini girin: ")
        sanatci = input("Sanatcinin adini girin: ")

        self.sarkiListesi.append(sarkiadi + " " + sanatci)

    def sarkisil(self):
        sayac = 1
        for sarki in self.sarkiListesi:
            print("{}){}".format(sayac,sarki))
            sayac += 1
        silineceksarki = int(input("Silmek istediginiz sarkiyi secin: "))
        while silineceksarki < 1 or silineceksarki > len(self.sarkiListesi):
            silineceksarki = int(
                input("Silmek istediginiz sarkinin numarasini dogru girin(1-{}): ".format(self.sarkiListesi)))
        self.sarkiListesi.pop(silineceksarki-1)

    def kapat(self):
        self.durum = False

    def menugöster(self):
        print("
Sarki Listesi: {}
Suan calan sarkinin adi: {}
Ses düzeyi: {}

1)Sarki Sec
2)Sesi Azalt
3)Sesi Arttir
4)Rastgele Sarki
5)Sarki Ekle
6)Sarki Sil
7)MP3 Calari Kapat
              ".format(self.sarkiListesi,self.suancalansarki,self.ses))

    def secim(self):
        sec = int(input("Ne yapmak istiyorsunuz: "))
        while sec < 1 or sec > 7:
                sec = int(input("Girdiginiz deger 1-7 arasinda olmalidir: "))

        return sec

    def calistir(self):
        self.menugöster()
        secim = self.secim

        if self.secim == 1:
            self.sarkisec()
        elif self.secim == 2:
            self.sesazalt()
        elif self.secim == 3:
            self.sesarttir()
        elif self.secim == 4:
            self.rasgelesarkisec()
        elif self.secim == 5:
            self.sarkiekle()
        elif self.secim == 6:
            self.sarkisil()
        elif self.secim == 7:
            self.kapat()

mp3calar = MP3calar()
while mp3calar.durum:
    mp3calar.calistir()

print("Program Sonlandi")
