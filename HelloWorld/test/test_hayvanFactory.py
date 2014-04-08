__author__ = 'ismail kocacan'

from unittest import TestCase
from hayvanfactory import HayvanFactory
from hayvan import Hayvan
from esek import Esek

class TestHayvanFactory(TestCase):

    def test_konus_invoke(self):
       factory = HayvanFactory()
       hayvan_list= factory.get_list()
       for hayvan in hayvan_list:
            print(hayvan.hayvan_adi+" => "+hayvan.konus())


    def test_call_hayvan_class_abstract_method(self):
        #abstract error !
        hayvan = Hayvan("Köpek")
        print(hayvan.konus())

    def test_create_esek(self):
        hayvan = Esek("Karakaçan")
        print(hayvan.hayvan_adi+" => "+hayvan.konus())