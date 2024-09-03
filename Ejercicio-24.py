def imprimir_caracteres(Palabra, indice=0):
  #Lent: Contador de caracteres que hay
    if indice == len(Palabra):
        return
    # Imprime
    print(Palabra[indice])
    # Llamada recursiva
    imprimir_caracteres(Palabra, indice + 1)


#Principal 
Palabra = input("Ingrese una frase: ")
imprimir_caracteres(Palabra)
