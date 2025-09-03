"""
Módulo que define la clase telefono, heredando de dispositivos,
con atributos específicos para telefono.
"""

from dispositivo import Dispositivo


class Telefono(Dispositivo):
    """
    Clase que representa una telefono, con atributos como
    marca, modelo, precio y ram(GB).
    """

    def __init__(self,marca, modelo, precio, camara):
        """
        Inicializa una telefono.

        Args:
            marca (str): Marca del dispositivo.
            modelo (str): Modelo del dispositivo.
            precio (float): Precio del dispositivo (debe ser mayor a 0).
            camara (float): Cantidad de megapixeles del dispositivo
        """    
        super().__init__(marca, modelo, precio)
        self.camara = camara

    def descripcion(self):
        """
        Devuelve una descripción completa de la camara.
        """
        return (f"telefono marca {self.marca}, modelo {self.modelo} "
                f"con camara de {self.camara} megapixeles")
        
    #Dividir la línea usando paréntesis para que quede más corta
    #Por lo que cada línea queda por debajo de 100 caracteres y Pylint no marcará el error.
    