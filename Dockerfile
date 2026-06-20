# 1. Imagem base do Python
FROM python:3.10-slim

# 2. Define o diretório de trabalho
WORKDIR /app

# 3. Copia o arquivo de dependências primeiro (para aproveitar o cache do Docker)
COPY requirements.txt .

# 4. Instala as dependências (incluindo o gunicorn se não estiver no seu arquivo)
RUN pip install --no-cache-dir -r requirements.txt && pip install gunicorn

# 5. Copia o resto do seu projeto (controllers, templates, models...)
COPY . .

# 6. Expõe a porta interna que o Gunicorn vai rodar
EXPOSE 5000

# 7. Comando para rodar o app com Gunicorn
# Substitua 'app:app' por 'nome_do_seu_arquivo_principal:nome_da_instancia_flask'
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]