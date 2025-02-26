FROM python:3.12.6

WORKDIR /app

# Copiem toate fisierele necesare
COPY . /app

# Instalăm dependențele fără a copia tot codul (pentru caching)
RUN pip install --no-cache-dir -r requirements.txt

# Setăm PYTHONPATH pentru a include `src/`
ENV PYTHONPATH="/app/src"

# Expunem portul 80
EXPOSE 80

CMD ["python", "src/testam/main.py"]
