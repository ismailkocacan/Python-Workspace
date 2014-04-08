from inek import Inek
from beygir import Beygir
from esek import Esek


class HayvanFactory:
    def get_list(self):
      hayvan_list = [Esek("Karakaçan"),Beygir("Düldül"),(Inek("Sarıkız"))]
      return hayvan_list