# Book Plan: Dynamics of Closed-Chain Multibody Systems

## 1. Project Brief

### Purpose

Create a high-level, technically rigorous book explaining how to formulate, simulate, and validate the dynamics of closed-chain multibody systems. Use the existing planar five-link mechanism as the main running example, while clearly distinguishing general principles from choices specific to that model.

### Audience

Engineering students and practitioners familiar with introductory mechanics, rigid-body motion, and ordinary differential equations.

### Scope and examples

- Main case study: five planar rigid links joined by five revolute pins in one perimeter loop, with link 4 fixed horizontally.
- The case study uses 15 Cartesian generalized coordinates, 13 scalar constraint equations, and two degrees of freedom at the modeled configuration. Explain that equation count alone does not determine mobility; assess constraint independence using the Jacobian rank, which may change at singular configurations.
- Teaching example: an open-chain double pendulum used to introduce energy-based equation derivation and conversion to a first-order ODE. State explicitly that it is not itself a closed-chain system.
- State modeling assumptions and exclusions, including ideal rigid bodies and joints, planar motion, gravity, and omitted contact, compliance, or friction effects where relevant.

### Learning outcomes

Readers should be able to:

1. Compare common dynamics formulations and select one suited to a model.
2. Derive equations of motion from kinematics, energies, and applied generalized forces.
3. Convert second-order equations to first-order ODE form for numerical integration.
4. Formulate holonomic joint and loop-closure constraints and differentiate them to velocity and acceleration levels.
5. Assemble constrained equations with reaction forces and explain their DAE/KKT structure.
6. Prepare consistent initial conditions and select a time-integration and drift-control strategy.
7. Validate numerical examples using residuals, constraint errors, energy behavior where appropriate, and sensitivity checks.

## 2. Authoring Workflow

Build the book iteratively; do not attempt to write it in one pass. The execution details and verified current status are recorded in `execution.md`.

1. **Scaffold:** Create the LaTeX source tree, frontmatter/chapter/appendix shells, shared files, and buildable placeholders.
2. **Establish framework:** Set page design, notation/citation conventions, and the reusable chapter template; pilot standalone and master builds.
3. **Research and prepare:** Map chapter purposes, dependencies, sources, technical examples, and open questions in `research/phase3_source_map.md`.
4. **Pilot a complete example:** Develop the double-pendulum symbolic derivation and ODE chapter/notebook together, then refine the shared template from that experience.
5. **Draft core mechanics:** Draft the formulations, mechanism, coordinates, loop constraints, constraint kinematics, constrained dynamics, and consistent-initial-condition chapters.
6. **Draft simulation and supporting material:** Draft integration/drift, verification, results, limitations, general introduction, general State of the Art, and the Python implementation appendix; complete executable validation artifacts and figures.
7. **Review and integrate:** Complete focused State of the Art research, technical/editorial review, cross-chapter consistency checks, and repeated revisions; keep rebuilding chapter and master outputs.
8. **Release:** Run clean validation artifacts, regenerate figures, resolve bibliography/references, compile standalone chapters and the complete book, and record release versions and limitations.

These phases are milestones, not a one-way waterfall. Research continues during drafting, review can return work to any earlier phase, and phases 5–7 may proceed in dependency-aware parallel work units. The book is not considered complete until Phase 7's content/review gates and Phase 8's release checks pass.

## 3. LaTeX Project and Supporting Artifacts

Use a modular LaTeX book: individual chapter sources are independently compilable, while `main.tex` assembles the full volume. A shared preamble and document class should govern both build modes. A package such as `subfiles` may support this arrangement.

```text
main.tex
preamble.tex
macros.tex
conventions.md
references.bib
research/
  phase3_source_map.md
templates/
  chapter_template.tex
frontmatter/
  introduction.tex
  general_state_of_the_art.tex
chapters/
  chapter01_formulations.tex
  chapter02_mechanism.tex
  chapter03_coordinates.tex
  chapter04_lagrange_double_pendulum.tex
  chapter05_loop_constraints.tex
  chapter06_constraint_kinematics.tex
  chapter07_constrained_dynamics.tex
  chapter08_initial_conditions.tex
  chapter09_integration_and_drift.tex
  chapter10_verification.tex
  chapter11_results.tex
  chapter12_limitations.tex
appendices/
  appendix_A_python_implementations.tex
notebooks/
  double_pendulum_validation.ipynb
constrained_five_link_dynamics.ipynb
scripts/
  # Focused symbolic derivation, validation, or figure-generation scripts
figures/
```

