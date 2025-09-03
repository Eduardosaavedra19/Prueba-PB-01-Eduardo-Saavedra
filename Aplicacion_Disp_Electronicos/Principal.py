"""Clase principal para ejecutar la tienda"""

from computadora import Computadora
from telefono import Telefono
from tienda import Tienda
from tablet import Tablet

# Crear la tienda
mi_tienda = Tienda()

# Instanciar computadoras, telefonos y tablets (se crea el objeto)

computadoras = [
    Computadora("Hp", "Home", 400000, 8),
    Computadora("Asus", "Gamer", 1400000, 32),
    Computadora("Olidatta", "Oficina", 850000, 16)
]

telefonos = [
    Telefono("Xiaomi", "Delta", 950000, 40),
    Telefono("Sanesnug", "Chamullo", 50000, 10),
    Telefono("Asus", "Rog8", 1500000, 50)
]

tablets = [
    Tablet("Samsung", "Mono5", 600000, 15),
    Tablet("Xiaomi", "R500", 550000, 10),
    Tablet("Lenovo", "Active", 789999, 12)
]

# Usar el setter para modificar el precio de dos de ellos
# Telefono("Xiaomi", "Delta", 950000, 40),
# Tablet("Xiaomi", "R500", 550000, 10),
telefonos[0].set_precio(959999)
tablets[1].set_precio(559999)

# Agregar todos a la concesionaria
for d in telefonos + tablets + computadoras:
    mi_tienda.agregar_dispositivo(d)

# Mostrar el catálogo completo
mi_tienda.mostrar_catalogo()
