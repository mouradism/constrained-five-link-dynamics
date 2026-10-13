# Execution Guide: Iteratively Building the Book

This file explains how to carry out [plan.md](plan.md). The plan defines the book's content and standards; this guide defines the working process. Treat both as living project documents and update them deliberately when the project changes.

## 1. Operating Principles

- Work in small, reviewable increments. Do not draft or finalize the whole book in one pass.
- Keep derivation, exposition, validation, and implementation in their intended places: use Python/SymPy notebooks or scripts to perform symbolic derivations; show the equations and language-neutral pseudocode in chapters; use executable artifacts for numerical checks and computed figures; and place documented Python listings in the end-of-book appendix.
- Validate the smallest affected unit first, then integrate it into the larger book.
- Keep the project buildable throughout development. Early chapters may contain placeholders, but the master build should continue to work.
- Track decisions, open questions, sources, and validation evidence close to the material they affect.
- Revisit earlier chapters when later work changes notation, assumptions, equations, references, or interfaces. Iteration is expected, not a failure of the outline.

## 2. Eight Execution Phases

The phases provide project-level gates, not a one-way waterfall. Phases 1–2 establish the framework; Phases 3–4 prepare and pilot the technical workflow; Phases 5–7 produce and review the complete manuscript; Phase 8 packages the release. Research and revision continue across phases, and work returns to earlier phases whenever evidence requires it.

### Phase 1: Scaffold the project

**Goal:** Establish a safe, buildable workspace without drafting the whole book.

- Review `plan.md`, the existing five-link notebook, Git status, and available LaTeX/Python tools. Preserve current work.
- Create the source tree for `main.tex`, shared preamble/macros, frontmatter and chapter shells, `references.bib`, appendices, figures, and optional validation notebooks/scripts.
- Add minimal placeholders, ignore build output, and establish an initial master build.
- Record the current build/environment baseline and known warnings in `work-log.md`.

**Exit gate:** Source layout exists and placeholder master plus one standalone chapter compile.

### Phase 2: Establish the book framework

**Goal:** Make shared layout, notation, citations, and the chapter template testable.

- Choose document class/layout, heading hierarchy, citation and figure styles, notation, units, label conventions, build commands, and Python/SymPy environments.
- Record decisions in `conventions.md`; create `templates/chapter_template.tex`.
- Pilot with a small chapter section that tests State of the Art heading, equations, citation, figure, standalone build, and master inclusion.

**Exit gate:** The representative chapter compiles standalone and in the master, with citations and figures resolving. Review the pilot PDF before scaling the design.

### Phase 3: Research and prepare

**Goal:** Make each upcoming work unit ready to draft without pretending the entire literature review is complete.

- Maintain `research/phase3_source_map.md` with each frontmatter/chapter purpose, research questions, source candidates and verification status, dependencies, open decisions, and readiness.
- Map accepted sources to claims and chapters in `references.bib`; record coverage boundaries for general and chapter-specific State of the Art reviews.
- Plan symbolic Python/SymPy artifacts for worked dynamics derivations, plus numerical checks and figures where needed.
- Prepare one bounded next work unit at a time. Research continues during later drafting phases.

**Exit gate:** The next work unit has a reader purpose, outline, assumptions, dependencies, source needs, and measurable completion checks. A literature section is not considered complete until its scoped search and source checks are recorded.

### Phase 4: Pilot a complete technical example

**Goal:** Prove that the book can explain a worked example from physical assumptions through equations to numerical behavior.

- Use the double pendulum to complete and refine the Chapter 4 derivation, SymPy artifact, first-order ODE, numerical run, energy check, and figures.
- Keep the manuscript explanation synchronized with the notebook, but put no executable Python in the chapter.
- Use the pilot to refine notation, chapter flow, figure/caption conventions, validation reporting, and the implementation-appendix pattern.

