from task3 import hash_table
from string import punctuation
import time

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
    for word in words_list[:50]:
        if word not in word_hash_table:
            word_hash_table[word] = 0
        word_hash_table[word] += 1
    t2 = time.time()
    print(t2-t1)
        
if __name__ == "__main__":
    main()