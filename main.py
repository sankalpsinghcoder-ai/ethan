from fastapi import FastAPI

app = FastAPI()   # ← THIS LINE IS REQUIRED

@app.get("/")
def home():
    return {"status": "running"}