**Exit gate:** Chapter 4 is a coherent technical draft; its equations match the executed symbolic artifact; its example runs reproducibly; and the standalone/master builds pass. Its State of the Art may remain open but must be tracked explicitly before whole-book completion.

### Phase 5: Draft the core mechanics chapters

**Goal:** Explain the modeling and constrained dynamics foundations needed for the five-link case study.

- Draft Chapters 1–3 and 5–8: formulations, mechanism assumptions, coordinates/kinematics, loop constraints, constraint derivatives, KKT dynamics, and consistent initial conditions.
- Work in dependency order: mechanism and coordinates before constraints; constraints and derivatives before the KKT system; KKT system before initial consistency.
- Use the existing five-link notebook as the executable source of symbolic and numerical facts. Update it only when a defined work unit requires a change; preserve existing user modifications.
- Compile a chapter standalone when its work unit stabilizes and integrate it into `main.tex` at checkpoints.

**Exit gate:** Each core chapter has a complete technical draft, resolved assumptions/notation, its required State of the Art subsection drafted or explicitly queued for Phase 7 completion, and relevant equations checked against the notebook or independent derivation.

### Phase 6: Draft simulation, evidence, and end matter

**Goal:** Complete the book’s numerical-method, results, scope, and implementation material.

- Draft Chapters 9–12: integration/drift, verification/validation, results/visualization, and limitations/extensions.
- Draft the general introduction and general State of the Art as the overall argument and chapter structure become stable; retain a broad survey distinct from chapter reviews.
- Complete the Python implementation appendix from the canonical notebooks/scripts. Generate numerical figures reproducibly and record input parameters/software versions.
- Check that every worked dynamics derivation has a Python/SymPy artifact and every worked numerical example has an appropriate executable validation artifact.

**Exit gate:** Every planned frontmatter/chapter/appendix section has a complete first draft, all worked examples have their canonical executable artifacts, and every planned figure has a source or an explicit reason it is direct/analytical.

### Phase 7: Whole-book review and revision

**Goal:** Turn complete drafts into one technically consistent, properly sourced manuscript.

- Complete the book-level and all chapter-level State of the Art reviews with recorded scope/search dates and verified citations.
- Review equations, units, sign conventions, assumptions, constraint rank, force notation, and numerical claims across chapters.
- Run notebooks from clean kernels and scripts in fresh processes; check position and velocity closure throughout constrained trajectories, energy behavior where relevant, solver status, and sensitivity to settings.
- Conduct technical, reference, editorial, and reader-flow reviews. Resolve findings and repeat affected work units until their acceptance checks pass.

**Exit gate:** Every planned chapter has passed technical and editorial checks; literature reviews are complete to their stated scopes; examples and figures are reproducible; and no unresolved issue is hidden or mislabeled as done.

### Phase 8: Integrate and release

**Goal:** Produce and verify the final complete book artifact.

- Run clean standalone chapter builds and the full master build, including BibTeX processing; resolve LaTeX errors, undefined labels/citations, duplicate labels, and numbering/figure-path problems.
- Regenerate computed figures from canonical artifacts and verify the final Python appendix matches them.
- Read the assembled book front to back and confirm limitations, source credits, build instructions, software versions, and known issues are documented.
- Archive or publish the agreed outputs and record final build and validation results in `work-log.md`.

**Exit gate:** The complete manuscript is present, all final builds and validation checks pass, reproducibility information is recorded, and release artifacts are ready. If any content or review gate fails, return to Phases 3–7 as appropriate; Phase 8 does not conceal unfinished chapters.

### Verified project status (2026-10-07)

