from unittest import TestCase
from kisi_service import KisiService
from kisi import  Kisi

class TestKisiService(TestCase):
    def test_insert_kisi(self):
      kisi = Kisi("ismail","Kocacan")
      kisi_service = KisiService()
      kisi_service.insert(kisi)


    def test_select_kisi_list(self):
      kisi_service = KisiService()
      kisi_list = kisi_service.get_all_kisi()
      for kisi in kisi_list:
          print("kisi.id => "+str(kisi[0]))
          print("kisi.adi => "+kisi[1])
          print("kisi.soyadi => "+kisi[2])
