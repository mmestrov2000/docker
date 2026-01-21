# 1. Baza: Sluzbeni Python image
FROM python:3.11-slim

# 2. Radni direktorij u containeru
WORKDIR /app

# 3. Instalacija ovisnosti
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kopiranje koda aplikacije
COPY app.py .

# 5. Otkrivanje porta
EXPOSE 5000

# 6. Postavljanje varijable okruženja
ENV APP_ENV=container

# 7. Komanda za pokretanje
CMD ["python", "app.py"]
