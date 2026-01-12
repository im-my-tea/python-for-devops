from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from the Cloud!"}

@app.get("/user/{username}")
def get_user(username: str):
    return {"user": username, "status": "active"}

@app.get("/cpu")
def get_cpu():
    # Returns a float representing percentage
    usage = psutil.cpu_percent(interval=1)
    return {"cpu_usage": usage, "status": "nominal" if usage < 80 else "warning"}

@app.get("/ram")
def get_ram():
    # Returns a named tuple with memory stats
    memory = psutil.virtual_memory()
    return {
        "total_gb": round(memory.total / (1024**3), 2),
        "available_gb": round(memory.available / (1024**3), 2),
        "percent": memory.percent
    }