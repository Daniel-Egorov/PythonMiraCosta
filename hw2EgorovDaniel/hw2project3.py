def main():
    amountOfTests = eval(input('Enter the number of scores to be averaged: '))
    score = 0
    count = 1
    for i in range(amountOfTests):
        score += eval(input(f'Enter exam score {count}: '))
        count += 1
    avg = score / amountOfTests
    print(f'The average test score is {avg}')
main()