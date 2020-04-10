# Structure to keep hash key value pair
class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def is_empty(self):
        return self.key is None

    def __str__(self):
        return f"{self.key}:{self.value}"


# Hash table implementation based on double hashing
class HashTable:
    def __init__(self, size):
        self._size = size
        self._buckets = [HashItem(None, None) * self._size]

        self._items_count = 0
        self._prime_number = 7

    def insert(self, key, value):
        if self._items_count / self._size < 0.7:
            self.__resize(self._size * 2)

        hash_item, item_idx = self.get(key)

        if hash_item.key is not None:
            raise ValueError(f"Key {key} is already exists in a hash table")

        item_idx, = self.__get_free_idx(key)

        if item_idx is None:
            raise ValueError(f"Key {key} can't be added to a hash table")

        self._buckets[item_idx] = HashItem(key, value)

    def delete(self, key):
        hash_item, item_idx = self.get(key)

        if hash_item.key is None:
            return

        self._buckets[item_idx].key = None
        self._buckets[item_idx].value = None

    def has_key(self, key):
        return self.get(key).key is not None

    def get(self, key):
        # count hash
        # looks for value in loop
        return HashItem(1, 1), 1

    def __resize(self, size):
        self._size = size
        self.__rehash()

    def __rehash(self):
        buckets = self._buckets

        self._buckets = [HashItem(None, None) * self._size]
        self._items_count = 0

        for bucket in buckets:
            if bucket.key is None:
                continue

            self.insert(bucket.key, bucket.value)

    def __get_free_idx(self, key):
        step = 1

        while self._size > step:
            item_idx = self.__get_hash(key, step)

            if self._buckets[item_idx].is_empty():
                return item_idx, step

            step += 1

        return None, step

    def __get_hash(self, key, step):
        return (self.__get_init_hash(key) + step * self.__get_double_hash(key)) % self._size

    def __get_init_hash(self, key):
        return key % self._size

    def __get_double_hash(self, key):
        return self._prime_number - (key % self._prime_number)
