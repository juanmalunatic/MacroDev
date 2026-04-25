from __future__ import annotations

from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
LOCAL_SITE_PACKAGES = SCRIPT_DIR.parents[3] / ".venv" / "Lib" / "site-packages"
if LOCAL_SITE_PACKAGES.exists():
    sys.path.insert(0, str(LOCAL_SITE_PACKAGES))

import numpy as np
import pandas as pd

TOL = 1e-10


def main() -> None:
    student_output_dir = SCRIPT_DIR / "output"
    unified_output_dir = SCRIPT_DIR.parent / "output" / "unified"

    student_country_path = student_output_dir / "p6_p4_student_country_level.csv"
    student_item_b_path = student_output_dir / "p6_p4_student_item_b_variance_decomposition.csv"
    student_item_c_path = student_output_dir / "p6_p4_student_item_c_education_contribution.csv"

    unified_country_path = unified_output_dir / "p6_p4_unified_country_level.csv"
    unified_item_b_path = unified_output_dir / "p6_p4_unified_item_b_variance_decomposition.csv"
    unified_item_c_path = unified_output_dir / "p6_p4_unified_item_c_education_contribution.csv"

    for path in [
        student_country_path,
        student_item_b_path,
        student_item_c_path,
        unified_country_path,
        unified_item_b_path,
        unified_item_c_path,
    ]:
        if not path.exists():
            raise FileNotFoundError(f"Missing file for dev check: {path}")

    student_country = pd.read_csv(student_country_path)
    unified_country = pd.read_csv(unified_country_path)
    if set(student_country["countrycode"]) != set(unified_country["countrycode"]):
        raise AssertionError("Student and unified country samples differ.")

    merged_country = student_country.merge(unified_country, on="countrycode", suffixes=("_student", "_unified"))
    country_columns = [
        "tilde_A",
        "y_observed",
        "K_over_Y",
        "h",
        "ln_y_rel_us",
        "ln_tilde_A_rel_us",
        "ln_K_over_Y_rel_us",
        "ln_h_rel_us",
        "ln_capital_factor_rel_us",
        "ln_yhat_with_A_rel_us",
        "ln_yhat_without_A_rel_us",
        "residual",
    ]

    rows = []
    for column in country_columns:
        max_abs_diff = float(
            np.max(np.abs(merged_country[f"{column}_student"].to_numpy() - merged_country[f"{column}_unified"].to_numpy()))
        )
        rows.append((f"country_level::{column}", max_abs_diff, max_abs_diff <= TOL))

    student_item_b = pd.read_csv(student_item_b_path)
    unified_item_b = pd.read_csv(unified_item_b_path)
    merged_item_b = student_item_b.merge(unified_item_b, on="component", suffixes=("_student", "_unified"))
    for row in merged_item_b.itertuples(index=False):
        for column in ["share", "covariance_with_ln_y", "variance_ln_y"]:
            max_abs_diff = abs(float(getattr(row, f"{column}_student")) - float(getattr(row, f"{column}_unified")))
            rows.append((f"item_b::{row.component}::{column}", max_abs_diff, max_abs_diff <= TOL))

    student_item_c = pd.read_csv(student_item_c_path)
    unified_item_c = pd.read_csv(unified_item_c_path)
    merged_item_c = student_item_c.merge(unified_item_c, on="concept", suffixes=("_student", "_unified"))
    for row in merged_item_c.itertuples(index=False):
        max_abs_diff = abs(float(row.value_student) - float(row.value_unified))
        rows.append((f"item_c::{row.concept}::value", max_abs_diff, max_abs_diff <= TOL))

    failed_rows = [row for row in rows if not row[2]]
    if failed_rows:
        failed_text = ", ".join(f"{name} (max_abs_diff={diff:.3e})" for name, diff, _ in failed_rows)
        raise AssertionError(f"Student dev check failed: {failed_text}")

    maximum_diff = max(diff for _, diff, _ in rows)
    print("Student dev check passed.")
    print(f"Maximum benchmark difference: {maximum_diff:.3e}")


if __name__ == "__main__":
    main()
