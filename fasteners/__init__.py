from . import cli

from pint import UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

if __name__ == '__main__':
    cli.hello()
