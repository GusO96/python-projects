print()
print('IMPOSTO POR ESTADO')
print()

value = float(input('Enter the value of the product: '))
state = (input('Enter the state (UF): '))
print()

# Calculating the tax rate by state
if state == 'MG':
    tax = value * 0.07
    final_price = value + tax
    print('The tax in Minas Gerais - MG is 7%')
    print(f'Total product value: R${final_price:.2f}')
    print()
elif state == 'SP':
    tax = value * 0.12
    final_price = value + tax
    print('The tax in São Paulo - SP is 12%')
    print(f'Total product value: R${final_price:.2f}')
    print()
elif state == 'RJ':
    tax = value * 0.15
    final_price = value + tax
    print('The tax in Rio de Janeiro - RJ is 15%')
    print(f'Tota product value: R${final_price:.2f}')
    print()
elif state == 'MS':
    tax = value * 0.08
    final_price = value + tax
    print('The tax in Mato Grosso do Sul - MS is 8%')
    print(f'Total product value: R${final_price:.2f}')
    print()
else:
    print('This UF is invalid, products only available in MG, SP, RJ and MS')
    print()
    