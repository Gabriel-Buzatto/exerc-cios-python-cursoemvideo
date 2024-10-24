preco = float(input('Preço do produto: R$'))
desconto = preco * 0.05
novo_preco = preco - desconto
print(f'Com o desconto o valor vai de R${preco}, para RS{novo_preco:.2f}')
