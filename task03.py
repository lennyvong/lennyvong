def characterFrequency(sentences: str) -> dict:
    a = 0
    tab = {}

    for i in sentences:
        if i in tab:
            tab[i] += 1
        else:
            tab[i] = 1
    return tab

assert(characterFrequency("If you ignore both your program and yourself, you will only count your battles by your defeats. ~ Rob Tzu") == \
    {' ': 19, 'o': 12, 'y': 8, 'u': 8, 'r': 7, 'e': 5, 't': 5, 'l': 5, 'n': 4, 'b': 4, 'a': 4, 'f': 3, 's': 3, 'i': 2, 'g': 2, 'd': 2, 'I': 1,\
        'h': 1, 'p': 1, 'm': 1, ',': 1, 'w': 1, 'c': 1, '.': 1, '~': 1, 'R': 1, 'T': 1, 'z': 1}), "As this one is."