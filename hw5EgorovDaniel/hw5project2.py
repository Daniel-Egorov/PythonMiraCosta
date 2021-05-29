

def main():
    outputNums = []

    with open('input.txt') as file:
        inputNums = file.read()

    inputNums = inputNums.split('\n')

    for numberSet in inputNums:

        numberSet = numberSet.split()

        num1 = int(numberSet[0])
        num2 = int(numberSet[1])

        summed = num1 + num2

        outputNums.append(str(summed))

    final = '\n'.join(outputNums)
    with open('output.txt', 'w') as file:
        file.write(final)

main()