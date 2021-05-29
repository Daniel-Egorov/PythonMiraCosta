def main():
    year = int(input("Input a 4 digit year: "))
    c = year // 100
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19))  % 30
    print(f'The epact value is {epact}')
main()
