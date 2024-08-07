#lista
nomes = ['Fulano','cicrano','Beltrano','Joao','Maria','Jose']

#  indice vai funcionar como uma chave primaria pois ele nao se repete
# exibir a lista com seus indices

for i in range(len(nomes)): # range é a quantidade de vezes que vai percorrer de acordo com quantidade existente na lista
    print(f' Indice {i}: {nomes[i]}.')


#quebra de linha
print('\n')

try: # usuario informa o indice
    indice = int(input(' Informe o numero o indice: '))

    # faz a alteração

    nomes[indice] = input('Informe o novo nome: ').capitalize()
except:
    print('Nao foi possivel fazer a alteração.')

# exibir de novo a lista para verificar

for i in range(len(nomes)):
    print(f'Indice {i}: {nomes[i]}.')


 