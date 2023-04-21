print('Bem Vindo a Companhia de Logistica Clara Dinato')

#Função para verificar as dimensões do objeto
def dimensoesObjetos():
    while True:
        try:
            comprimeto = float(input('Digite o comprimento do produto(cm): '))
            altura = float(input('Digite a altura do produto(cm): '))
            largura = float(input('Digite a largura do produto(cm): ')) 
            volume = comprimeto * altura * largura
            return volume / 1000000 # Convertendo cm³ para m³
        except ValueError:
            print('Digite apenas números válidos!') 

#Função para verificar o peso do objeto
def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do produto(kg): '))
            if peso >= 30:
                print('O peso do produto deve ser menor que 30kg!')
                continue
            elif peso <= 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
        except ValueError:
            print('Digite apenas números válidos!')

#Função para selecionar a rota
def rotaObjeto():
    while True:
        try:
            rota = input('Selecione a rota: \n BR - Brasília para Rio de Janeiro \n BS - Brasília para São Paulo \n RB - Rio de Janeiro para Brasília \n RS - Rio de Janeiro para São Paulo \n SR - São Paulo para Rio de Janeiro \n SB - São Paulo para Brasília \n')
            
            if rota not in ['BR', 'BS', 'RB', 'RS', 'SR', 'SB']:
                print('BR', 'BS', 'RB', 'RS', 'SR', 'SB')
                continue
            
            elif rota == 'RS' or rota == 'SR':
                return 1
            
            elif rota == 'BS' or rota == 'SB':
                return 1.2
            
            elif rota == 'BR' or rota == 'RB':
                return 1.5
        except ValueError:
            print('Você digitou uma rota que não existe!')

#Funçaõ para calcular o frete	           
def calculoFrete():
    dimensoes = dimensoesObjetos()
    peso = pesoObjeto()
    rota = rotaObjeto()
    
    total = dimensoes * peso * rota
    
    print('Total a ser pago: R$ {:.2f}'.format(total))

calculoFrete()