# Ejercicio 2

> Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué
> ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique

Asignar una variable fuera de rango se refiere normalmente a errores de índice (IndexError, KeyError o StopIteration)

Ejemplo de IndexError:

```py
lista = [1, 2, 3]
print(lista[3]) # IndexError
```

Ejemplo de KeyError:

```py
diccionario = {'a': 1, 'b': 2}
valor = diccionario['c']  # KeyError
```

Ejemplo de StopIteration:

```py
iterador = iter([1, 2, 3])
for i in range(5):
    print(next(iterador)) # StopIteration
```

## Manejo del problema

Siempre hay que asegurarse de que los rangos establecidos sean los adecuados y se respeten.
La solución que se puede usar en caso de que sea un problema que pueda venir por parte del usuario, se puede usar `try` y `except`.

Por ejemplo:

### Para las listas

```py
lista = [1, 2, 3]
try:
    print(lista[3]) # IndexError
except IndexError as e:
    print(f"Error{e}")
```

## Para los diccionarios

```py
diccionario = {'a': 1, 'b': 2}
try:
    valor = diccionario['c']  # KeyError
except KeyError as e:
    print(f"Error{e}")
```

## Para los iteradores

```py
iterador = iter([1, 2, 3])
for i in range(5):
    try:
        print(next(iterador)) # StopIteration
    except StopIteration as e:
        print(f"Error {e}")
```