- The master file controls title/frontmatter, contents, chapter order, appendices, and bibliography. Place the general introduction and general State of the Art before Chapter 1.
- Keep shared notation macros, references, figures, labels, and formatting conventions centralized. Label equations and figures and reference them in text rather than typing numbers manually.
- Each chapter should compile independently using the shared setup and resolve its citations; the full book should resolve all cross-chapter references and citations.
- The existing `constrained_five_link_dynamics.ipynb` remains the executable source for the five-link case study and its SymPy derivations. Add a dedicated double-pendulum notebook for its symbolic derivation and ODE example.
- Use Python with SymPy to derive the symbolic equations for each worked dynamics example. Keep symbolic parameters and exact expressions while deriving; document the symbolic steps and resulting equations in the book, and retain the notebook/script as the reproducible derivation record.
- Maintain `research/phase3_source_map.md` as the living map from each frontmatter/chapter unit to its research questions, candidate and verified sources, dependencies, open decisions, and readiness. Its existence does not mean the literature reviews are complete.
- For unconstrained examples, symbolically form the Euler-Lagrange residual and extract `M(q)` and `h(q,qdot)`. For the closed-chain example, symbolically derive `Phi(q)`, `J(q)`, `Jdot(q,qdot) qdot`, the ideal acceleration constraints, and the KKT equations. Simplify and verify identities/residuals before substituting numerical parameters for simulation.
- Every worked numerical example must have a reproducible executable validation artifact: use a Jupyter notebook for exploratory, multi-step, or pedagogical work; use a focused Python script when that is sufficient for a targeted check or figure-generation task. Create these artifacts when validation or figure generation requires execution, rather than adding code artifacts without a purpose.
- Every worked symbolic dynamics derivation must also have a reproducible Python/SymPy notebook or script; prefer a notebook when the derivation's intermediate steps are part of the teaching example.
- Record the validation artifact, parameter values, and relevant software versions for each generated figure; regenerate outputs from a clean notebook kernel or a fresh script run before release.
- Keep the notebook or script and appendix listing aligned; designate one validated implementation as canonical and avoid maintaining divergent copies of the same algorithm.

## 4. Manuscript Structure

### Frontmatter: General Introduction

- Motivate closed-chain multibody dynamics and explain the book's purpose, audience, scope, assumptions, and objectives.
- Introduce the five-link case study and double-pendulum teaching example, distinguishing their roles.
- Give a concise roadmap through the book.

### Frontmatter: General State of the Art

- Provide a book-wide overview of the field: major dynamics formulations, coordinate choices, constrained ODE/DAE approaches, drift-control methods, current research directions, and broad open challenges.
- State a literature-search date or coverage boundary, describe source-selection scope, and cite foundational and current authoritative work.
- Keep this synthesis distinct from the more focused State of the Art section in each numbered chapter; avoid repeating the same survey in full.

### Chapter 1: Dynamics Formulations

- Compare Newton-Euler force/moment balance and Lagrangian energy-based derivation, including how reaction forces are handled.
- Briefly introduce virtual work/d'Alembert, Kane's method, and Hamiltonian formulation, with proportional attention to their relevance.
- Include a concise comparison by starting principle, typical equations/unknowns, strengths, and tradeoffs.
- Distinguish dynamics formulations from coordinate choices (minimal/redundant), equation formulations (ODE/DAE), and integration schemes (explicit/implicit).
- Explain why the book uses Lagrange's method for the double pendulum and redundant Cartesian coordinates with multipliers for the five-link loop.

### Chapter 2: Mechanism and Modeling Assumptions

- Explain open versus closed chains and introduce the five-link topology, body labels, pins, ground, mass properties, and external loading.
- State assumptions and identify physical effects outside the example's scope.

### Chapter 3: Coordinates and Rigid-Body Kinematics

- Define generalized positions and velocities, coordinate ordering, reference frames, planar rotations, and world positions of body-fixed points.
- Explain the convenience and redundancy of Cartesian body coordinates for closed loops.

### Chapter 4: Deriving Dynamics and Preparing an ODE

