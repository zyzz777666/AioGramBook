import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    sign = [',', '.', '!', '?', ':', ';']
    full_text = ''

    for i in range(start, len(text)):
        full_text += text[i]
        if len(full_text) >= size:
            break
    while True:
        if full_text[-1] in sign and full_text[-2] in sign and full_text[-3] in sign:
            full_text = full_text[:-3]
        elif full_text[-1] in sign and full_text[-2] in sign:
            full_text = full_text[:-2]
        elif full_text[-1] not in sign:
            full_text = full_text[:-1]
        else:
            break
    return full_text, len(full_text)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as f:
        file = f.read().rstrip()
        step = 0
        full_page = len(file) // PAGE_SIZE + 2
        page = 1
        while page != full_page:
            book[page] = _get_part_text(file, step, PAGE_SIZE)[0].lstrip()
            step += _get_part_text(file, step, PAGE_SIZE)[1]
            page += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))