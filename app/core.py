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