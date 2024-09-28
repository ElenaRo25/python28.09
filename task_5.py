import os
import logging
import argparse
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Определение namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', 'name extension is_directory parent_directory')

def gather_directory_info(path):
    try:
        # Проверяем, что путь существует и это директория
        if not os.path.exists(path) or not os.path.isdir(path):
            raise ValueError(f"Указанный путь '{path}' не является существующей директорией.")
        
        contents = []
        parent_directory = os.path.basename(os.path.normpath(path))

        # Проходим по элементам директории
        for entry in os.listdir(path):
            entry_path = os.path.join(path, entry)
            is_directory = os.path.isdir(entry_path)
            name, extension = os.path.splitext(entry)
            entry_info = FileInfo(name, extension[1:] if not is_directory else '', is_directory, parent_directory)

            # Добавляем информацию в список
            contents.append(entry_info)
            logging.info(f"Обработано: {entry_info}")

        return contents

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Сбор информации о содержимом директории.')
    parser.add_argument('path', type=str, help='Путь до директории')

    args = parser.parse_args()
    
    
    # Получаем информацию о директории
    info = gather_directory_info(args.path)

    # Выводим результат в консоль
    for item in info:
        print(item)