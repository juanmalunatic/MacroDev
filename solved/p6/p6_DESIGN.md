# p6_DESIGN.md — PS6 Part III, Problem 4

## Purpose

This file is the incremental implementation handoff for `solved/p6/`.

It guides Codex to implement, validate, and refactor the empirical work for PS6, Part III, Problem 4 without rewriting the whole folder or touching manual LaTeX.

`p6_AGENTS.md` controls folder discipline and process. This file controls the selected math/economic task and the current implementation plan.

## Current repository convention

Use the real file names in this repository:

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

Do not modify human-written LaTeX files in `solved/p6/latex/`.

## Incremental workflow rule

Before creating or rewriting anything, inspect the current state of the repository.

1. Read `solved/p6/p6_AGENTS.md`.
2. Read this file.
3. Inspect the relevant existing scripts and outputs.
4. If an existing component already satisfies the specification, do not rewrite it.
5. If an existing component mostly satisfies the specification but has gaps, patch only the missing or incorrect pieces.
6. If a new component is requested, add it without deleting or reconstructing completed work.
7. Do not delete or reconstruct unrelated PS6 work.
8. The Python scripts may regenerate output files on every run. That is expected.
9. The restriction is against Codex rewriting completed source code from scratch, not against reproducibly overwriting generated outputs.

## Frozen benchmark implementation

The current script is considered a frozen benchmark:

```text
solved/p6/code/p6_part3_p4_item_a.py
```

It already implements items (a), (b), and (c). Do not edit this script in Phase 4 unless explicitly instructed later.

Use its outputs as the benchmark for validating the refactor:

```text
solved/p6/code/output/p6_p4_item_a_country_level.csv
solved/p6/code/output/p6_p4_item_a_summary.txt
solved/p6/code/output/p6_p4_item_a_with_A.png
solved/p6/code/output/p6_p4_item_a_without_A.png
solved/p6/code/output/p6_p4_item_b_variance_decomposition.csv
solved/p6/code/output/p6_p4_item_b_variance_decomposition.md
solved/p6/code/output/p6_p4_item_b_summary.txt
solved/p6/code/output/p6_p4_item_c_education_contribution.csv
solved/p6/code/output/p6_p4_item_c_education_contribution.md
solved/p6/code/output/p6_p4_item_c_summary.txt
```

The refactor is successful only if the new pipeline reproduces the relevant numerical benchmark outputs up to numerical tolerance.

## Economic constants and notation

Use natural logs.

```python
YEAR = 2010
US_CODE = "USA"
GAMMA = 1 / 3
CAPITAL_EXPONENT = GAMMA / (1 - GAMMA)  # equals 1/2
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

Z_BY_GROUP = {group: np.exp(z) for group, z in Z_LOG_BY_GROUP.items()}
```

The firm-productivity object is:

\[
\tilde A_c = \left(\sum_i \theta_{i,c} Z_i^2\right)^{1/2}.
\]

Do not call this object plain `A_c` in code unless clearly distinguishing it from:

\[
A_c = C\tilde A_c.
\]

Preferred code name:

```python
tilde_A
```

The unknown constant cancels under US normalization:

\[
\ln\frac{A_c}{A_U}
=
\ln\frac{C\tilde A_c}{C\tilde A_U}
=
\ln\frac{\tilde A_c}{\tilde A_U}.
\]

## Raw data inputs

Use exactly:

```text
data/Barro_Lee.xls
data/pwt1001.xlsx
```

Barro-Lee ends in 2010 in this repository. Use:

```python
YEAR = 2010
```

Use the same year in PWT.

If a required input file is missing, stop with a clear error message.

If reading `.xls` requires `xlrd` and it is not installed, stop with a clear message explaining that `.xls` reading requires `xlrd`.

## PWT mapping

Following the previous development-accounting convention, use:

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

Do not use `pop` for the main calculation. Even though the problem wording says per capita, the model equation and the previous development-accounting convention use output per worker/person engaged:

\[
Y_c/N_c.
\]

## Barro-Lee mapping

Use 2010 observations for population aged 25 and over.

