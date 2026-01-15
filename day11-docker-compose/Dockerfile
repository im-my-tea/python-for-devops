FROM python:3.9-slim

# 1. Force logs to show instantly
ENV PYTHONUNBUFFERED=1

# 2. Create folder
WORKDIR /app

# 3. Copy requirements first
COPY requirements.txt .

# 4. Install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the app
COPY . .

# 6. Run the app
CMD ["python", "main.py"]