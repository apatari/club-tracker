#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.club import Club

c1 = Club('chess', 4)
Club.create_table()


ipdb.set_trace()
