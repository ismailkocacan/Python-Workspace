__author__ = 'ismail'


class Kisi():
    def selam_ver(self):
      return "Selam"

    @classmethod
    def selam_al(self):
      return "Aleykümselam"



kisi = Kisi()

print(kisi.selam_ver())

print(Kisi.selam_al())

