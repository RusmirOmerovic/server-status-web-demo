from typing import TypeAlias

# constant for server data type
ServerData: TypeAlias = dict[str, str | None]
ServerDict: TypeAlias = dict[str, ServerData]

SERVERS = {"web1", "web2", "db1"}


#Server initialization function
def init_servers(servers: list[str]) -> ServerDict:
    server_dict: ServerDict = {}

    for server in servers:
        server_dict[server] = {
            "status": "offline",
            "ip": None,
            "os": None,
            "role": None,
        }

    return server_dict

# Initialize the server store
server_store = init_servers(SERVERS)

# get servers from the server store
def get_servers() -> ServerDict:
    return server_store

# add a new server to the server store
def add_server(
        server_name: str,
        ip: str,
        os_name: str,
        role: str,
) -> bool:
    if server_name in server_store:
        return False  # Server already exists

    server_store[server_name] = {
        "status": "offline",
        "ip": ip,
        "os": os_name,
        "role": role,
    }
    return True       

# update servers in server store
def update_server(
        server_name: str,
        ip: str | None = None, 
        os: str | None = None, 
        role: str | None = None
) -> bool:
    if server_name not in server_store:
        return False  # Server does not exist

    if ip is not None:
        server_store[server_name]["ip"] = ip
    if os is not None:
        server_store[server_name]["os"] = os
    if role is not None:
        server_store[server_name]["role"] = role

    return True

# Server status update function
def toggle_status(server_name: str) -> bool:
    if server_name not in server_store:
        return False  # Server does not exist

    current_status = server_store[server_name]["status"]

    if current_status == "offline":
        server_store[server_name]["status"] = "online"
    else:
        server_store[server_name]["status"] = "offline"

    return True


# Delete server function
def remove_server(server_name: str) -> bool:
    if server_name not in server_store:
        return False

    del server_store[server_name]
    return True