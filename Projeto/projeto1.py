import json
import os.path
import sys

from cv2 import dnn_KeypointsModel

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    lista_categorias = []
    for produtos in dados:
        if produtos["categoria"] not in lista_categorias:
            lista_categorias.append(produtos["categoria"])
    lista_categorias.sort()
    return lista_categorias
    ...

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    lista_por_categoria = []
    for produtos in dados:
        if produtos["categoria"] == categoria:
            lista_por_categoria.append(produtos)
    return lista_por_categoria
    ...
    

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    lista_por_categoria = []
    for produtos in dados:
        if produtos["categoria"] == categoria:
            lista_por_categoria.append(produtos)
    lista_em_ordem = sorted(lista_por_categoria, key=lambda x:float(x["preco"]), reverse = True)   
    return lista_em_ordem[0]
    ...

def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    lista_por_categoria = []
    for produtos in dados:
        if produtos["categoria"] == categoria:
            lista_por_categoria.append(produtos)
    lista_em_ordem = sorted(lista_por_categoria, key=lambda x:float(x["preco"]))   
    return lista_em_ordem[0]
    ...

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    top_10 = sorted(dados, key=lambda x:float(x["preco"]), reverse = True)[0:10]    
    return top_10
    ...

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    menores_10 = [["",9999999],["",9999999],["",9999999],["",9999999],["",9999999],["",9999999],["",9999999],["",9999999],["",9999999],["",9999999]]
    under_10 = []
    for produtos in dados:
        if float(produtos["preco"]) <= menores_10[-1][1]:
            aux = []  
            menores_10.pop()
            aux.append(produtos["id"])         
            aux.append(float(produtos["preco"]))
            menores_10.append(aux)
            menores_10.sort(key=lambda x:x[1])    

    for auxiliares in menores_10:
        for produtos in dados:
            aux = []
            aux.append(produtos["id"])         
            aux.append(float(produtos["preco"]))
            if auxiliares == aux :
                under_10.append(produtos)
                
    return under_10
    ...

def valida_opção(opção):
    while not opção.isdigit():
        opção = input("Opção inválida, digite um valor entre 0 e 6 ")
    opção = int(opção) 
    while opção <0 or opção >6:
        opção = input("Opção inválida, digite um valor entre 0 e 6 ")    
        opção = valida_opção(opção)
    return opção

def mostrar_opções():
    print("Digite o número que deseja selecionar a opção ")
    print("1. Listar categorias")
    print("2. Listar produtos de uma categoria")
    print("3. Produto mais caro por categoria")
    print("4. Produto mais barato por categoria")
    print("5. Top 10 produtos mais caros")
    print("6. Top 10 produtos mais baratos")
    print("0. Sair")

def validacategoria(dados,categoria):
    lista = listar_categorias(dados)
    while categoria not in lista:
        categoria = input("categoria inválida, digite uma categoria presente no banco de dados. ")
    return categoria

def print_maior_valor(maior_valor,categoria):
    print(f"\nO produto de maior valor da categoria {categoria} é: ")
    print("id : "+maior_valor["id"])
    print("Preço : " +maior_valor["preco"])
    print("")

def print_menor_valor(menor_valor,categoria):
    print(f"\nO produto de menor valor da categoria {categoria} é: ")
    print("id : "+menor_valor["id"])
    print("Preço : " +menor_valor["preco"])
    print("")

def print_top_10_caros(top_10):
    for indice,valor in enumerate(top_10):
        print(f"\nO {indice+1}º produto mais caro é: ")
        id = valor["id"]
        preco = valor["preco"]
        categoria = valor["categoria"]
        print(f"id : {id}")
        print(f"preço : {preco}")
        print(f"categoria :  {categoria}")
    print("")

def print_top_10_baratos(top_10):
    for indice,valor in enumerate(top_10):
        print(f"\nO {indice+1}º produto mais barato é: ")
        id = valor["id"]
        preco = valor["preco"]
        categoria = valor["categoria"]
        print(f"id : {id}")
        print(f"preço : {preco}")
        print(f"categoria :  {categoria}")
    print("")

def print_por_categoria(lista_por_categoria,categoria):
    for indice,valor in enumerate(lista_por_categoria):
        id = valor["id"]
        preco = valor["preco"]
        categoria = valor["categoria"]
        print(f"\nO {indice+1}º produto da categoria {categoria} é:")
        print(f"id : {id}")
        print(f"preço : {preco}")
    print("")



def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    opção = 10
    while opção != 0:
        mostrar_opções()
        opção = valida_opção(input(""))        
        if 2<=opção<=4 :
            categoria = input("Digite a categoria desejada ")
            categoria = validacategoria(dados,categoria)
        if opção == 1 : 
            lista_categorias = listar_categorias(dados)
            print("\nAs categorias no banco de dados são: \n")
            for i in lista_categorias:
                print(i)
            print("")
        elif opção == 2 : 
            lista_por_categoria = listar_por_categoria(dados,categoria)  
            print_por_categoria(lista_por_categoria,categoria)             
        elif opção == 3 :
            produto_maior_valor = produto_mais_caro(dados,categoria)
            print_maior_valor(produto_maior_valor,categoria)
        elif opção == 4 :
            produto_menor_valor = produto_mais_barato(dados,categoria)
            print_menor_valor(produto_menor_valor,categoria)            
        elif opção == 5 : 
            top_mais_caros = top_10_caros(dados)
            print_top_10_caros(top_mais_caros)
        elif opção == 6 :
            top_mais_baratos = top_10_baratos(dados)
            print_top_10_baratos(top_mais_baratos)        
        
    print("programa encerrado")

# Programa Principal - não modificar!
d = obter_dados()
menu(d)
