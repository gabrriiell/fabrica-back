
class Carro:
    def __init__(self, ano: int, modelo: str, marca: str, velocidade: int):
        # Atributos
        self.ano = ano
        self.modelo = modelo
        self.marca = marca
        self.velocidade = velocidade

    def movimento(self):
        if self.velocidade > 0 or self.velocidade < 0:
            movimento = True
            print(f"A sua velocidade é {self.velocidade}")
        else:
            movimento = False

        return movimento

# Criando uma instância de Carro
carro1 = Carro(2000, "Camaro", "Fiat", 100)

# Chamando o método movimento e exibindo o resultado
print(carro1.movimento())