from models.__init__ import CONN, CURSOR
from models.club import Club
from models.student import Student

Club.drop_table()
Club.create_table()

Student.drop_table()
Student.create_table()

Club.create(name='Skiing', capacity=3)
Club.create(name='Biking', capacity=4)
Club.create(name='Checkers', capacity=8)

Student.create(name="Joe", club_id = 1)
Student.create(name="Bill", club_id = 1)
Student.create(name="Rod", club_id = 2)
Student.create(name="Jill", club_id = 1)

print('Seeding complete')