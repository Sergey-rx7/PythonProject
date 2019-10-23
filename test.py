class textToList:
    entryText: str

    def show_info(self):
        print(f"List1: {self.entryText}, List2: {self.textSplit}")

    def __init__(self, newEntryText):
        self.entryText = newEntryText

    def textSplit(self):
        return self.entryText.split()


# entryText = str("Some, text for function")
textList = textToList("asd")
print(textList.textSplit())
# print(textList.textSplit(entryText))
