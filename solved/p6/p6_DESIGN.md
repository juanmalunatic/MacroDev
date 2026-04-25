# p6_DESIGN.md — PS6 Part III, Problem 4

## Purpose

This file is the durable implementation handoff for `solved/p6/`.

`p6_AGENTS.md` controls folder discipline and general process. This file controls the selected empirical task, the current implementation state, and future non-destructive changes.

## Current repository convention

Use the actual file names in this repository:

```text
solved/p6/p6_AGENTS.md
solved/p6/p6_DESIGN.md
solved/p6/code/
solved/p6/latex/
```

Treat these as read-only unless explicitly instructed:

```text
data/
docs/
solved/p6/latex/
```

Do not modify human-written LaTeX files in `solved/p6/latex/` from Codex unless the user explicitly asks.

## Incremental workflow rule

Before creating or rewriting anything, Codex must inspect the current state of the repository.

1. Read `solved/p6/p6_AGENTS.md`.
2. Read this file.
3. Inspect relevant existing scripts and outputs.
4. If an existing component already satisfies the specification, do not rewrite it.
5. If an existing component mostly satisfies the specification but has gaps, patch only the missing or incorrect pieces.
6. If a new component is requested, add it without deleting or reconstructing completed work.
7. The Python scripts may regenerate output files on every run. That is expected.
8. The restriction is against rewriting completed source code from scratch, not against reproducibly overwriting generated outputs.

## Current implementation state

### Frozen benchmark script

The original monolithic implementation is frozen and should remain untouched:

```text
solved/p6/code/p6_part3_p4_item_a.py
```

It implements PS6 Part III, Problem 4, items (a), (b), and (c), and acts as the numerical benchmark for the refactored pipeline.

### Submission-quality refactored pipeline

The submission-quality implementation is split into two layers:

```text
solved/p6/code/p6_part3_p4_unified_data.py
solved/p6/code/p6_part3_p4_unified_modeling.py
```

Run from the repository root:

```bash
py solved/p6/code/p6_part3_p4_unified_data.py
py solved/p6/code/p6_part3_p4_unified_modeling.py
```

If the local environment requires it:

```powershell
$env:PYTHONPATH='C:\AcademicRepos\MacroDevBase\.venv\Lib\site-packages'
py solved/p6/code/p6_part3_p4_unified_data.py
py solved/p6/code/p6_part3_p4_unified_modeling.py
```

The scripts must not depend on absolute paths.

## Data inputs

Use exactly:

```text
data/Barro_Lee.xls
data/pwt1001.xlsx
```

Use the most recent common year available in Barro-Lee and PWT. In this repository, Barro-Lee ends in 2010, so:

```python
YEAR = 2010
```

## Economic constants and notation

Use natural logs.

```python
YEAR = 2010
US_CODE = "USA"
GAMMA = 1 / 3
CAPITAL_EXPONENT = GAMMA / (1 - GAMMA)
BAR_R = 0.08

EDUCATION_GROUPS = ["no_schooling", "primary", "secondary", "tertiary"]

SCHOOLING_YEARS = {
    "no_schooling": 0,
    "primary": 6,
    "secondary": 12,
    "tertiary": 17,
}

Z_LOG_BY_GROUP = {
    "no_schooling": 0.28,
    "primary": 0.60,
    "secondary": 0.93,
    "tertiary": 1.20,
}
```

Construct:

```python
Z_BY_GROUP = {group: np.exp(z) for group, z in Z_LOG_BY_GROUP.items()}
```

The firm-productivity object is:

\[
\tilde A_c = \left(\sum_i \theta_{i,c} Z_i^2\right)^{1/2}.
\]

Do not call this object plain `A_c` unless clearly distinguishing it from the unknown-scaled object:

\[
A_c = C\tilde A_c.
\]

The unknown constant cancels under US normalization:

