# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt y lo instala
COPY fast-api-backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de tu aplicación
COPY fast-api-backend/main.py ./
COPY fast-api-backend/utils ./utils

# Copia el frontend construido
COPY random_name_frontend/build ../random_name_frontend/build

# Expone el puerto en el que la aplicación escuchará
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
