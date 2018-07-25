from decimal_to_binary import decimal_to_binary
from decimal_to_hex import decimal_to_hex

def hex_to_dec(hex_num):
    """
    This function converts hexadecimal numbers to decimal representation
    :param hex_num: a string
    :return: returns the decimal rep as a string
    :raises: no exceptions
    :precondition: no preconditions
    :complexity: O(1)
    """
    return str(int(hex_num, 16))

def binary_to_dec(bin_num):
    """
    This function converts binary numbers to decimal representation
    :param bin_num: a string
    :return: returns the decimal rep as a string
    :raises: no exceptions
    :precondition: no preconditions
    :complexity: O(1)
    """
    return str(int(bin_num, 2))

def print_menu():
    """
    This function prints the menu
    :param: none
    :return: no returns
    :raises: no exceptions
    :precondition: no preconditions
    :complexity: O(1)
    """
    print('\nMenu')
    print('1. Decimal to Hex')
    print('2. Decimal to Binary')
    print('3. Binary to Decimal')
    print('4. Binary to Hex')
    print('5. Hex to Decimal')
    print('6. Hex to Binary')
    print('7. Quit')

quit = False
while not quit:
    print_menu()

    command = int(input("\nEnter command: "))

    if command == 1:
        dec_no = int(input("Decimal: "))
        print(decimal_to_hex(dec_no))
    elif command == 2:
        dec_no = int(input("Decimal: "))
        print(decimal_to_binary(dec_no))
    elif command == 3:
        bin_no = input("Binary: ")
        print(binary_to_dec(bin_no))
    elif command == 4:
        bin_no = input("Binary: ")
        print(decimal_to_hex(int(binary_to_dec(bin_no))))
    elif command == 5:
        hex_no = input("Hex: ")
        print(hex_to_dec(hex_no))
    elif command == 6:
        hex_no = input("Hex: ")
        print(decimal_to_binary(int(hex_to_dec(hex_no))))
    elif command == 7:
        quit = True