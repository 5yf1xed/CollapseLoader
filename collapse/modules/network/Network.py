import requests

from ...arguments import args
from ..utils.Module import Module


class Network(Module):
    """Module for network operations"""

    def __init__(self):
        super().__init__()
        
        self.session = requests.Session()
        self.timeout = args.timeout if args.timeout else 1

    def get(self, url, params=None, headers=None, stream=False):
        """Make a GET request to the given URL"""
        try:
            response = self.session.get(url, params=params, headers=headers, stream=stream, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            self.error(f"An error occurred: {e}")
            raise e
 
    def close(self):
        self.session.close()

network = Network()