from dagster import build_asset_context
from dagster_hello_world.assets.hello import hello

def test_hello():
    context = build_asset_context()
    result = hello(context)
    assert result == ["Hello!"]