The Excel file may have multi-row headers and merged cells. The loader must handle this robustly.

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

Optional sanity check: if Australia 2010 is available, raw total-category percentages should be approximately:

```text
No Schooling       0.8
Primary Total      6.5
Secondary Total   54.7
Tertiary Total    38.0
```

They should sum to 100.0 before dividing by 100. Do not make the whole script fail solely because this country label is absent or differs slightly.

## Country merge

PWT has `countrycode`; Barro-Lee may only have country names.

Implement or reuse a country-name normalization helper:

```python
def normalize_country_name(name: str) -> str:
    ...
```

The helper should:

- lowercase;
- strip whitespace;
- remove repeated spaces;
- handle simple punctuation differences where safe;
- standardize common alternate names through a small alias dictionary if needed.

Merge on normalized country names unless Barro-Lee has a reliable country-code field.

Do not silently proceed if the matched sample is implausibly small. Fail if fewer than 80 countries match.

Keep unmatched diagnostics in the output folder.

---

# Phase 1 — Frozen benchmark: item (a)

**Status:** implemented and frozen in `p6_part3_p4_item_a.py`.

No new work is required in this phase.

The benchmark computes:

\[
\ln\frac{y_c}{y_U}
=
\ln(y_c)-\ln(y_U).
\]

Model with aggregate firm productivity:

\[
\left(\widehat{\ln\frac{y_c}{y_U}}\right)_{con}
=
\ln\frac{\tilde A_c}{\tilde A_U}
+
\frac{\gamma}{1-\gamma}
\ln\left(
\frac{K_c/Y_c}{K_U/Y_U}
\right)
+
\ln\frac{h_c}{h_U}.
\]

Model without aggregate firm productivity:

\[
\left(\widehat{\ln\frac{y_c}{y_U}}\right)_{sin}
=
\frac{\gamma}{1-\gamma}
\ln\left(
\frac{K_c/Y_c}{K_U/Y_U}
\right)
+
\ln\frac{h_c}{h_U}.
\]

---

# Phase 2 — Frozen benchmark: item (b)

**Status:** implemented and frozen in `p6_part3_p4_item_a.py`.

No new work is required in this phase.

The benchmark computes variance-decomposition shares:

\[
s_x =
\frac{\operatorname{Cov}(x_c,\ell^y_c)}
{\operatorname{Var}(\ell^y_c)}.
\]

Components:

```text
firm_productivity
capital_factor
worker_human_capital
residual
total
```

The capital factor must include the model exponent:

\[
\ell^K_c =
\frac{\gamma}{1-\gamma}
\ln\left(
\frac{K_c/Y_c}{K_U/Y_U}
\right).
\]

Do not decompose using the raw `ln_K_over_Y_rel_us` without multiplying by `CAPITAL_EXPONENT`.

---

# Phase 3 — Frozen benchmark: item (c)

**Status:** implemented and frozen in `p6_part3_p4_item_a.py`.

No new work is required in this phase.

The benchmark computes:

```text
firm_productivity_education_channel = share(firm_productivity)
worker_human_capital_channel = share(worker_human_capital)
total_education_contribution = firm_productivity_education_channel + worker_human_capital_channel
human_capital_only = worker_human_capital_channel
added_contribution_from_firm_productivity = firm_productivity_education_channel
ratio_total_to_human_capital_only = total_education_contribution / human_capital_only
```

Using writeup notation:

\[
s_{education} = s_A + s_h.
\]

---

# Phase 4 — Non-destructive refactor for submission-quality code

**Status:** not implemented.

## Phase 4 goal

Create a cleaner, two-layer Python implementation suitable for delivery to the professor.

Keep the current benchmark script unchanged:

```text
solved/p6/code/p6_part3_p4_item_a.py
```

Add two new scripts:

```text
solved/p6/code/p6_part3_p4_unified_data.py
solved/p6/code/p6_part3_p4_unified_modeling.py
```

The first script creates a clean unified base dataset from raw PWT + Barro-Lee.

The second script loads only the unified base dataset and performs all model calculations, tables, and figures.

