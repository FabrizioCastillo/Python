# Ejercicio 14

> Indique si en Python existen o no variables de tipo valor y su contraparte tipo
> referencia como sucede en otros lenguajes como Java.

En Python, dependiendo del tipo de dato que se trate, se comporta de forma distinta.

## Tipos de valor (inmutables)

- Enteros (int)
- Flotantes (float)
- Cadenas de texto (str)
- Tuplas (tuple)
- Booleanos (bool)

En estos tipos de datos, al crearse una variable, llámese `x`, y se le asigna un valor, por ejemplo 5, se crea un objeto en la memoria que contiene el valor de la variable. Cuando se asigna la referencia a la variable anterior a una nueva variable, llámese `y`, el valor ésta última será una referencia al objeto de la memoria de `x` hasta que alguno de los dos sea modificado.

Por ejemplo:

```py
x = 5 
y = x
```

En este caso, la variable `y` es una referencia a `x`

```py
x = 5 
y = x
x += 1
print(y)
```

En este otro caso, primero `y` es una referencia a `x`. Luego, cuando se cambia el valor de `x`, se crea un objeto en la memoria que contenga un 6 y se actualiza `x`, manteniendo `y` el valor de 5.

## Tipos de referencia (mutables)

- Listas (list)
- Diccionarios (dict)
- Conjuntos (set)
- Objetos personalizados (clases)

Los objetos mutables, como listas, diccionarios, sets y clases, se comportan como tipos de referencia. Esto significa que cuando asignas uno de estos objetos a otra variable, ambas variables apuntan al mismo objeto en memoria.

Por ejemplo:

```py
lista1 = [1, 2, 3]
lista2 = lista1  # lista2 referencia a la misma lista que lista1
lista2.append(4)  # Modificación en lista2
print(lista1)  # Salida: [1, 2, 3, 4]
```

```py
class MiClase:
    def __init__(self, valor):
        self.valor = valor

objeto1 = MiClase(10)
objeto2 = objeto1  # objeto2 referencia a objeto1
objeto2.valor = 20  # Modificación en objeto2
print(objeto1.valor)  # Salida: 20
```
