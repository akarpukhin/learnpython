def file_read(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read().splitlines()
    return text


def count(text):
    lines = 0
    words_in_line = 0
    total_words = 0
    letters = 0
    for line in text:
        lines += 1
        letters += len(line)
        print('строка номер: {line}'.format(line=lines))
        words_in_line = line.split(' ')

        if len(words_in_line) == 1 and '' in words_in_line:
            print('Пустая строка')
            total_words += 0
        else:
            print('Колличество слов: {words_in_line}'
                .format(words_in_line=len(words_in_line)))
            total_words += len(words_in_line)
        print('Колличество символов в этой строке: {len}\n'
            .format(len=len(line)))
    return lines, total_words, letters


if __name__ == '__main__':
    print('---=== Начинаю подсчет: ===---\n')

    text = file_read('referat.txt')
    lines, total_words, letters = count(text)

    print("\n---=== ИТОГО: ===---")
    print("Строк:", lines)
    print("Слов:", total_words)
    print("Символов:", letters)