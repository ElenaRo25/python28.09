import argparse

def main(number, text, verbose, repeat):
    if verbose:
        print(f"Полученные аргументы: число = {number}, строка = '{text}', повтор = {repeat}")

    # Печатаем строку 'repeat' раз
    for _ in range(repeat):
        print(text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Обработка числа и строки.')
    parser.add_argument('number', type=int, help='Число для обработки (обязательный аргумент)')
    parser.add_argument('text', type=str, help='Строка для вывода (обязательный аргумент)')
    parser.add_argument('--verbose', action='store_true', help='Выводить дополнительную информацию о процессе')
    parser.add_argument('--repeat', type=int, help='Сколько раз повторить строку в выводе', default=1)

    args = parser.parse_args()
    
    main(args.number, args.text, args.verbose, args.repeat)