import os
from colorama import Fore, Back, Style
from modelos.Contabancaria import ContaBancaria
from time import sleep

def exibir_texto(texto):
    sleep(0.2)
    os.system('cls')
    print(Fore.RED + '-' * (len(texto)
     + 1) + Fore.RESET)
    print(Fore.RED + texto + Fore.RESET)
    print(Fore.RED + '-' * (len(texto) + 1) + Fore.RESET)
    print()

def acesso_a_conta_adicionar():
    for conta in ContaBancaria.contas:
        exibir_texto(texto='Adicionar Dinhero')
        dinheiro_adicionado = float(input(Fore.GREEN + 'quando dinheiro vc quer adiciona: '))

    saldo = conta._saldo
    total = saldo + dinheiro_adicionado
    print(f'O seu saldo foi para {total}' + Fore.RESET)
    acesso_a_conta_voltar_pro_menu()

def acesso_a_conta_voltar_pro_menu():
    input('digite algo pra voltar pro menu de contas: ')
    acesso_a_conta()

def acesso_a_conta_opcao_errada():
    exibir_texto(texto='Opição Errada: ')
    acesso_a_conta_voltar_pro_menu()

def acesso_a_conta_tranferir():
    for conta in ContaBancaria.contas:
        exibir_texto(texto='Tranferir')
        quando_dinheiro_vai_ser_tranferido = float(input('Qundo dinhero vc quer que vai cheja tranferido: '))
        pra_quem = input('quem é o nome da pessoa que vc quer tranferir: ')
        print(Fore.GREEN + 'Pronto o dinheiro foi tranferido' + Fore.RESET)
        acesso_a_conta_voltar_pro_menu()
    saldo = conta._saldo
    saldo - quando_dinheiro_vai_ser_tranferido

def acesso_a_conta_opicao():
    try:
        print('''
              Opção
          
          1. Adicionar
          2. Tranferir
          3. voltar ao Menu
              ''')
        ver_opcao = int(input('Escolha uma opção: '))
        
        if ver_opcao == 1:
            acesso_a_conta_adicionar()
        elif ver_opcao == 2:
            acesso_a_conta_tranferir()
        elif ver_opcao == 3:
            voltar_pro_menu()
        else:
            acesso_a_conta_opcao_errada()

    except:
        acesso_a_conta_opcao_errada()


def voltar_pro_menu():
    input('Digite algo para voltar pro menu: ')
    os.system('cls')
    main()

def acesso_a_conta():
    for conta in ContaBancaria.contas:
        exibir_texto(texto=f'Conta de {conta._titular} acessada')
        print(f'O seu saldo é {conta._saldo}')
        acesso_a_conta_opicao()



def titulo():
    os.system('cls')
    print(Fore.RED + '''
██████╗░░█████╗░███╗░░██╗░█████╗░░█████╗░  ██╗░░░░░██╗░░░██╗░█████╗░░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗  ██║░░░░░██║░░░██║██╔══██╗██╔══██╗
██████╦╝███████║██╔██╗██║██║░░╚═╝██║░░██║  ██║░░░░░██║░░░██║██║░░╚═╝███████║
██╔══██╗██╔══██║██║╚████║██║░░██╗██║░░██║  ██║░░░░░██║░░░██║██║░░██╗██╔══██║
██████╦╝██║░░██║██║░╚███║╚█████╔╝╚█████╔╝  ███████╗╚██████╔╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░  ╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝
''' + Fore.RESET
)

def cadastra_conta():
    exibir_texto(texto='Cadastra Conta')
    nome = input('qual é o do titular da conta: ').title()
    saldo = float(input('qual é o saldo da sua conta: '))
    email = input('Digite o um email para cadastra sua conta: ').lower()
    senha = input('Digite uma senha com no minimo 8 digitos: ')
    confirmacao_de_senha = input('Confirme a senha: ')
    senha_numero = 'aaaaaaaa'
    while senha != confirmacao_de_senha and len(senha_numero) > len(senha):
        if senha == confirmacao_de_senha and len(senha) >= len(senha_numero):
            conta = ContaBancaria(nome, saldo, email, senha)
            voltar_pro_menu()
        else:
            senha = ''
            confirmacao_de_senha = ''
            senha = input('Digite uma senha com no minimo 8 digitos: ')
            confirmacao_de_senha = input('Confirme a senha: ')
            

def listar_conta():
    exibir_texto(texto='Acessar Conta')
    conta_encontrada = False
    ContaBancaria.listar()
    ver_opicao = input('qual o nome de conta que vc quer acessar: ').title()
    for conta in ContaBancaria.contas:
        if ver_opicao == conta._titular:
            exibir_texto(texto=f'Verficação de acesso a conta {conta._titular}')
            verificar_email = input('digite o email da conta: ').lower()
        else:
            print('Nome errado')
            voltar_pro_menu()
            return
    
        if verificar_email == conta._email:
            print(Fore.GREEN + 'email certo' + Fore.RESET)
            verficar_senha = input('digite a senha da conta: ')
        else:
                print(Fore.RED + 'Email errado' + Fore.RESET)
                voltar_pro_menu()
                return
        
        if verficar_senha == conta._senha:
            print(Fore.GREEN + 'Conta acessada' + Fore.RESET)
            sleep(0.5)
            acesso_a_conta()
            conta_encontrada = not conta_encontrada


        else:
            print(Fore.RED + 'Senha errado' + Fore.RESET)
            voltar_pro_menu()

def opicao():
    try:
        print(Style.BRIGHT + '''OPIÇÃO
        
1. Cadastra Conta
2. Acessar Conta
3. Sair''')
        opicao_escolida = int(input('Escolha uma opição: '))
    
        if opicao_escolida == 1:
            cadastra_conta()
        elif opicao_escolida == 2:
            listar_conta()
        elif opicao_escolida == 3:
            finalizar_app()
        else:
            opicao_errada()
    except:
        opicao_errada()
    

def finalizar_app():
    exibir_texto(texto='Finalizar o APP')

def opicao_errada():
    exibir_texto(texto='Opição Errada')
    input('Digite algo para voltar pro menu')
    main()

def main():
    titulo()
    opicao()

if __name__ == '__main__':
    main()