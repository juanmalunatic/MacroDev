# DESIGN.md — PS6 Part III, Problem 4

## Purpose

This file is the incremental implementation handoff for `solved/p6/`. It should guide Codex to implement and validate the empirical work for PS6, Part III, Problem 4 without rewriting the whole folder every time.

`AGENTS.md` controls folder discipline and process. This file controls the selected math/economic task and the current implementation plan.

## Incremental workflow rule

Before creating or rewriting anything, inspect the current state of the repository.

1. Check whether the target script already exists:

   ```text
   solved/p6/code/p6_part3_p4_item_a.py
   ```

2. If it exists, read it and compare it against the specification below.

3. If it already satisfies the specification, do not rewrite it. Run it, validate outputs, and report results.

4. If it mostly satisfies the specification but has gaps, patch only the missing or incorrect pieces.

5. If it does not exist, create it from scratch.

6. Do not delete or reconstruct unrelated PS6 work.

7. Do not implement item (b) or item (c) yet. This file is intentionally structured so later sections can be added for those items without replacing the item (a) instructions.

## Current task scope

Implement only:

```text
PS6, Part III, Problem 4, item (a)
```

The goal is to create, test, or validate a complete Python script that:

1. loads PWT and Barro--Lee data;
2. constructs education shares \(\theta_{i,c}\);
3. constructs entrepreneurial productivity \(\tilde A_c\);
4. computes observed log output per worker relative to the United States;
5. computes model-implied log output per worker relative to the United States, with and without aggregate firm productivity;
6. generates the two scatter plots requested by the problem statement.

Do not implement the variance decomposition for item (b) yet.

## Repository paths

Use these input files:

```text
data/Barro_Lee.xls
data/pwt1001.xlsx
```

Write generated files under:

```text
solved/p6/code/
```

Use this output folder:

```text
solved/p6/code/output/
```

Treat `data/` and `docs/` as read-only.

## Python execution convention

From the repository root, use the Windows Python launcher:

```bash
py solved/p6/code/p6_part3_p4_item_a.py
```

Do not assume `python` is available on PATH.

The script should infer the repository root from `__file__` using `pathlib`; it must not depend on absolute paths.

## Data year

Barro--Lee ends in 2010 in this repository. Use:

```python
YEAR = 2010
```

Use the same year in PWT.

If either dataset is missing or does not contain the required year, stop with a clear error message.

## Economic notation and constants

Use names that mirror the writeup notation as much as possible.

```python
gamma = 1 / 3
capital_exponent = gamma / (1 - gamma)  # equals 1/2

z_by_group = {
    "no_schooling": 0.28,
    "primary": 0.60,
    "secondary": 0.93,
    "tertiary": 1.20,
}

Z_by_group = {group: np.exp(z) for group, z in z_by_group.items()}

EDUCATION_GROUPS = ["no_schooling", "primary", "secondary", "tertiary"]
```

Use natural logs.

## Economic objects

For each country \(c\), construct:

\[
\tilde A_c = \left(\sum_i \theta_{i,c}Z_i^2\right)^{1/2}.
\]

Do not call this object plain `A_c` in code unless clearly distinguishing it from the unknown-scaled object:

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

Important: `hc` from PWT is a human-capital index in levels. It corresponds to \(h_c\), not to \(\bar r\bar s_c\). Since the accounting equation is in logs, the human-capital term is:

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

For 2010, construct:

```python
y_observed = rgdpo / emp
K_over_Y = cn / rgdpo
h = hc
```

Drop observations with missing or non-positive values in any required PWT variable.

Do not use `pop` for the main calculation. Even though the problem wording says per capita, the model equation and the previous development-accounting convention use output per worker/person engaged:

\[
Y_c/N_c.
\]

## Barro--Lee mapping

Use the 2010 observations for population aged 25 and over.

The Excel file may have multi-row headers and merged cells. Write a robust loader that handles this. Acceptable approach:

1. Read the sheet with `header=None`.
2. Identify or manually reconstruct the relevant columns from the visible header rows.
3. Forward-fill country names if repeated country cells are blank after the first row.
4. Keep rows with `year == 2010` and age group `25+`.
5. Convert education columns to numeric.
6. Map the four theta columns from total categories.

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

Optional sanity check: if Australia 2010 is available, the raw total-category percentages should be approximately:

```text
No Schooling       0.8
Primary Total      6.5
Secondary Total   54.7
Tertiary Total    38.0
```

They should sum to 100.0 before dividing by 100. Do not make the whole script fail solely because this country label is absent or differs slightly.

If reading `.xls` requires `xlrd` and it is not installed, stop with a clear message explaining that `.xls` reading requires `xlrd`.

## Country merge

PWT has `countrycode`; Barro--Lee may only have country names.

Implement a country-name normalization helper:

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

Merge on normalized country names unless Barro--Lee has a reliable country-code field.

Write unmatched names to diagnostics:

```text
solved/p6/code/output/p6_p4_unmatched_barro_lee.csv
solved/p6/code/output/p6_p4_unmatched_pwt.csv
```

Do not silently proceed if the matched sample is implausibly small. Fail if fewer than 80 countries match.

## US normalization

Use `countrycode == "USA"` to identify the United States after merging with PWT.

Observed relative log output per worker:

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

In code, verify that all US-relative terms are numerically zero for the United States up to tolerance.

## Required script

Create or validate this script:

```text
solved/p6/code/p6_part3_p4_item_a.py
```

