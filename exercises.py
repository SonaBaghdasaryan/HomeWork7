# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from random import choices, randint
from string import ascii_lowercase, digits

# def make_files(extansion: str, min_name: int = 6, max_name: int = 30, min_size:
# int = 256, max_size: int = 4096, count: int = 42) -> None:
#     for _ in range(count):
#         name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
#         data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
#         with open(f'{name}.{extansion}', 'wb') as f:
#             f.write(data)
#     if __name__ == '__main__':
#         make_files('bin', count=1)
# def file_generate(**kwargs) -> None:
#     for extension, count in kwargs.items():
#         make_files(extension=extension, count=count)
#
#     if __name__ == '__main__':
#         file_generate(bin=2, jpg=1)

# Дорабатываем функции из предыдущих задач.
#  Генерируйте файлы в указанную директорию — отдельный параметр функции.
#  Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
#  Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

# from pathlib import  Path
# from random import choices, randint
# from string import  ascii_lowercase, digits
# from os import chdir
#
#
# def make_files(extansion: str, min_name: int = 6, max_name: int = 30, min_size:
# int = 256, max_size: int = 4096, count: int = 42) -> None:
#     for _ in range(count):
#         print(Path.cwd())
#         while True:
#             name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
#             if not Path(f'{name}.{extansion}').is_file():
#                 break
#         data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
#         with open(f'{name}.{extansion}', 'wb') as f:
#             f.write(data)
#
# def file_generate(path: str | Path, **kwargs) -> None:
#     if isinstance(path, str):
#         path = Path(path)
#     if not path.is_dir():
#         path.mkdir(parents=True)
#     chdir(path)
#     for exttansion, count in kwargs.items():
#         make_files(extansion=extansion, count=count,min_name=1, max_name=1)
# if __name__ == '__main__':
#     file_generate('Desktop/new/new_tab', bin=2, jpg=10)

# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

# from os import chdir
# from pathlib import Path
#
# def sorted_file(path: Path, groups: dict[Path, list[str]] = None) -> None:
#     chdir(Path)
#
#     if groups is None:
#         groups = {
#             Path('video'): ['avi', 'mkv'],
#             Path('image'): ['jpg', 'png'],
#             Path('text'): ['txt', 'doc'],
#     }
#
#     rev_group = {}
#     for target_dir, extansion_list in groups.items():
#         if not target_dir.is_dir():
#             target_dir.mkdir()
#         for extansion in extansion_list:
#             rev_group[f'.{extansion}'] = target_dir
#     for file in path.iterdir():
#         if file.is_file() and file.suffix in rev_group.keys():
#             file.replace(rev_group[file.suffix] / file.name)
#
# if __name__ == '__main__':
#     sorted_file(Path('Desktop/new/new_tab'))



