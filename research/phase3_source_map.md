# Phase 3 Research and Preparation Map

This is the working research map for the book described in `plan.md`. It is a preparation artifact, not a claim that the book-wide or chapter-level literature reviews are complete.

**Initial coverage:** source mapping and a small verified seed set only. Topic-specific literature searches remain open for every chapter.

## Source-Use Rules

- Use foundational sources to establish standard formulations and original methods.
- Use recent peer-reviewed work for chapter State of the Art sections, especially open problems and current practice.
- Use official documentation only for software behavior (solver methods, tolerances, output sampling, APIs).
- Each source must support an identified claim or derivation; record the chapter/claim it serves before citation.
- Do not call a selective seed list a systematic or exhaustive review. Update the search date and coverage statement during each chapter's research pass.

## Verified Seed Sources

| Key | Source | Verified metadata | Use |
| --- | --- | --- | --- |
| `meurer2017sympy` | Meurer et al., “SymPy: symbolic computing in Python,” *PeerJ Computer Science* 3:e103 (2017), DOI `10.7717/peerj-cs.103` | Crossref and publisher metadata; already in `references.bib` | SymPy symbolic differentiation and algebra system context; not a mechanics reference. |
| `baumgarte1972stabilization` | Baumgarte, “Stabilization of constraints and integrals of motion in dynamical systems,” *Computer Methods in Applied Mechanics and Engineering* 1(1), 1–16 (1972), DOI `10.1016/0045-7825(72)90018-7` | Crossref metadata | Original source for Baumgarte stabilization. |
| `scipy_solve_ivp` | SciPy `solve_ivp` reference documentation | Official SciPy documentation, accessed 2026-10-07 | RK45/Radau/BDF usage, `t_eval`, tolerances, `max_step`, and solver-result semantics. Recheck against the software version used for final figures. |

## Frontmatter Research Map

| Unit | Literature question / evidence needed | Seed sources | Dependencies / open questions | Status |
| --- | --- | --- | --- | --- |
| General Introduction | What practical and scientific problems motivate closed-chain multibody simulation? Which audiences and scope are defensible? | `shabana2013dynamics`; project case-study assumptions and verified examples. | Drafted with explicit scope and distinction between open-chain teaching example and closed-chain case study. | Drafted |
| General State of the Art | How do formulations, coordinate choices, DAE/ODE approaches, drift-control methods, applications, and verification practice relate? | `goldstein2002classical`, `shabana2013dynamics`, `schiehlen1997roots`, `laulusa2008classical`, `bauchau2008contemporary`, `arnold2017dae`, `baumgarte1972stabilization`, `garciaorden2010energyprojection`, `braun2009drift`, `arnold2011vehicle`, `shabana1997flexible`, `arnold2015lieerror`, `ascherpetzold1998`, `hairerwanner1996`, `hairer2006geometric`, `scipy_solve_ivp`, `oberkampfroy2010`, `sandve2013reproducible`. | Expanded targeted narrative review. Crossref/publisher-linked metadata/abstracts checked 2026-10-07; discovery terms and scope boundary stated in manuscript. Not systematic, exhaustive, or a complete 2026 literature survey. | Expanded; bounded coverage stated |

## Chapter Research Map

| Chapter | Focused State of the Art questions | Initial source direction | Prerequisites / open questions | Status |
| --- | --- | --- | --- | --- |
| 1. Dynamics Formulations | Current use and tradeoffs of Newton–Euler, Lagrange, virtual work/d'Alembert, Kane, Hamiltonian methods for multibody systems. | Foundational analytical mechanics and multibody dynamics texts; primary sources for Kane/Hamiltonian where discussed. | First comparison draft exists; keep formulations distinct from coordinate choice and integrator choice. Literature review and editorial review remain open. | Drafted; literature review open |
| 2. Mechanism and Modeling Assumptions | Current modeling practice for rigid links, ideal joints, grounding, and model fidelity. | Multibody modeling texts; sources for ideal joint assumptions and application-specific fidelity. | First topology/assumptions draft exists; verify all model-specific properties against the canonical five-link notebook and add sourced modeling context. | Drafted; technical review open |
| 3. Coordinates and Rigid-Body Kinematics | Redundant Cartesian versus minimal/generalized coordinates for closed loops; robustness and singularity tradeoffs. | `shabana2013dynamics`. | Coordinate order and Jacobian blocks agree with symbolic/numeric notebook evaluation at the initial pose; broader recent comparisons excluded by the stated focused-source scope. | Drafted; checked for declared scope |
| 4. Deriving Dynamics and Preparing an ODE | Symbolic equation generation in multibody mechanics; reproducibility/verification practices for computer algebra. | `meurer2017sympy`; mechanics sources for Euler–Lagrange derivation; research on symbolic multibody generation. | Double pendulum is an open-chain teaching example only. Symbolic equations and sign convention are cross-checked against the notebook. Still add an authoritative analytical-mechanics source and current work on symbolic multibody equation generation; deepen chapter State of the Art and editorial review. | Drafted; literature review open |
| 5. Joint Constraints and Loop Closure | Holonomic loop constraints and independent-constraint/mobility interpretation. | `shabana2013dynamics`. | Symbolic residual/Jacobian retain all symbolic link lengths and agree with the numerical formulation to machine precision at the projected pose; rank 13 there. | Drafted; checked for declared scope |
| 6. Constraint Velocities and Accelerations | Differentiated constraints and acceleration bias. | `shabana2013dynamics`. | Symbolic `Jdot*qdot` agrees with the numerical centripetal-bias implementation to `4.4e-19` at the initial pose; broader implementation comparisons excluded by review scope. | Drafted; checked for declared scope |
| 7. Closed-Chain Dynamics and Reaction Forces | Multipliers, KKT equations, and ideal reaction forces. | `shabana2013dynamics`, `ascherpetzold1998`. | KKT signs and gravity convention match notebook; initial force residual `4.663e-15`; Baumgarte correction remains separate from ideal equations. | Drafted; checked for declared scope |
| 8. Consistent Initial Conditions | Position/velocity consistency and initial projection. | `shabana2013dynamics`, `ascherpetzold1998`. | Notebook projects only initial position/velocity; both initial residuals are below `5e-16`; no per-step projection is claimed. | Drafted; checked for declared scope |
| 9. Time Integration and Constraint Drift | DAE and ODE integration, Baumgarte stabilization, projection, coordinate reduction, penalty methods, and stiffness/error control. | `baumgarte1972stabilization`, `ascherpetzold1998`, `hairerwanner1996`, `hairer2006geometric`, `scipy_solve_ivp`. | Focused foundational and official-software synthesis; separates formulation, drift control, and stepper. Scope checked 2026-10-07; no solver benchmark claimed. | Drafted; bounded coverage stated |
| 10. Verification and Validation | Verification of equations/code/solver behavior versus validation against physical evidence. | `oberkampfroy2010`, `sandve2013reproducible`; project notebook residuals and trajectory checks. | Drafted acceptance checks from reproduced notebook metrics. No experimental validation data or domain-specific standard is claimed. Scope checked 2026-10-07. | Drafted; bounded coverage stated |
| 11. Results and Visualization | Reproducible reporting and visual communication of multibody trajectories and diagnostics. | `sandve2013reproducible`; canonical notebook and generated figure/GIF. | Drafted from a reproduced 10 s run with saved parameters, versions, and residual metrics. Scope checked 2026-10-07; no benchmark or physical comparison claimed. | Drafted; bounded coverage stated |
| 12. Limitations and Extensions | Scope choices for spatial motion, flexible/compliant bodies, contact/friction, and actuation. | `shabana2013dynamics`, `ascherpetzold1998`, `hairerwanner1996`. | Drafted as a scoped outlook based on foundational sources, not topic-by-topic recent surveys. Scope checked 2026-10-07. | Drafted; bounded coverage stated |

