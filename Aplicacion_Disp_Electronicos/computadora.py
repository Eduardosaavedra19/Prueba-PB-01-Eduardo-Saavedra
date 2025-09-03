"""
Módulo que define la clase computadora, heredando de dispositivos,
con atributos específicos para computadora.
"""

from dispositivo import Dispositivo


class Computadora(Dispositivo):
    """
    Clase que representa una computadora, con atributos como
    marca, modelo, precio y ram(GB).
    """

    def __init__(self,marca, modelo, precio, ram):
        """
        Inicializa una computadora.

        Args:
            marca (str): Marca del dispositivo.
            modelo (str): Modelo del dispositivo.
            precio (float): Precio del dispositivo (debe ser mayor a 0).
            ram (float): Cantidad de ram en GB del dispositivo.
        """    
        super().__init__(marca, modelo, precio)
        self.ram = ram

    def descripcion(self):
        """
        Devuelve una descripción completa de la computadora.
        """
        return (f"Computadora marca {self.marca}, modelo {self.modelo} "
                f"con una ram integrada de {self.ram} GB")
        
    #Dividir la línea usando paréntesis para que quede más corta
    #Por lo que cada línea queda por debajo de 100 caracteres y Pylint no marcará el error.
    