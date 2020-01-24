from ml.textConvertor import textToList
from ml.wordCatalog import *
from collections import Counter

class determinantSex:

    def mwlendef(self):
        mwlen = len(MALE_WORDS.intersection(self))
        return mwlen

    def fwlendef(self):
        fwlen = len(FEMALE_WORDS.intersection(self))
        return fwlen

    def genderize(self):
        if determinantSex.mwlendef(self) > 0 and determinantSex.fwlendef(self) == 0:
            return MALE
        elif determinantSex.mwlendef(self) == 0 and determinantSex.fwlendef(self) > 0:
            return FEMALE
        elif determinantSex.mwlendef(self) > 0 and determinantSex.fwlendef(self) > 0:
            return BOTH
        else:
            return UNKNOWN

    def count_gender(self):
        words = Counter()
        if determinantSex.genderize(self) == 'male':
            sexlen = determinantSex.mwlendef(self)
        elif determinantSex.genderize(self) == 'female':
            sexlen = determinantSex.fwlendef(self)
        for sexlen in self:
            words[sexlen] += 1
        return words

someText = textToList("man, text for. function")
print(determinantSex.genderize(someText.textPunctuation()))
print(determinantSex.count_gender(someText.textPunctuation()))