from dagster import Definitions
from .assets.hello import hello
from .assets.world import world

defs = Definitions(assets=[hello, world])
