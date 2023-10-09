from models.__init__ import CONN, CURSOR
from models.club import Club

Club.drop_table()
Club.create_table()

Club.create(name='skiing', capacity=5)
Club.create(name='ultimate', capacity=4)
Club.create(name='checkers', capacity=10)

print('Seeding complete')