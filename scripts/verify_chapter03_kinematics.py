import sympy as sp


def assert_zero(expression, label):
    residual = sp.trigsimp(sp.simplify(expression), method="fu")
    if isinstance(residual, sp.MatrixBase):
        is_zero = residual == sp.zeros(*residual.shape)
    else:
        is_zero = residual == 0
    if not is_zero:
        raise AssertionError(f"{label} failed: {residual}")
    print(f"PASS: {label}")


def circle_intersection(center_a, radius_a, center_b, radius_b, branch):
    displacement = center_b - center_a
    distance = sp.sqrt(displacement.dot(displacement))
    along = (radius_a**2 - radius_b**2 + distance**2) / (2 * distance)
    height_squared = radius_a**2 - along**2
    normal = sp.Matrix([-displacement[1], displacement[0]]) / distance
    point = center_a + along * displacement / distance + branch * sp.sqrt(height_squared) * normal
    return point, distance, along, height_squared


length1, length2 = sp.symbols("L1 L2", positive=True, real=True)
theta1, theta2 = sp.symbols("theta1 theta2", real=True)
coordinate = sp.Matrix([theta1, theta2])
unit1 = sp.Matrix([sp.sin(theta1), -sp.cos(theta1)])
unit2 = sp.Matrix([sp.sin(theta2), -sp.cos(theta2)])
tangent1 = sp.Matrix([sp.cos(theta1), sp.sin(theta1)])
tangent2 = sp.Matrix([sp.cos(theta2), sp.sin(theta2)])
pivot = sp.zeros(2, 1)
mass1_position = pivot + length1 * unit1
mass2_position = mass1_position + length2 * unit2
mass_position_jacobian = mass2_position.jacobian(coordinate)
expected_jacobian = sp.Matrix.hstack(length1 * tangent1, length2 * tangent2)
assert_zero(mass_position_jacobian - expected_jacobian, "double-pendulum forward Jacobian")
assert_zero(
    sp.det(mass_position_jacobian) + length1 * length2 * sp.sin(theta1 - theta2),
    "double-pendulum Jacobian determinant",
)

x_target, y_target = sp.symbols("x_target y_target", real=True)
target = sp.Matrix([x_target, y_target])
branch = sp.symbols("branch", real=True)
distance_squared = sp.expand(target.dot(target))
distance = sp.sqrt(distance_squared)
projection = (length1**2 - length2**2 + distance_squared) / (2 * distance)
height_squared = length1**2 - projection**2
unit_target = target / distance
perpendicular_target = sp.Matrix([-y_target, x_target]) / distance
elbow = projection * unit_target + branch * sp.sqrt(height_squared) * perpendicular_target
assert_zero(
    (elbow.dot(elbow) - length1**2).subs(branch, 1),
    "double-pendulum inverse first-link length",
)
assert_zero(
    ((target - elbow).dot(target - elbow) - length2**2).subs(branch, -1),
    "double-pendulum inverse second-link length",
)

lengths = sp.symbols("L1 L2 L3 L4 L5", positive=True, real=True)
L1, L2, L3, L4, L5 = lengths
alpha1, alpha5 = sp.symbols("alpha1 alpha5", real=True)
alpha1_rate, alpha5_rate = sp.symbols("alpha1_rate alpha5_rate", real=True)
branch_middle = sp.symbols("branch_middle", real=True)
anchor34 = sp.Matrix([0, 0])
anchor45 = sp.Matrix([L4, 0])
axis1 = sp.Matrix([sp.cos(alpha1), sp.sin(alpha1)])
axis5 = sp.Matrix([sp.cos(alpha5), sp.sin(alpha5)])
pin51_forward = anchor45 + L5 * axis5
pin12_forward = pin51_forward + L1 * axis1
normal1 = sp.Matrix([-sp.sin(alpha1), sp.cos(alpha1)])
normal5 = sp.Matrix([-sp.sin(alpha5), sp.cos(alpha5)])
five_link_target_jacobian = sp.Matrix.hstack(L1 * normal1, L5 * normal5)
assert_zero(
    pin12_forward.jacobian(sp.Matrix([alpha1, alpha5])) - five_link_target_jacobian,
    "five-link target-pin forward Jacobian",
)
assert_zero(
    five_link_target_jacobian.det() - L1 * L5 * sp.sin(alpha5 - alpha1),
    "five-link target-pin Jacobian determinant",
)
pin23_forward, distance23, along23, height23_squared = circle_intersection(
    pin12_forward, L2, anchor34, L3, branch_middle
)
assert_zero(
    ((pin23_forward - pin12_forward).dot(pin23_forward - pin12_forward) - L2**2).subs(branch_middle, 1),
    "five-link forward link-2 closure",
)
assert_zero(
    ((pin23_forward - anchor34).dot(pin23_forward - anchor34) - L3**2).subs(branch_middle, -1),
    "five-link forward link-3 closure",
)
local_along, local_distance, local_height = sp.symbols(
    "local_along local_distance local_height", real=True
)
local_d2 = sp.Matrix([local_along, branch_middle * local_height])
local_d3 = sp.Matrix([local_along - local_distance, branch_middle * local_height])
local_velocity_matrix = sp.Matrix.vstack(local_d2.T, local_d3.T)
assert_zero(
    (local_velocity_matrix.det() - branch_middle * local_distance * local_height).subs(branch_middle, 1),
    "five-link middle-pin velocity singularity factor",
)
assert_zero(
    (pin51_forward - anchor45).dot(pin51_forward - anchor45) - L5**2,
    "five-link forward link-5 length",
)
assert_zero(
    (pin12_forward - pin51_forward).dot(pin12_forward - pin51_forward) - L1**2,
    "five-link forward link-1 length",
)

x_goal, y_goal = sp.symbols("x_goal y_goal", real=True)
goal_pin12 = sp.Matrix([x_goal, y_goal])
pin23_inverse, _, _, _ = circle_intersection(goal_pin12, L2, anchor34, L3, branch_middle)
branch_outer = sp.symbols("branch_outer", real=True)
pin51_inverse, _, _, _ = circle_intersection(goal_pin12, L1, anchor45, L5, branch_outer)
assert_zero(
    ((pin23_inverse - goal_pin12).dot(pin23_inverse - goal_pin12) - L2**2).subs(branch_middle, 1),
    "five-link inverse link-2 circle",
)
assert_zero(
    ((pin23_inverse - anchor34).dot(pin23_inverse - anchor34) - L3**2).subs(branch_middle, -1),
    "five-link inverse link-3 circle",
)
assert_zero(
    ((pin51_inverse - goal_pin12).dot(pin51_inverse - goal_pin12) - L1**2).subs(branch_outer, 1),
    "five-link inverse link-1 circle",
)
assert_zero(
    ((pin51_inverse - anchor45).dot(pin51_inverse - anchor45) - L5**2).subs(branch_outer, -1),
    "five-link inverse link-5 circle",
)

print("All double-pendulum and five-link kinematic identities passed.")
