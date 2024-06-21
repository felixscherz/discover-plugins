import argparse
import sys
import subprocess

from importlib.metadata import entry_points


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name")
    parser.add_argument("--value")
    parser.add_argument("--group")

    options = parser.parse_args()
    print(discover(name=options.name, value=options.value, group=options.group))


def discover(name: str | None = None, value: str | None = None, group: str | None = None):
    kwargs = {}
    if name:
        kwargs.update(name=name)
    if value:
        kwargs.update(value=value)
    if group:
        kwargs.update(group=group)
    eps = entry_points(**kwargs)
    return eps

def source():
    import inspect
    this = sys.modules[__name__]
    code = inspect.getsource(this)
    return code

def inject():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name")
    parser.add_argument("--value")
    parser.add_argument("--group")
    parser.add_argument("--interpreter")


    options = parser.parse_args()
    if options.interpreter:
        code = source()
        stdout = subprocess.run([options.interpreter, "-c", code])
        print(stdout.stdout)
        raise SystemExit(stdout.returncode)

    print(discover(name=options.name, value=options.value, group=options.group))

if __name__ == "__main__":
    main()
