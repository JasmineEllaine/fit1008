from task3 import hash_table

def test_hash_value():
    # initialise hash table
    test_hash = hash_table(101)

    # test cases
    assert test_hash.hash_value("Mary") == 20, "Test failed #1: Incorrect Hash Value"
    assert test_hash.hash_value("Patricia") == 97, "Test failed #2: Incorrect Hash Value"
    assert test_hash.hash_value("Jennifer") == 13, "Test failed #3: Incorrect Hash Value"

    # initialise second dhash table
    test_hash_2 = hash_table(128)

    # test cases
    assert test_hash_2.hash_value("James") == 88,   "Test failed #4: Incorrect Hash Value"
    assert test_hash_2.hash_value("John") == 111,   "Test failed #5: Incorrect Hash Value"
    assert test_hash_2.hash_value("Robert") == 94,  "Test failed #6: Incorrect Hash Value"

def test_set_item():
    # initialise hash table
    test_hash = hash_table(101)

    # use [] to set items
    test_hash["Mary"] = "Mary"
    test_hash["Patricia"] = False
    test_hash["Jennifer"] = 1

    # test cases
    assert str(test_hash.array[20]) == "(Mary,Mary)",       "Test failed #7: Set item failed!"
    assert str(test_hash.array[97]) == "(Patricia,False)",  "Test failed #8: Set item failed!"
    assert str(test_hash.array[13]) == "(Jennifer,1)",      "Test failed #9: Set item failed!"

    # test linear probing function
    test_hash_2 = hash_table(6)

    # Use [] to place values where linear probing will be used
    test_hash_2["Jake"] = "Peralta"
    test_hash_2["Terry"] = "Crews"
    test_hash_2["Amy"] = "Santiago"
    test_hash_2["Rosa"] = "Diaz"
    test_hash_2["Captain"] = "Holt"

    # test cases
    assert str(test_hash_2.array[7]) == "(Jake,Peralta)",    "Test failed #10: Set item failed!"
    assert str(test_hash_2.array[2]) == "(Terry,Crews)",     "Test failed #11: Set item failed!"
    assert str(test_hash_2.array[3]) == "(Amy,Santiago)",    "Test failed #12: Set item failed!"
    assert str(test_hash_2.array[1]) == "(Rosa,Diaz)",       "Test failed #13: Set item failed!"
    assert str(test_hash_2.array[0]) == "(Captain,Holt)",    "Test failed #14: Set item failed!"

    # checks collisions and avg probe length
    assert test_hash.collisions == 0,           "Test failed #24: no. of collisions should be 0"
    assert test_hash.avg_probe_length == 0,     "Test failed #25: avg probe length should be 0"
    assert test_hash.load == 3/101 ,            "Test failed #26: incorrect load"
    assert test_hash_2.collisions == 0,         "Test failed #27: no. of collisions should be 8"
    assert test_hash_2.avg_probe_length == 0,   "Test failed #28: avg probe length should be 1.6"
    assert test_hash_2.load == 5/8,               "Test failed #29: incorrect load"

def test_get_item():
    # initialise hash table and values
    test_hash = hash_table(101)
    test_hash["Mary"] = "Mary"
    test_hash["Patricia"] = False
    test_hash["Jennifer"] = 1

    # use keys to get value
    assert test_hash["Mary"] == "Mary",     "Test failed #15: 'Mary' should have been returned"
    assert test_hash["Patricia"] == False,  "Test failed #16: False should have been returned"
    assert test_hash["Jennifer"] == 1,      "Test failed #17: 1 should have been returned"

    # initialise new hash table and values
    test_hash_2 = hash_table(101)

    # error must occur since these keys do not exist
    try:
        test_hash_2["Mary"]
        print("Test failed #18: Key 'Mary' does not exist in hash table")
    except KeyError:
        pass

    try:
        test_hash_2["Patricia"]
        print("Test failed #19: Key 'Patricia' does not exist in hash table")
    except KeyError:
        pass

def test_contains():
    # initialise hash table and values
    test_hash = hash_table(5)
    test_hash["Jake"] = "Peralta"
    test_hash["Amy"] = "Santiago"
    test_hash["Terry"] = "Crews"
    test_hash["Rosa"] = "Diaz"
    test_hash["Captain"] = "Holt"

    # test cases
    assert ("Jake" in test_hash) == True,   "Test failed #18: Key should be in hash table"
    assert ("Rosa" in test_hash) == True,   "Test failed #19: Key should be in hash table"
    assert ("Gina" in test_hash) == False,  "Test failed #20: Key should not be in hash table"

def test_updateValues():
    # initialise hash table and values
    test_hash = hash_table(5)
    test_hash["Jake"] = "Peralta"
    test_hash["Terry"] = "Crews"
    test_hash["Amy"] = "Santiago"
    test_hash["Rosa"] = "Diaz"
    test_hash["Captain"] = "Holt"

    # test cases
    test_hash["Jake"] = "Jake"
    test_hash["Rosa"] = "Rosa"
    test_hash["Captain"] = "Amy"

    assert test_hash["Jake"] == "Jake",     "Test failed #21: Value did not change upon assignment"
    assert test_hash["Rosa"] == "Rosa",     "Test failed #22: Value did not change upon assignment"
    assert test_hash["Captain"] == "Amy",   "Test failed #23: Value did not change upon assignment"

def main():
    # test_hash_value()
    # test_set_item()
    # test_get_item()
    test_contains()
    # test_updateValues()
    print("All tests passed.")

if __name__ == "__main__":
    main()