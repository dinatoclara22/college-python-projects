print('Bem Vindo ao Controle de Estoque da Bicicletaria da Clara Dinato')
print('--' * 30)

pecas = {}
contador = 0

# Função para cadastrar peça
def cadastrarPeca(codigo):
    global contador
    nome = input('Digite o nome da peça: ')
    fabricante = input('Digite o fabricante da peça: ')
    valor = float(input('Digite o valor da peça: '))

    # Criando um dicionário com os dados da peça
    peca = {'nome': nome, 'fabricante': fabricante, 'valor': valor}
    pecas[codigo] = peca
    contador += 1

# Função para consultar peça
def consultarPeca():
    while True:
        print("\nMenu de Consulta de Peças:")
        print("1 - Consultar Todas as Peças")
        print("2 - Consultar Peças por Código")
        print("3 - Consultar Peças por Fabricante")
        print("4 - Sair")

        opcao = int(input(">>Digite a opção desejada: "))

        if opcao == 1:
            if len(pecas) == 0:
                print(">>Não há peças cadastradas.")
            else:
                print('>>Todas as peças cadastradas:')
                for codigo, peca in pecas.items():
                    print(
                        f'Código: {codigo} | Nome: {peca["nome"]} | Fabricante: {peca["fabricante"]} | Valor: {peca["valor"]}')

        elif opcao == 2:
            codigo = int(input("Digite o código da peça: "))
            if codigo in pecas:
                peca = pecas[codigo]
                print(
                    f'Código: {codigo} | Nome: {peca["nome"]} | Fabricante: {peca["fabricante"]} | Valor: {peca["valor"]}')
            else:
                print('>>Peça não encontrada.')

        elif opcao == 3:
            fabricante = input('Digite o fabricante da peça: ')
            encontrou = False
            for codigo, peca in pecas.items():
                if peca['fabricante'] == fabricante:
                    encontrou = True
                    print(
                        f'Código: {codigo} | Nome: {peca["nome"]} | Fabricante: {peca["fabricante"]} | Valor: {peca["valor"]}')
            if not encontrou:
                print('>>Peça não encontrada.')
        elif opcao == 4:
            return
        else:
            print('>>Opção inválida.')

#Função para remover peça
def removerPeca():
  codigo = int(input('>>Digite o código da peça que deseja remover: '))
  if codigo in pecas:
    del pecas[codigo]
    print('>>Peça removida com sucesso!')
  else:
    print('>>Peça não encontrada.')
    

while True:
  print('Escolha a opção desejada:')
  print('1 - Cadastrar Peça')
  print('2 - Consultar Peça')
  print('3 - Remover Peça')
  print('4 - Sair')
  
  opcao = int(input('>>Digite a opção desejada: '))
  
  if opcao == 1:
    cadastrarPeca(contador)
  elif opcao == 2:
    consultarPeca()
  elif opcao == 3:
    removerPeca()
  elif opcao == 4:
    break
  else:
    print('>>Opção inválida.')