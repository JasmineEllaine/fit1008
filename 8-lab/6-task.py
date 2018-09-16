from task3 import LinkedList

class textEditor:
    def __init__(self):
        self.lines = LinkedList()

    def insert(self, text, num=None):
        if (num == None):
            print("?")
            raise Exception("No 'num' value provided")
        else:
            self.lines.insert(int(num), text)

    def read(self, filename):
        file = open(filename)
        for line in file:
            self.lines.append(line.strip())
        file.close()

    def write(self, filename):
        file = open(filename, "w")
        for item in self.lines:
            file.write("{}\n".format(item))
        file.close()

    def printLines(self, num1, num2):
        if (num1 < num2):
            while (num1 < num2):
                print(self.lines[num1])
                num1 += 1

    def delete(self, num=None):
        if (num == None):
            self.lines = ArrayBasedList()
        else:
            self.lines.delete(num)

    def search(self, word):
        i = 0
        for line in self.lines.lower():
            if word in line:
                print("Line", i)

    def run(self):
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