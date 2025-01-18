from dagster import asset, AssetExecutionContext
from dagster_hello_world.assets.hello import hello

@asset(deps=[hello])
def world(context: AssetExecutionContext):
    context.log.info("World!")
    return ["World!"]