- Present a reusable Lagrange derivation: choose coordinates and conventions; derive positions and velocities; form kinetic and potential energy; define external generalized forces; apply Euler-Lagrange equations; collect `M(q) qddot + h(q,qdot) = Q_ext`, with `h` containing velocity-coupling and potential/gravity terms; and convert to a first-order state `y = [q,qdot]` with `ydot = [qdot,qddot]`.
- Use Python/SymPy to carry out and expose the symbolic derivation: form `E = d/dt(dL/dqdot) - dL/dq`, with `E = Q_ext`; when affine in `qddot`, obtain `M = dE/dqddot` and `h = E - M qddot`; verify that `E - (M qddot + h)` simplifies to zero. Explain each step and present the readable result in the book.
- Explain substituting physical parameters, evaluating the acceleration solve without explicitly forming `M^{-1}`, checking mass-matrix nonsingularity, and preparing state, solver, tolerances, time span, and diagnostics.

**Worked example: double pendulum**

- Model point masses `m1,m2` on massless rods `l1,l2`, fixed first pivot, no friction or applied torque initially. Define absolute angles positive clockwise from the downward vertical and positive world `y` upward.
- Derive positions:

  ```text
  x1 = l1 sin(theta1)              y1 = -l1 cos(theta1)
  x2 = x1 + l2 sin(theta2)         y2 = y1 - l2 cos(theta2)
  ```

- Differentiate for velocities and derive:

  ```text
  T = 1/2 (m1 + m2) l1^2 theta1_dot^2
      + 1/2 m2 l2^2 theta2_dot^2
      + m2 l1 l2 theta1_dot theta2_dot cos(theta1 - theta2)

  V = -(m1 + m2) g l1 cos(theta1) - m2 g l2 cos(theta2)
  L = T - V
  ```

- With `delta = theta1 - theta2`, derive the equations:

  ```text
  [ (m1+m2)l1^2       m2 l1 l2 cos(delta) ] [theta1_ddot]
  [ m2 l1 l2 cos(delta)       m2 l2^2     ] [theta2_ddot]

  + [ m2 l1 l2 sin(delta) theta2_dot^2 + (m1+m2) g l1 sin(theta1) ]
    [ -m2 l1 l2 sin(delta) theta1_dot^2 + m2 g l2 sin(theta2)       ]
  = [tau1, tau2]^T
  ```

- Perform the position, velocity, energy, Euler-Lagrange, and mass-matrix extraction steps symbolically in the double-pendulum Python/SymPy artifact. Check the resulting equations by simplifying the residual and, where practical, comparing with an independent derivation or numerical evaluation.
- Identify the configuration-dependent mass matrix and the gravity/velocity terms. For the unforced case, set `tau1=tau2=0`; state torque sign conventions if actuation is added.
- Show language-neutral pseudocode for an ODE right-hand side: split state into positions and velocities; evaluate `M` and `h`; solve `M qddot = tau - h`; return `[qdot,qddot]`.
- Show generic solver pseudocode with illustrative SI parameters, initial angles/velocities, interval, output times and tolerances; integrate; check solver status; plot or animate. Include no executable-language syntax in the chapter.
- Validate the unforced example with energy history and tolerance/step sensitivity. Explain the distinction between energy error and long-time trajectory agreement. The notebook repeats the run with `rtol=1e-10`, `atol=1e-12`, and `max_step=0.005 s`; the measured scaled energy error is `4.494e-10` and the maximum sampled state difference from baseline is `4.736e-8`.
- Transition to the five-link case: the double pendulum uses minimal coordinates and no loop-closure multipliers; the closed-chain model uses redundant coordinates and explicit constraints.

### Chapter 5: Joint Constraints and Loop Closure

- List the five-link perimeter pins and grounded link before deriving equations.
- Derive a pin residual by transforming each body-fixed attachment point to world coordinates and equating the two points.
- Explain that each planar pin contributes two scalar holonomic equations and grounding a planar pose adds three.
- Assemble `Phi(q)=0`; distinguish the number of written equations from independent constraints.
- Define `J(q)=dPhi/dq`; use rank to discuss local independence, mobility, and singular configurations.
- Derive `Phi(q)` and `J(q)` symbolically in the five-link Python/SymPy artifact, retaining symbolic link lengths and checking the expressions against the numerical kinematic model.

### Chapter 6: Constraint Velocities and Accelerations

- Differentiate position closure to obtain `J(q) qdot=0`.
- Differentiate again to obtain `J(q) qddot + Jdot(q,qdot) qdot=0`.
- Explain rotating-point centripetal terms and connect acceleration compatibility to the constrained dynamics solve.
- Use symbolic differentiation to derive and simplify `Jdot(q,qdot) qdot`; compare its numerical evaluation with the independently implemented acceleration bias.

