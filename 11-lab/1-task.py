from referential_array import build_array

def hash_value(self , key):
    prime_mult = 101
    result = 0
    for character in key:
        result = (result * prime_mult + ord(character)) % self.table_size
    return result

class kv_pair:
    def __init__(self, key, value):
        self.key = key
        self.value = val

    def __str__(self):
        return "("+str(self.key)+","+str(self.value)+")"

class hash_table:
    def __init__(self, tableSize):
        self.array = build_array(tableSize)
        self.tableSize = tableSize
        self.count = 0

    def __str__(self):
        string = ""
        for index in range(self.tableSize):
            if self.array[index] is None:
                pass
            else:
                string += str((index,str(self.array[index])))
                string += ","
        return string

    def __setitem__(self, key, value):
        candidate_place = self.linear_probe(key)
        if self.array[candidate_place] is None:
            self.count += 1
        self.array[candidate_place]=kv_pair(key,value)

    def __getitem__(self, key):
        candidate_place = self.linear_probe(key)
        if self.array[candidate_place] is None:
            raise KeyError(str(key)+" not found")
        return self.array[candidate_place]

    def __len__(self):
        return self.count

    def hash_value(self,key):
        return date_of_birth_hash(key,self.tableSize)

    def hash2(self,key):
        return self.hash_value(key)*31 % self.tableSize

    def hash3(self,key):
        date = key
        days_from_year = 367 * (date.year - 1)
        days_from_month = 37 * (date.month - 1)
        key = date.day + days_from_month + days_from_year
        return key % self.tableSize

    def double_hashing_probe(self,key):
        initPos = self.hash_value(key)
        if self.array[initPos] is None or self.array[initPos].key = key:
            return initPos
        pos = initPos
        collisions = 1
        offsetHash = self.hash3(key)
        while not (self.array[pos] is None or self.array[pos].key == key):
            pos = (initPos + collisions*offsetHash) % self.tableSize
        return pos

    def linear_probe(self,key,sneakykey = None):
        """

        :param self:
        :param key: the key to place something using
        :return: the location in the table for it to go or where it lives if there
        :raise: index error where not possible
        """
        if self.count == self.tableSize:
            raise IndexError("hash table is full!")
        if not sneakykey is None:
            hashv = sneakykey
        else:
            hashv = self.hash_value(key)  # first try
        pos = hashv
        while not (self.array[pos] is None or self.array[pos].key == key):
            pos = (pos +1)%self.tableSize
        return pos