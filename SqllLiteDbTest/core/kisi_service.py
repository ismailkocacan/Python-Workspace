from database import Database

class KisiService:

  def __init__(self):
    self.db = Database()

  def insert(self,kisi):
    self.db.instance.execute('''insert into kisi(adi,soyadi) values (?,?)''',(kisi.adi,kisi.soyadi))
    self.db.instance.commit()

  def get_all_kisi(self):
    cursor = self.db.get_cursor()
    cursor.execute("select * from kisi")
    kisi_list = cursor.fetchall()
    return kisi_list





