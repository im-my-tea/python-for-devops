# 1. Start with a lightweight Linux + Python base
FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

# 2. Create a folder inside the container
WORKDIR /app

# 3. Copy the requirements file first (for caching speed)
COPY requirements.txt .

# 4. Install the libraries inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your code
COPY . .

# 6. The command to run when the container starts
CMD ["python", "main.py"]