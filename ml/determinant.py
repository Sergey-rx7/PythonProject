from ml.textConvertor import textToList
from ml.wordCatalog import *


class determinantSex:
    def genderize(self):
        mwlen = len(MALE_WORDS.intersection(self))
        fwlen = len(FEMALE_WORDS.intersection(self))
        if mwlen > 0 and fwlen == 0:
            return MALE
        elif mwlen == 0 and fwlen > 0:
            return FEMALE
        elif mwlen > 0 and fwlen > 0:
            return BOTH
        else:
            return UNKNOWN


someText = textToList("man, text for. function")
print(determinantSex.genderize(someText.textPunctuation()))