## Phase 4 non-destructive rules

1. Do not edit `solved/p6/code/p6_part3_p4_item_a.py`.
2. Do not delete or rename existing benchmark outputs.
3. Do not edit anything under `solved/p6/latex/`.
4. Do not edit raw inputs under `data/`.
5. Do not edit source documents under `docs/`.
6. Add new files and new outputs only.
7. Every new numerical output must be benchmarked against the existing output where applicable.
8. If a benchmark comparison fails, stop with a clear error explaining which column differs and by how much.

## Phase 4 output folder

Create a separate output folder for the refactor:

```text
solved/p6/code/output/unified/
```

All new generated outputs from Phase 4 should go there.

---

## Phase 4A — Unified data script

Create:

```text
solved/p6/code/p6_part3_p4_unified_data.py
```

This script should only do data loading, cleaning, country matching, and construction of the base country-level dataset.

It must not compute model predictions, variance decompositions, or figures.

### Inputs

```text
data/Barro_Lee.xls
data/pwt1001.xlsx
```

### Required output

```text
solved/p6/code/output/unified/p6_p4_unified_base_data.csv
```

Also create diagnostics and summaries:

```text
solved/p6/code/output/unified/p6_p4_unified_data_summary.txt
solved/p6/code/output/unified/p6_p4_unmatched_barro_lee.csv
solved/p6/code/output/unified/p6_p4_unmatched_pwt.csv
solved/p6/code/output/unified/p6_p4_unified_data_benchmark_check.csv
solved/p6/code/output/unified/p6_p4_unified_data_benchmark_check.md
```

### Required columns in unified base data

Include at least:

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
theta_no_schooling
theta_primary
theta_secondary
theta_tertiary
theta_sum
theta_sum_before_norm
```

Also include if useful:

```text
no_schooling_raw_pct
primary_total_raw_pct
secondary_total_raw_pct
tertiary_total_raw_pct
```

Do not include model-calculated columns like `tilde_A`, `K_over_Y`, `y_observed`, log-relative terms, variance decomposition terms, or education-contribution terms. Those belong in the modeling script.

### Unified data benchmark check

Compare `p6_p4_unified_base_data.csv` against the existing benchmark:

```text
solved/p6/code/output/p6_p4_item_a_country_level.csv
```

For matching `countrycode`, the following columns should match exactly or up to numerical tolerance:

```text
rgdpo
emp
cn
hc
theta_no_schooling
theta_primary
theta_secondary
theta_tertiary
theta_sum
```

If available in the benchmark, also compare:

```text
theta_sum_before_norm
country_norm
country_barro_lee
```

Use a tight numerical tolerance for floating-point values, e.g.:

```python
NUMERIC_TOLERANCE = 1e-10
```

The benchmark check output should include:

```text
column
max_abs_diff
passed
```

The script should raise an error if any required benchmark check fails.

### Unified data script structure

Suggested structure:

```python
from pathlib import Path

import numpy as np
import pandas as pd

YEAR = 2010
NUMERIC_TOLERANCE = 1e-10

def find_repo_root() -> Path:
    ...

def ensure_input_file_exists(path: Path) -> None:
    ...

def normalize_country_name(name: str) -> str:
    ...

def load_pwt_base(pwt_path: Path, year: int) -> pd.DataFrame:
    ...

def load_barro_lee_base(barro_path: Path, year: int) -> pd.DataFrame:
    ...

def build_theta(bl_df: pd.DataFrame) -> pd.DataFrame:
    ...

def merge_base_data(pwt_df: pd.DataFrame, bl_df: pd.DataFrame, output_dir: Path) -> pd.DataFrame:
    ...

def write_unified_base_data(df: pd.DataFrame, output_dir: Path) -> Path:
    ...

def compare_unified_data_to_benchmark(unified_df: pd.DataFrame, benchmark_path: Path, output_dir: Path) -> pd.DataFrame:
    ...

def run() -> None:
    ...

if __name__ == "__main__":
    run()
