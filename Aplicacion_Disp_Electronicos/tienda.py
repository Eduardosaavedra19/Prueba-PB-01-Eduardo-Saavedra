"""Módulo que define la clase Tienda para gestionar dispositivos.

Permite agregar dispositivos de diferentes tipos (Computadora, Telefono, Tablet),
mostrar su catálogo completo y calcular el total en pesos de la tienda.
"""

class Tienda:
    """Clase que representa una tienda de dispositivos."""

    def __init__(self):
        """Inicializa la tienda con una lista vacía de dispositivos."""
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        """
        Agrega un dispositivo a la tienda.

        Args:
        dispositivo (Dispositivo): Instancia de Dispositivo o cualquiera de sus clases hijas 
        (computadora, telefono, tablet).
        Acción:
            - Aplica polimorfismo al llamar a dispositivo.descripcion() sin importar su tipo.
            - Muestra mensaje indicando que se agregó el dispositivo con su precio.
        """

        print(
            f"Agregado: {dispositivo.descripcion()} - Precio: "
            f"${dispositivo.get_precio()}"
        )
        #Dividir la línea usando paréntesis para que quede más corta
        #Por lo que cada línea queda por debajo de 100 caracteres y Pylint no marcará el error.
        self.dispositivos.append(dispositivo)

    def mostrar_catalogo(self):
        """
        Muestra todos los dispositivos en la tienda y calcula el total.

        Acción:
            - Recorre la lista de dispositivos y llama a descripcion() de cada uno (polimorfismo).
            - Suma los precios usando get_precio() (encapsulamiento).
            - Imprime el total acumulado de la tienda.
        """

        print("--- Catálogo de Dispositivos ---")
        total = 0
        for d in self.dispositivos:
            # Llamada a metodo descripcion() de cada dispositivo (polimorfismo)
            print(
                f"{d.descripcion()} | "
                f"${d.get_precio()}"
            )
            # Sumar el precio del dispositivo al total
            total += d.get_precio()
        # Muestra el valor total de todos los dispositivos de la tienda
            #si pongo este print dentro del bucle me mostrara valores acumativos
            #print(f"Valor total de dispositivos en la tienda: ${total}")
        print(f"Valor total de dispositivos en la tienda: ${total}")
