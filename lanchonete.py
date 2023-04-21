# Tabela de produtos
produtos = {
    "100": ["Cachorro-Quente", 9.00],
    "101": ["Cachorro-Quente Duplo", 11.00],
    "102": ["X-Egg", 12.00],
    "103": ["X-Salada", 13.00],
    "104": ["X-Bacon", 14.00],
    "105": ["X-Tudo", 17.00],
    "200": ["Refrigerante Lata", 5.00],
    "201": ["Chá Gelado", 4.00]
}

total = 0.0
pedidos = []

while True:
    # Exibir tabela de produtos
    print("Código | Descrição                 | Valor (R$)")
    print("**************Cardápio**************")

    for codigo, produto in produtos.items():
        descricao = produto[0]
        valor = produto[1]
        print(f"|{codigo} | {descricao:25} | {valor:.2f}|")
    print("---------------------------------------------")

    codigo_produto = input("Entre com o código desejado: ")

    if codigo_produto not in produtos:
        print("Opção Inválida!")
        continue

    print('Você pediu um(a) ', produtos.get(codigo_produto)[0], ' no valor de R$', produtos.get(codigo_produto)[1], '.')

    # Calcular o total
    pedidos.append(codigo_produto)
    total += produtos.get(codigo_produto)[1]

    opcao = input("Deseja realizar uma nova compra? \n 1 - Sim \n 2 - Não \n ")
    if opcao == '2':
        print('Encerrando programa...')
        break

    descricao_produto = produtos.get(codigo_produto)[0]
    valor_produto = produtos.get(codigo_produto)[1]

print(f"O total a ser pago é: R${total:.2f}")
