from task3 import hash_table
from string import punctuation
import time
import pickle
import csv
# with open(filename, ‘wb’) as f:
#     pickle.dump(your_content, f)

def import_text(filename):
    text_file = open(filename)
    text_string = ""
    for line in text_file:
        text_string += " " + line.strip()
    text_string = text_string.translate(str.maketrans("".join(punctuation[:].split("'")), " "*(len(punctuation)-1))).lower()

    text_file.close()
    return text_string.split()

def main():
    words_list = import_text('text.txt')
    word_hash_table = hash_table(399989)

    t1 = time.time()
    for word in words_list:
        if word not in word_hash_table:
            word_hash_table[word] = 0
        word_hash_table[word] += 1
    
    # with open('words-hash-table.pickle', 'wb') as f:
    #     pickle.dump(word_hash_table, f)
    t2 = time.time()
    print(t2-t1)

    with open('words_frequency_list.csv', mode='w') as frequency_file:
        frequency_writer = csv.writer(frequency_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range(word_hash_table.table_size):
            cur_word = word_hash_table.array[i]
            if cur_word is not None:
                frequency_writer.writerow([cur_word.key, cur_word.value])
        
if __name__ == "__main__":
    main()