```

Keep it modular and readable.

---

## Phase 4B — Unified modeling script

Create:

```text
solved/p6/code/p6_part3_p4_unified_modeling.py
```

This script must load only:

```text
solved/p6/code/output/unified/p6_p4_unified_base_data.csv
```

It should not load raw PWT or raw Barro-Lee.

If the unified base dataset is missing, stop with a clear error instructing the user to run:

```bash
py solved/p6/code/p6_part3_p4_unified_data.py
```

### Required outputs

Create:

```text
solved/p6/code/output/unified/p6_p4_unified_country_level.csv
solved/p6/code/output/unified/p6_p4_unified_modeling_summary.txt
solved/p6/code/output/unified/p6_p4_unified_modeling_benchmark_check.csv
solved/p6/code/output/unified/p6_p4_unified_modeling_benchmark_check.md
```

### Required columns in unified country-level output

Include at least all base-data columns plus:

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

### Modeling benchmark check

Compare `p6_p4_unified_country_level.csv` against:

```text
solved/p6/code/output/p6_p4_item_a_country_level.csv
```

For matching `countrycode`, verify that all relevant model and result columns match up to numerical tolerance:

```text
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

Use:

```python
NUMERIC_TOLERANCE = 1e-10
```

If any benchmark check fails, raise an error.

Also compare item (b) and item (c) outputs generated by the unified modeling script against the existing benchmark files:

```text
solved/p6/code/output/p6_p4_item_b_variance_decomposition.csv
solved/p6/code/output/p6_p4_item_c_education_contribution.csv
```

---

## Phase 4B item (a): PDF figures in Spanish

Create main report figures in PDF format.

Required main PDF figures:

```text
solved/p6/code/output/unified/p6_p4_unified_item_a_with_A_relative.pdf
solved/p6/code/output/unified/p6_p4_unified_item_a_without_A_relative.pdf
```

These are the figures intended for the report.

### Main figure axes

Figure with aggregate firm productivity:

Horizontal axis:

\[
\left(\widehat{\ln(y_c/y_U)}\right)_{con}
\]

Vertical axis:

\[
\ln(y_c/y_U)
\]

Figure without aggregate firm productivity:

Horizontal axis:

\[
\left(\widehat{\ln(y_c/y_U)}\right)_{sin}
\]

Vertical axis:

\[
\ln(y_c/y_U)
\]

### Main figure formatting

All visible text in the figures must be in Spanish.

Use titles/labels similar to:

```text
Ingreso observado vs. ingreso explicado
Modelo con productividad agregada de firmas
Modelo sin productividad agregada de firmas
Ingreso explicado relativo a EE.UU. (log)
Ingreso observado relativo a EE.UU. (log)
Año 2010
Línea de 45°
```

Use fixed axis limits across both main figures so they are directly comparable.

The limits must not drop any points.

Recommended approach:

1. Compute min and max across:
   - `ln_y_rel_us`
   - `ln_yhat_with_A_rel_us`
   - `ln_yhat_without_A_rel_us`
2. Add a margin, e.g. 5% of the range.
3. Use the same `(min_limit, max_limit)` for both x-axis and y-axis in both main figures.

Close figures after saving.

Use vector PDF output. Do not save these main report figures only as PNG.

Optional PNG copies are allowed only if explicitly useful, but PDF is required.

Country labels are optional. If labels are used, label only a small set such as:

```text
USA, ARG, AUS, CHN, IND, DEU, BRA, MEX
```

Do not require optional label-adjustment packages.

---

## Phase 4B item (a): absolute debug figures

Create additional debug figures in PDF format using absolute log output.

These are not the main report figures. They are only for debugging and comparison with classmates.

Required debug PDF figures:

```text
solved/p6/code/output/unified/p6_p4_unified_item_a_with_A_absolute_debug.pdf
solved/p6/code/output/unified/p6_p4_unified_item_a_without_A_absolute_debug.pdf
```

### Treatment of the unknown constant in absolute debug figures

The model with \(\tilde A_c\) is identified up to a constant. Therefore, absolute predicted log output must be calibrated.

For debug figures, use the US anchor:

\[
\widehat{\ln y_c}^{abs}
=
\ln y_U
+
\widehat{\ln(y_c/y_U)}.
\]

