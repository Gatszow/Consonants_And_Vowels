vowels = 'aąeęiouy'


def count_vowels(string: str) -> int:
    if len(string) == 0:
        return 0
    if string[0].isalpha() and string[0].lower() in vowels:
        return 1 + count_vowels(string[1:])
    return count_vowels(string[1:])


def count_consonants(string: str) -> int:
    if len(string) == 0:
        return 0
    if string[0].isalpha() and string[0].lower() not in vowels:
        return 1 + count_consonants(string[1:])
    return count_consonants(string[1:])
