#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program gets a string from the user and repeats however many times they
# want

def main():
    # this program gets a string from the user and repeats however many times
    # they want
    counter = 0

    # input
    given_string = input("Enter any string please: ")
    print("\n", end="")

    # input, process & output
    while True:
        amount_of_copies = input("Enter the amount of times you would like the"
                                 " string to be repeated: ")
        print("\n", end="")
        try:
            amount_of_copies = int(amount_of_copies)

            if amount_of_copies > 0:
                for counter in range(amount_of_copies):
                    print("{0}".format(given_string), end="")
                    counter = counter + 1
                break
            else:
                print("{0} was not a positive integer. Enter an integer"
                      " above 0.".format(amount_of_copies))
                print("\n", end="")

        except Exception:
            print("{0} is not an integer. Please enter an integer."
                  .format(amount_of_copies))
            print("\n", end="")


if __name__ == "__main__":
    main()
