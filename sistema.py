from datetime import datetime
print("Desenvolvendo Sistemas Bancários!")

saldo, depositos, saques, data_do_saque, data_deposito = 0.0, [], [], [], []
agora = datetime.now() # Captura a data Atual
sacado = 0

menu = '''
    ####### Sistema Bancário #######
      WR***    Escolha Uma Opção  ***WR

    [1] -->>> Depósito
    [2] -->>> Saque
    [3] -->>> Extrato Bancário
    [0] -->>> Sair Do ProGrama

'''

def depositar():
    valor_deposito = float(input("Quanto deseja Depositar? R$"))
    global saldo
    if valor_deposito > 0:
        saldo += valor_deposito
        depositos.append(valor_deposito)
        agora_atual_deposito = datetime.now()
        d_deposito = agora_atual_deposito.strftime("%d/%m/%Y %H:%M:%S")
        data_deposito.append(d_deposito)

    else:
        print("Erro Na Operação! Digite Um Valor Válido ")

def saque():
    LIMITE_DE_SAQUE = 3
    global saldo
    global sacado
    if sacado < LIMITE_DE_SAQUE: #verifica se já foi excedido o limite de saque
        valor_saque = float(input("Quanto Deseja Sacar? R$"))
        if valor_saque > 0:#verifica se o valor que o usuario esta colocando é positivo
            if valor_saque <= 500: #verifica se o valor do saque segue a regra de R$500 por saque
                if (saldo - valor_saque) < 0:
                    print("Saldo Insuficiente")
                else:
                    saldo -= valor_saque
                    saques.append(valor_saque)
                    agora_atual_saque = datetime.now() #captura a Data Atual no momento em que é feito o saque
                    data_format = agora_atual_saque.strftime("%d/%m/%Y %H:%M:%S") # Deixa a Data Atual Formatada
                    data_do_saque.append(data_format)
                    sacado += 1
                    print(f"Quantidade de Saques {sacado}")
            else:
                print("Você Não Pode Fazer um Saque acima de R$500")
        else:
            print("Erro Na Operação! Digite um Valor positivo!")
    else:
        print("Limite de Saque Excedido! Você não Pode fazer mais que três Saque!")


def extratos():

    print("###########  Extrato ###########")
    info_extrato = "Ainda Não Há Movimentações" if not saques and not depositos else "  " #Ternario utlizado para Informar se Houve Movimentações
    print(info_extrato)
    print("###########    SALDO   ############")
    print(f"Saldo: R$ {saldo:.2f}")
    #Ternario utlizado para Informar se Houve Saques
    info_saque = "Ainda Não Há Saques " if not saques and  depositos else "  "
    print("############      Saques    ################")
    print(info_saque)
    for saque,data_s in zip(saques,data_do_saque):
        print(f"Saque :R$ {saque:.2f} -- {data_s}")
    print("################# Depositos ################:")
    for deposito,data_d in zip(depositos,data_deposito):
        print(f"Deposito:R$ {deposito:.2f} -- {data_d}")

while True:

    print(menu)
    try:

        parada = True
        opcao = int(input("Escolha Uma Das Opções? "))
        match(opcao):
            case 1:
                depositar()
            case 2:
                saque()
            case 3:
                extratos()
            case 0:
                parada = False
            case _:
                print("Digite Uma Opção Válida")# aqui ele verifica se o usuario digitou algum numero diferente das opções Fornecidas
        if parada == False:
            print("Programa Finalizado Com Sucesso")
            break
    except ValueError: #aqui ele verifica se foi clicado a tecla enter
        print("Digite Uma Opção Válida ")
