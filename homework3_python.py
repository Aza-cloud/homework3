# Задача 1
# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

list_1 = [1, 2, 3, 4, 5]
k = 3
count = 0

# Введите ваше решение ниже

for i in list_1:
    if i == k:
        count += 1
print(count)
#_____________________________________________________________________________________________________________

# Задача 2
# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
k = 10
list_2 = []
list_3 = []

# Введите ваше решение ниже

if k in list_1:
    print(k)
else:
    for i in list_1:
        if i < k:
            list_2.append(i)
        if i > k:
            list_3.append(i)

    if len(list_2) == 0:
        print(min(list_3))

    if len(list_3) == 0:
        print(max(list_2))

    if len(list_2) and len(list_3) != 0:
        num1 = k - max(list_2)
        num2 = min(list_3) - k

        if num1 < num2:
            print(max(list_2))
        else:
            print(min(list_3))
#_____________________________________________________________________________________________________________

# Задача 3
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# # В случае с английским алфавитом очки распределяются так:
#
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
#
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

k = 'ящерица'

# Введите ваше решение ниже

eng = 'qwertyuiopasdfghjklzxcvbnm'
rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

list_english = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
                 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
list_russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}

if k[0].lower() in eng:
    sum = 0
    for letter in k:
        for key, value in list_english.items():
            if letter.upper() in value:
                sum += key
    print(sum)
else:
    if k[0].lower() in rus:
        sum = 0
        for letter in k:
            for key, value in list_russian.items():
                if letter.upper() in value:
                    sum += key
    print(sum)