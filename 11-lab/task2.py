""" Task 2
    
    Modified task 1 to track number of collisions, load, and the 
    average probe length.
"""
from referential_array import build_array

class kv_pair:
    def __init__(self,key,value,collisions=0):
        """ Key-value pair constructor
        Args:
            key (any): key
            value (any): value
            collisions (int): collisions for this pair during hashing        
        Returns:
            None
        Raises:
            No exceptions
        Precondition:
            Key and value cannot be None
        Postcondition:
            Creates a key-value pair instance and tracks collisions
        """
        self.key = key
        self.value = value
        self.collisions = collisions

    def __str__(self):
        """ Generates string representation of key-value pair class
        Args:
            None
        Returns:
            (str) string representing the key-value pair
        Raises:
            No exceptions
        Precondition:
            Key and value can be represented as a string
        Postcondition:
            Returns a string representation of the pair
        """
        return "("+str(self.key)+","+str(self.value)+")"

class hash_table:
    def __init__(self,table_size=31):
        """ Hash table constructor
        Args:
            table_size (int): maximum size of the table
        Returns:
            None
        Raises:
            No exceptions
        Precondition:
            table_size > 0
        Postcondition:
            Creates a hash table instance that tracks collisions
                and average probe length
        """
        self.array = build_array(table_size)
        self.table_size = table_size
        self.count = 0
        self.collisions = 0
        self.avg_probe_length = 0
        self.load = 0

    def __str__(self):
        """ Generates string representation of this hash table
        Args:
            None
        Returns:
            (str) string representing the hash table
        Raises:
            No exceptions
        Precondition:
            None
        Postcondition:
            Returns a string representation of the hash table
        """
        string = ""
        for index in range(self.table_size):
            if self.array[index] is None:
                pass
            else:
                string += str((index,str(self.array[index])))
                string += ","
        return string

    def __setitem__(self, key, value):
        """ Places a key-value pair onto the hash table
        Args:
            key (any): key to be added to the table
            value (any): valuea associcated with key
        Returns:
            None
        Raises:
            No exceptions
        Precondition:
            Table is not full
        Postcondition:
            self.array[i] = (key, value)
        """
        candidate_place, collisions = self.linear_probe(key)
        if self.array[candidate_place] is None:
            self.count += 1
        self.array[candidate_place]=kv_pair(key,value,collisions)
        self.calc_stats(collisions)

    def calc_stats(self, collisions):
        """ Re-calculates the hash table's stats
        Args:
            collisions (int): number of collisions from latest
                key-value pair addition
        Returns:
            None
        Raises:
            None
        Precondition:
            Must only be called by __setitem__ method
        Postcondition:
            Updates the total number of collisions, avg probe length,
                and load
        """
        # collisions = [self.array[i].collisions for i in range(self.table_size) if self.array[i] is not None]
        self.collisions += collisions
        self.avg_probe_length = self.collisions/self.count
        self.load = self.count/self.table_size

    def __getitem__(self, key):
        """ Gets the value corresponding to a key from the table
        Args:
            key (any): key sought fromt the table
        Returns:
            value (any): value associcated with key
        Raises:
            KeyError: if key is not in hash table
        Precondition:
            Key must exist in hash table
        Postcondition:
            Returns the value corresponding to key
        """
        candidate_place, _ = self.linear_probe(key)
        if self.array[candidate_place] is None:
            raise KeyError(str(key)+" not found")
        return self.array[candidate_place].value

    def __contains__(self, key):
        """ Checks if key is in the hash table
        Args:
            key (any): key to be checked
        Returns:
            (bool): True if key is in table
                    False otherwise
        Raises:
            None
        Precondition:
            None
        Postcondition:
            Returns a boolean corresponding to whether key is found or not
        """
        for i in range(self.table_size):
            if self.array[i] is not None and self.array[i].key == key:
                return True
        return False

    def __len__(self):
        """ Gets the number of key-value pairs currently in the table
        Args:
            None
        Returns:
            (int): number of key-value pairs in the table
        Raises:
            None
        Precondition:
            None
        Postcondition:
            Returns the number of items in the table
        """
        return self.count

    def hash_value(self, key):
        """ Gets the hash value of a given key
        Args:
            key (any): key to be hashed
        Returns:
            result (int): hash value of key
        Raises:
            None
        Precondition:
            key must be hashable
        Postcondition:
            Returns the hash value of the given key
        """
        prime_mult = 101
        result = 0
        for character in key:
            result = (result * prime_mult + ord(character)) % self.table_size
        return result

    def linear_probe(self, key, sneakykey=None):
        """ Linear probing implementation
        Args:
            key (any): key 
            sneakykey (int): predetermined hash value
        Returns:
            pos (int): index where key-value pair is to be placed
                or located in the array
            i (int): number of collisions occurring during probing
        Raises:
            None
        Precondition:
            None
        Postcondition:
            Returns the position where key-value pair is to be
                placed/located and the number of collisions before
                this position is determined
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
        return pos, i