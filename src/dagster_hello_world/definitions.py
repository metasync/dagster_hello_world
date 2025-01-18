from dagster import Definitions
from dagster_hello_world.assets.hello import hello
from dagster_hello_world.assets.world import world

defs = Definitions(assets=[hello, world])
