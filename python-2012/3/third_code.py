def decode_morse(string):
    table = ['iI', 'Iiii', 'IiIi', 'Iii', 'i', 'iiIi', 'IIi', 'iiii', 'ii', 'iIII', 'IiI', 'iIii', 'II', 'Ii', 'III', 'iIIi', 'IIiI', 'iIi', 'iii', 'I', 'iiI', 'iiiI', 'iII', 'IiiI', 'IiII', 'IIii']
    result = ''
    for i in string.split():
        result += chr(ord('A') + table.index(i))

    return result
