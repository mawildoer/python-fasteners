from . import ureg, Q_

import re
import pint


def root_unit(dim):
    uc = pint.registry.UnitsContainer({dim: 1})
    return next(ureg.get_root_units(unit)[1] for unit in ureg if ureg.get_dimensionality(unit) == uc)


def parse(s, default_unit):
    units_re = re.compile("[a-zA-Z%]+/?")
    nominal, *tolerance = units_re.sub("", s).split("+/-")
    if not tolerance:
        tolerance = None
    else:
        tolerance = float(tolerance[0])
    units = units_re.findall(s) or [default_unit]

    nominal = Q_(float(nominal), units[0])

    if tolerance is None:
        return nominal
    else:
        if len(units) == 2:
            if units[1] == "%":
                return nominal.plus_minus(tolerance/100.0, relative=True)
            else:
                tolerance = Q_(tolerance, units[-1])
                return nominal.plus_minus(tolerance.to(nominal.units))
        else:
            return nominal.plus_minus(tolerance)