### Chapter 7: Closed-Chain Dynamics and Reaction Forces

- Introduce rigid-body kinetic/potential energy, mass matrix, applied generalized forces, and ideal joint reactions.
- Present and interpret the ideal acceleration-level KKT system:

  ```text
  M qddot + J^T lambda = Q
  J qddot + Jdot qdot = 0
  ```

- Explain multiplier interpretation, block-system dimensions, and the relationship between the constrained equations and a DAE. Keep the ideal equations distinct from numerical stabilization.
- For the five-link center-of-mass coordinates, define the KKT right-hand side `Q = Q_ext + Q_g`, where `Q_g = -dV/dq`; state that this model has a constant mass matrix and no velocity-dependent inertial bias in these coordinates. Keep notation for generalized forces consistent with Chapter 4.
- Derive the ideal KKT matrix and right-hand side symbolically, then represent stabilization as a separate symbolic variant. Verify force-balance and acceleration-constraint residuals before numerical integration.

### Chapter 8: Consistent Initial Conditions

- Require initial position and velocity to satisfy `Phi(q0)=0` and `J(q0)qdot0=0`; obtain acceleration from the constrained equations rather than choosing it independently.
- Explain position/velocity projection and rank/singularity checks; use the notebook's projected state as the example.

### Chapter 9: Time Integration and Constraint Drift

- Explain why a general-purpose ODE integrator does not automatically preserve algebraic position and velocity constraints.
- Describe the notebook workflow: solve the stabilized acceleration/KKT equations within the RHS and return `[qdot,qddot]` for state `[q,qdot]`.
- Present Baumgarte stabilization separately from the ideal equations:

  ```text
  Phi_ddot + 2 zeta omega Phi_dot + omega^2 Phi = 0
  ```

  This adds `-Jdot qdot - 2 zeta omega (J qdot) - omega^2 Phi` to the lower KKT right-hand side. Interpret gains; weak gains permit drift, while aggressive gains can introduce stiffness and poor conditioning. The notebook's `zeta=1`, `omega=20` are example values, not defaults.
- Distinguish solver choice from constraint handling. Compare explicit adaptive Runge-Kutta and implicit methods for ODE reformulations; neither by itself guarantees closure. Explain tolerances, maximum internal step, and why requested output times do not force solver step locations.
- Compare drift-handling approaches:

  | Technique | Principle | Advantage | Limitation |
  | --- | --- | --- | --- |
  | Baumgarte stabilization | Feedback on position/velocity error in acceleration constraints | Easy to add to an acceleration-level ODE workflow | Gains require tuning and can make the system stiff |
  | Position/velocity projection | Correct each integrated state toward `Phi=0` and `J qdot=0` | Directly reduces closure errors | Adds solves and may perturb momentum, energy, or accuracy |
  | Direct DAE integration | Integrate differential and algebraic equations together | Treats constraints directly | Requires a suitable solver, consistent initialization, and appropriate formulation |
  | Coordinate reduction | Use independent coordinates with closure built in | Removes redundant coordinates and explicit reactions | Can be difficult to derive; singularities or branch changes matter |
  | Penalty forces | Approximate constraints with spring/damper-like forces | Simple when small violations are acceptable | Approximate closure; large stiffness makes integration difficult |

- Explain that projection can accompany an ODE stepper; Baumgarte modifies acceleration constraints; DAE changes the solver formulation; penalty forces soften ideal constraints. Treat penalty stiffness as numerical unless actual compliance is modeled.
- Recommend choosing based on closure accuracy, stiffness, system size, solver availability, and simulation duration. Outline pseudocode for consistent initialization, integration, monitoring, and a tighter-settings repeat.

### Chapter 10: Verification and Validation

- Verify dimensions, rank/mobility at representative configurations, derivatives (symbolic/analytic versus independent or finite-difference checks), force balance, and acceleration residuals.
- Validate trajectories by checking solver status, constraint closure, velocity closure, grounded pose, and sensitivity to tolerances/stabilization. Compare with known results or physical data when available.
- Distinguish implementation verification from validation against the physical system. Treat notebook thresholds as example-specific, not universal.

### Chapter 11: Results and Visualization

- Report units, parameters, time span, solver settings, saved samples, stabilization settings, and key diagnostics.
- Show initial/final configurations or selected animation frames where useful; explain that visualization alone does not prove correctness.
- Include a compact results table when it improves comparison.