\[
\ln\frac{A_c}{A_U}
=
\ln\frac{C\tilde A_c}{C\tilde A_U}
=
\ln\frac{\tilde A_c}{\tilde A_U}.
\]

## PWT mapping

Use:

\[
y_c = \frac{Y_c}{N_c} = \frac{\texttt{rgdpo}_c}{\texttt{emp}_c},
\]

\[
\frac{K_c}{Y_c} = \frac{\texttt{cn}_c}{\texttt{rgdpo}_c},
\]

\[
h_c = \texttt{hc}_c.
\]

Important: `hc` from PWT is a human-capital index in levels. It corresponds to \(h_c\), not to \(\bar r\bar s_c\). Since the accounting equation is in logs:

\[
\ln h_c = \ln(\texttt{hc}_c).
\]

Use PWT columns:

```text
countrycode
country
year
rgdpo
emp
cn
hc
```

Do not use `pop` for the main calculation.

## Barro-Lee mapping

Use observations for population aged 25 and over.

Correct mapping:

\[
\theta_{0,c} = \text{No Schooling}_c,
\]

\[
\theta_{1,c} = \text{Primary Total}_c,
\]

\[
\theta_{2,c} = \text{Secondary Total}_c,
\]

\[
\theta_{3,c} = \text{Tertiary Total}_c.
\]

Use the `Total` columns, not the `Completed` columns. The `Completed` columns are subsets of the corresponding `Total` columns. Do not add them again.

Convert percentages to shares by dividing by 100. Then renormalize the four shares so they sum to one:

\[
\theta_{i,c}^{norm} = \frac{\theta_{i,c}}{\sum_j \theta_{j,c}}.
\]

This renormalization is only for rounding or formatting issues. It must not hide a wrong mapping that double-counts `Completed` columns.

## Country merge

PWT has `countrycode`; Barro-Lee may only have country names.

Use a country-name normalization helper and a small alias dictionary as needed.

Do not silently proceed if the matched sample is implausibly small. Fail if fewer than 80 countries match.

Keep unmatched diagnostics in the output folder.

## Output folder

The refactored pipeline writes all new outputs under:

```text
solved/p6/code/output/unified/
```

## Unified data layer

Script:

```text
solved/p6/code/p6_part3_p4_unified_data.py
```

Purpose: load raw PWT and Barro-Lee, normalize country names, merge countries, keep the selected year, build education shares, and produce a clean base country-level dataset.

Required main output:

```text
solved/p6/code/output/unified/p6_p4_unified_base_data.csv
```

Required diagnostics and checks:

```text
solved/p6/code/output/unified/p6_p4_unified_data_summary.txt
solved/p6/code/output/unified/p6_p4_unmatched_barro_lee.csv
solved/p6/code/output/unified/p6_p4_unmatched_pwt.csv
solved/p6/code/output/unified/p6_p4_unified_data_benchmark_check.csv
solved/p6/code/output/unified/p6_p4_unified_data_benchmark_check.md
```

The unified base data should include at least:

```text
countrycode
country
country_norm
country_barro_lee
year
rgdpo
emp
cn
hc
no_schooling_raw_pct
primary_total_raw_pct
secondary_total_raw_pct
tertiary_total_raw_pct
theta_no_schooling
theta_primary
theta_secondary
theta_tertiary
theta_sum
theta_sum_before_norm
```

The data layer should not compute model objects such as `tilde_A`, `y_observed`, `K_over_Y`, log-relative variables, residuals, or variance decompositions.

Benchmark against the frozen output:

```text
solved/p6/code/output/p6_p4_item_a_country_level.csv
```

Required data-layer checks:

1. Input files exist.
2. `YEAR == 2010` exists in PWT and Barro-Lee.
3. Required PWT columns exist.
4. Barro-Lee columns are mapped correctly.
5. Education shares are nonnegative.
6. Education shares sum to one after normalization.
7. The United States exists.
8. Matched sample has at least 80 countries.
9. Benchmark comparison passes.

