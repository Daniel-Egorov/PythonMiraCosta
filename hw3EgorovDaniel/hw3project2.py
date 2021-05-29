def main():
    # get the first number
    numerator = int(input('What is the numerator? '))
    # get the second number
    denominator = int(input('What is the denominator? '))
    # do math to get the number before R
    firstNum = numerator // denominator
    # more math to get number after R
    secondNum = numerator % denominator
    # print the answer
    print(f'{firstNum}R{secondNum}')
main()