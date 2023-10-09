from models.__init__ import CURSOR, CONN
from models.club import Club

class Student:

    all = {}

    def __init__(self, name, club_id, id=None):
        self.id = id
        self.name = name
        self.club_id = club_id

    def __repr__(self):
        return f'<Student {self.id}: {self.name}, Club ID: {self.club_id}>'
    
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
        if isinstance(club_id, int):
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

    @classmethod
    def drop_table(cls):
        sql = 'DROP TABLE IF EXISTS students;'
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = 'INSERT INTO students (name, club_id) VALUES (?, ?)'
        CURSOR.execute(sql, (self.name, self.club_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Student.all[self.id] = self
    
    def update(self):
        club = Club.find_by_id(self.club_id)
        if club.student_count() < club.capacity:
            sql = 'UPDATE students SET name = ?, club_id = ? WHERE id = ?'
            CURSOR.execute(sql, (self.name, self.club_id, self.id))
            CONN.commit()
        else:
            self = Student.find_by_id(self.id)
            raise ValueError('Club is already at capacity')
    
    def delete(self):
        sql = 'DELETE FROM students WHERE id = ?'
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del Student.all[self.id]

        self.id = None
    
    @classmethod
    def create(cls, name, club_id):
        club = Club.find_by_id(club_id)
        if club.student_count() < club.capacity:
            student = cls(name, club_id)
            student.save()
            return student    
        else:
            raise ValueError('Club is already at capacity')

        

    @classmethod
    def instance_from_db(cls, row):
        student = cls.all.get(row[0])
        if student:
            student.name = row[1]
            student.club_id = row[2]
        else:
            student = cls(row[1], row[2])
            student.id = row[0]
            cls.all[student.id] = student
        return student

    @classmethod
    def get_all(cls):
        sql = 'SELECT * FROM students'

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = 'SELECT * FROM students WHERE id = ?'
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = 'SELECT * FROM students WHERE name is ?'
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None