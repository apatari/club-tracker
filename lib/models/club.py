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
    