"""
Ref: http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/
"""


class Hashtable:
    def __init__(self, size):
        self.table_size = size
        self.table = [[] for _ in range(self.table_size)]

    def hashing(self, key):
        return hash(key) % self.table_size

    def set(self, key, value):
        bucket = self.table[self.hashing(key)]
        found = False
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                found = True
                break
        if found:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def get(self, key):
        bucket = self.table[self.hashing(key)]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def remove(self, key):
        bucket = self.table[self.hashing(key)]
        found = False
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                found = True
                break
        if found:
            del bucket[i]
        return found


table = Hashtable(10)

for i in range(20):
    table.set(i, i)

print(table.table)