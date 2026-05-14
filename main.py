from abc import ABC, abstractmethod
# Interface
class Gama(ABC):

    @abstractmethod
    def tipo_gama(self):
        pass
class Electrodomestico:
    def __init__(self,id, marca, modelo, precio):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}"
class Lavadora(Electrodomestico, Gama):
    def __init__(self, id, marca, modelo, precio, capacidad_carga,consumo_agua,ciclos_de_lavado):
        super().__init__(id, marca, modelo, precio)
        self.capacidad = capacidad_carga
        self.consumo_agua = consumo_agua
        self.ciclos_de_lavado = ciclos_de_lavado
    def __str__(self):
        return super().__str__() + f", Capacidad de Carga: {self.capacidad} kg, Consumo de Agua: {self.consumo_agua} L, Ciclos de Lavado: {self.ciclos_de_lavado}"

    def tipo_gama(self):
        if self.capacidad <= 10 and self.ciclos_de_lavado <= 3:
            return "Gama Baja"
        elif self.capacidad <= 15 and self.ciclos_de_lavado <= 5:
            return "Gama Media"
        else:
            return "Gama Alta"

