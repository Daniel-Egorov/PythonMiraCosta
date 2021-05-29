def main():
    print('\nThis program will convert Celsius temperatures to Fahrenheit for you!\n')
    celsius = eval(input('What is the Celsius temperature? '))
    fahrenheit = 9/5 * celsius + 32
    print(f'The temperature is {fahrenheit} degrees Fahrenheit')
main()