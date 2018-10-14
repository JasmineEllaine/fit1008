import linked_list as link
from referential_array import build_array

class kv_pair:
    def __init__(self,key,value,collisions=0):
        self.key = key
        self.value = value
        self.collisions = collisions

    def __str__(self):
        return "("+str(self.key)+","+str(self.value)+")"

class hash_table:
    def __init__(self,table_size=31):
        self.array = build_array(table_size)
        self.table_size = table_size
        self.count = 0
        self.total_items = 0
        self.collisions = 0
        self.avg_probe_length = 0
        self.load = 0

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
        candidate_place, collisions = self.sep_chain(key)
        if self.array[candidate_place] is None:
            self.count += 1
            self.array[candidate_place] = link.LinkedList(kv_pair(key,value,collisions))
        elif key in self:
            self.array[candidate_place][collisions].value = value
        else:
            self.array[candidate_place].append(kv_pair(key,value,collisions))
        self.calc_stats(collisions)

    def calc_stats(self, collisions):
        # collisions = [self.array[i].collisions for i in range(self.table_size) if self.array[i] is not None]
        self.collisions += collisions
        self.total_items += 1
        self.avg_probe_length = self.collisions/self.total_items
        self.load = self.count/self.table_size

    def __getitem__(self, key):
        candidate_place, i = self.sep_chain(key)
        if self.array[candidate_place] is None:
            raise KeyError(str(key)+" not found")
        return self.array[candidate_place][i].value

    def __contains__(self, key):
        for i in range(self.table_size):
            if self.array[i] is not None:
                for j in range(len(self.array[i])):
                    if self.array[i][j].key == key:
                        return True
        return False

    def __len__(self):
        return self.count

    def hash_value(self, key):
        prime_mult = 101
        result = 0
        for character in key:
            result = (result * prime_mult + ord(character)) % self.table_size
        return result

    def sep_chain(self, key):
        pos = self.hash_value(key)
        collisions = 0
        if (self.array[pos] is not None):
            while not (self.array[pos][collisions] is None or self.array[pos][collisions].key == key):
                collisions += 1
                if collisions == len(self.array[pos]):
                    return pos, collisions
        return pos, collisions