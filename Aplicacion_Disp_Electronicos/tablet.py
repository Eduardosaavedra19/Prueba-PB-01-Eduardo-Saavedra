"""
Módulo que define la clase tablet, heredando de dispositivos,
con atributos específicos para tablet.
"""

from dispositivo import Dispositivo


class Tablet(Dispositivo):
    """
    Clase que representa una tablet, con atributos como
    marca, modelo, tamaño de la pantalla en pulgadas.
    """

    def __init__(self,marca, modelo, precio, tamaño):
        """
        Inicializa una tablet.

        Args:
            marca (str): Marca del dispositivo.
            modelo (str): Modelo del dispositivo.
            precio (float): Precio del dispositivo (debe ser mayor a 0).
            tamaño (float): tamaño de la pantalla en pulgadas
        """    
        super().__init__(marca, modelo, precio)
        self.tamaño = tamaño

    def descripcion(self):
        """
        Devuelve una descripción completa de la tablet.
        """
        return (f"Tablet marca {self.marca}, modelo {self.modelo} "
                f"con una pantalla de  {self.tamaño} pulgadas")
        
    #Dividir la línea usando paréntesis para que quede más corta
    #Por lo que cada línea queda por debajo de 100 caracteres y Pylint no marcará el error.
    