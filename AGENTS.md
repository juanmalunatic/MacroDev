# AGENTS.md

## Project purpose

This repository is a plain-text knowledge base and reproducible workspace for UTDT Macro-Development / Development Economics problem sets.

The intended workflow is:

- ChatGPT helps parse theory, problem statements, equations, and solution strategy.
- Codex implements scripts, tables, figures, and reproducible outputs.
- `docs/` and `data/` are source context.
- `solved/` contains generated work by problem set.

## Repository map

- `data/`: raw or provided datasets. Treat as read-only unless explicitly instructed.
- `docs/theory/`: transcribed lecture notes, slides, and theory context.
- `docs/problem_sets/`: transcribed problem statements and instructions.
- `solved/<problem_set>/`: working folder for each solved problem set.
- `solved/<problem_set>/code/`: scripts, generated tables, figures, logs.
- `solved/<problem_set>/latex/`: final writeups, LaTeX, Markdown, PDFs.

## Source-of-truth rules

1. Do not edit, rename, move, or overwrite files in `docs/` or `data/`.
2. Treat `docs/` as the source of theory/problem text.
3. Treat `data/` as the source of empirical inputs.
4. Put all generated work under the relevant `solved/<problem_set>/` folder.
5. Do not solve extra exercises beyond the requested task.
6. Do not invent missing data, file names, parameters, or assumptions. If something is missing, stop and state exactly what is needed.

## Task workflow

Before making changes:

1. Read the local `AGENTS.md` files that apply.
2. Read the relevant `DESIGN.md` or `PLAN.md` if present.
3. Read the relevant problem statement from `docs/problem_sets/`.
4. Read only the theory documents needed for the selected task.
5. Identify expected outputs before coding.

During work:

1. Make small, scoped changes.
2. Prefer reproducible scripts over manual notebook-style work.
3. Use relative paths from the active problem-set folder.
4. Save intermediate outputs in a clear generated-output folder.
5. Keep code and final writeup separate.
6. Record commands needed to reproduce the result.

After work:

1. Run the relevant script/check.
2. Confirm output files were created.
3. Summarize files changed, commands run, and any assumptions.
4. Flag unresolved issues or missing data clearly.

## Coding defaults

- Prefer Python for empirical work unless the task clearly calls for another language.
- Prefer plain `.py` scripts over notebooks.
- Use existing project dependencies when available.
- Ask before installing new packages.
- Reasonable default Python stack: `pandas`, `numpy`, `scipy`, `matplotlib`, `openpyxl`.
- Do not use internet access unless explicitly requested.
- Set random seeds for any stochastic simulation.
- Make scripts re-runnable from a clean checkout.
- Avoid hard-coded absolute paths.
- Keep input paths and output paths declared near the top of scripts.

## Math and writeup defaults

- Use LaTeX for equations.
- Preserve original notation when possible.
- Use `\ln` for natural logs.
- Clearly distinguish data objects from model objects.
- When normalizing to the US, state the normalization explicitly.
- When doing variance/covariance decompositions, state the exact formula used.
- Tables should have readable labels and units.
- Figures should have titles, axis labels, legends, and saved image files.

## Safety and cleanliness

- Do not run destructive commands such as deleting folders, mass-renaming files, or overwriting source files.
- Do not commit changes unless explicitly asked.
- Do not create large binary artifacts unless needed.
- Keep generated files organized and easy to delete/rebuild.