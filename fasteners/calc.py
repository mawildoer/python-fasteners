import sympy

# Calculation based on NASA-STD-5020A

preload_initial_nominal = sympy.symbols("preload_initial_nominal")  # pg. 13
preload_scatter = sympy.symbols("preload_scatter")  # 25% for lubricated fasteners, 35% for as received, pg. 25

c_max = sympy.symbols("c_max")  # tolerance range max (1.05 for +/-5%), pg. 22
c_min = sympy.symbols("c_min")  # tolerance range min (0.95 for +/-5%), pg. 22

n_f = sympy.symbols("n_f")  # the number of fasteners in a joint, must be 1 if the joint is separation critical

preload_initial_max = c_max * (1+preload_scatter) * preload_initial_nominal
# "Separation critical" calculation (pg. 22) neglected as it's equivalent for 1 fastener
preload_initial_min = c_min * (1-preload_scatter/n_f**0.5) * preload_initial_nominal

relaxation_factor = sympy.symbols("relaxation_factor")  # expected at 5% for single faying surface joints, pg. 22

preload_max = preload_initial_max  # recalculate at a edges of operational temperature ranges
preload_min = preload_initial_min * (1 - relaxation_factor)  # recalculate at a edges of operational temperature ranges
