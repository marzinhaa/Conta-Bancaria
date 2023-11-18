class ContaBancaria:

    def __init__(self, numero, saldo, nome, limite, status = False):
        self.numero=numero
        self.saldo=saldo
        self.nome=nome
        self.limite=limite
        self.status=status

    def depositar(self):
        deposito = float(input("Deseja depositar quanto?: "))
        if deposito <= 0:
            print("Depósito inválido")
        else:
            self.saldo += deposito
            print(f"Seu novo saldo é {self.saldo}")

    def sacar(self):
        self.limite = 30000
        print(f"Seu limite de saque é {self.limite}")
        saque = float(input("Quanto deseja sacar?: "))
        if saque > self.saldo:
            print("Saldo Insuficiente")
        elif saque > self.limite:
            print("Limite Insuficiente")
        else:
            self.saldo -= saque
            print(f"Seu saldo em conta é {self.saldo}")

    def ativarconta(self):
        if self.status == False:
            self.status = True
            print("Conta ativada")
        else:
            print("Está conta ja está ativa")

    def verificarsaldo(self):
        print(f"Seu saldo em conta é {self.saldo}")