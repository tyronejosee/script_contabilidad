# **Script Contabilidad**

Scripts y automatizaciones para manipulación y limpieza de datos en documentos contables (Chile).

## **Crea un clon del repositorio**

```bash
git clone git@github.com:tyronejosee/script_contabilidad.git
```

## **Comandos Útiles**

Reemplaza completamente tu código local con la versión más reciente de la rama `main`, descartando cualquier cambio local.

```bash
git reset --hard origin/main
```

## **Instalar Poetry**

Si aún no tienes Poetry instalado, puedes hacerlo ejecutando el siguiente comando:

```bash
pip install poetry
```

## **Instalar dependencias**

Para agregar dependencias a tu proyecto, utiliza:

```bash
poetry add <dependencia>
```

Si es una dependencia de desarrollo, agrega el `--dev`:

```bash
poetry add --dev <dependencia>
```

## **Activar el entorno virtual**

Poetry gestiona automáticamente el entorno virtual. Para activarlo, puedes usar:

```bash
poetry shell
```

---

## **Comandos GIT**

- `git reset --hard origin/main`: Reemplaza completamente tu código local con la versión más reciente de la rama `main`, descartando cualquier cambio local.
- `git fetch --all`: Descarga los últimos cambios del repositorio remoto sin fusionarlos.
- `git stash`: Guarda temporalmente los cambios locales sin confirmarlos.
- `git pull origin main`: Descarga y fusiona los últimos cambios del repositorio remoto.
- `git stash pop`: Recupera tus cambios previamente guardados.
- `git checkout -- .`: Descartar todos los cambios locales no confirmados.
- `git pull origin main`: Descargar la última versión del código del repositorio remoto y fusionarla.
- `git fetch --all`: Obtiene las actualizaciones del remoto.
- `git reset --hard origin/main`: Restablece el código a la última versión del remoto.
- `git clean -fd`: Elimina archivos o directorios no rastreados por Git (útil si has agregado nuevos archivos que no están en el repositorio remoto).
