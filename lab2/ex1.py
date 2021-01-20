if __name__ == '__main__':
    my_number = 5

    while True:
        user_number = int(input("Guess a number - "))

        if user_number == my_number:
            print("Number guessed!")
            break
        elif user_number < my_number:
            print("Cold")
        elif user_number > my_number:
            print("Hot")


