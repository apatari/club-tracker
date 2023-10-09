from models.__init__ import CONN, CURSOR
from models.club import Club
from models.student import Student

Club.drop_table()
Club.create_table()

Student.drop_table()
Student.create_table()

Club.create(name='skiing', capacity=3)
Club.create(name='ultimate', capacity=4)
Club.create(name='checkers', capacity=10)

Student.create(name="Joe", club_id = 1)
Student.create(name="Bill", club_id = 1)
Student.create(name="Rod", club_id = 2)
Student.create(name="Jill", club_id = 1)

print('Seeding complete')