## Technical Work-Unit Readiness

### Double pendulum

- **Available:** `notebooks/double_pendulum_validation.ipynb` derives positions, velocities, energies, Euler–Lagrange equations, `M`, `h`, and checks the symbolic form before integrating.
- **Verified run:** `.venv` with NumPy 2.5.3, SymPy 1.14.0, SciPy 1.18.1, Matplotlib 3.11.2. Ten-second RK45 run succeeds with 2,001 samples. Maximum relative energy drift observed: `9.373e-09` under the recorded parameters/tolerances.
- **Figures:** `figures/double_pendulum_geometry.png` and `figures/double_pendulum_response.png` are notebook-generated.
- **Open for Chapter 4:** add an authoritative analytical-mechanics source; extend the chapter State of the Art beyond software citations; review the derivation and figure captions for pedagogical clarity.

### Five-link closed chain

- **Available:** `constrained_five_link_dynamics.ipynb` contains the numeric and symbolic model and generated ten-second animation.
- **Verified notebook status:** all code cells were rerun sequentially in the configured Python environment. Symbolic/numeric differences were below `3.4e-16` for `Phi`, `2.3e-16` for `J`, and `4.4e-19` for `Jdot*qdot`; the 10 s RK45 run completed with 13,154 RHS evaluations and 2,001 saved states.
- **Trajectory diagnostics:** maximum saved-state `||Phi(q)||_inf = 1.108e-9`; maximum `||J(q) qdot||_inf = 1.247e-7`; maximum grounded-pose error `1.333e-17`. Initial KKT force-balance residual was `4.663e-15`. The regenerated GIF is 10.00 s, 200 frames at 20 fps; `figures/five_link_configurations.png` is notebook-generated.
- **Sensitivity checks:** at `rtol=1e-9`, `atol=1e-11`, `max_step=0.01`, and the baseline gains, maximum `||J qdot||_inf` falls to `1.019e-8` with 20,492 RHS evaluations; maximum coordinate difference from baseline is `9.397e-5`. Halving the Baumgarte frequency to `10 s^-1` uses 8,654 RHS evaluations, with maximum `||Phi||_inf = 2.018e-9`, maximum `||J qdot||_inf = 1.058e-7`, and maximum coordinate difference `2.405e-4`. The constraint Jacobian rank remains 13 at every saved state in both variants. Relative energy drifts are `3.158e-7` baseline, `2.548e-8` tighter tolerance, and `3.191e-7` lower gain.
- **Remaining validation boundary:** no measurement data or near-singularity stress test is available, and the small tolerance/gain comparison is not a convergence proof. The example is internally verified for this configuration and parameter set, not physically validated or generally robust.

## Phase 3 Readiness Decisions

- **Research baseline:** the expanded general State of the Art now includes paired 2008 reviews of classical and contemporary constraint enforcement, Arnold's 2017 DAE-focused multibody chapter, projection/stabilization and drift-elimination studies, a vehicle-system numerical-methods review, Shabana's flexible multibody review, and Lie-group integration error analysis. Records were checked through Crossref/publisher-linked metadata and abstracts on 2026-10-07; the overview states discovery terms and scope.
- **Coverage limitation:** this targeted narrative synthesis is not a systematic literature review and does not claim to survey all current solver benchmarks or every application extension. The manuscript labels these limits rather than implying comprehensive coverage.
- **Next review work:** technical and editorial review of all chapters, multi-state independent symbolic/numeric comparisons, tolerance and Baumgarte sensitivity, and near-singularity tests remain necessary before a research-grade release.
