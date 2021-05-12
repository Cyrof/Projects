# test code for github
# building random number generator
# import random
import random as r

# function for processing


def process(num1):
    # initialise list to store numbers
    number = []

    # for loop to generate rnd number one by one
    for x in range(num1):
        # use randint function from random to generate number between specified values
        num = r.randint(1, 10)
        number.append(str(num))

    print("%d" % int(''.join(number)))

# function to prompt user for input


def user():
    num_1 = int(input("How many digit do you want the random number to be? : "))

    # call process function
    process(num_1)


if __name__ == "__main__":
    user()