class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')
        else:
            print('Valor do depósito deve ser maior que zero.')

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')
            else:
                print('Saldo insuficiente.')
        else:
            print('Valor do saque deve ser maior que zero.')

    def consultar_saldo(self):
        print(f'Saldo atual da conta de {self.titular}: R${self.saldo}')

    def transferir(self, outra_conta, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                outra_conta.depositar(valor)
                print(f'Transferência de R${valor} realizada para a conta de {outra_conta.titular}.')
            else:
                print('Saldo insuficiente para realizar a transferência.')
        else:
            print('Valor da transferência deve ser maior que zero.')


# Exemplo de uso:
if __name__ == "__main__":
    # Criando algumas contas
    conta1 = ContaBancaria('João', 1000)
    conta2 = ContaBancaria('Maria', 500)

    # Realizando operações nas contas
    conta1.depositar(500)
    conta2.sacar(200)
    conta1.transferir(conta2, 300)

    # Consultando saldo final
    conta1.consultar_saldo()
    conta2.consultar_saldo()
