def decimal_to_hex(decimal_number):
    """
    This program converts from decimal to hex representation
    :param decimal_number: an integer
    :return: hex representation as a string
    :raises: no exceptions
    :precondition: no preconditions
    :complexity: O(log(n))
    """
    my_list = []
    while decimal_number > 0:
        rem = decimal_number % 16
        if rem > 9:
            if rem == 10:
                rem = 'A'
            elif rem == 11:
                rem = 'B'
            elif rem == 12:
                rem = 'C'
            elif rem == 13:
                rem = 'D'
            elif rem == 14:
                rem = 'E'
            else:
                rem = 'F'
        my_list.insert(0, str(rem))
        decimal_number = decimal_number // 16
    return '0x' + ''.join(my_list)
    
if __name__ == '__main__':
    number = int(input('Enter a number: '))
    print('The hexadecimal representation is ' + decimal_to_hex(number))
