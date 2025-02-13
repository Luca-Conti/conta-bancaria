import os
class ContaBancaria():
    contas = []
    def __init__(self, titular, saldo, email, senha):
        self._titular = titular
        self._saldo = saldo
        self.email = email
        self.senha = senha
        self._ativar = True
        ContaBancaria.contas.append(self)
    def __str__(self):
        return f'{self._titular} || {self._saldo}'

    
    @classmethod
    def listar(cls):
        print(f'{'Contas'.ljust(25)}')
        for conta in cls.contas:
            print(f'{conta._titular.ljust(25)}')


def exibir_texto(texto):
    os.system('cls')
    print('-' * (len(texto)
     + 1))
    print(texto)
    print('-' * (len(texto) + 1))
    print()

def voltar_pro_menu():
    input('Digite algo para voltar pro menu: ')
    os.system('cls')
    main()

def titulo():
    print('''
██████╗░░█████╗░███╗░░██╗░█████╗░░█████╗░  ██╗░░░░░██╗░░░██╗░█████╗░░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗  ██║░░░░░██║░░░██║██╔══██╗██╔══██╗
██████╦╝███████║██╔██╗██║██║░░╚═╝██║░░██║  ██║░░░░░██║░░░██║██║░░╚═╝███████║
██╔══██╗██╔══██║██║╚████║██║░░██╗██║░░██║  ██║░░░░░██║░░░██║██║░░██╗██╔══██║
██████╦╝██║░░██║██║░╚███║╚█████╔╝╚█████╔╝  ███████╗╚██████╔╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░  ╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝
''')

def cadastra_conta():
    exibir_texto(texto='Cadastra Conta')
    nome = input('qual é o do titular da conta: ').title()
    saldo = float(input('qual é o saldo da sua conta: '))
    email = input('Digite o um email para cadastra não sua conta: ')
    senha = input('Digite uma senha com no minimo 8 digitos: ')
    confirmacao_de_senha = input('Confirme a senha: ')
    senha_numero = 'aaaaaaaa'
    if senha == confirmacao_de_senha and len(senha) >= len(senha_numero):
        conta = ContaBancaria(nome, saldo, email, senha)
        voltar_pro_menu()
    else:
        print('Faça o cadastro de novo')
        input('Digite algo para voltar pro cadastro')
        cadastra_conta()

def listar_conta():
    exibir_texto(texto='Acessar Conta')
    ContaBancaria.listar()
    ver_opicao = input('Qual o nome da conta que você quer acessar: ')

    for conta in ContaBancaria.contas:
        if ver_opicao == conta._titular:
            exibir_texto(texto=f'Verificação de acesso à conta {conta._titular}')
            verificar_email = input('Digite o e-mail da conta: ')

            if verificar_email == conta.email:
                print('E-mail correto.')
                verificar_senha = input('Digite a senha da conta: ')

                if verificar_senha == conta.senha:
                    print('Você acessou a conta!')
                    voltar_pro_menu()
                else:
                    print('Senha errada.')
                    voltar_pro_menu()
            else:
                print('E-mail errado.')
                voltar_pro_menu()
            return  

    print('Conta não encontrada.')
    voltar_pro_menu()


def opicao():
    try:
        print('''OPIÇÃO
        
1. Cadastra Conta
2. Acessar Conta
3. Sair''')
        opicao_escolida = int(input('Escolha uma opiçaõ: '))
    
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
main()
