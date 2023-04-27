#Crie uma classe chamada Produto com os seguintes atributos:
# nome, preço e quantidade.
class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
#Crie uma classe chamada Principal com um método menu que
# apresenta as opções de cadastro, movimentação, reajuste
# de preços, relatórios e saída do sistema.
class Principal():
    def menu(self):
        print('Menu Principal')
        print('1 - Cadastro')
        print('2 - Movimentação')
        print('3 - Reajuste')
        print('4 - Relatórios')
        print('5 - Sair')
        opcao = int(input('Digite a opção: '))
        if opcao == 1:
            op_cad = Cadastro()
            op_cad.menu()
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            self.gravaRelatorio()
        elif opcao == 5:
            pass
        else:
            print('opção invalida!')
            self.menu()
    def gravaRelatorio(self):
        total = 0
        with open('relatorio.txt', 'w', encoding='utf-8') as arq:
            arq.write("ACME Inc.               Lista de produtos\n")
            arq.write("------------------------------------------------------------------------\n")

            arq.write('Descrição        Quantidade               Total\n')
            for i in produtos:
                valor = i['quantidade']*i['preco']
                arq.write(f"{i['nome'].ljust(18)}  {str(i['quantidade']).ljust(20)}  R${str(valor).ljust(10):.2f}\n")
                total +=i['quantidade']*i['preco']
            arq.write("------------------------------------------------------------------------\n")
            arq.write(f'Valor total de produtos R${total:.2f}')

#Crie uma classe chamada Cadastro que herda da classe
# Principal e possui os métodos inserir, alterar, excluir
# e consultar, que permitem cadastrar, alterar, excluir e
# consultar produtos, respectivamente.
class Cadastro(Principal):
    def menu(self):
        objeto.menu()
        print('Menu de Cadastro')
        print('1 - Cadastrar novo produto')
        print('2 - Alterar nome do Produto')
        print('3 - Excluir Produto')
        print('4 - Consultar produto')
        print('5 - Voltar')
        opcao = int(input('Digite a opção: '))
        if opcao == 1:
            self.inserir()
            self.menu()
        elif opcao == 2:
            self.alterar()
            self.menu()
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            objeto.menu()
        else:
            print('opção invalida!')
            self.menu()
    def inserir(self):
        novo = Produto('', 0, 0)
        novo.nome = input('Digite o nome do produto: ')
        novo.preco = input(f'Digite o preço do {novo.nome}: ')
        novo.quantidade = input('Digite a quantidade: ')
        produtos.append({'nome': novo.nome, 'preco': novo.preco, 'quantidade': novo.quantidade})
    def alterar(self):
        busca = input('Digite o nome do produto que está procurando:')
        for listadeprodutos in produtos:
            if busca.upper() == listadeprodutos['nome'].upper:
                novo = input(f'Altere {busca} para: ')
                listadeprodutos['nome'] = novo
            else:
                print('Produto não encontrado')
    def excluir(self):
        pass
    def consulta(self):
        pass
objeto = Principal()
produtos=[]
produtos = [{'nome':'tomate','preco':2.22,'quantidade': 200},
            {'nome':'cebola','preco':5.52,'quantidade': 500}]
objeto.menu()
# item =  input('Digite o nome: ')
# preco = input(f'Digite o preço do {item} :')
# quantidade = input('Digite a quantidade: ')
# produtos.append({'nome':item, 'preco':preco, 'quantidade': quantidade})
# for i in produtos:
#     print(f"O produto {i['nome']} tem {i['quantidade']}")