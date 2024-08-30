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
> Si se usa `git clone` no hace falta porque el remoto ya viene añadido

Para traer (pull) los cambios del repositorio remoto al local:
```shell
git pull
```

Para añadir los cambios al área de preparación (stage)
- `git add archivo` añade un archivo, puede ser más de uno.
- `git add .` añade todos los cambios.

Para confirmar (commit) los cambios hechos que estén añadidos al área de preparación:
```shell
git commit -m "mensaje"
```
>[!TIP]
>El mensaje debe estar vacío

Para enviar (push) los cambios confirmados al repositorio remoto:
```shell
git push origin rama
```
> La rama principal puede ser **main** o **master**