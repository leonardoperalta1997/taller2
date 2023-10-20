Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Bienvenido")
... print("")
... 
... precio = int(input("Ingrese el precio del producto a escoger: "))
... 
... if precio > 50:
...     descuento = precio * 0.1
...     print("Se aplico un descuento del 10%!")
... 
...     total = precio - descuento
... else:
...     descuento = 0
...     total = precio
...     
... print("PRECIO: $", precio) 
... print("DESCUENTO: $", descuento)
