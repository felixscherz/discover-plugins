import subprocess
import sys

import pytest


@pytest.fixture
def interpreter(tmp_path):
    path = tmp_path / "venv"
    out = subprocess.run([sys.executable, "-m", "virtualenv", path.as_posix()])
    assert out.returncode == 0
    return path / "bin/python"


def test_discover_plugins_for_specified_interpreter(interpreter):
    out = subprocess.run([interpreter, "-m", "pip", "install", "./testdata/packages/myplugin"])
    out = subprocess.run(["discover-plugins", "--interpreter", interpreter])
    print(out.stdout)
    assert out.returncode == 0
