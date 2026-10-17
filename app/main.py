from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.core import (
    get_servers, 
    add_server, 
    update_server, 
    toggle_status,
    remove_server,
)

app = FastAPI()

# Datenmodelle für Server
class ServerCreate(BaseModel):
    server_name: str
    ip: str
    os: str
    role: str

class ServerUpdate(BaseModel):
    ip: str | None = None
    os: str | None = None
    role: str | None = None

# Startpoint for the FastAPI application
@app.get("/")
def root():
    return {"status": "Server Status API running"}


# ENDPOINTS 
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

# PATCH endpoint to update an existing server
@app.patch("/servers/{server_name}")
def patch_server(server_name: str, server: ServerUpdate):
    updated = update_server(
        server_name,
        ip=server.ip,
        os=server.os,
        role=server.role,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail=f"Server '{server_name}' not found.",
        )

    return {
        "message": f"Server '{server_name}' updated successfully.",
        "server": get_servers()[server_name]
    }

# POST endpoint to toggle the status of a server
@app.post("/servers/{server_name}/toggle")
def toggle_server_status(server_name: str):
    toggled = toggle_status(server_name)

    if not toggled:
        raise HTTPException(
            status_code=404,
            detail=f"Server '{server_name}' not found.",
        )

    return {
        "message": f"Server '{server_name}' status toggled successfully.",
        "server": get_servers()[server_name]
    }

# DELETE endpoint to remove a server
@app.delete("/servers/{server_name}")
def delete_server(server_name: str):
    removed = remove_server(server_name)

    if not removed:
        raise HTTPException(
            status_code=404,
            detail=f"Server '{server_name}' not found."
        )

    return {
        "message": f"Server '{server_name}' deleted successfully."
    }