That is, convert relative model predictions into absolute log-output predictions by adding observed US log output.

This makes the United States fit exactly by construction and is only a normalization for debugging. Make this clear in titles, labels, or summary text.

Create:

```python
ln_y_abs = np.log(y_observed)
ln_yhat_with_A_abs_us_anchor = np.log(y_US) + ln_yhat_with_A_rel_us
ln_yhat_without_A_abs_us_anchor = np.log(y_US) + ln_yhat_without_A_rel_us
```

### Absolute debug figure formatting

All visible text must be in Spanish.

Use titles/labels similar to:

```text
Figura de depuración: ingreso absoluto observado vs. explicado
Modelo con productividad agregada de firmas, anclado en EE.UU.
Modelo sin productividad agregada de firmas, anclado en EE.UU.
Ingreso explicado absoluto (log, anclado en EE.UU.)
Ingreso observado absoluto (log)
Año 2010
Línea de 45°
```

Use fixed axis limits across both absolute debug figures.

The limits must not drop any points.

Recommended approach:

1. Compute min and max across:
   - `ln_y_abs`
   - `ln_yhat_with_A_abs_us_anchor`
   - `ln_yhat_without_A_abs_us_anchor`
2. Add a margin.
3. Use the same limits for both x and y in both absolute debug figures.

---

## Phase 4B item (b): tables in CSV, Markdown, and LaTeX

Generate item (b) variance-decomposition tables from the unified modeling script.

Required outputs:

```text
solved/p6/code/output/unified/p6_p4_unified_item_b_variance_decomposition.csv
solved/p6/code/output/unified/p6_p4_unified_item_b_variance_decomposition.md
solved/p6/code/output/unified/p6_p4_unified_item_b_variance_decomposition.tex
```

The CSV/Markdown table should include at least:

```text
component
share
covariance_with_ln_y
variance_ln_y
```

Use Spanish labels in Markdown and LaTeX where appropriate.

Suggested Spanish display labels:

```text
Productividad de firmas
Factor capital
Capital humano trabajadores
Residuo
Total
```

The LaTeX table should use the style:

```latex
\begin{table}[H]
    \centering
    \begin{tabular}{lrrr}
        \toprule
        Componente & Participación & Covarianza con $\ell^y_c$ & Varianza de $\ell^y_c$ \\
        \midrule
        ...
        \bottomrule
    \end{tabular}

    \caption{Descomposición de varianza del ingreso relativo.}
    \label{tab:p6_p4_var_decomp}
\end{table}
```

Use `booktabs` conventions: `\toprule`, `\midrule`, `\bottomrule`.

Do not include a full LaTeX document preamble. Output only the table environment.

---

## Phase 4B item (c): tables in CSV, Markdown, and LaTeX

Generate item (c) education-contribution tables from the unified modeling script.

Required outputs:

```text
solved/p6/code/output/unified/p6_p4_unified_item_c_education_contribution.csv
solved/p6/code/output/unified/p6_p4_unified_item_c_education_contribution.md
solved/p6/code/output/unified/p6_p4_unified_item_c_education_contribution.tex
```

The CSV/Markdown table should include at least:

```text
concept
value
```

Use Spanish labels in Markdown and LaTeX where appropriate.

Suggested Spanish display labels:

```text
Canal productividad de firmas
Canal capital humano trabajadores
Contribución total de educación
Capital humano solamente
Contribución adicional del canal firmas
Ratio total / capital humano
```

The LaTeX table should use the style:

```latex
\begin{table}[H]
    \centering
    \begin{tabular}{lr}
        \toprule
        Concepto & Valor \\
        \midrule
        ...
        \bottomrule
    \end{tabular}

    \caption{Contribución total de la educación.}
    \label{tab:p6_p4_education_contribution}
\end{table}
```

Use `booktabs` conventions.

Do not include a full LaTeX document preamble. Output only the table environment.

---

## Phase 4B optional parameter table

If useful, create a small parameter table for the education groups.

Required only if easy and non-invasive:

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

Spanish group labels:

