class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        size = self.size
        return "\U0001F36A" * size

    def deposit(self, n):
        capacity = self.capacity
        size = self.size
        if size + n > capacity:
            raise ValueError
        self.size = size + n

    def withdraw(self, n):
        size = self.size
        if size - n < 0:
            raise ValueError
        self.size = size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Negative Capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        self._size = size
