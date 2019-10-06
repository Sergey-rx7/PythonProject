# Входящая строка текста
# Можно вводить из консоли, заменив на str = input("Write down or insert some text:\n")
# unknow
# str = 'Now you just have to find a work friend who will dress up as Popeye!'
str = 'Wear a Superman t-shirt underneath your work suit and leave your shirt unbuttoned. It’s the perfect excuse to look a little sloppy at work! These punny Halloween costumes will give everyone a laugh.'

# знаки препинания, которые могут содержаться в тексте
punctuation = ['.', ',', ':', ';', '!', '?', '(', ')']

# Метод split() без аргументов разделяет строку
# по символам пробела.
# Получаем список слов, которые могут начинаться
# или заканчиваться знаком препинания.
wordList = str.split()

# переменная-индекс слов в списке wordList
i = 0
# Извлекается каждое слово из списка.
for word in wordList:
    # Если последний символ этого слова содержится
    # в списке punctuation
    if word[-1] in punctuation:
        # то на место (i) этого слова в список wordList
        # помещается копия этого слова, но без последнего символа.
        # Срез [:-1] обозначает взять последовательность от ее начала
        # до последнего элемента (не включая его).
        wordList[i] = word[:-1]
        # Заменяется значение word на текущее, иначе алгоритм ниже
        # будет обрабатывать старое слово, а не то, у которого уже мог
        # быть удален последний символ.
        word = wordList[i]
    # Еще если первый символ слова содержится в списке знаков препинания
    if word[0] in punctuation:
        # то переписать слово на его копию без первого символа.
        # Срез [1:] обозначает взять последовательность от элемента
        # с индексом 1 (он второй по счету) до конца.
        wordList[i] = word[1:]
    # увеличение переменной-индекса, т. е. переход к следующему слову
    i += 1

# Код ниже выводит слова по пять штук в строке.
# Можно так не делать, а просто вывести список командой
# print(wordList)
# i = 0
# while i < len(wordList):
#     print(wordList[i], end=' ')
#     i += 1
#     if i % 5 == 0:
#         print()

MALE = 'male'
FEMALE = 'female'
UNKNOWN = 'unknown'
BOTH = 'both'
# Массив относящийся к определителям мужского пола
MALE_WORDS = set(
    ['guy', 'spokesman', 'Superman', 'chairman', "men's", 'men', 'him', "he's", 'his', 'boy', 'boyfriend', 'boyfriends', 'boys',
     'brother', 'brothers', 'dad', 'dads', 'dude', 'father', 'fathers', 'fiance', 'gentleman', 'gentlemen',
     'god', 'grandfather', 'grandpa', 'grandson', 'groom', 'he', 'himself', 'husband', 'husbands', 'king', 'male',
     'man', 'mr', 'nephew', 'nephews', 'priest', 'prince', 'son', 'sons', 'uncle', 'uncles', 'waiter', 'widower',
     'widowers'])
# Массив относящийся к определителям женского пола
FEMALE_WORDS = set(
    ['heroine', 'spokeswoman', 'chairwoman', "women's", 'actress', 'women', "she's", 'her', 'aunt', 'aunts', 'bride',
     'daughter', 'daughters', 'female', 'fiancee', 'girl', 'girlfriend', 'girlfriends', 'girls', 'goddess',
     'granddaughter',
     'grandma', 'grandmother', 'herself', 'ladies', 'lady', 'mom', 'moms', 'mother', 'mothers', 'mrs', 'ms', 'niece',
     'nieces', 'priestess', 'princess', 'queens', 'she', 'sister', 'sisters', 'waitress', 'widow', 'widows', 'wife',
     'wives', 'woman'])


def genderize(wordList):
    mwlen = len(MALE_WORDS.intersection(wordList))
    fwlen = len(FEMALE_WORDS.intersection(wordList))
    if mwlen > 0 and fwlen == 0:
        return MALE
    elif mwlen == 0 and fwlen > 0:
        return FEMALE
    elif mwlen > 0 and fwlen > 0:
        return BOTH
    else:
        return UNKNOWN


print(genderize(wordList))