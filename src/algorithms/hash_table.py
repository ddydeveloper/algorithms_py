from random import randint


# Structure to keep hash key value pair
class HashItem:
    def __init__(self, key=None, value=None):
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
        self._buckets = [HashItem(None, None) for _ in range(size)]

        self._items_count = 0
        self._prime_number = 7

    def walk_through(self, action):
        for item_idx, current_hash_item in enumerate(self._buckets):
            action(item_idx, current_hash_item)

    def insert(self, key, value):
        if self._items_count > 0 and self._items_count / self._size > 0.7:
            self.__resize(self._size * 2)

        item_idx, duplicate_key = self.__get_free_idx(key)

        if item_idx == -1:
            raise ValueError(f"Key {key} can't be added to a hash table")

        if duplicate_key:
            raise ValueError(f"Key {key} already exists in a hash table")

        self._buckets[item_idx] = HashItem(key, value)
        self._items_count += 1

    def delete(self, key):
        item_idx, hash_item_value = self.__get_hash_item(key)

        if item_idx == -1:
            return

        self._buckets[item_idx].key = None
        self._buckets[item_idx].value = None

    def key_exists(self, key):
        item_idx, hash_item_value = self.__get_hash_item(key)
        return item_idx != -1

    def value(self, key):
        item_idx, hash_item_value = self.__get_hash_item(key)
        return hash_item_value

    def __resize(self, size):
        self._size = size
        self.__rehash()

    def __rehash(self):
        buckets = self._buckets

        self._buckets = [HashItem(None, None) for i in range(self._size)]
        self._items_count = 0

        for bucket in buckets:
            if bucket.key is None:
                continue

            self.insert(bucket.key, bucket.value)

    def __get_hash_item(self, key):
        step = 1

        while self._size >= step:
            item_idx = self.__get_hash(key, step)
            current_hash_item = self._buckets[item_idx]

            if not current_hash_item.is_empty():
                return item_idx, current_hash_item.value

            step += 1

        return -1, None

    def __get_free_idx(self, key):
        step = 1
        duplicate_key = False

        while self._size >= step:
            item_idx = self.__get_hash(key, step)
            current_hash_item = self._buckets[item_idx]

            if current_hash_item.is_empty():
                return item_idx, duplicate_key
            else:
                duplicate_key = current_hash_item.key == key

            step += 1

        return -1, duplicate_key

    def __get_hash(self, key, step):
        return (self.__get_init_hash(key) + step * self.__get_double_hash(key)) % self._size

    def __get_init_hash(self, key):
        return key % self._size

    def __get_double_hash(self, key):
        return self._prime_number - (key % self._prime_number)


hash_table = HashTable(11)

keys = []

for i in range(1, 200000):
    rand_key = randint(1000, 500000)

    if rand_key in keys:
        continue

    keys.append(rand_key)
    hash_table.insert(rand_key, f"item {rand_key}")


def print_item(hash_idx, hash_item):
    print(f"{hash_idx} - {str(hash_item)}")


hash_table.walk_through(print_item)
