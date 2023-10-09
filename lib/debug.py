#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.club import Club
from models.student import Student

c1 = Club.find_by_id(1)
c2 = Club.find_by_id(2)


ipdb.set_trace()
