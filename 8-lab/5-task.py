from task2 import ArrayBasedList

class textEditor:
    def __init__(self):
        self.commands = ["insert", "read", "write", "print", "delete", "search", "quit"]
        self.lines = ArrayBasedList()

    def insert(self, text, num=None):
        if (num == None):
            print("?")
            raise Exception("No 'num' value provided")
        else:
            self.lines.insert(num, text)

    def read(self, filename):
        file = open(filename)
        for line in file:
            self.lines.append(line.strip())

    def run(self):
        userInput = input("Enter command: ")
        while (userInput != "quit"):
            userInput = input("Enter command: ")

if __name__ == "__main__":
    myEditor = textEditor()
    myEditor.run()
