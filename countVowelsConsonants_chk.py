


def countVowelsAndCon(inp):

    vowels = ['a','e', 'i', 'o', 'u']

    countVowels = 0
    countConsonants = 0

    for ch in inp:
        if ch.lower() in vowels:
            countVowels+= 1
        else:
            countConsonants+= 1
    else:
        return countVowels, countConsonants

print(countVowelsAndCon('abcdefgh'))