| Phase | Status | Evidence / remaining gate |
| --- | --- | --- |
| 1. Scaffold | Complete | All planned source/artifact paths exist, including optional scripts guidance; master and standalone Chapter 1 placeholders compiled; baseline in `work-log.md`. |
| 2. Framework | Complete, provisional | `conventions.md` and template exist; template compiles standalone; Chapter 4 pilot tested standalone/master with citation and figure paths. |
| 3. Research and prepare | Complete with bounded scope | Source map and metadata-checked references support focused foundational/software reviews; the manuscript explicitly disclaims systematic or exhaustive current-literature coverage. |
| 4. Technical pilot | Complete | Chapter 4 and its sequentially rerun SymPy notebook agree; the 10 s integration and figures regenerated, and the chapter builds standalone and in the master. |
| 5. Core mechanics chapters | Complete as a verified draft | Chapters 1–3 and 5–8 have technical drafts, standalone builds, and checks against the five-link symbolic/numeric model; further research-grade review is outside the declared bounded literature scope. |
| 6. Simulation/supporting chapters | Complete as a first manuscript draft | Chapters 9–12, frontmatter, generated figures, and an implementation appendix exist. Appendix kernels are concise extracts; notebooks remain the canonical full derivations and validation artifacts. |
| 7. Whole-book review | Complete for the declared scope | Equation/sign conventions and reproducibility claims were checked against both notebooks; sensitivity evidence and limitations are recorded; remaining risks are explicit (no experimental validation, singularity stress test, or broad benchmark study). |
| 8. Release | Complete for the reproducible draft | All 12 standalone chapters and the master build pass with citations/labels resolved and no overfull boxes; release artifact and exact scope/limitations are recorded in `work-log.md`. |

## 3. Select the Next Work Unit

Choose one bounded unit for each cycle. Examples include:

- One subsection of a chapter, such as the derivation of a pin constraint.
- One equation chain, such as positions to velocities to double-pendulum energies.
- One literature review topic and its sources.
- One numerical validation, notebook/script, or generated figure.
- One chapter-level integration or copyedit pass.

Before starting a unit, write down:

- **Target:** exact file and subsection, notebook cell group, or shared convention being changed.
- **Purpose:** what the reader should understand or what question the work should answer.
- **Inputs:** relevant plan section, source references, notation, notebook outputs, and dependencies on other chapters.
- **Done when:** observable acceptance checks for this unit.
- **Open questions:** unresolved technical or editorial decisions. Do not silently invent important physical assumptions.

Prefer a unit whose output can be checked without waiting for the rest of the book to be complete.

## 4. The Repeatable Draft-and-Review Loop

Run this loop for each work unit. Repeat any step that fails or reveals a needed change.

### A. Prepare

1. Read the relevant section of `plan.md`, the current chapter draft, shared conventions, and directly related notebook/source material.
2. Confirm the unit's assumptions, notation, source needs, and completion checks.
3. If the unit depends on a technical fact, derive or verify it before presenting it as established. Mark uncertain claims for research or review.

### B. Research and outline

1. Gather sources appropriate to the claim: foundational sources for established formulations, current literature for the State of the Art, and authoritative documentation for software-specific behavior.
2. Record bibliographic entries in `references.bib` as sources are accepted. Add a short internal note connecting each source to the claim or chapter it supports.
3. Draft a short subsection outline before full prose. Check that it advances the chapter's purpose and does not repeat the general State of the Art or another chapter unnecessarily.
4. State the literature search date or coverage boundary for State of the Art material. Avoid calling a selective review exhaustive.

### C. Draft

1. Write equations with definitions, assumptions, sign conventions, dimensions, and a plain-language interpretation.
2. In chapters, explain algorithms with language-neutral pseudocode only. When a derivation needs executable checking or a figure needs numerical generation, choose the smallest suitable artifact:
	- Use a Jupyter notebook for exploratory work, multi-step examples, interactive derivations, plots, or animations that benefit from narrative and visible intermediate results.
	- Use a focused Python script for a narrow repeatable check, batch figure generation, or validation that does not need notebook interaction.
	- Do not create a notebook or script when equations, symbolic reasoning, or a direct diagram are sufficient. Avoid producing both a notebook and script for the same task unless they have distinct roles.
	Keep executable artifacts in the relevant notebook or scripts area. After validation, include the reader-facing Python implementation in the end-of-book appendix when appropriate; chapters remain free of executable-language code.
