import requests

from ...static import SERVERS
from ..utils.Module import Module
from .Network import network


class Servers(Module):
    """Class to manage and check the availability of servers"""

    def __init__(self) -> None:
        """Initialize with a list of server URLs"""
        super().__init__()
        self.servers = SERVERS

    def check_servers(self) -> str:
        """Check the servers for availability and return the first accessible server"""
        for server in self.servers[:]:
            try:
                r = network.get(f'https://{server}/')
                self.debug(f'Server {server} responds with {r.status_code}')

                self.debug(f'Using {server} server')
                return f'https://{server}/'
            except requests.exceptions.RequestException:
                self.info(f"The server {server} is down/inaccessible")
                self.servers.remove(server)

        return 'https://google.com/'


servers = Servers()