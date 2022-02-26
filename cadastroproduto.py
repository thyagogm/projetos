produtos = []


# Função Cadastro Produto!
def cadastro_produto(cod, name, price, qnt):
    produtos.append([cod, name, price, qnt])


# Função Formulario do Produto!
def formulario_produto():
    print('-=' * 2, 'Cadastro Produto', '-=' * 2)
    codigo = int(input('Codigo do Produto:'))
    nome = str(input('Nome do Produto:'))
    valor = float(input('Preço do Produto:'))
    estoque = int(input('Estoque:'))
    print('-=' * 13)
    cadastro_produto(codigo, nome, valor, estoque)


# Função Menu!
def menu():
    print('-=' * 5, 'Menu', '-=' * 5)
    print('[1]Cadastrar Produto!')
    print('[2]Consultar Produto!')
    print('[3]Deletar Produto!')
    print('[4]Sair')
    print('-=' * 13)


# Função Retorno
def retornar():
    continuar = str(input('Voltar ao Menu? (S/N)')).upper()
    while continuar == 'S':
        programa()
    if continuar == 'N':
        exit()
    else:
        print('Opção Invalida, Tente Novamente!')
        retornar()


# Função Programa
def programa():
    while True:
        # Chamando o Menu!
        menu()
        # Pegando a Informação da Opção!
        resp = int(input('Escolha uma Opção:'))
        print('-=' * 13)
        # Se a Opção for 1 então Faça!
        if resp == 1:
            # Chama o Formulário!
            formulario_produto()
            # Produto Cadastrado com Sucesso!
            print('Produto Cadastrado com Sucesso!')
            # Retorna ao Menu!
            retornar()
        # Se a Opção for 2 então Faça!
        elif resp == 2:
            # Exibe os Produtos Cadastrados!
            print('-=', 'Produtos Cadastrados', '-=')
            print(produtos)
            print('-=' * 13)
            # Retorna ao Menu!
            retornar()
        # Se a Opção for 3 então Faça!
        elif resp == 3:
            # Pega o Numero Digitado!
            num = int(input('Digite o Codigo do Produto:'))
            real = (num - 1)
            # Deleta da Lista o Item Cadastrado!
            try:
                del produtos[real]
                print('Produto Deletado com Sucesso!')
            except IndexError:
                print('Codigo Não Encontrado!')
            else:
                print('Digite Apenas Números!')
            # Retorna ao Menu!
            retornar()
        # Se a Opção for 4 Então Faça!
        elif resp == 4:
            confirmar = input(str('Voce Realmente Deseja Sair? (S/N)')).upper()
            if confirmar == 'S':
                break
            if confirmar == 'N':
                menu()
            else:
                print('Opção Invalida, Tente Novamente!')
                retornar()
        break


# Iniciando o Programa
programa()
