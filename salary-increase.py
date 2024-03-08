print()
print('SALARY INCREASE')
print()

# Receiving the employee's name and salary
name = (input('Enter your name: '))
salary = (float(input('Enter your salary: ')))

# Calculation of salary increase
increase = salary * 0.25
total = salary + increase

# Printing the results
print()
print('INFORMATION - 25% INCREASE')
print(f'Name: {name}')
print(f'Salary: {salary:.2f} $')
print(f'Increase: {increase:.2f} $')
print(f'New Salary: {total:.2f} $')
