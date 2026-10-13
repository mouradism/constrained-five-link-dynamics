# Work Log

## 2026-10-07: Phase 1 scaffold

### Scope

Created the minimal modular LaTeX book scaffold from `plan.md` and Phase 1 of `execution.md`. Existing notebook and GIF files were left unchanged; no chapter content was drafted.

### Environment

- OS: Windows
- TeX distribution: MiKTeX 25.12
- Engine: pdfTeX 4.23
- `latexmk`: present, but cannot run because Perl is not installed.
- `subfiles`: available in the active MiKTeX user package tree.

### Build checks

- Master build: `pdflatex -output-directory=build -interaction=nonstopmode -halt-on-error main.tex` — passed; generated `build/main.pdf` (17 pages).
- Standalone check: `pdflatex -output-directory=build -interaction=nonstopmode -halt-on-error chapters/chapter01_formulations.tex` — passed; generated `build/chapter01_formulations.pdf`.
- The master build initially reported a duplicate page-anchor warning. Title-page anchors were disabled to avoid collision with restarted frontmatter/mainmatter numbering; the subsequent master build completed without that warning.

### Known environment notices

- MiKTeX reports that its package database has not been checked for updates. This is an environment notice; it did not prevent `pdflatex` builds.
- `main.bbl` does not exist yet because `references.bib` is an empty placeholder. Bibliography processing will be added when sources are introduced.

### Phase 1 status

- Source directories and placeholder files created.
- Master and standalone chapter compilation verified with direct `pdflatex`.
- Phase 1 follow-up audit confirmed all planned source and artifact paths exist, including `scripts/README.md` for focused scripts.
- Build products are kept in ignored `build/`.
- Phase 1 is complete. Phase 2 is recorded below.

## 2026-10-07: Phase 2 book framework

### Decisions recorded

- Provisional layout: `book` class, 11 pt, one-sided A4, 30 mm margins, Computer Modern with T1 encoding, and `microtype` with font expansion disabled for MiKTeX bitmap-font compatibility.
- Citation style: numeric BibTeX citations in order of appearance (`unsrt`). Standalone subfiles include a chapter-local bibliography; the master prints one bibliography at the end.
- Shared notation and modeling conventions are in `conventions.md`.
- Reusable chapter shell is `templates/chapter_template.tex`; Chapter 4 is the pilot.
- The generic chapter template compiled independently to `build/chapter_template.pdf`.
- The reusable chapter template also compiled standalone to `build/chapter_template.pdf`.
- Pilot uses the generated double-pendulum geometry figure and a SymPy software citation. The angle convention is absolute angles, positive clockwise from downward vertical, with world `y` positive upward.

### Validation

- Standalone pilot sequence: pdfLaTeX, BibTeX, then two pdfLaTeX passes on `chapters/chapter04_lagrange_double_pendulum.tex` — passed. The pilot PDF includes the geometry figure and resolves `meurer2017sympy` in its chapter bibliography.
- Master sequence: pdfLaTeX, BibTeX, then two pdfLaTeX passes on `main.tex` — passed. The citation appears in the master bibliography; no undefined citations/references, duplicate page anchors, or fatal build errors remain in the final log.
- Pilot build exposed a MiKTeX font-expansion failure with `microtype`; `expansion=false` fixed the build while preserving microtype's other features.
- `latexmk` remains unavailable because Perl is not installed. Direct pdfLaTeX/BibTeX commands are the current verified build route.

### Phase 2 status

- Shared layout and conventions selected provisionally and tested.
- Chapter template established, independently compiled, and piloted in Chapter 4 with citation and generated figure paths.
- Standalone and master builds, citation handling, and figure handling verified. Phase 2 exit gate is met; review the pilot PDF before scaling the design across all chapters.
- Phase 3 research/preparation and full chapter drafting had not begun at Phase 2 close.

## 2026-10-07: Phase 3 preparation started

- Created `research/phase3_source_map.md` with chapter-specific research questions, source directions, dependencies, readiness, and open checks for frontmatter and all 12 chapters.
- Added verified seed sources for the original Baumgarte stabilization method and official SciPy `solve_ivp` documentation to `references.bib`. The existing SymPy article remains a software-method reference, not a mechanics derivation source.
- Chapter 4 is the first ready drafting unit: the symbolic double-pendulum notebook and pilot layout exist. It still needs a full chapter-specific State of the Art search and authoritative analytical-mechanics sources.
- General State of the Art and the other chapter reviews remain incomplete; the source map records research needs rather than claiming coverage.
- The five-link notebook has existing executed outputs, but still needs a clean-kernel run and trajectory-wide position/velocity closure diagnostics before it is publication-ready.

## 2026-10-07: Phase 4, Chapter 4 technical draft

- Replaced the Chapter 4 layout pilot with a technical draft following the double-pendulum notebook: model assumptions and coordinates, positions/velocities, energies, Euler–Lagrange residual, symbolic `M`/`h` extraction, matrix equations, first-order ODE state, language-neutral pseudocode, numerical settings, energy result, and transition to closed-chain coordinates.
- Kept executable Python in the notebook; Chapter 4 contains equations and language-neutral procedure steps only.
- Standalone Chapter 4 build passed after BibTeX and repeated pdfLaTeX passes. The full master book also built with the two intended references and figure. Final logs showed no unresolved citations/references, duplicate page anchors, or fatal errors.
- The chapter remains a technical draft, not release-ready: its State of the Art is a short tool-focused orientation. Add authoritative analytical-mechanics sources, extend current symbolic multibody literature coverage, and conduct editorial review.