3. Add a diagram, plot, or table only when it materially clarifies the subsection. Give it a descriptive caption, a stable label, and a reference in the prose.
4. Keep general results distinct from facts specific to the double pendulum or five-link example.
5. Add cross-references using labels/keys; do not manually guess final equation, figure, chapter, or citation numbers.

### D. Validate the technical content

For a mathematical derivation:

- Check dimensions, units, signs, coordinate ordering, and limiting/special cases.
- Carry out the worked dynamics derivation in Python/SymPy, preserving symbolic parameters and exact expressions until the derivation is complete.
- For Lagrangian systems, form the Euler-Lagrange residual, extract `M` and `h` when the residual is affine in acceleration, and verify the symbolic decomposition simplifies to zero.
- For constrained systems, symbolically derive the position constraints, Jacobian, acceleration bias, and ideal KKT equations. Keep numerical stabilization terms as a distinct variant.
- Verify symbolic identities/residuals, dimensions, and important limiting cases before substituting numerical parameters. Compare with an independent derivation or the numerical implementation where practical.
- Compare against an authoritative source or independent derivation when a sign or convention is uncertain.

For a worked numerical example or any figure requiring computed data:

- Extend the canonical symbolic derivation artifact for simulation and validation where practical. Prefer a Jupyter notebook for a substantial pedagogical example and a focused Python script for a small, automated check or figure task.
- Run notebooks from a clean kernel; run scripts from a fresh process with documented inputs and parameters.
- Check solver success and example-specific residuals or invariants, such as energy for a conservative open-chain example and position/velocity closure for a constrained example.
- Compare the resulting numeric output with the displayed equations and parameter values.
- Regenerate any affected figure and record the notebook or script, parameter values, and software versions.

Do not use a plausible animation as the only validation evidence. Do not impose a universal numeric threshold without relating it to the model, units, and tolerances.

### E. Build and review

1. Compile the affected chapter standalone. Resolve new LaTeX errors, undefined labels, missing citations, and figure-path issues.
2. Review the subsection at reader level: Is the motivation clear? Are variables defined before use? Does each equation follow from the previous one? Are general methods distinguished from example-specific choices?
3. Check bibliography entries and source attributions, including borrowed/adapted figures.
4. If shared notation, macros, references, or chapter interfaces changed, rebuild the master book and inspect affected chapters.
5. Correct issues in the same work unit, then rerun the checks that cover the correction.

### F. Close the cycle

Record the unit's state, validation evidence, references added, files changed, and remaining questions. Then select the next unit based on dependencies and unresolved risks, not merely chapter order. A unit may return to drafting or research after review; do not mark it stable just to keep the sequence moving.

## 5. Work States and Readiness Gates

Use a small status per chapter or work unit; update it as work progresses.

- **Planned:** scope and purpose are known, but prerequisites or outline may be incomplete.
- **Ready:** assumptions, subsection structure, source needs, and completion checks are clear enough to draft.
- **Drafting:** prose/equations/pseudocode are being created; gaps and questions are recorded.
- **Technical review:** derivation and claims are being checked; relevant notebook or script validation may still be in progress.
- **Editorial review:** organization, readability, notation, citations, and visual quality are being checked.
- **Stable for integration:** chapter compiles standalone, technical checks pass, references/figures resolve, and open issues are either closed or explicitly accepted.
- **Integrated:** stable chapter builds successfully in the master book and cross-references are checked.

A chapter can move backward when new evidence requires revision. Keep separate states for a notebook and chapter if one is validated while the other is still being drafted.

A chapter is not **Ready** just because it has a title. A chapter is not **Stable for integration** just because it compiles. Apply the technical and editorial acceptance checks relevant to its scope.

## 6. Integration Checkpoints

Integrate continuously at sensible boundaries rather than waiting until every chapter is finished.

### After shared-layout or convention changes

