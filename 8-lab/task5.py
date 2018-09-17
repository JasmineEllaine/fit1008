from task2 import ArrayBasedList

class textEditor:
    def __init__(self):
        """ Constructor for textEditor 
        Args:
            None
        Returns:
            None
        Raises:
            None
        Precondition:
            None
        Postcondition:
            None
        Complexity:
            O(1)
        """
        self.lines = ArrayBasedList()

    def insert(self, text, num=None):
        """ Inserts text into index num
        Args:
            text (str): text to be inserted
            num (int): optional, index of text
        Returns:
            None
        Raises:
            Exception: if no num value inputed
        Precondition:
            num must be inputted
        Postcondition:
            text will be inserted
        Complexity:
            O(n)
        """
        if (num == None):
            print("?")
            raise Exception("No 'num' value provided")
        else:
            self.lines.insert(int(num), text)

    def read(self, filename):
        """ Reads filename into array
        Args:
            filename (str): filename to be read
        Returns:
            None
        Raises:
            None
        Precondition:
            None
        Postcondition:
            contents of file will be read
        Complexity:
            O(n)
        """
        file = open(filename)
        for line in file:
            self.lines.append(line.strip())
        file.close()

    def write(self, filename):
        """ Writes array into filename
        Args:
            filename (str): filename to be written
        Returns:
            None
        Raises:
            None
        Precondition:
            None
        Postcondition:
            contents of file will be written
        Complexity:
            O(n)
        """
        file = open(filename, "w")
        for item in self.lines:
            file.write("{}\n".format(item))
        file.close()

    def printLines(self, num1, num2):
        """ Lines between num1 num2
        Args:
            num1 (int): first
            num2 (int): second
        Returns:
            None
        Raises:
            None
        Precondition:
            None
        Postcondition:
            line iwll be printed
        Complexity:
            O(n)
        """
        if (num1 < num2):
            while (num1 < num2-1):
                print(self.lines[num1])
                num1 += 1

    def delete(self, num=None):
        """ Lines between num1 num2
        Args:
            num1 (int): first
            num2 (int): second
        Returns:
            None
        Raises:
            None
        Precondition:
            None
        Postcondition:
            line iwll be printed
        Complexity:
            O(n)
        """
        if (num == None):
            self.lines = ArrayBasedList()
        else:
            self.lines.delete(num)

    def search(self, word):
        """ Lines between num1 num2
        Args:
            num1 (int): first
            num2 (int): second
        Returns:
            None
        Raises:
            None
        Precondition:
            None
        Postcondition:
            line iwll be printed
        Complexity:
            O(n)
        """
        i = 0
        for line in self.lines.lower():
            if word in line:
                print("Line", i)

    def run(self):
        """ Runs textEditor
        Args:
            None
        Returns:
            None
        Raises:
            None
        Precondition:
            None
        Postcondition:
            line iwll be printed
        Complexity:
            O(n)
        """
        userInput = input("Enter command: ").split()
        while (userInput[0] != "quit"):
            tooShort = len(userInput) < 2
            if (userInput[0] == "insert"):
                textInsert = input("Enter line of text to insert: ")
                if tooShort:
                    userInput += [None]
                textEditor.insert(self, textInsert, userInput[1])
            elif (userInput[0] == "read"):
                textEditor.read(self, userInput[1])
            elif (userInput[0] == "write"):
                textEditor.write(self, userInput[1])
            elif (userInput[0] == "print"):
                textEditor.printLines(self, int(userInput[1]), int(userInput[2]))
            elif (userInput[0] == "delete"):
                if tooShort:
                    textEditor.delete(self)
                else:
                    textEditor.delete(self, int(userInput[1]))
            elif (userInput[0] == "search"):
                textEditor.search(self, userInput[1])
            else: 
                print("?")
                raise Exception("Unrecognised command")
            userInput = input("Enter command: ").split()

if __name__ == "__main__":
    myEditor = textEditor()
    myEditor.run()