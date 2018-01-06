class Dictionary:
    dictionary = {'a': [],
                  'b': [],
                  'c': [],
                  'd': [],
                  'e': [],
                  'f': [],
                  'g': [],
                  'h': [],
                  'i': [],
                  'j': [],
                  'k': [],
                  'l': [],
                  'm': [],
                  'n': [],
                  'o': [],
                  'p': [],
                  'q': [],
                  'r': [],
                  't': ['tree', ],
                  'u': ['urde', 'uref', 'urfe', 'used'],
                  'v': ['vrde'],
                  'w': [],
                  'x': [],
                  'y': [],
                  'z': []
                  }

    @classmethod
    def getWords(cls, key):
        result = []
        if key in cls.dictionary.keys():
            result = cls.dictionary[key]
        return result


class Directory:
    keypad = {'0': [],
              '1': [],
              '2': ['a', 'b', 'c'],
              '3': ['d', 'e', 'f'],
              '4': ['g', 'h', 'i'],
              '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r', 's'],
              '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y''z']
              }

    @classmethod
    def getLetters(cls, key):
        result = []
        if key in cls.keypad.keys():
            result = cls.keypad[key]
        return result


def transform(words, letters=[], index=0):
    result = []
    for word in words:
        if len(word) > index and word[index] in letters:
            result.append(word)
    return result


def getvalidwords(sequence):
    result = []
    digit = sequence[0]
    letters = Directory.getLetters(digit)
    for character in letters:
        words = Dictionary.getWords(character)
        for index in range(1, len(sequence)):
            words = transform(words, Directory.getLetters(sequence[index]), index)
        if len(words) > 0:
            result.append(words)
    return result


if __name__ == '__main__':
    sequence = "8733"
    print(getvalidwords(sequence))
