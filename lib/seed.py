from models.__init__ import CONN, CURSOR
from models.club import Club

Club.drop_table()
Club.create_table()

print('Seeding complete')