## 2026-10-07: First core mechanics drafts

- Drafted Chapters 1–3 and 5–8: formulation comparison; mechanism assumptions and mobility; Cartesian coordinates and rigid-body kinematics; loop constraints; differentiated constraints; multiplier/KKT dynamics; and consistent initial conditions.
- Kept chapters equation- and pseudocode-focused; executable Python remains in notebooks/scripts and is reserved for the appendix listings.
- Standalone pdfLaTeX/BibTeX builds completed for Chapters 1–3 and 5–8. Final chapter logs showed no unresolved citations/references or fatal errors. Chapter 1's formulation table initially had an overfull row; its label was shortened and the focused standalone rebuild passed.
- The full master build completed with Chapters 1–12 and the appendix included. Individual core drafts still require technical equation checks against the five-link notebook, literature research for each required State of the Art subsection, and editorial review; they are not marked stable.
- Updated `execution.md` and `research/phase3_source_map.md` to record the pilot as technically drafted and the core chapters as first drafts in progress. The general/chapter literature surveys and Chapters 9–12/frontmatter/appendix content remain open.

## 2026-10-07: Complete bounded-scope manuscript draft and release checks

- Drafted Chapters 9–12, the general introduction, the book-level State of the Art, and Python implementation excerpts. Added a PowerShell build script for all 12 standalone chapters plus the master document.
- Verified reference metadata against Crossref/publisher records for Shabana, Ascher--Petzold, Hairer--Lubich--Wanner, Hairer--Wanner, and Oberkampf--Roy; verified SciPy solver claims against the official `solve_ivp` documentation. Corrected the Shabana print ISBN. Coverage is explicitly foundational and selective, not a systematic review.
- Reran the double-pendulum notebook sequentially. The symbolic equation checks passed; baseline RK45 completed 10 s with 2,001 saved states and 7,334 RHS evaluations; maximum scaled energy error was `9.373e-9`. A tighter run (`rtol=1e-10`, `atol=1e-12`, `max_step=0.005 s`) used 13,136 RHS evaluations, reduced maximum scaled energy error to `4.494e-10`, and differed from baseline by at most `4.736e-8` in sampled state. Regenerated both double-pendulum figures and corrected the response plot label to “Scaled energy error.”
- Added and ran the planned double-pendulum tolerance/step sensitivity case with `rtol=1e-10`, `atol=1e-12`, and `max_step=0.005 s`. It completed with 13,136 RHS evaluations, maximum scaled energy error `4.494e-10`, and maximum sampled state difference `4.736e-8` from baseline. This is a focused refinement check, not a convergence proof.
- Reran the five-link notebook sequentially. Symbolic/numeric differences were below `3.4e-16` for `Phi`, `2.3e-16` for `J`, and `4.4e-19` for `Jdot*qdot`. The 10 s baseline run completed with 13,154 RHS evaluations; maximum pin-position closure and pin-velocity errors were `1.108e-9 m` and `1.247e-7 m/s`; grounded translation and orientation errors were `1.333e-17 m` and `3.031e-19 rad`. Initial KKT residuals are reported by units: `1.998e-15 N` translational force, `4.663e-15 N m` moment, and `7.834e-15 m/s^2` stabilized pin acceleration. Baseline scaled mechanical-energy drift was `3.158e-7`.
- Sensitivity checks: tighter tolerances increased RHS evaluations to 20,492 and reduced maximum `||J qdot||_inf` to `1.019e-8`, with maximum coordinate difference `9.397e-5`; halving the Baumgarte frequency reduced RHS evaluations to 8,654, with maximum `||Phi||_inf=2.018e-9`, maximum `||J qdot||_inf=1.058e-7`, and maximum coordinate difference `2.405e-4`. Rank remained 13 at all saved samples in both checks. The notebook regenerated and verified the ten-second, 200-frame GIF and saved `figures/five_link_configurations.png`.
- The initial PowerShell build-script attempt exposed two environment/script issues: machine execution policy is `Restricted`, and MiKTeX's benign stderr update notice must not be treated as a terminating error. The script now checks native exit codes explicitly; it was run under a process-only policy bypass, without changing persistent policy.
- All 12 standalone chapter builds and the master build completed. A final all-log scan found no BibTeX warnings, undefined citations/references, duplicate anchors, fatal errors, or overfull boxes. Chapter 11 uses explicit chapter numbers so standalone builds also resolve their references. The final `build/main.pdf` is 45 pages.
- Final visual/layout follow-up removed a table-width overflow in Chapter 1 by eliminating unnecessary inter-column padding. The master and affected standalone chapters were rebuilt afterward.
- Expanded the general State of the Art after a targeted 2026-10-07 Crossref/publisher search. Added verified references for classical/contemporary constraint-enforcement reviews, DAE aspects of multibody dynamics, projection energy behavior, drift elimination, vehicle-system numerical methods, flexible multibody dynamics, and Lie-group error analysis. The section now covers formulation and coordinate choices, DAE index/conditioning, enforcement families, integration/application trends, V&V, open challenges, and an explicit non-systematic search boundary. The refreshed master build resolves all added citations and has no overflow/fatal errors.
- Release boundary: this is a reproducible, internally verified manuscript draft, not an empirically validated engineering model. No physical measurement comparison, broad benchmark study, or near-singularity stress test was performed. These limits are stated in the book and source map.
