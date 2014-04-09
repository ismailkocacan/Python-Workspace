import sqlite3


class Database(object):

  def __init__(self):
    self.instance = sqlite3.connect('../store/mydb.sqllite')

  def get_cursor(self):
    return self.instance.cursor()

  def __del__(self):
    self.instance.close()

