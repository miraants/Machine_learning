FROM python:3.10

# Installer les dépendances système pour pyodbc
RUN apt-get update && \
    apt-get install -y \
        gcc \
        g++ \
        unixodbc \
        unixodbc-dev \
        libodbc1 \
        curl \
        gnupg && \
    rm -rf /var/lib/apt/lists/*

# Installer le Microsoft ODBC Driver pour SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port pour Render
EXPOSE 8000

# Lancer l'API
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
