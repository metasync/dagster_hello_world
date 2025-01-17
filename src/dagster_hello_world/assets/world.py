from dagster import asset, AssetExecutionContext
from .hello import hello

@asset(deps=[hello])
def world(context: AssetExecutionContext):
    context.log.info("World!")
    return ["World!"]
