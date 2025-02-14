class ContaBancaria():
    contas = []
    def __init__(self, titular, saldo, email, senha):
        self._titular = titular
        self._saldo = saldo
        self._email = email
        self._senha = senha
        self._ativar = True
        ContaBancaria.contas.append(self)
    def __str__(self):
        return f'{self._titular} || {self._saldo}'

    
    @classmethod
    def listar(cls):
        print(f'{'Contas'.ljust(25)}')
        for conta in cls.contas:
            print(f'{conta._titular.ljust(25)}')