## Unified modeling layer

Script:

```text
solved/p6/code/p6_part3_p4_unified_modeling.py
```

Purpose: load only the unified base dataset and compute the model, figures, tables, and benchmark checks.

The modeling script must load only:

```text
solved/p6/code/output/unified/p6_p4_unified_base_data.csv
```

It should not load raw PWT or raw Barro-Lee.

If the unified base dataset is missing, stop with a clear error instructing the user to run:

```bash
py solved/p6/code/p6_part3_p4_unified_data.py
```

Required main output:

```text
solved/p6/code/output/unified/p6_p4_unified_country_level.csv
```

Required modeling summaries and checks:

```text
solved/p6/code/output/unified/p6_p4_unified_modeling_summary.txt
solved/p6/code/output/unified/p6_p4_unified_modeling_benchmark_check.csv
solved/p6/code/output/unified/p6_p4_unified_modeling_benchmark_check.md
```

The country-level output should include at least:

```text
Z_no_schooling
Z_primary
Z_secondary
Z_tertiary
tilde_A
y_observed
K_over_Y
h
ln_y_rel_us
ln_tilde_A_rel_us
ln_K_over_Y_rel_us
ln_h_rel_us
ln_yhat_with_A_rel_us
ln_yhat_without_A_rel_us
ln_capital_factor_rel_us
residual
```

## Item (a) figures

Main report figures must be PDF and in Spanish:

```text
solved/p6/code/output/unified/p6_p4_unified_item_a_with_A_relative.pdf
solved/p6/code/output/unified/p6_p4_unified_item_a_without_A_relative.pdf
```

Both figures should use US-relative log variables, fixed shared axis limits, and a 45-degree line. Axis limits must be chosen so no points are dropped.

All visible figure text must be in Spanish.

Absolute debug figures are also generated for comparison/debugging:

```text
solved/p6/code/output/unified/p6_p4_unified_item_a_with_A_absolute_debug.pdf
solved/p6/code/output/unified/p6_p4_unified_item_a_without_A_absolute_debug.pdf
```

For absolute debug figures, use the US anchor:

\[
\widehat{\ln y_c}^{abs}
=
\ln y_U
+
\widehat{\ln(y_c/y_U)}.
\]

This is only for debugging and comparison with classmates. It is not the main object for the report.

## Item (b) variance decomposition

Use:

\[
\ell^y_c \equiv \ln\frac{y_c}{y_U},
\]

\[
\ell^A_c \equiv \ln\frac{\tilde A_c}{\tilde A_U},
\]

\[
\ell^K_c \equiv
\frac{\gamma}{1-\gamma}
\ln\left(
\frac{K_c/Y_c}{K_U/Y_U}
\right),
\]

\[
\ell^h_c \equiv \ln\frac{h_c}{h_U}.
\]

The residual is:

\[
\varepsilon_c
=
\ell^y_c
-
\ell^A_c
-
\ell^K_c
-
\ell^h_c.
\]

For each component:

\[
s_x =
\frac{\operatorname{Cov}(x_c,\ell^y_c)}
{\operatorname{Var}(\ell^y_c)}.
\]

Required outputs:

```text
solved/p6/code/output/unified/p6_p4_unified_item_b_variance_decomposition.csv
solved/p6/code/output/unified/p6_p4_unified_item_b_variance_decomposition.md
solved/p6/code/output/unified/p6_p4_unified_item_b_variance_decomposition.tex
```

The LaTeX output should be a table environment only, using `booktabs` style.

## Item (c) education contribution

Education affects income through two channels:

```text
firm_productivity
worker_human_capital
```

Compute:

```text
firm_productivity_education_channel = share(firm_productivity)
worker_human_capital_channel = share(worker_human_capital)
total_education_contribution = firm_productivity_education_channel + worker_human_capital_channel
human_capital_only = worker_human_capital_channel
added_contribution_from_firm_productivity = firm_productivity_education_channel
ratio_total_to_human_capital_only = total_education_contribution / human_capital_only
```

