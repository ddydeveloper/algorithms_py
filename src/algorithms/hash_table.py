# Hash table implementation based on double hashing
class HashTable:
    def __init__(self, size):
        self._buckets = [None * size]
        self._items_count = 0
        self._size = size
        self._prime_number = 7

    def insert(self, key, value):
        # check capacity
        # check item already exists
        # count hash
        # check key for collision
        # insert value by key
        pass

    def delete(self, key):
        # count hash
        # check has_key
        # remove item
        # todo: probably re-hash collision items in order to fill first step item
        pass

    def has_key(self, key):
        # count hash
        # look for key in loop
        pass

    def get(self, key):
        # count hash
        # looks for value in loop
        pass

    def __count_hash(self, key, step):
        (self.__init_hash(key) + step * self.__double_hash(key)) % self._size

    def __init_hash(self, key):
        return key % self._size

    def __double_hash(self, key):
        return self._prime_number - (key % self._prime_number)
