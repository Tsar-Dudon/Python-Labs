from pathlib import Path
import shutil
input_path = input("Введите путь к папке(оставьте пустым для текущей папки): ")
path = None
if input_path:
    path = Path(input_path)
else:
    path = Path('.')
files = list(path.iterdir())
goodFiles = []
for i in files:
    if i.is_file() and (i.stat().st_size < 2048):
        print(i) 
        goodFiles.append(i)
if len(goodFiles) == 0:
    print("Нет подходящих файлов")
else: 
    small_folder = Path('.') / 'small'
    small_folder.mkdir(parents= True, exist_ok=True)
    for file in goodFiles:
        shutil.copy(file, small_folder / file.name)
    print(f"Файлы скопированы в папку: {small_folder}")