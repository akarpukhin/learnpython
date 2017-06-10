def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        print('---=== Начинаю подсчет: ===---\n')
        lines = 0
        words_in_line = 0
        total_words = 0
        letters = 0
        for line in f:
            lines += 1
            letters += len(line)
            print('строка номер: {line}'.format(line=lines))
            words_in_line = line.split(' ')

            if len(words_in_line) == 1 and ('\n' in words_in_line):
                print('Пустая строка')
                total_words += 0
            else:
                print('Колличество слов: {words_in_line}'
                    .format(words_in_line=len(words_in_line)))
                total_words += len(words_in_line)
            print('Колличество символов в этой строке: {len}\n'
                .format(len=len(line)))

        print("\n---=== ИТОГО: ===---")
        print("Строк:", lines)
        print("Слов:", total_words)
        print("Символов:", letters)

if __name__ == '__main__':
    main()