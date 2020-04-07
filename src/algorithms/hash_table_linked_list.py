class Cell:
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"{self.key}:{self.value}"


class HashTable:
    def __init__(self, size):
        self.size = size
        self.elements = 0
        self.buckets = [Cell(None, None, None) for i in range(self.size)]

    def _hash(self, key, size=None):
        return key % (size or self.size)

    def _find_cell_before(self, key):
        bucket_num = self._hash(key)
        top = self.buckets[bucket_num]

        cell = top
        while cell.next is not None:
            if cell.next.key == key:
                return cell
            cell = cell.next

        return None

    def get(self, key):
        cell_before = self._find_cell_before(key)

        if cell_before is None:
            return None

        return cell_before.next

    def insert(self, key, value):
        if self.get(key) is not None:
            raise ValueError("Ключ {key} уже находится в хэш-таблице.".format(key=key))

        bucket_num = self._hash(key)
        linked_list = self.buckets[bucket_num]

        new_cell = Cell(key, value, linked_list.next)
        linked_list.next = new_cell

        self.elements += 1

    def delete(self, key):
        cell_before = self._find_cell_before(key)

        if cell_before is None:
            raise ValueError(f"Ключа {key} нет в хэш-таблице.")

        cell_before.next = cell_before.next.next

        self.elements -= 1
        return None

    def __str__(self):
        text = ""
        for _, cell in enumerate(self.buckets):
            text += f"{_}->"
            cell = cell.next
            cells = []
            while cell is not None:
                cells.append(f"{cell}")
                cell = cell.next
            text += "[{}] ".format(";".join(cells))
        return text.strip()

    def change_size(self, new_size):
        old_buckets = self.buckets

        self.size = new_size
        self.buckets = [Cell(None, None, None) for i in range(new_size)]

        for c in old_buckets:
            self.re_insert_cell(c.next)

    def re_insert_cell(self, cell):
        if cell is None:
            return

        self.insert(cell.key, cell.value)
        self.re_insert_cell(cell.next)
