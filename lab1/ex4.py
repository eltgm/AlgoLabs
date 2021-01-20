import random

if __name__ == '__main__':
    test_values = [random.random() * 20 for i in range(random.randint(1, 10))]
    print(test_values)

    min_in_values = test_values[0]

    for item in test_values:
        if min_in_values > item:
            min_in_values = item

    print(min_in_values)
