from unittest import TestCase
from database import Database

class TestDatabase(TestCase):
    def test_create_kisi_table(self):
     db = Database()
     db.instance.execute("create table kisi(id integer primary key,adi text,soyadi text)")
     db.instance.commit()
