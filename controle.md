# Inverse Dynamics and Control Strategies

## Purpose and current scope

The first goal is to compute and study the planar five-link system's natural dynamics without external actuation. The baseline is gravity-driven and constrained, with no motor torques, damping, contact, or controller. In this first phase set \(Q_{\mathrm{ext}}=0\) and \(u=0\), retain gravity and ideal constraint reactions, and examine free response from consistent initial conditions. Inverse dynamics and control are later extensions; they will require explicit actuator locations, signs, limits, and a force mapping.

The Cartesian generalized-coordinate vector is ordered by body as
\[
q=(x_1,y_1,\theta_1,\ldots,x_5,y_5,\theta_5)^T\in\mathbb{R}^{15}.
\]
The loop and grounding constraints are \(\Phi(q)=0\), with Jacobian \(J=\partial\Phi/\partial q\in\mathbb{R}^{13\times15}\). At a regular configuration, the model has two local degrees of freedom. The mass matrix is constant for the present center-of-mass coordinates; gravity is included in \(Q_g=-\partial V/\partial q\).

## Unactuated constrained dynamics

For the initial study, the equations are
\[
M\ddot q+J^T\lambda=Q_g(q),
\qquad
J\ddot q+\gamma(q,\dot q)=0,
\qquad
\gamma=\dot J\dot q.
\]
At each admissible state, solve the constrained acceleration system for \(\ddot q\) and the ideal reaction multipliers \(\lambda\), then integrate the resulting motion. No prescribed acceleration or control effort is needed. A meaningful numerical run still needs initial position and velocity satisfying \(\Phi(q_0)=0\) and \(J(q_0)\dot q_0=0\), plus stated parameters and solver settings.

The first analysis can characterize the two-degree-of-freedom free response: inspect the initial acceleration and reaction forces, plot the motion and energy history, and measure pin closure and grounded-pose drift. For an ideal conservative model, mechanical energy should be conserved in continuous time; numerical energy error and constraint drift should be monitored separately. Baumgarte stabilization or projection may be included as numerical treatments, but they do not add physical actuation and should be distinguished from the ideal equations.

## Equations with actuation (later extension)

Let \(u\in\mathbb{R}^m\) be the actuator effort vector and let \(B(q)\in\mathbb{R}^{15\times m}\) map actuator efforts into Cartesian generalized forces. With known external loading \(Q_{\mathrm{ext}}\), the equations are
\[
M\ddot q+J^T\lambda=Q_g+Q_{\mathrm{ext}}+B(q)u,
\qquad
J\ddot q+\gamma(q,\dot q)=0,
\qquad
\gamma=\dot J\dot q.
\]
The multiplier vector \(\lambda\) represents ideal constraint reactions, not motor inputs. A motor torque applied across a revolute joint contributes equal-and-opposite generalized moments to the two bodies; its column in \(B\) must follow the chosen positive-angle convention. An external motor or ground reaction has a different mapping and should be specified separately.

Baumgarte terms or projection may be used to control numerical constraint drift. They are not substitutes for actuator feedback or trajectory tracking. Keep the physical motion objective, the actuator law, and numerical constraint treatment conceptually separate.

## Inverse dynamics

Inverse dynamics starts from a desired feasible trajectory \((q_d,\dot q_d,\ddot q_d)\) and determines the actuator efforts and reactions needed to realize it. The desired motion must satisfy loop closure and its differentiated constraints to the accuracy required by the solve:
\[
\Phi(q_d)=0,\qquad J(q_d)\dot q_d=0,\qquad
J(q_d)\ddot q_d+\gamma(q_d,\dot q_d)=0.
\]
Substituting the desired acceleration into force balance gives
\[
B(q_d)u-J(q_d)^T\lambda
=M\ddot q_d-Q_g(q_d)-Q_{\mathrm{ext}}.
\]
This is 15 equations for the \(m\) actuator efforts and 13 reaction multipliers. With two independent actuators it is square, but solvability still depends on actuator placement and regularity: the actuator directions must provide independent effort in the two admissible motion directions. A poorly placed actuator set can be singular or badly conditioned even when the constraint Jacobian has full rank.

If there are more than two actuators, effort allocation is redundant. A useful formulation is a constrained optimization such as
\[
\min_u\;\tfrac12 u^T W u
\quad\text{subject to force balance, constraints, and actuator limits},
\]
where positive-definite \(W\) encodes effort cost or preferences. If fewer than two independent actuation directions are available, arbitrary two-degree-of-freedom acceleration commands cannot generally be realized; the reference must respect the underactuated dynamics.

## Reduced-coordinate formulation

