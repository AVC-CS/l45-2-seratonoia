import random


def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    nums = random.randint(0,100)

    while nums < 100:
        for i in range (5):
        numbers.append(nums)
        i += 1
        total += nums
        if nums > 100:
            break
        print (total)

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
