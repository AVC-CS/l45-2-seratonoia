import random


def main():
    total = 0
    numbers = [0] * 5
    """
    ########################################
    Code Your Program here
    ########################################
    """
    i = 0
    #syntax for append is listname.append(element)
    while (total < 100):
        for i in range (len(numbers)):
            rndNum = random.randint(0,100)
            numbers.append(rndNum)
            total += rndNum
    print(total)
    

    


    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
