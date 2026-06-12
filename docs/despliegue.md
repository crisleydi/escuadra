# Guía de Despliegue

Esta guía describe el proceso de instalación y ejecución de Escuadra en sistemas Windows, Linux y macOS. Incluye la configuración del entorno virtual, la instalación del proyecto mediante pip y la verificación del funcionamiento de la interfaz de línea de comandos (CLI).

---

# Prerrequisitos

Antes de instalar Escuadra, asegúrese de tener instalado:

* Python 3.10 o superior
* pip (incluido con Python)
* Git

> Escuadra requiere Python 3.10 o superior. Versiones anteriores no están soportadas.

Verificar las versiones instaladas:

```bash
python --version
pip --version
git --version
```

> En algunos sistemas Linux o macOS puede ser necesario utilizar `python3` en lugar de `python`.

---

# Obtener el código fuente

## Clonar el repositorio
Si desea utilizar Escuadra únicamente como usuario:

```bash
git clone https://github.com/sis-inf/escuadra.git
cd escuadra
```

Si trabaja mediante el flujo de contribución del proyecto, clone primero su fork personal:

```bash
git clone https://github.com/TU-USUARIO/escuadra.git
cd escuadra
```

Para más detalles sobre el flujo de contribución consulte `CONTRIBUTING.md`.

---

# Entorno virtual en Linux/macOS

Crear el entorno virtual:

```bash
python -m venv .venv
```

Activarlo:

```bash
source .venv/bin/activate
```

Cuando el entorno esté activo, la terminal mostrará un prefijo similar a:

```text
(.venv)
```

---

# Entorno virtual en Windows

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Activar en PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Activar en CMD:

```cmd
.venv\Scripts\activate
```

Cuando el entorno esté activo, la terminal mostrará un prefijo similar a:

```text
(.venv)
```

---

# Instalación con pip

Desde el directorio raíz del proyecto ejecutar:

```bash
pip install -e .
```

La opción `-e` (*editable*) instala el proyecto enlazándolo al código fuente local. Esto permite que los cambios realizados en el proyecto se reflejen inmediatamente sin necesidad de reinstalar el paquete.

---

# Dependencias de desarrollo (opcional)

Para instalar herramientas adicionales utilizadas durante el desarrollo:

```bash
pip install -r requirements-dev.txt
```

Estas dependencias incluyen herramientas para pruebas, validación de código y automatización de tareas de desarrollo.

---

# Verificar la instalación

Verificar que el comando de Escuadra esté disponible:

```bash
escuadra --help
```

o consultar la versión instalada:

```bash
escuadra --version
```

También puede verificarse mediante:

```bash
python -m escuadra --help
```

Si la instalación fue exitosa, el comando mostrará la ayuda de la aplicación o la versión instalada.

---

# Ejecución

Mostrar la ayuda general de la aplicación:

```bash
escuadra --help
```

También es posible ejecutar el paquete directamente:

```bash
python -m escuadra
```

---

# Desactivar el entorno virtual

Cuando finalice su sesión de trabajo:

```bash
deactivate
```

---

# Problemas comunes

## El comando `python` no es reconocido

Verifique que Python esté instalado correctamente y agregado al PATH del sistema.

## El comando `pip` no es reconocido

Reinstale Python asegurándose de habilitar la opción:

```text
Add Python to PATH
```

durante la instalación.

## El comando `escuadra` no funciona

Verifique que:

1. El entorno virtual esté activo.
2. La instalación se haya realizado correctamente.
3. Se haya ejecutado:

```bash
pip install -e .
```

## Error por dependencias faltantes

Reinstale las dependencias del proyecto:

```bash
pip install -e .
```

---

# Documentación relacionada

* README.md
* CONTRIBUTING.md
* docs/arquitectura.md
* pyproject.toml
