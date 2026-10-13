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
def update_servers(server_name: str, status: str, ip: str | None = None, os: str | None = None, role: str | None = None) -> ServerDict:
    if server_name in server_store:
        server_store[server_name]["status"] = status
        server_store[server_name]["ip"] = ip
        server_store[server_name]["os"] = os
        server_store[server_name]["role"] = role
    else:
        raise ValueError(f"Server '{server_name}' not found in the store.")

    return server_store

    