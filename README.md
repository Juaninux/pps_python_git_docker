# pps_python_git_docker
Repositorio para la creación de una aplicación tipo galleta de la suerte/servilleta de bar.
Cada vez que accedes muestra un mensaje auspicioso aleatorio.

Práctica ideada para practicar:

- Docker
- Python (venv)
- Git y Github.

Contributors: Juan Carrasco Milla y Víctor Manuel Andreu.

v02

## Requisitos
- Python 3

## Crear entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate
```
## Instalar dependencias
```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación (Flask)
```bash
source venv/bin/activate
python app.py
```

## Endpoints

* GET / -> devuelve "Hola, mundo"
* GET /frotar/<n_frases> -> devuelve JSON con n_frases frases auspiciosas