The script should be modular and readable. Suggested structure:

```python
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

YEAR = 2010
US_CODE = "USA"
GAMMA = 1 / 3
CAPITAL_EXPONENT = GAMMA / (1 - GAMMA)

Z_BY_GROUP = {...}
EDUCATION_GROUPS = [...]


def find_repo_root() -> Path:
    ...


def normalize_country_name(name: str) -> str:
    ...


def load_pwt(pwt_path: Path, year: int) -> pd.DataFrame:
    ...


def load_barro_lee(barro_path: Path, year: int) -> pd.DataFrame:
    ...


def build_theta(bl_df: pd.DataFrame) -> pd.DataFrame:
    ...


def compute_tilde_A(df: pd.DataFrame) -> pd.DataFrame:
    ...


def merge_data(pwt_df: pd.DataFrame, bl_df: pd.DataFrame, output_dir: Path) -> pd.DataFrame:
    ...


def add_model_terms(df: pd.DataFrame) -> pd.DataFrame:
    ...


def make_scatter_plot(df: pd.DataFrame, x_col: str, y_col: str, output_path: Path, title: str) -> None:
    ...


def run() -> None:
    ...


if __name__ == "__main__":
    run()
```

Avoid duplicated logic. Prefer small functions with clear names over one long script.

## Required generated outputs for item (a)

Create or validate these files:

```text
solved/p6/code/output/p6_p4_item_a_country_level.csv
solved/p6/code/output/p6_p4_item_a_with_A.png
solved/p6/code/output/p6_p4_item_a_without_A.png
```

Optional but useful:

```text
solved/p6/code/output/p6_p4_item_a_summary.txt
```

The country-level CSV should include at least:

```text
countrycode
country
year
theta_no_schooling
theta_primary
theta_secondary
theta_tertiary
theta_sum
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
```

## Required figures for item (a)

Generate two separate scatter plots.

### Figure 1: with aggregate firm productivity

File:

```text
solved/p6/code/output/p6_p4_item_a_with_A.png
```

Horizontal axis:

\[
\left(\widehat{\ln(y_c/y_U)}\right)_{con}
\]

Vertical axis:

\[
\ln(y_c/y_U)
\]

### Figure 2: without aggregate firm productivity

File:

```text
solved/p6/code/output/p6_p4_item_a_without_A.png
```

Horizontal axis:

\[
\left(\widehat{\ln(y_c/y_U)}\right)_{sin}
\]

Vertical axis:

\[
\ln(y_c/y_U)
\]

For both plots:

- include a 45-degree line;
- use readable titles;
- label axes clearly;
- include the year in the title or subtitle;
- use the same axis limits across both figures if practical;
- save at high enough resolution, e.g. `dpi=200`;
- close figures after saving.

Country labels are optional. If labels are used, label only a few relevant countries such as USA, ARG, AUS, CHN, IND, DEU, BRA, and MEX if present. Do not require optional label-adjustment packages.

## Required checks for item (a)

The script must check:

1. `YEAR == 2010` exists in both datasets.
2. Required PWT columns exist.
3. Barro--Lee columns are mapped correctly to no schooling / primary total / secondary total / tertiary total.
4. Education shares are nonnegative.
5. Education shares sum to one after normalization.
6. `Z_i = exp(z_i)` matches approximately:
   - no schooling: 1.32;
   - primary: 1.83;
   - secondary: 2.53;
   - tertiary: 3.32.
7. `h_i = exp(0.08 * s_i)` matches approximately:
   - no schooling: 1.00;
   - primary: 1.62;
   - secondary: 2.61;
   - tertiary: 3.90.
   This is only a statement/table sanity check, not a variable used for worker human capital in the empirical computation.
8. `tilde_A > 0` for every country in the final sample.
9. `y_observed > 0`, `K_over_Y > 0`, and `h > 0`.
10. The United States exists in the final sample.
11. For the United States:
    - `ln_y_rel_us` is approximately zero;
    - `ln_tilde_A_rel_us` is approximately zero;
    - `ln_K_over_Y_rel_us` is approximately zero;
    - `ln_h_rel_us` is approximately zero;
    - both model-predicted relative log income values are approximately zero.
12. Both figure files exist after the run.

Use assertions or explicit exceptions with useful messages.

The script must print a concise run summary:

- year used;
- number of PWT countries loaded;
- number of Barro--Lee countries loaded;
- number of matched countries;
- output paths created;
- warnings if education shares were far from summing to one before normalization;
- unresolved matching or data issues, if any.

## Item (b) placeholder — do not implement yet

Later, add the variance decomposition here. Do not implement it now.

Expected future extension:

- consume the item (a) country-level CSV if useful;
- define the decomposition variables;
- compute covariance-over-variance shares;
- export a decomposition table;
- validate that shares sum appropriately.

## Item (c) placeholder — do not implement yet

Later, add the education-total contribution here. Do not implement it now.

Expected future extension:

- combine the worker-human-capital channel and entrepreneurial-productivity channel;
- compare total education contribution against the worker-human-capital-only contribution.

## Final response expected from Codex

After inspecting, creating, patching, or running the script, Codex should report only:

1. whether the script already existed, was patched, or was created;
2. files created or modified;
3. command used to reproduce;
4. number of matched countries;
5. output figure paths;
6. checks passed;
7. unresolved matching/data issues, if any.

Do not present unverified numerical results as final.
