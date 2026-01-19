from fastapi import FastAPI
import time

app = FastAPI()

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

@app.get("/")
def home():
    return {"message": "Golden Image Factory v1.0"}

@app.get("/check/{number}")
def check_prime(number: int):
    start = time.time()
    result = is_prime(number)
    duration = time.time() - start
    return {
        "number": number,
        "is_prime": result,
        "calc_time": f"{duration:.6f}s"
    }