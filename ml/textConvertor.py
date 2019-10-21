class textToList:
    # entryText = str("Some text for function")
    entryText = input(str())
    punctuation = ['.', ',', ':', ';', '!', '?', '(', ')']

    def textSplit(self):
        return self.entryText.split()


textList = textToList()
print(textList.textSplit())
