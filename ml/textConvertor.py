class textToList:
    entryText: str
    punctuation = ['.', ',', ':', ';', '!', '?', '(', ')']

    def __init__(self, strEntryText):
        self.entryText = strEntryText

    def textSplit(self):
        return self.entryText.split()

    def textPunctuation(self):
        i = 0
        afterChange = self.textSplit()
        for word in afterChange:
            if word[-1] in self.punctuation:
                afterChange[i] = word[:-1]
                word = afterChange[i]
            if word[0] in self.punctuation:
                afterChange[i] = word[1:]
            i += 1
        return afterChange


# textList = textToList("Some, text for. function")
# print(textList.textPunctuation())
