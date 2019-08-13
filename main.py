alphabet_rus = ('А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З',
                'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
                'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',
                'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
                )

print('Добро пожаловать в игру:\nAmazing trip!')

gamer = {'name': input('Как тебя зовут?\n'),
         'age': int(input('Сколько тебе лет?\n')),
         'sex': input('Какого ты пола?\n'),
         'pet_name': input('Как зовут твоего питомца?\n'),
         'desire': False,
         }

answer_desire = input('Любишь ли ты играть - ДА/НЕТ?\n').lower()

if answer_desire == 'да':
    gamer['desire'] = True

if gamer['age'] < 18:
    print('Тебе нельзя играть')
elif gamer['age'] > 90:
    print('Эта игра может быть для тебя утомительна')
    answer_90 = input('Хочешь ли ты играть - ДА/НЕТ?\n').lower()
    if answer_90 == 'да':
        answer_90 = input('Ты точно хочешь играть - ДА/НЕТ?\n').lower()
        if answer_90 == 'да':
            print('Тогда начнем игру')
        else:
            print('До свидания,', gamer['name'])
    else:
        print('До свидания,', gamer['name'])
else:
    print('Добро пожаловать в Игру,', gamer['name'])

if 18 <= gamer['age'] <= 90 or gamer['age'] > 90 and answer_90 == 'да':
    print('Я могу назвать буквы алфавита, которых нет в твоем имени. Вот они:')
    for char in alphabet_rus:
        if char not in gamer['name'].upper():
            print(char, end = ' ')
print()