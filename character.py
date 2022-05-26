texto = input("texto: ")
"""numeroVogais = 0
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for car in texto:
    if car in vogais:
        numeroVogais += 1
print(numeroVogais)
"""
newText = ''
for car in texto:
    if 'A' <= car <= 'Z':
        car = chr(ord(car)+32)
    newText += car
print(newText)
