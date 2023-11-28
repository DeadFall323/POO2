import itertools

resultado = 30
lista_bolas = [1, 3, 5, 7, 9, 11, 13, 15]

# encontre todas as combinações possíveis de 3 bolas
combinacoes = itertools.combinations(lista_bolas, 3)

# verifique se alguma das combinações resulta em 30
for combinacao in combinacoes:
    if sum(combinacao) == resultado:
        print("Combinação encontrada: ", combinacao)
        break
else:
    print("Nenhuma combinação resulta em 30.")
