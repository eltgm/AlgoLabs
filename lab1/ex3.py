import random

if __name__ == '__main__':
    test_values = [random.random() * 20 for i in range(random.randint(1, 10))]
    print(test_values)

    test_values_sum = 0
    for item in test_values:
        if 0 < item < 10:
            test_values_sum += item

    print(test_values_sum)
