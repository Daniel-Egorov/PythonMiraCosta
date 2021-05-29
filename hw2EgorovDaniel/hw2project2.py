def main():
    print('\nThis program will convert Fahrenheit temperatures to Celsius for you!\n')
    fahrenheit = eval(input('What is the Fahrenheit temperature? '))
    celsius = round((fahrenheit - 32) * (5/9), 1)
    print(f'The temperature is {celsius} degrees Celsius')
main()