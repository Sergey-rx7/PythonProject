class textToList:
    entryText = str("Some, text for function")
    # entryText = input(str())
    punctuation = ['.', ',', ':', ';', '!', '?', '(', ')']
    i = 0
    word = []

    def textSplit(self):
        return self.entryText.split()

    def textPunctuation(self):
        self.i = 0
        self.word = []
        for self.word in textToList.textSplit():
            if self.word[-1] in textToList.punctuation:
                textToList.punctuation[self.i] = self.word[:-1]
                word = textToList.punctuation[self.i]
            if self.word[0] in textToList.punctuation:
                textToList.punctuation[self.i] = self.word[1:]
            self.i += 1
        return self.word

textList = textToList()
print(textList.textSplit())
print(textList.textPunctuation())