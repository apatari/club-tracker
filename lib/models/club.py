from models.__init__ import CURSOR, CONN

class Club:
    all = {}

    def __init__(self, name, capacity, id=None):
        self.id = id
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f'<Club {self.id}: {self.name}, capacity = {self.capacity}>'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError('Name must be a string that is not empty')
        
    @property 
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if isinstance(capacity, int) and capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError('Capacity must be an integer greater than zero')
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS clubs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            capacity INTEGER
            )"""
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = 'DROP TABLE IF EXISTS clubs;'
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = 'INSERT INTO clubs (name, capacity) VALUES (?, ?)'
        CURSOR.execute(sql, (self.name, self.capacity))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Club.all[self.id] = self

    @classmethod
    def create(cls, name, capacity):
        club = cls(name, capacity)
        club.save()
        return club
    
    def update(self):
        sql = 'UPDATE clubs SET name = ?, capacity = ? WHERE id = ?'
        CURSOR.execute(sql, (self.name, self.capacity, self.id))
        CONN.commit()

    def delete(self):
        sql = 'DELETE FROM clubs WHERE id = ?'
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del Club.all[self.id]

        self.id = None