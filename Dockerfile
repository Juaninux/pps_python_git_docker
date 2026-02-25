# Fase 1: resolución de dependencias
FROM python:3.12-slim AS deps
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Fase 2: ejecución
FROM python:3.12-slim AS runtime
WORKDIR /app

# Copiamos las librerías instaladas desde la fase deps
COPY --from=deps /usr/local /usr/local

# Copiamos el código de la aplicación
COPY app.py bayeta.py frases.txt ./

EXPOSE 5000

CMD ["python", "app.py"]
