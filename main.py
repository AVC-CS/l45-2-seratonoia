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
    
    while (i < len(numbers)):
        numbers.append(random.randint(0,100))
        print((numbers[i]), end = ' ')
        total += numbers[i]
        i += 1
    
    
    


    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