### Chapter 12: Limitations and Extensions

- Discuss ideal rigid joints, planar motion, fixed topology, no contact, and simplified loading as limitations.
- Outline extensions to actuation, damping/friction, spatial systems, contact, flexibility, parameter studies, and alternative constraint formulations; explain that extensions require renewed verification.

### End Matter: Python Implementation Appendix

- Provide organized, commented Python listings corresponding to the validated notebook examples.
- Include readable symbolic-derivation listings as well as the numerical ODE/integration pieces; cite the corresponding validation notebook or script for complete reproducibility.
- Keep chapter exposition focused on equations, explanatory prose, diagrams, and language-neutral pseudocode; refer readers to the relevant notebook and appendix listing for executable implementation.
- Maintain consistency between notebooks and appendix listings; do not duplicate evolving algorithms independently.

## 5. Shared Chapter, Reference, and Visual Standards

### Chapter template

Each numbered chapter contains, as appropriate:

1. Learning goal or framing question.
2. Clearly labeled, chapter-specific **State of the Art** subsection.
3. Assumptions, notation, and derivation/explanation.
4. Language-neutral pseudocode where it helps describe a procedure.
5. Purposeful figures/tables only where they improve understanding.
6. Summary and transition to the next chapter.

### Literature and citation policy

- The general State of the Art is a broad, book-level synthesis; chapter State of the Art sections focus on current practice, research, and open issues for that chapter. Avoid repeating surveys; cross-reference instead.
- State the search date or coverage boundary and avoid claiming exhaustive coverage without support.
- Cite authoritative textbooks/original sources for established methods, reliable software documentation for implementation-specific behavior, sources for nontrivial external claims, and the original source for borrowed/adapted material. Put citations near the claims they support.
- Distinguish external claims and assumptions from the book's own derivations and simulation results; do not cite standard algebra or original results merely decoratively.
- Store entries in the shared `references.bib`; use consistent keys and citation style. Verify citations in both standalone chapter and full-book builds, including unresolved citations and missing/unused entries.

### Figures and diagrams

- Visuals are optional and purpose-driven, not required in every chapter. Candidate visuals include formulation comparison, mechanism topology, coordinate/attachment-point geometry, double-pendulum diagram, constraint differentiation, KKT blocks, solver workflow, constraint-error histories, and mechanism configurations.
- Give each visual a descriptive caption and stable label, introduce and interpret it in the text, define symbols/units as needed, and cite borrowed/adapted material.
- Keep visuals legible in print and on screen, use color-independent distinctions where practical, and retain editable source files when feasible under `figures/`.

### Notation, prose, and technical consistency

- Define symbols before use; maintain consistent notation, units, signs, coordinate ordering, and labels across chapters.
- Pair equations with interpretation and assumptions. Label general principles separately from example-specific facts.
- Keep ideal dynamics equations distinct from numerical stabilization terms and implementation details.
- Include diagrams only when useful; never treat a plausible animation as proof of validity.

## 6. Review and Completion Criteria

### During each iteration

- Compile the changed chapter independently and rebuild the master book at integration checkpoints.
- Run the relevant validation notebook from a clean kernel or script in a fresh process when equations, parameters, or generated figures change; inspect solver status, expected behavior, numerical residuals, and figure output.
- Review clarity, equation signs, assumptions, citations, figure references, and cross-chapter consistency; revise and repeat as needed.

### Before release

- Build every standalone chapter and the complete book; resolve LaTeX errors, labels, cross-references, citations, numbering, and figure paths/placement.
- Check for missing or unused bibliography entries, duplicated labels, and inconsistent chapter/full-book output.
- Regenerate computed book figures from their recorded validation notebook or script, parameters, and software versions; confirm every worked numerical example has an appropriate executable validation artifact.
- Have a mechanics reviewer check signs, coordinate ordering, units, rank/mobility claims, and the distinction between DAE formulation and time integrator.
- Have a reference reviewer confirm sources support their claims, chapter State of the Art sections are current and focused, and borrowed/adapted material is credited.
- Confirm the main text remains equations, explanatory prose, purposeful figures, and language-neutral pseudocode; executable Python appears in development validation artifacts and, as published book code, only in the end-of-book implementation appendix.
- Confirm readers can follow the path from physical model to equations, initial data, numerical simulation, and validation, including stated limitations and evidence beyond animation.
