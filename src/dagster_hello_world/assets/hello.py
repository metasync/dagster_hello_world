from dagster import asset, AssetExecutionContext

@asset
def hello(context: AssetExecutionContext):
    context.log.info("Hello!")
    return ["Hello!"]
