print('Bem Vindo a Loja da Clara Dinato')

#Variaveis de armazenamento para o valor unitario e quantidade
valor_unitario = float(input("Digite o valor unitário do produto: "))
qtd = int(input("Digite a quantidade do produto: "))

valor_total_sem_desconto = valor_unitario * qtd

#Fazendo verificação para aplicar descontos
if qtd >= 1000:
    desconto = 0.15
elif qtd >= 100:
    desconto = 0.10
elif qtd >= 10:
    desconto = 0.05
else:
    desconto = 0

valor_total_com_desconto = valor_total_sem_desconto - (valor_total_sem_desconto * desconto)

#Informando os valores com e sem desconto
print(f"Valor total sem desconto: R$ {valor_total_sem_desconto:.2f}")
print(f"Valor total com desconto: R$ {valor_total_com_desconto:.2f}")
