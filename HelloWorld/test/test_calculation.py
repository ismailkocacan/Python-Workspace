__author__ = 'ismail'

# testing a calculation class example.

from unittest import TestCase
from calculation import Calculation

class TestCalculation(TestCase):
    def test_topla(self):
        self.assertTrue(Calculation().topla(5,5)==10,"Toplam yanlış !")

    def test_carp(self):
        self.assertTrue(Calculation().carp(5,5)==25,"Çarpım yanlış !")

    def test_bolum(self):
       self.assertTrue(Calculation().bolum(10,2)==4,"Bölüm yanlış !")

    def test_fark(self):
        self.assertTrue(Calculation().fark(10,5)==5,"Fark yanlış !")

    def test_karekok(self):
       self.assertTrue(Calculation().karekok(100)==10,"Karekök yanlış !")