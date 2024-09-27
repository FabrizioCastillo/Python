
# Ejercicio 15

Al ejecutar el siguente código:

```py
x = None 
print(x)
```

> Salida: None

## Explicacion

None significa la ausencia de un valor o un valor nulo.Se puede utilizar 
(cuando no tenemos un valor establecido para una variable) como valor predeterminado
o cuando una funcion no devuelve ningun valor.

## Ejemplo

```py
def funcion_sin_retorno():

 print("Esta funcion no devuelve ningun valor")



resultado=funcion_sin_retorno()
print(resultado)  # Salida:None

```