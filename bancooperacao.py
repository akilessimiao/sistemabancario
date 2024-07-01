# Banco,
# Mono usuário com 3 operacoes:
# Depósito, saque e extrato

# 1) Depósito
# Apenas Valores positivos;
# incluir histórico desta operação no extrato

# 2) Saque
# 3 saques diários com limite máximo de 500,00 por saque
# Caso nao tenha saldo em conta, informar mensagem que nao sera possivel sacar
# incluir histórico desta operação no extrato

# 3) Extrato
# Listar todos os depósitos e saques do histórico.
# Ao final exibir o saldo atual da conta.
# Padrão R$ xxx.yy

from datetime import datetime

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.saques_diarios = 0
        self.historico = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.historico.append(f'Depósito: {timestamp} - R$ {valor:.2f}')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def saque(self, valor):
        if valor > 0:
            if valor < 2001 and self.saques_diarios < 5:
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.saques_diarios += 1
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.historico.append(f'Saque: {timestamp} - R$ {valor:.2f}')
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
                else:
                    print('Saldo insuficiente para realizar o saque.')
            else:
                print('Limite diário de saque excedido ou valor de saque inválido (limite máximo por saque: R$ 2000).')
        else:
            print('Valor de saque inválido.')

    def extrato(self):
        print('Histórico de transações:')
        for transacao in self.historico:
            print(transacao)
        print(f'Saldo atual: R$ {self.saldo:.2f}')


def main():
    conta = ContaBancaria()

    while True:
        print("\nOpções:")
        print("1) Depósito")
        print("2) Saque")
        print("3) Extrato")
        print("0) Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Informe o valor do depósito: R$ "))
            conta.deposito(valor)
        elif opcao == '2':
            valor = float(input("Informe o valor do saque: R$ "))
            conta.saque(valor)
        elif opcao == '3':
            conta.extrato()
        elif opcao == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()