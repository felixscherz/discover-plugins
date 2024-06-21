import subprocess
import sys
from pathlib import Path

import pytest


def create_virtualenv(path: Path):
    out = subprocess.run([sys.executable, "-m", "virtualenv", path.as_posix()])
    return path / "bin/python"

def test_install(tmp_path):
    path = Path("./testdata/packages/myplugin")
    venv_path = tmp_path / "venv"
    interpreter = create_virtualenv(venv_path)
    out = subprocess.run([interpreter, "-m", "pip", "install", "."])
    with open("./discover_plugins.py") as handle:
        code = handle.read()
    out = subprocess.run([interpreter, "-c", code])
    print(out)


def test_install_and_find_code(tmp_path):
    path = Path("./testdata/packages/myplugin")
    venv_path = tmp_path / "venv"
    interpreter = create_virtualenv(venv_path)
    out = subprocess.run([interpreter, "-m", "pip", "install", "."])
    with open("./discover_plugins.py") as handle:
        code = handle.read()
    out = subprocess.run([interpreter, "-c", code])
    print(out)


def test_install_and_find_code2(tmp_path):
    path = Path("./testdata/packages/myplugin")
    venv_path = tmp_path / "venv"
    interpreter = create_virtualenv(venv_path)
    out = subprocess.run([interpreter, "-m", "pip", "install", "."])
    out = subprocess.run(["discover-plugins", "--interpreter", interpreter])
    print(out)
    assert out.returncode == 0


def test_find_code():
    print(__file__)
