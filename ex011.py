altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}. Para pintar sua parede, você precisará de {area / 2:.1f}l de tinta!')
