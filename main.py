import random


def main():
    total = 0
    numbers = [] 
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    #syntax for append is listname.append(element)
    while (total < 100):
        rndNum = random.randint(0,100)
        numbers.append(rndNum)
        total += rndNum
        if total > 100:
            break

    
    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
