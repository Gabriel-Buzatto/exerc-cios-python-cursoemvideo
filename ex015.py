aluguel = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (aluguel * 60) + (km * 0.15)
print(f'O total a pagar é de R${pago:.2f}')
