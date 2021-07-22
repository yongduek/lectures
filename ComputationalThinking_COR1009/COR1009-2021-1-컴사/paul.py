alist = [1, 2, 'helo']
print(alist)

adictionary = {'kata': 5, 'Petes kata': 10, 'life': 0, 11: 'tank', 'mylist': [1, 2, 10]}
print(adictionary)

print('score of kata :', adictionary['kata'])

print(adictionary[11])

print(adictionary.keys())

print(adictionary.values())

for key, value in adictionary.items():
    print(key, ': ', value)

x = ['kata', 'life', 'Petes kata', 'kata']

score = 0
for k in x:
    print(' --> ', k, adictionary[k], score)
    score += adictionary[k]

score += adictionary['kata']

print('score: ', score)