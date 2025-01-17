from dagster import build_asset_context
from dagster_hello_world.assets.world import world

def test_world():
    context = build_asset_context()
    result = world(context)
    assert result == ["World!"]