- Compile the master and representative standalone chapter.
- Check chapter numbering, notation macros, bibliography style, and figure paths.

### After a chapter becomes stable

- Include it in the master build.
- Check chapter order, labels, cross-chapter references, citation visibility, and transitions to adjacent chapters.
- Revisit earlier text if the new chapter changes terminology or assumptions.

### After a related group of chapters

Useful groups include the dynamics derivation and double pendulum, or the constraint and KKT chapters. Review the full conceptual chain across the group and run relevant validation artifacts from a clean state.

### At book-level review

- Read the assembled book in order, including frontmatter, general State of the Art, chapter-level State of the Art sections, appendices, and bibliography.
- Check that the general survey gives a broad map while chapter surveys provide distinct, topic-specific detail.
- Check that the double pendulum serves as a bridge and is not misrepresented as a closed chain.
- Confirm the five-link model's assumptions, coordinate/constraint counts, and solver treatment are consistent everywhere.

## 7. Figure Production Loop

For each figure intended for the book:

1. Identify the concept or result the figure should clarify and where it will be used.
2. Decide whether the figure is analytical/drawn directly or requires computed data. If computation is needed, identify the source notebook or script and exact model parameters/software environment.
3. Run the source notebook from a clean kernel or run the script in a fresh process, then regenerate the figure.
4. Inspect labels, units, sign conventions, framing, and legibility at book scale.
5. Save the figure and editable source, when available, under `figures/`.
6. Add a caption, stable label, in-text reference, and source attribution if applicable.
7. Record the figure provenance so it can be recreated after notebook or parameter changes.

If a diagram can be drawn directly and unambiguously without running a model, do not create executable code just to draw it. Symbolic dynamics derivations are still performed in their canonical Python/SymPy artifact. Generate numerical plots and simulation frames reproducibly from that artifact when practical, and avoid duplicating the same derivation or figure-generation logic in multiple places.

## 8. Iteration and Change Management

- Keep a short work log or issue list with the current focus, decisions made, unresolved questions, and next candidate units.
- Update `plan.md` when book scope, chapter purpose/order, or acceptance requirements change. Keep `execution.md` focused on process; do not duplicate the full technical outline there.
- When notation or a modeling assumption changes, search for dependent equations, pseudocode, symbolic derivation cells/scripts, figures, and appendix listings; update and revalidate every affected artifact.
- When a source changes a literature claim, update the citation and bibliography entry together.
- Make small, meaningful version-control commits after coherent checkpoints. Before committing, inspect the diff and status; never include virtual environments, transient notebook checkpoints, or unrelated files.
- Do not let a convenient build workaround silently become a technical assumption. Record accepted limitations and deferred work explicitly.

## 9. Final Release Procedure

1. Run every validation artifact from a clean state: restart notebooks and run all relevant cells, or run scripts in fresh processes with documented inputs. Confirm expected checks pass.
2. Regenerate all book figures and confirm provenance records match the final parameters and environment.
3. Compile each chapter independently and compile the complete book; resolve errors, undefined references, duplicate labels, citation problems, and inconsistent numbering.
4. Review the equations and examples with a mechanics-focused pass, then review sources and citations, then perform a book-level readability and consistency pass.
5. Confirm all required chapters and frontmatter are present, the Python implementation appendix corresponds to validated notebooks, limitations are stated, and the book provides evidence beyond visualization.
6. Record final build commands, software versions, validation outcomes, and known limitations.

## 10. Cycle Record Template

Copy this for each significant work unit:

```text
Work unit:
Date:
Purpose / reader question:
Files or sections in scope:
Assumptions and notation:
Sources to add or verify:
Definition of done:

Draft status:
Technical checks and results:
Validation artifact (notebook/script/none):
Run command or clean-kernel procedure:
Environment and parameters:
Standalone chapter build:
Master build (if applicable):
Figures regenerated:
Review findings and revisions:
Open questions / accepted limitations:
Next work unit:
```
