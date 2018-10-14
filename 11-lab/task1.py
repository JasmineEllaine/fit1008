from referential_array import build_array

class kv_pair:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return "("+str(self.key)+","+str(self.value)+")"

class hash_table:
    def __init__(self,table_size=31):
        self.array = build_array(table_size)
        self.table_size = table_size
        self.count = 0

    def __str__(self):
        string = ""
        for index in range(self.table_size):
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
        return self.array[candidate_place].value

    def __contains__(self, key):
        candidate_place = self.linear_probe(key)
        return self.array[candidate_place].key == key

    def __len__(self):
        return self.count

    def hash_value(self, key):
        prime_mult = 101
        result = 0
        for character in key:
            result = (result * prime_mult + ord(character)) % self.table_size
        return result

    def linear_probe(self, key, sneakykey=None):
        """
        :param self:
        :param key: the key to place something using
        :return: the location in the table for it to go or where it lives if there
        :raise: index error where not possible
        """
        if not sneakykey is None:
            hashv = sneakykey
        else:
            hashv = self.hash_value(key)  # first try
        pos = hashv
        scannedTable = False
        i = 0
        while not (self.array[pos] is None or self.array[pos].key == key or scannedTable):
            pos = (pos +1)%self.table_size
            i += 1
            if i == self.table_size + 1:
                scannedTable = True
        return pos