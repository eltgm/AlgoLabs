if __name__ == '__main__':
    test_string = 'Лидер, лидировал и любил носить линзы. Даже дарил их Лизе.'

    start_index_alphabet = ord('А')
    end_index_alphabet = ord('я')

    is_done = False

    string_length = len(test_string)

    new_string = ''
    start_index_of_finding = None
    while not is_done:
        start_index_of_substring = test_string.find('Ли', start_index_of_finding)

        for i in range(start_index_of_substring, string_length):
            if start_index_alphabet <= ord(test_string[i]) <= end_index_alphabet:
                new_string += test_string[i]
            else:
                new_string += ', '
                start_index_of_finding = i
                break

        if start_index_of_finding == string_length - 1:
            is_done = True

    print(new_string)
