import sympy as sp


def assert_zero(expression, label):
    residual = sp.trigsimp(sp.simplify(expression), method="fu")
    expected = sp.zeros(*residual.shape) if isinstance(residual, sp.MatrixBase) else 0
    if residual != expected:
        raise AssertionError(f"{label} did not simplify to zero: {residual}")
    print(f"PASS: {label}")


theta1, theta2 = sp.symbols("theta1 theta2", real=True)
omega1, omega2 = sp.symbols("omega1 omega2", real=True)
alpha1, alpha2 = sp.symbols("alpha1 alpha2", real=True)
mass1, mass2, length1, length2, gravity = sp.symbols(
    "m1 m2 l1 l2 g", positive=True, real=True
)
reaction1, reaction2 = sp.symbols("R1 R2", real=True)
q = sp.Matrix([theta1, theta2])
qdot = sp.Matrix([omega1, omega2])
qddot = sp.Matrix([alpha1, alpha2])
delta = theta1 - theta2

unit1 = sp.Matrix([sp.sin(theta1), -sp.cos(theta1)])
unit2 = sp.Matrix([sp.sin(theta2), -sp.cos(theta2)])
tangent1 = sp.Matrix([sp.cos(theta1), sp.sin(theta1)])
tangent2 = sp.Matrix([sp.cos(theta2), sp.sin(theta2)])
vertical = sp.Matrix([0, 1])
position1 = length1 * unit1
position2 = position1 + length2 * unit2
positions = [position1, position2]
velocities = [position.jacobian(q) * qdot for position in positions]
accelerations = [
    velocity.jacobian(q) * qdot + velocity.jacobian(qdot) * qddot
    for velocity in velocities
]

kinetic = sp.Rational(1, 2) * (
    mass1 * velocities[0].dot(velocities[0])
    + mass2 * velocities[1].dot(velocities[1])
)
potential = gravity * (mass1 * position1[1] + mass2 * position2[1])
lagrangian = kinetic - potential
momentum = sp.Matrix([sp.diff(lagrangian, speed) for speed in qdot])
momentum_rate = momentum.jacobian(q) * qdot + momentum.jacobian(qdot) * qddot
lagrange_residual = momentum_rate - sp.Matrix(
    [sp.diff(lagrangian, coordinate) for coordinate in q]
)
mass_matrix = lagrange_residual.jacobian(qddot)
bias = sp.simplify(lagrange_residual - mass_matrix * qddot)

expected_mass = sp.Matrix(
    [
        [(mass1 + mass2) * length1**2, mass2 * length1 * length2 * sp.cos(delta)],
        [mass2 * length1 * length2 * sp.cos(delta), mass2 * length2**2],
    ]
)
expected_bias = sp.Matrix(
    [
        mass2 * length1 * length2 * sp.sin(delta) * omega2**2
        + (mass1 + mass2) * gravity * length1 * sp.sin(theta1),
        -mass2 * length1 * length2 * sp.sin(delta) * omega1**2
        + mass2 * gravity * length2 * sp.sin(theta2),
    ]
)
assert_zero(mass_matrix - expected_mass, "Euler-Lagrange mass matrix")
assert_zero(bias - expected_bias, "Euler-Lagrange bias vector")

force1 = (
    mass1 * accelerations[0]
    + reaction1 * unit1
    - reaction2 * unit2
    + mass1 * gravity * vertical
)
force2 = (
    mass2 * accelerations[1]
    + reaction2 * unit2
    + mass2 * gravity * vertical
)
newton_projection = sp.Matrix(
    [
        length1 * tangent1.dot(force1 + force2),
        length2 * tangent2.dot(force2),
    ]
)
assert_zero(
    newton_projection - lagrange_residual,
    "Newton-Euler tangent projection equals Euler-Lagrange residual",
)

jacobians = [position.jacobian(q) for position in positions]
virtual_work_residual = sum(
    (
        jacobian.T
        * (mass * acceleration + mass * gravity * vertical)
        for jacobian, mass, acceleration in zip(
            jacobians, [mass1, mass2], accelerations
        )
    ),
    sp.zeros(2, 1),
)
assert_zero(
    virtual_work_residual - lagrange_residual,
    "d'Alembert virtual-work residual equals Euler-Lagrange residual",
)

partial_velocities = [jacobian for jacobian in jacobians]
kane_residual = sp.zeros(2, 1)
for jacobian, mass, acceleration in zip(
    partial_velocities, [mass1, mass2], accelerations
):
    active_force = jacobian.T * (-mass * gravity * vertical)
    inertia_force = -jacobian.T * (mass * acceleration)
    kane_residual += active_force + inertia_force
assert_zero(
    kane_residual + lagrange_residual,
    "Kane generalized-force equations equal Euler-Lagrange equations",
)

canonical_momenta = expected_mass * qdot
phase_momenta = sp.Matrix(sp.symbols("p1 p2", real=True))
hamiltonian = (
    (phase_momenta.T * expected_mass.inv() * phase_momenta)[0] / 2 + potential
)
velocity_from_hamiltonian = sp.Matrix(
    [sp.diff(hamiltonian, p) for p in phase_momenta]
)
substitution = dict(zip(phase_momenta, canonical_momenta))
assert_zero(
    velocity_from_hamiltonian.subs(substitution) - qdot,
    "Hamilton equation for q recovers qdot",
)
phase_force = sp.Matrix([sp.diff(hamiltonian, coordinate) for coordinate in q])
canonical_momentum_rate = (
    canonical_momenta.jacobian(q) * qdot
    + canonical_momenta.jacobian(qdot) * qddot
)
assert_zero(
    canonical_momentum_rate + phase_force.subs(substitution) - lagrange_residual,
    "Hamilton momentum equation equals Euler-Lagrange residual",
)

angular_acceleration = mass_matrix.LUsolve(-bias)
reaction2_expression = mass2 * (
    length1 * sp.sin(delta) * angular_acceleration[0]
    + length1 * sp.cos(delta) * omega1**2
    + length2 * omega2**2
    + gravity * sp.cos(theta2)
)
reaction1_expression = (
    mass1 * length1 * omega1**2
    + reaction2_expression * sp.cos(delta)
    + mass1 * gravity * sp.cos(theta1)
)
substitutions = {
    alpha1: angular_acceleration[0],
    alpha2: angular_acceleration[1],
    reaction1: reaction1_expression,
    reaction2: reaction2_expression,
}
assert_zero(force1.subs(substitutions), "recovered mass-1 force balance")
assert_zero(force2.subs(substitutions), "recovered mass-2 force balance")
print("All double-pendulum formulation checks passed.")
