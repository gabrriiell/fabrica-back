class Contador:#cria o molde contador
    def __init__(self):
        self.valor = 0 #atributo chamado valor

    def incrementar(self):#função de incrementar um 
        self.valor += 1

    def resetar(self):#função de resetar o valor
        self.valor = 0

# Criar uma instância da classe Contador
contador = Contador()

# Incrementar o valor do contador
contador.incrementar()
contador.incrementar()

print("Valor do contador:", contador.valor)

contador.resetar()
print("Valor do contador após resetar:", contador.valor)
