import sympy

# Calculation based on NASA-STD-5020A

locking_torque = sympy.symbols("locking_torque")  # 0-x N.m, depending on locking feature
applied_torque = sympy.symbols("applied_torque")
torque = applied_torque - locking_torque

nut_factor = sympy.symbols("nut_factor")
fastener_diameter = sympy.symbols("fastener_diameter")

preload_scatter = sympy.symbols("preload_scatter")  # 25% for lubricated fasteners, 35% for as received, pg. 25

# the number of fasteners in a joint, must be 1 if the joint is separation critical
fastener_count = sympy.symbols("fastener_count")

# "Separation critical" calculation (pg. 22) neglected as it's equivalent for 1 fastener
preload_initial = (preload_scatter/(fastener_count**0.5)) * torque / nut_factor / fastener_diameter

relaxation_factor = sympy.symbols("relaxation_factor")  # expected at 5% for single faying surface joints, pg. 22

preload = preload_initial * relaxation_factor

n = sympy.symbols("load_introduction_factor")

# Fastener stiffnesses from: https://faculty.mercer.edu/jenkins_he/documents/MAE322Bolts2.pdf
fastener_material_E = sympy.symbols("fastener_material_E")
stackup_length = sympy.symbols("stackup_length")
fastener_shoulder_diameter = sympy.symbols("fastener_shoulder_diameter")
fastener_shoulder_area = sympy.pi * (fastener_shoulder_diameter/2)**2
fastener_tensile_area = sympy.symbols("fastener_tensile_area")
fastener_unthreaded_length = sympy.symbols("fastener_unthreaded_length")
fastener_threaded_length = stackup_length - fastener_unthreaded_length  # fastener_threaded_length
fastener_stiffness = fastener_shoulder_area * fastener_tensile_area * fastener_material_E / \
                     (fastener_shoulder_area * fastener_threaded_length +
                      fastener_tensile_area * fastener_unthreaded_length)
clamped_stiffness = sympy.symbols("clamped_stiffness")
