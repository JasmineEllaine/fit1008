def decimal_to_binary(decimal_number):
    """
    This fucntion converts decimals to binary
    :param decimal_number: decimal to be converted (int)
    :return: binary representation (str)
    :raises: no exceptions
    :precondition: none
    :complexity: O(log(n))
    """
    my_list = []
    while decimal_number > 0:
        rem = decimal_number % 2
        my_list.insert(0, str(rem))
        decimal_number = decimal_number // 2
    return '0b' + ''.join(my_list)

if __name__ == '__main__':
    number = int(input('Enter a number: '))
    print('The binary representation is ' + decimal_to_binary(number))

# print(decimal_to_binary.__doc__)