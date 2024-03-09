print()
print('LEAP YEAR')
print()

year = int(input('Enter the year: '))
print()

# Calculation of leap year
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f'The year {year} is a leap year.')
    print()
else:
    print(f'The year {year} is not a leap year')
    print()
