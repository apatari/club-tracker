from models.__init__ import CURSOR, CONN
from models.club import Club

class Student:

    all = {}

    def __init__(self, name, club_id, id=None):
        self.id = id
        self.name = name
        self.club_id = club_id

    def __repr__(self):
        return f'<Student {self.id}: {self.name}, Club ID: {self.club_id}'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError('Name must be a string and cannot be empty')
    
    @property
    def club_id(self):
        return self._club_id
    
    @club_id.setter
    def club_id(self, club_id):
        if isinstance(club_id, int) and Club.find_by_id(club_id):
            self._club_id = club_id
        else:
            raise ValueError('No matching club id in the database')
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            club_id INTEGER,
            FOREIGN KEY (club_id) REFERENCES clubs(id)
            )"""
        
        CURSOR.execute(sql)
        CONN.commit()

    
    