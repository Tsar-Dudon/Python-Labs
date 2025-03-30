from pathlib import Path
dirpath = input("Введите путь к папке(оставьте пустым для текущей папки): ")
path = None
if dirpath:
    path = Path(dirpath)
else:
    path = Path('.')
f = open('uncommon.txt', 'r')
a = list(f.readlines())
f.close()
a = [line.rstrip() for line in a]
for i in a:
    file = path / i
    file.touch(exist_ok=True)