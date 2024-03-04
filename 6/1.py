from itertools import permutations

letter = ['Т', 'И', 'М', 'О', 'Ф', 'Е', 'Й']
code = set()

for p in permutations(letters, 5):
    if p[0] != 'Й' and p[-1] != 'Й' and 'ИЙ' and 'ЙИ' not in ''.join(p):
        code.add(''.join(p))

print(len(code))
