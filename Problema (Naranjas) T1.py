Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Bienvenido")
... print("")
... 
... precio_kilo = 2.37
... 
... cantidad_naranjas = int(input("Ingresar la cantidad de naranjas: "))
... print("")
... 
... precio_original = precio_kilo * cantidad_naranjas
... 
... if cantidad_naranjas < 3:
...     descuento = 0
...     num_descuento = "0"
... 
... elif cantidad_naranjas >= 3.01 and cantidad_naranjas <= 6:
...     descuento = 0.1
...     num_descuento = "10"
... 
... elif cantidad_naranjas >= 6.01 and cantidad_naranjas <= 10:
...     descuento = 0.15
...     num_descuento = "15"
...     
... else:
...     descuento = 0.2
...     num_descuento = "20"
... 
... descuento = precio_original * descuento
... descuento = round(descuento,2)
... 
... precio_final = precio_original - descuento
... precio_final = round(precio_final, 2)
... 
... print("CANTIDAD DE NARANJAS: ", cantidad_naranjas, "KILOS")
... print("DESCUENTO: ",num_descuento,"%")
... print("PRECIO ORIGINAL: $", precio_original)
