def print_menu():
    print('\nMenu')
    print('1. append')
    print('2. sort')
    print('3. print')
    print('4. quit')
    print('5. clear')
    print('6. reverse')
    print('7. pop')
    print('8. insert')

my_list = []
quit = False
input_line = None

while not quit:
    print_menu()

    command = int(input("\nEnter command: "))

    if command == 1:
        item = input("Item: ")
        my_list.append(item)
    elif command == 2:
        my_list.sort()
    elif command == 3:
        print(my_list)
    elif command == 4:
        quit = True
    elif command == 5:
        my_list = []
    elif command == 6:
        my_list.reverse()
    elif command == 7:
        print(my_list.pop())
    elif command == 8:
        item = input("Item: ")
        pos = int(input("Index: "))
        my_list.insert(pos, item)