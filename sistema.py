from datetime import datetime
print("Desenvolvendo Sistemas Bancários!")

saldo, depositos, saques, data_do_saque, data_deposito = 0.0, [], [], [], []
agora = datetime.now() # Captura a data Atual
LIMITE_DE_SAQUE = 3

menu = '''
    ####### Sistema Bancário #######
      WR***    Escolha Uma Opção  ***WR

    [1] -->>> Depósito
    [2] -->>> Saque
    [3] -->>> Extrato Bancário
    [0] -->>> Sair Do ProGrama

'''

def depositar():
    valor_deposito = float(input("Quanto deseja Depositar?"))
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
    sacado = 0.0
    global saldo
    valor_saque = float(input("Quanto Deseja Sacar?"))
    if valor_saque > 0:
        if valor_saque <= 500 and sacado < LIMITE_DE_SAQUE:
            if (saldo - valor_saque) < 0:
                print("Saldo Insuficiente")
            else:
                saldo -= valor_saque
                saques.append(valor_saque)
                agora_atual_saque = datetime.now() #captura a Data Atual no momento em que é feito o saque
                data_format = agora_atual_saque.strftime("%d/%m/%Y %H:%M:%S") # Deixa a Data Atual Formatada
                data_do_saque.append(data_format)
                sacado += 1
        elif valor_saque <= 500 and sacado == LIMITE_DE_SAQUE:
            print("Você Não Pode fazer mais de Três Saques ")
        else:
            print("Você Não Pode Fazer um Saque acima de R$500")
    else:
        print("Erro Na Operação! Digite um Valor positivo!")



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
        opcao = int(input("Qual Sua Opção? "))
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
                print("Digite Uma Opção Válida")
        if parada == False:
            print("Programa Finalizado Com Sucesso")
            break
    except ValueError:
        print("Digite Uma Opção Válida ")