For analysis and tracking, it may be clearer to parameterize the constraint manifold locally with two independent coordinates \(s\in\mathbb{R}^2\), such that \(q=\psi(s)\). Define \(N(s)=\partial\psi/\partial s\), so \(\dot q=N\dot s\) and \(\ddot q=N\ddot s+\dot N\dot s\). Projecting force balance by \(N^T\) eliminates ideal constraint reactions:
\[
M_r(s)\ddot s+h_r(s,\dot s)
=Q_r(s,\dot s)+B_r(s)u,
\]
where
\[
M_r=N^TMN,\qquad
h_r=N^T\bigl(M\dot N\dot s-Q_g\bigr),\qquad
Q_r=N^TQ_{\mathrm{ext}},\qquad
B_r=N^TB.
\]
This representation is local unless a nonsingular global parameterization is established. It needs a reliable map between \(s\) and the five body poses, and its conditioning can deteriorate near a change in coordinate chart or a mechanism singularity. For the existing notebook, the Cartesian KKT form is already implemented; a reduced-coordinate model would be an additional layer, not an assumed feature.

## Candidate tracking strategies

### Inverse-dynamics feedforward with computed-acceleration feedback

Given a feasible reference \((s_d,\dot s_d,\ddot s_d)\), define tracking errors \(e=s_d-s\), \(\dot e=\dot s_d-\dot s\) and request
\[
\ddot s_{\mathrm{cmd}}
=\ddot s_d+K_d\dot e+K_p e.
\]
For fully actuated reduced dynamics, choose \(u\) to satisfy
\[
B_r u=M_r\ddot s_{\mathrm{cmd}}+h_r-Q_r.
\]
If \(B_r\) is square and nonsingular, this determines \(u\); if redundant, use a weighted allocation subject to limits. This computed-torque design cancels the nominal model and gives a second-order tracking target in the ideal model. Model error, actuator saturation, unmodeled friction, and noisy velocity estimates can erode that behavior, so feedback gains and robustness claims need simulation and validation.

### Joint-space PD with gravity compensation

A simpler baseline is proportional-derivative feedback in reduced coordinates with gravity compensation. It is easier to explain and can be less dependent on exact inertial parameters, but it does not cancel the full nonlinear dynamics and may track rapid references poorly. It is a sensible comparison controller before adding more elaborate methods.

### Other strategies to consider later

- **Operational-space or task-space control:** regulate a selected point, orientation, or path rather than all independent coordinates; requires a task Jacobian and careful treatment near singularities.
- **Robust/adaptive control:** address bounded model uncertainty or unknown parameters; requires stated uncertainty assumptions and stability analysis.
- **Model predictive control:** handle effort and state constraints explicitly; increases computational and implementation complexity.
- **Passivity or energy shaping:** attractive for energy-based objectives and interaction, but needs a deliberate storage function and damping design.

These are candidate directions, not implemented or verified controllers.

## Constraint handling in a controller

For a Cartesian controller, solve the constrained forward-dynamics KKT system with the control force \(B u\) included in the right-hand side. A desired acceleration should either be generated in admissible coordinates or projected to satisfy \(J\ddot q+\gamma=0\). Do not independently command all 15 Cartesian accelerations: only two are locally independent, and incompatible commands conflict with the 13 constraints.

Numerical Baumgarte feedback can stabilize constraint residuals while the tracking controller acts on the mechanism's two physical degrees of freedom. Monitor these separately: pin closure and grounded-pose errors for constraint preservation; tracking error and actuator effort for control performance. Report each residual family with its units rather than combining metres, radians, and force or moment components into one unscaled norm.

## Proposed development sequence

1. Run the unactuated gravity-driven model from consistent initial conditions; verify acceleration-level residuals, constraint preservation, reaction forces, and energy behavior.
2. Characterize the free response across selected initial configurations and velocities, while separating physical motion from numerical stabilization effects.
3. Choose two independent configuration coordinates or a local coordinate chart, and verify its mapping to the Cartesian model.
4. If the later control study is pursued, specify actuator joints, torque signs, generalized-force map \(B(q)\), torque limits, and whether actuation is ideal or includes motor dynamics.
5. Generate a smooth reference trajectory that satisfies loop closure and velocity/acceleration consistency; implement inverse dynamics as a trajectory-to-effort calculation and check force-balance residuals, reaction multipliers, effort magnitudes, and power balance.
6. Add a tracking controller and compare it against the unactuated response; if appropriate, compare joint-space PD plus gravity compensation with computed-acceleration feedback under identical initial conditions and limits.
7. Test constraint preservation, tracking error, effort saturation, sensitivity to parameter error, and behavior near poorly conditioned configurations. Numerical verification is not experimental validation; measured actuator and mechanism data are needed for physical validation.

## Decisions still open

- Which two joints or bodies are actuated, and are there additional redundant actuators?
- Are the controlled variables two generalized coordinates, selected joint angles, or a task-space output?
- Is the objective point-to-point motion, periodic motion, or path following?
- What torque and speed limits, damping, sensing, and parameter uncertainty should be represented?
- Should the first example prioritize a transparent PD baseline or demonstrate computed-torque tracking?
