"""
Módulo que define la clase del dispositivo, base para otros tipos de dispositivos.
"""

class Dispositivo:
    """
    Clase base que representa un dispositivo genérico sus atributos 
    marca, modelo y precio.
    """

    def __init__(self, marca, modelo, precio):
        """
        Inicializa un dispositivo.

        Args:
            marca (str): Marca del dispositivo.
            modelo (str): Modelo del dispositivo.
            precio (float): Precio del dispositivo (debe ser mayor a 0).
        """       
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio

    def get_precio(self):
        """
        Getter que devuelve el precio del dispositivo.

        Returns:
            float: Precio del dispositivo.
        """
        return self.__precio

    def set_precio(self, nuevo_precio):
        """
        Setter que modifica el precio del dispositivo.

        Args:
            nuevo_precio (float): Nuevo precio del dispositivo. Debe ser mayor que 0.
        """
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El nuevo precio debe ser mayor que 0")

    def descripcion(self):
        """
        Método que devuelve una descripción del dispositivo.
        Este método puede ser sobreescrito por clases hijas.

        Returns:
            str: Descripción del dispositivo.
        """
        return f"Dispositivo marca {self.marca} y modelo {self.modelo}"
