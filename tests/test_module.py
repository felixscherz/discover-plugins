import inspect
import sys
import discover_plugins
def test_module():


    print(inspect.getsource(discover_plugins))

    assert True


def test_other():
    print(discover_plugins.source())
