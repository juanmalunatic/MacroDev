# AGENTS.md — Problem Set 6

## Scope

This folder is only for Problem Set 6:

**Competencia monopolística, Elección Ocupacional y Contabilidad del Desarrollo**

Work only on the exercise or subproblem explicitly requested by the user or specified in `DESIGN.md`.

Do not solve the whole problem set unless explicitly instructed.

## Required read order

Before coding or writing:

1. Read this file.
2. Read `DESIGN.md` if present.
3. Read the PS6 problem statement in `../../docs/problem_sets/`.
4. Read relevant theory files in `../../docs/theory/` only as needed.

Likely relevant theory sources:

- Competencia monopolística vs. competencia perfecta.
- Entrepreneurial human capital and firm dynamics.
- Empresas y producción agregada.
- Tamaño de firmas y desarrollo.
- Development accounting / human capital, if the selected exercise needs it.

## Folder rules

Use this folder as the working root:

`solved/p6/`

Expected structure:

- `solved/p6/AGENTS.md`
- `solved/p6/DESIGN.md`
- `solved/p6/code/`
- `solved/p6/latex/`

Use:

- `code/` for scripts, generated tables, generated figures, logs, and numerical outputs.
- `latex/` for final written answers, derivations, and report files.
- `DESIGN.md` for the ChatGPT-authored plan/handoff.

Do not place generated PS6 outputs outside `solved/p6/`.

## DESIGN.md authority

`DESIGN.md` is the task handoff from ChatGPT.

It should define:

- selected problem/subproblem,
- solution strategy,
- equations to derive or implement,
- required data,
- expected scripts,
- expected tables/figures,
- validation checks,
- final writeup requirements.

If `DESIGN.md` conflicts with this file:

- this file controls process and folder discipline;
- `DESIGN.md` controls the selected math/economic task.

If `DESIGN.md` is ambiguous, stop and ask for clarification.

## PS6 task boundaries

Problem Set 6 has three broad parts:

1. Competencia monopolística y función de producción agregada.
2. Elección ocupacional con agentes heterogéneos.
3. Educación y desarrollo / Queiró-style development accounting.

When working on one part:

- Do not modify work for other parts.
- Do not create unnecessary infrastructure for the full PS unless requested.
- Keep outputs named by problem number, e.g. `p6_p2_...`, `p6_p4_...`.

## Mathematical conventions

Use the notation from the problem statement unless `DESIGN.md` says otherwise.

Common notation:

- `N`: population or worker mass, depending on section.
- `M`: number/mass of firms or entrepreneurs.
- `L`: employment / labor / human-capital labor input.
- `w`: wage.
- `z_1`: worker ability component.
- `z_2`: entrepreneur ability component.
- `\alpha`: production exponent in occupational-choice entrepreneur technology.
- `\eta`: exponent used in monopolistic-competition derivations, often `\eta = (\sigma - 1)/\sigma`.
- `\sigma`: CES elasticity of substitution.
- `\gamma`: capital share in the Queiró-style production function.
- `\bar r = 0.08`: schooling return parameter in PS6 Part III.
- For PS6 Part III, default values from the statement include `\sigma = 3` and `\gamma = 1/3`.

Use natural logs.

## Numerical work defaults

For numerical equilibrium tasks:

1. Write the market-clearing equation explicitly in code comments.
2. Use robust root-finding.
3. Check that the market-clearing residual is close to zero.
4. Report the equilibrium wage and relevant aggregates.
5. If using simulation, set a fixed random seed and report simulation size.
6. Prefer deterministic quadrature/integration when practical.

For bivariate normal tasks:

- Use the parameters stated in the problem or `DESIGN.md`.
- For baseline numerical exercises, expected values include:
  - `\mu_1 = \mu_2 = 0`
  - `\sigma_1 = \sigma_2 = 1`
  - `\rho = 0.5`
- Vary only the parameter requested by the subproblem.

## Empirical work defaults

For PS6 Part III / Problem 4:

1. Use the most recent common year available across the required datasets.
2. Use PWT and Barro-Lee data only if present in `data/`.
3. If the required data files are missing, stop and list the missing files.
4. Compute education shares so they sum to one:
   - no schooling,
   - primary incomplete + complete,
   - secondary incomplete + complete,
   - higher incomplete + complete.
5. Assume the entrepreneur education distribution equals the population education distribution unless instructed otherwise.
6. Assume firms per capita are constant across countries unless instructed otherwise.
7. Save country-level constructed variables to a CSV.
8. Save plots as image files and, if useful, export tables as CSV/Markdown/LaTeX.

## Validation checks

Always run checks appropriate to the selected task.

Possible checks:

- market-clearing residual is near zero;
- education shares sum to one;
- no negative employment, capital, or human-capital inputs;
- no missing values in final regression/decomposition sample;
- US normalization equals one when used;
- variance decomposition components sum to the target variance up to numerical tolerance;
- generated figures and tables exist at the expected paths.

## Output expectations

At the end of a task, provide:

1. Files changed or created.
2. Exact command(s) to reproduce.
3. Main numerical results or generated artifact paths.
4. Checks performed.
5. Remaining assumptions or unresolved issues.

Do not present unverified results as final.
