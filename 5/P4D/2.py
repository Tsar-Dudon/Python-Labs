from pathlib import Path
dirpath = input("Введите путь к папке(оставьте пустым для текущей папки): ")
files = ['a.txt','b.txt', 'f.txt','aboba.txt','rrr.txt'] # - Сюда вставить названия файлов
path = None
if dirpath:
    path = Path(dirpath)
else:
    path = Path('.')
fInDir = list(path.iterdir())
if len(files) > 0:
    common = []
    uncommon = []
    for i in fInDir:
        if i.name in files:
            common.append(i.name)
    for i in files:
        if i not in common:
            uncommon.append(i)
    print("Есть в файле:", *common)
    print("Нет в файле:", *uncommon)
    f = open('common.txt', 'w')
    for i in common:
        f.write(i + '\n')
    f.close()
    f = open('uncommon.txt', 'w')
    for i in uncommon:
        f.write(i + '\n')
    f.close()
else:
    c1 = 0
    c2 = 0
    for i in fInDir:
        c1 += 1
        c2 += i.stat().st_size
    print('Файлов в папке:', c1)
    print('Общий вес:', c2)