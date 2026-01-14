import fastapi
import os

app = fastapi.FastAPI()

@app.get("/logs")
def logs():
    files = os.listdir("logs_backup")
    return {"files": files}

@app.get("/logs/{filename}")
def name(filename: str):
    path = os.path.join("logs_backup", filename)
    
    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()
        return {"contents": content}
    else:
        return {"error": "File not found"}
