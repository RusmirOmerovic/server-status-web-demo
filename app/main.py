from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.core import get_servers, add_server, update_servers

app = FastAPI()

# Datenmodell für Server
class ServerCreate(BaseModel):
    server_name: str
    ip: str
    os: str
    role: str

# Startpoint for the FastAPI application
@app.get("/")
def root():
    return {"status": "Server Status API running"}

# GET endpoint to retrieve the server status
@app.get("/servers")
def read_servers():
    return get_servers()

# POST endpoint to create a new server
@app.post("/servers", status_code=201)
def create_server(server: ServerCreate):
    created = add_server(
        server.server_name,
        server.ip,
        server.os,
        server.role,
    )

    if not created:
        raise HTTPException(
            status_code=409,
            detail=f"Server '{server.server_name}' already exists.",
        )

    return {
        "message": f"Server '{server.server_name}' created successfully.",
        "server": get_servers()[server.server_name]
    }