```text
Sin escolaridad
Primaria
Secundaria
Superior
```

Use \(h_i=\exp(0.08s_i)\) only as a statement/table sanity check. It is not the worker-human-capital series used in the empirical computation.

LaTeX caption:

```latex
\caption{Tipos educativos, años de escolaridad y productividad emprendedora.}
```

LaTeX label:

```latex
\label{tab:p6_p4_education_parameters}
```

---

## Phase 4B script structure

Suggested structure:

```python
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

YEAR = 2010
US_CODE = "USA"
GAMMA = 1 / 3
CAPITAL_EXPONENT = GAMMA / (1 - GAMMA)
NUMERIC_TOLERANCE = 1e-10

def find_repo_root() -> Path:
    ...

def ensure_input_file_exists(path: Path) -> None:
    ...

def load_unified_base_data(path: Path) -> pd.DataFrame:
    ...

def compute_tilde_A(df: pd.DataFrame) -> pd.DataFrame:
    ...

def add_model_terms(df: pd.DataFrame) -> pd.DataFrame:
    ...

def add_item_b_terms(df: pd.DataFrame) -> tuple[pd.DataFrame, float]:
    ...

def compute_variance_decomposition(df: pd.DataFrame) -> pd.DataFrame:
    ...

def compute_education_contribution(variance_decomposition: pd.DataFrame) -> pd.DataFrame:
    ...

def write_markdown_table(...):
    ...

def write_latex_table(...):
    ...

def make_scatter_plot_pdf(...):
    ...

def compare_modeling_to_benchmark(...):
    ...

def run() -> None:
    ...

if __name__ == "__main__":
    run()
```

Keep code readable and modular.

Avoid duplicated logic.

---

## Phase 4 required checks

The new scripts must check:

### Unified data checks

1. Required input files exist.
2. `YEAR == 2010` exists in PWT and Barro-Lee.
3. Required PWT columns exist.
4. Barro-Lee columns are mapped correctly to no schooling / primary total / secondary total / tertiary total.
5. Education shares are nonnegative.
6. Education shares sum to one after normalization.
7. The United States exists in the merged sample.
8. Matched sample has at least 80 countries.
9. Unified base data benchmark check passes against `p6_p4_item_a_country_level.csv`.

### Unified modeling checks

1. Unified base data file exists.
2. `tilde_A > 0`.
3. `y_observed > 0`, `K_over_Y > 0`, and `h > 0`.
4. US-relative terms are zero for the United States up to tolerance.
5. Benchmark check passes for model columns against `p6_p4_item_a_country_level.csv`.
6. Item (b) decomposition shares sum to one.
7. Item (b) benchmark check passes against `p6_p4_item_b_variance_decomposition.csv`.
8. Item (c) values match definitions.
9. Item (c) benchmark check passes against `p6_p4_item_c_education_contribution.csv`.
10. Main PDF figures exist.
11. Absolute debug PDF figures exist.
12. Markdown and LaTeX table outputs exist.

---

## Phase 4 commands to run

From the repository root:

```bash
py solved/p6/code/p6_part3_p4_unified_data.py
py solved/p6/code/p6_part3_p4_unified_modeling.py
```

If the environment requires the project virtualenv on `PYTHONPATH`, use the known local convention:

```powershell
$env:PYTHONPATH='C:\AcademicRepos\MacroDevBase\.venv\Lib\site-packages'
py solved/p6/code/p6_part3_p4_unified_data.py
py solved/p6/code/p6_part3_p4_unified_modeling.py
```

The scripts themselves must not depend on absolute paths.

---

## Phase 4 expected Codex final response

After implementation and running both scripts, Codex should report only:

1. files created or modified;
2. commands used to reproduce;
3. whether the frozen benchmark script was left untouched;
4. unified base-data output path;
5. unified modeling output path;
6. main report PDF figure paths;
7. absolute debug PDF figure paths;
8. Markdown and LaTeX table paths;
9. benchmark checks passed;
10. unresolved matching/data issues, if any.

Do not present unverified numerical results as final.

Do not modify manual LaTeX.
