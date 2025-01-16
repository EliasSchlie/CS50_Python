class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return ("🍪" * self.size)

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        n = int(n)
        if self.size < n:
            raise ValueError("Can't take more cookies than there are in the jar")
        self.size = self.size - n
        
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        capacity = int(capacity)
        if capacity < 0:
            raise ValueError("Can't have negative cookies")
        self._capacity = capacity
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, n):
        if n > self.capacity:
            raise ValueError("Jar is full")
        self._size = n