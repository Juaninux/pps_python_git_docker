# pps_python_git_docker
Repositorio para la creación de una aplicación tipo galleta de la suerte/servilleta de bar.
Cada vez que accedes muestra un mensaje auspicioso aleatorio.

Práctica ideada para practicar:

- Docker
- Python (venv)
- Git y Github.

Contributors: Juan Carrasco Milla y Víctor Manuel Andreu.

# v02 - entorno aislado aislada

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

## Ejecutar la aplicación
```bash
source venv/bin/activate
python app.py
```
# v03 - Flask


## Endpoints

* GET / -> devuelve "Hola, mundo"
* GET /frotar/<n_frases> -> devuelve JSON con n_frases frases auspiciosas

# v04  Docker

### Build
```bash
docker build -t bayeta:docker .
```

### Run

```bash
docker run --rm -p 5000:5000 --name bayeta bayeta:docker
```

### Probar

```bash
curl http://localhost:5000/
curl http://localhost:5000/frotar/3
```


# v05 Persistencia con MongoDB

A partir de esta versión, las frases auspiciosas se almacenan en MongoDB en lugar de en memoria o en fichero de texto.

La aplicación utiliza el driver oficial `pymongo` para conectarse a la base de datos.

---

## Estructura de la base de datos

- Base de datos: `bayeta`
- Colección: `frases_auspiciosas`
- Cada documento tiene el formato:

```json
{
  "_id": ObjectId(...),
  "frase": "Texto de la frase"
}
```

# v06 Despliegue con Docker Compose

Levantar todos los servicios:

```bash
docker compose up --build
```

Detener servicios:

```bash
docker compose down
```

La aplicación quedará disponible en:

[http://localhost:5000](http://localhost:5000)

# v07 Añadido volúmen persistente

# v08 Añadida función POST para introducir frases

Uso:

```bash
curl -i -X POST http://localhost:5000/frotar/add \
  -H "Content-Type: application/json" \
  -d '{"frases":["Frase nueva 1","Frase nueva 2"]}'
```

