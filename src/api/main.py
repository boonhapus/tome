from __future__ import annotations
import logging
import os

from litestar.static_files.config import StaticFilesConfig
from sqlalchemy.engine import Connection
from litestar.di import Provide
from litestar import Litestar, Controller, get, post

from api import _dependency

if os.getenv("CI") is None:
    from dotenv import load_dotenv
    load_dotenv()

    BUILD_DIRECTORIES = ["./build"]
else:
    BUILD_DIRECTORIES = [""]

log = logging.getLogger(__name__)


class MantleOfIntelligence(Controller):
    """All the API endpoints associated with receiving data."""
    path = "/mantle"
    dependencies = {"cnxn": Provide(_dependency.get_database_connection)}

    @post(path="/fetch/{match_id:int}")
    async def fetch_match_id(self, match_id: int, *, cnxn: Connection) -> None:
        """UPSERT runtime environment into the Database."""
        # cnxn.execute(statement=...)
        pass


@get(path="/random")
async def _random() -> int:
    import random
    return random.randint(0, 100)


app = Litestar(
    route_handlers=[_random, MantleOfIntelligence],
    static_files_config=[StaticFilesConfig(directories=BUILD_DIRECTORIES, path="/", html_mode=True)],
)