Required outputs:

```text
solved/p6/code/output/unified/p6_p4_unified_item_c_education_contribution.csv
solved/p6/code/output/unified/p6_p4_unified_item_c_education_contribution.md
solved/p6/code/output/unified/p6_p4_unified_item_c_education_contribution.tex
```

The LaTeX output should be a table environment only, using `booktabs` style.

## Optional education-parameter table

Optional, only if easy and non-invasive:

```text
solved/p6/code/output/unified/p6_p4_unified_education_parameters.md
solved/p6/code/output/unified/p6_p4_unified_education_parameters.tex
```

Columns:

```text
i
grupo
s_i
z_i
Z_i
h_i
```

Use \(h_i=\exp(0.08s_i)\) only as a statement/table sanity check. It is not the worker-human-capital series used in the empirical computation.

## Required benchmark checks

The unified pipeline must benchmark against the frozen outputs.

Data-layer benchmark:

```text
solved/p6/code/output/p6_p4_item_a_country_level.csv
```

Modeling-layer benchmark:

```text
solved/p6/code/output/p6_p4_item_a_country_level.csv
solved/p6/code/output/p6_p4_item_b_variance_decomposition.csv
solved/p6/code/output/p6_p4_item_c_education_contribution.csv
```

If any benchmark comparison fails, stop with a clear error explaining which column or table differs and by how much.

Use a tight tolerance:

```python
NUMERIC_TOLERANCE = 1e-10
```

## Current accepted run status

The current accepted run has:

```text
Unified merged sample size: 139
Maximum benchmark difference: 2.910e-11
Item (b) share sum: 1.000000000000
Item (b) max absolute reconstruction error: 8.882e-16
Remaining unmatched Barro-Lee countries: 6
Remaining unmatched PWT countries: 43
```

Unified summary files now use repository-relative paths in human-readable summary output and console reporting.

Known unresolved data/matching issues:

```text
Barro-Lee unmatched:
Afghanistan
Cuba
Libyan Arab Jamahiriya
Papua New Guinea
Reunion
Tonga
```

Guyana is dropped because PWT 2010 has missing `cn`.

These are not currently blocking because benchmark checks pass and the final sample is large enough.

## Future change protocol

For future changes:

1. Preserve the frozen benchmark script unless explicitly instructed.
2. Prefer modifying the unified scripts, not the benchmark script.
3. Re-run both unified scripts.
4. Check benchmark files.
5. Commit in small logical commits.
6. Report a compare link.

For figure-only changes, modify only:

```text
solved/p6/code/p6_part3_p4_unified_modeling.py
```

and regenerated files under:

```text
solved/p6/code/output/unified/
```

For data-mapping changes, modify only:

```text
solved/p6/code/p6_part3_p4_unified_data.py
```

and rerun both unified scripts.

## Recommended cleanup backlog

These are low-priority improvements, not blockers:

1. Optionally add a raw merged-data diagnostic file before dropping missing/non-positive PWT variables.
2. Optionally create the education-parameter table in Markdown/LaTeX if it helps the final report.
3. Optionally align `p6_AGENTS.md` wording with the actual `p6_AGENTS.md` / `p6_DESIGN.md` filenames.

## Completed cleanup note

The relative-path summary cleanup has already been completed in the unified scripts. Human-readable summary files and console reporting now use repository-relative paths instead of absolute local Windows paths.

## Expected Codex final response for future changes

Codex should report only:

1. files created or modified;
2. commands used to reproduce;
3. whether the frozen benchmark script was left untouched;
4. output paths relevant to the change;
5. benchmark checks passed;
6. unresolved matching/data issues, if any.

Do not present unverified numerical results as final.

Do not modify manual LaTeX unless explicitly instructed.
