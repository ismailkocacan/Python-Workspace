# taban sınıf
class Hayvan(object):
    hayvan_adi = ""
    def __init__(self,hayvan_adi):
        self.hayvan_adi = hayvan_adi

    def konus(self):
      raise NotImplementedError("Bu methodu bir alt sınıfta implement ederek çağırabilisin !")

