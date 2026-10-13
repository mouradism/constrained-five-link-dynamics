# Project Conventions

## Document and build

- Main class: `book`, 11 pt, one-sided A4, 30 mm margins.
- Use the shared `preamble.tex` and `macros.tex` for master and standalone chapter builds.
- Use pdfLaTeX for the current scaffold. Build outputs and auxiliary files go under ignored `build/`.
- Run `scripts/build_book.ps1` from PowerShell to compile all standalone chapters with BibTeX and then build the assembled book; the script reports unresolved citations/references and overfull boxes.
- Use the `subfiles` package for standalone chapter compilation. Compile commands are run from the project root.

## Typography and structure

- Use the standard LaTeX Computer Modern family with T1 font encoding and `microtype`; revisit after the pilot PDF is reviewed.
- Keep heading hierarchy semantic: `\chapter`, `\section`, then `\subsection`.
- Each numbered chapter begins with a focused State of the Art section and follows the chapter template in `templates/chapter_template.tex`.
- Use figures only when they clarify a concept or result; provide captions and stable labels.

## Citations and references

- Use BibTeX with numeric citations in order of first appearance (`unsrt`).
- Store bibliography records in `references.bib`; citation keys use lowercase author/topic/year identifiers.
- Use `\label{eq:...}` for equations, `\label{fig:...}` for figures, and `\label{chap:...}` for chapters/sections when cross-referenced.
- Standalone chapters load the shared bibliography when compiled directly; the master document prints the bibliography once at the end.

## Technical notation and units

- Use SI units. Report units with numerical parameters and figure axes.
- In planar rigid-body coordinates, order each body's coordinates as `(x, y, theta)` and use world `y` positive upward.
- In the double-pendulum example, `theta_1` and `theta_2` are absolute angles, positive clockwise from the downward vertical; world `y` is positive upward. Define this convention wherever the model is introduced.
- For the unconstrained Lagrange example, write `M(q) qddot + h(q,qdot) = Q_ext`; `h` contains velocity-coupling and potential/gravity terms, while `Q_ext` contains applied nonconservative generalized forces such as torques.
- For the five-link Cartesian center-of-mass model, the mass matrix is constant and the velocity-dependent inertial bias is zero. Define `Q_total = Q_ext + Q_g`, with `Q_g = -dV/dq`; use `M qddot + J^T lambda = Q_total` together with the relevant acceleration constraint.
- Keep ideal acceleration constraints distinct from numerical drift stabilization terms.

## Symbolic and executable work

- Use Python/SymPy to derive symbolic equations for each worked dynamics example. Keep physical parameters symbolic during derivation and verify extracted equations by simplifying residuals.
- Substitute numerical values only after symbolic derivation when preparing numerical functions, integration, and plots.
- Use Jupyter notebooks for pedagogical, multi-step derivations; use a focused Python script only when interaction and displayed intermediate work are unnecessary.
- Chapters contain equations, explanatory prose, figures, and language-neutral pseudocode. Full Python listings belong in the implementation appendix.
