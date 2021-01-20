if __name__ == '__main__':
    test_string = ',,,,,,,,,,,,,,,,Лидер,,,,, лидировал ,,,,и любил носить линзы. Даже дарил их Лизе.'
    start_index_alphabet = ord('А')
    end_index_alphabet = ord('я')

    words_count = 0
    is_word_start = False
    for i in range(0, len(test_string)):
        if ord(test_string[i]) not in range(start_index_alphabet, end_index_alphabet, 1):
            if is_word_start:
                words_count += 1
                is_word_start = False
        else:
            is_word_start = True

    print('Количество символов в строке - {}\nКоличество слов в строке - {}'.format(len(test_string), words_count))

