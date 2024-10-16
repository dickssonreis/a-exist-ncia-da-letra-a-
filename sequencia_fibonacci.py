print('-'*30)
print('A existência da letra A')
print('-'*30)

letra = []
letra = str(input('Digite o seu texto:'))
existencia = letra.count('a')
letra_a = letra.count('A')
print(len(letra)) 
print(f'a letra aparece {existencia} vezes')
print(f'a letra aparece {letra_a} vezes')