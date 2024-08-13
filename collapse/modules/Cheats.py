import os

from rich.markup import escape

from ..modules.Module import Module
from ..static import SHOW_HIDDEN_CHEATS
from .network.API import api
from .storage.Cache import cache
from .Cheat import Cheat
from .storage.Data import data


class CheatManager(Module):
    """Class to manage and load cheats from the API"""

    def __init__(self) -> None:
        super().__init__()
        self.cheats = []
        self._load_cheats()

    def _load_cheats(self) -> list:
        """Load cheats from the API and return a list of Cheat instances"""
        clients = api.get('clients')
        cheats = []

        if clients is not None:
            cache.save(clients.json())
            self.make_array(clients.json())

        else:
            if not os.path.exists(cache.path):
                self.error('No clients cache found')

            else:
                c = cache.get()
                creation_time = c['_meta']['creation_time']
                self.info(f"Using latest clients cache ({creation_time})")

                self.make_array(c['clients'])

        return cheats

    def cheat_line(self, cheat) -> str:
        """Сreates a line to display the cheat"""
        return f"""{escape(cheat["name"])}{(" [red bold][-][/]" if not cheat["working"] else "")}"""

    def make_array(self, cheats: dict) -> None:
        """Adds clients to array"""
        for cheat in cheats:
            if cheat["show_in_loader"] or SHOW_HIDDEN_CHEATS:
                self.cheats.append(
                    Cheat(
                        name=self.cheat_line(cheat),
                        link=data.get_url(cheat["filename"]),
                        main_class=cheat["main_class"],
                        version=cheat["version"],
                        category=cheat["category"],
                        internal=cheat["internal"],
                        id=cheat["id"],
                    )
                )

cheat_manager = CheatManager()
