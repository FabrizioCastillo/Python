# Python

## Machete de git

Inicializar el repo:

```shell
git init
```

Para añadir el repositorio como origen remoto (GitHub) para git:

```shell
git remote add origin https://github.com/FabrizioCastillo/Python.git
```

> [!TIP]
> Si se usa `git clone` no hace falta porque el repositorio remoto ya viene añadido en la configuración en la carpeta .git.

Para traer (pull) los cambios del repositorio remoto al local:

```shell
git pull
```

Para añadir los cambios al área de preparación (stage)

- `git add archivo` añade un archivo, puede ser más de uno.
- `git add .` añade todos los cambios que hayan en el repositorio local.

Para confirmar (commit) los cambios hechos que estén añadidos al área de preparación:

```shell
git commit -m "mensaje"
```

>[!WARNING]
>El mensaje no debe estar vacío, de lo contrario se abrira el editor de texto predeterminado para editar el mensaje del commit.

Para enviar (push) los cambios confirmados al repositorio remoto:

```shell
git push origin rama
```

La rama principal puede ser **main** o **master**

> [!TIP]
> Si se encuentran conflictos al hacer git pull, como que haya un commit en el repositorio remoto anterior a la última confirmación que haya en el repositorio local y que este commit remoto no esté en el local, se puede usar `git pull --rebase` o `git pull --ff-only` para traer los cambios del repositorio remoto al local insertándolos en donde corresponda. Ésto mientras no sea un commit remoto y uno local en el que se modifique el mismo archivo, en ese caso el conflicto se resuelve revisando y modificando el archivo.
