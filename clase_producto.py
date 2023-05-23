import re
class Producto():
    existencia = 0
    def __init__(self, nombre='', precio=0.0):
        self.nombre = nombre
        self.precio = precio
        
    def iva(self):
        return self.precio * 0.16

    def entrada(self, cant):
        self.existencia += cant

    def salida(self, cant):
        self.existencia -= cant

def validareal(s):
    while True:
        num = input(s)
        if re.match(r'^[+]?\d*\.?\d*([E|e][+|-]?\d*)?$', num):
            return float(num)
        print('Debe ingresar un número real positivo.')

def validaentero(s):
    while True:
        num = input(s)
        if re.match(r'^[+]?\d+$', num):
            return int(num)
        print('Debe ingresar un número entero positivo.')

nombre = input('Nombre del producto: ')
precio = validareal("Ingrese el precio: ")
a = Producto(nombre, precio)
compra = validaentero('Ingrese la cantidad de producto entrante: ')
a.entrada(compra)

print('Nombre:',a.nombre)
print('Precio:',a.precio)
print('IVA:', a.iva())
print('Existencia:', a.existencia)
venta = validaentero('Ingrese la cantidad de producto vendido: ')
a.salida(venta)
print('Existencia:', a.existencia)