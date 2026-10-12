from fastapi import FastAPI
from app.core import get_servers
app = FastAPI()

@app.get("/")
def root():
    return {"status": "Server Status API running"}

@app.get("/servers")
def read_servers():
    return get_servers()