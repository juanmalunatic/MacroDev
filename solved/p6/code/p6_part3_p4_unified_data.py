from __future__ import annotations

from pathlib import Path
import re
import unicodedata

import numpy as np
import pandas as pd

YEAR = 2010
US_CODE = "USA"
NUMERIC_TOLERANCE = 1e-10

REQUIRED_PWT_COLUMNS = ["countrycode", "country", "year", "rgdpo", "emp", "cn", "hc"]
BARRO_NUMERIC_COLUMNS = [
    "year",
    "no_schooling",
    "primary_total",
    "primary_completed",
    "secondary_total",
    "secondary_completed",
    "tertiary_total",
    "tertiary_completed",
    "avg_years_total",
    "avg_years_primary",
    "avg_years_secondary",
    "avg_years_tertiary",
    "population_1000s",
]
THETA_COLUMNS = [
    "theta_no_schooling",
    "theta_primary",
    "theta_secondary",
    "theta_tertiary",
]
COUNTRY_ALIASES = {
    "bolivia": "bolivia plurinational state of",
    "china hong kong special administrative region": "china hong kong sar",
    "china macao special administrative region": "china macao sar",
    "cote divoire": "cote d ivoire",
    "democratic republic of the congo": "d r of the congo",
    "dominican rep": "dominican republic",
    "lao people s democratic republic": "lao people s dr",
    "swaziland": "eswatini",
    "united republic of tanzania": "u r of tanzania mainland",
    "usa": "united states",
    "venezuela": "venezuela bolivarian republic of",
}


def find_repo_root() -> Path:
    current = Path(__file__).resolve()
    for candidate in [current.parent, *current.parents]:
        if (candidate / "data").exists() and (candidate / "docs").exists() and (candidate / "solved").exists():
            return candidate
    raise FileNotFoundError("Could not infer the repository root from __file__.")


def ensure_input_file_exists(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Required input file not found: {path}")


def normalize_country_name(name: str) -> str:
    if pd.isna(name):
        return ""

    normalized = unicodedata.normalize("NFKD", str(name))
    normalized = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    normalized = normalized.lower().strip()
    normalized = normalized.replace("&", " and ")
    normalized = re.sub(r"[^\w\s]", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return COUNTRY_ALIASES.get(normalized, normalized)


def _text_cell(df: pd.DataFrame, row: int, col: int) -> str:
    value = df.iloc[row, col]
    if pd.isna(value):
        return ""
    return str(value).strip().lower()


def load_pwt_base(pwt_path: Path, year: int) -> pd.DataFrame:
    pwt_df = pd.read_excel(pwt_path, sheet_name="Data")

    missing_columns = [column for column in REQUIRED_PWT_COLUMNS if column not in pwt_df.columns]
    if missing_columns:
        raise KeyError(f"PWT is missing required columns: {missing_columns}")

    if year not in set(pd.to_numeric(pwt_df["year"], errors="coerce").dropna().astype(int)):
        raise ValueError(f"PWT does not contain year {year}.")

    pwt_df = pwt_df[REQUIRED_PWT_COLUMNS].copy()
    pwt_df["year"] = pd.to_numeric(pwt_df["year"], errors="coerce")
    pwt_df = pwt_df[pwt_df["year"] == year].copy()

    for column in ["rgdpo", "emp", "cn", "hc"]:
        pwt_df[column] = pd.to_numeric(pwt_df[column], errors="coerce")

    pwt_df = pwt_df.dropna(subset=["countrycode", "country"]).copy()
    pwt_df["country_norm"] = pwt_df["country"].map(normalize_country_name)
    return pwt_df


def load_barro_lee_base(barro_path: Path, year: int) -> pd.DataFrame:
    try:
        raw_df = pd.read_excel(barro_path, sheet_name="Sheet1", header=None)
    except ImportError as exc:
        if "xlrd" in str(exc).lower():
            raise RuntimeError("Reading data/Barro_Lee.xls requires xlrd. Install xlrd in the project environment.") from exc
        raise

    header_checks = {
        (7, 0): "country",
        (7, 1): "year",
        (7, 2): "age group",
        (7, 4): "no schooling",
        (9, 5): "primary",
        (10, 5): "total",
        (9, 7): "secondary",
        (10, 7): "total",
        (9, 9): "tertiary",
        (10, 9): "total",
    }
    for (row, col), expected in header_checks.items():
        actual = _text_cell(raw_df, row, col)
        if actual != expected:
            raise AssertionError(
                f"Unexpected Barro-Lee header at row {row}, column {col}: expected '{expected}', found '{actual}'."
            )

    column_map = {
        0: "country",
        1: "year",
        2: "age_group_main",
        3: "age_group_plus",
        4: "no_schooling",
        5: "primary_total",
        6: "primary_completed",
        7: "secondary_total",
        8: "secondary_completed",
        9: "tertiary_total",
        10: "tertiary_completed",
        11: "avg_years_total",
        12: "avg_years_primary",
        13: "avg_years_secondary",
        14: "avg_years_tertiary",
        15: "population_1000s",
        16: "region",
    }
    raw_df = raw_df.rename(columns=column_map)
    raw_df["country"] = raw_df["country"].ffill()

    for column in BARRO_NUMERIC_COLUMNS:
        raw_df[column] = pd.to_numeric(raw_df[column], errors="coerce")

    if year not in set(raw_df["year"].dropna().astype(int)):
        raise ValueError(f"Barro-Lee does not contain year {year}.")

    raw_df["age_group_main"] = raw_df["age_group_main"].fillna("").astype(str).str.strip()
    raw_df["age_group_plus"] = raw_df["age_group_plus"].fillna("").astype(str).str.strip()
    raw_df["age_group"] = raw_df["age_group_main"] + raw_df["age_group_plus"]

    filtered = raw_df[(raw_df["year"] == year) & (raw_df["age_group"] == "25+")].copy()
    if filtered.empty:
        raise ValueError(f"Barro-Lee does not contain any rows for year {year} and age group 25+.")

    filtered["country_norm"] = filtered["country"].map(normalize_country_name)
    return filtered


def build_theta(bl_df: pd.DataFrame) -> pd.DataFrame:
    df = bl_df.copy()
    df["no_schooling_raw_pct"] = pd.to_numeric(df["no_schooling"], errors="coerce")
    df["primary_total_raw_pct"] = pd.to_numeric(df["primary_total"], errors="coerce")
    df["secondary_total_raw_pct"] = pd.to_numeric(df["secondary_total"], errors="coerce")
    df["tertiary_total_raw_pct"] = pd.to_numeric(df["tertiary_total"], errors="coerce")

    raw_pct_columns = [
        "no_schooling_raw_pct",
        "primary_total_raw_pct",
        "secondary_total_raw_pct",
        "tertiary_total_raw_pct",
    ]
    if df[raw_pct_columns].isna().any().any():
        raise ValueError("Barro-Lee contains missing education shares for the selected year.")
    if (df[raw_pct_columns] < 0).any().any():
        raise AssertionError("Education shares must be nonnegative.")

    raw_share_columns = {
        "theta_no_schooling_raw": "no_schooling_raw_pct",
        "theta_primary_raw": "primary_total_raw_pct",
        "theta_secondary_raw": "secondary_total_raw_pct",
        "theta_tertiary_raw": "tertiary_total_raw_pct",
    }
    for raw_theta_column, source_column in raw_share_columns.items():
        df[raw_theta_column] = df[source_column] / 100.0

    raw_theta_cols = list(raw_share_columns.keys())
    df["theta_sum_before_norm"] = df[raw_theta_cols].sum(axis=1)
    if (df["theta_sum_before_norm"] <= 0).any():
        raise AssertionError("Education shares must sum to a positive value before normalization.")

    df["theta_no_schooling"] = df["theta_no_schooling_raw"] / df["theta_sum_before_norm"]
    df["theta_primary"] = df["theta_primary_raw"] / df["theta_sum_before_norm"]
    df["theta_secondary"] = df["theta_secondary_raw"] / df["theta_sum_before_norm"]
    df["theta_tertiary"] = df["theta_tertiary_raw"] / df["theta_sum_before_norm"]
    df["theta_sum"] = df[THETA_COLUMNS].sum(axis=1)

    if (df[THETA_COLUMNS] < 0).any().any():
        raise AssertionError("Normalized education shares must be nonnegative.")
    if not np.allclose(df["theta_sum"].to_numpy(), 1.0, atol=NUMERIC_TOLERANCE, rtol=0.0):
        raise AssertionError("Normalized education shares must sum to one.")

    return df


def merge_base_data(pwt_df: pd.DataFrame, bl_df: pd.DataFrame, output_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    unmatched_barro = (
        bl_df.loc[~bl_df["country_norm"].isin(set(pwt_df["country_norm"])), ["country", "country_norm"]]
        .drop_duplicates()
        .sort_values(["country_norm", "country"])
        .reset_index(drop=True)
    )
    unmatched_pwt = (
        pwt_df.loc[~pwt_df["country_norm"].isin(set(bl_df["country_norm"])), ["countrycode", "country", "country_norm"]]
        .drop_duplicates()
        .sort_values(["country_norm", "countrycode"])
        .reset_index(drop=True)
    )

    unmatched_barro.to_csv(output_dir / "p6_p4_unmatched_barro_lee.csv", index=False)
    unmatched_pwt.to_csv(output_dir / "p6_p4_unmatched_pwt.csv", index=False)

    merged = pwt_df.merge(
        bl_df[
            [
                "country",
                "country_norm",
                "no_schooling_raw_pct",
                "primary_total_raw_pct",
                "secondary_total_raw_pct",
                "tertiary_total_raw_pct",
                "theta_no_schooling",
                "theta_primary",
                "theta_secondary",
                "theta_tertiary",
                "theta_sum",
                "theta_sum_before_norm",
            ]
        ].rename(columns={"country": "country_barro_lee"}),
        on="country_norm",
        how="inner",
    )

    if len(merged) < 80:
        raise RuntimeError(f"Matched sample is implausibly small: only {len(merged)} countries matched.")

    merged = merged.dropna(
        subset=[
            "rgdpo",
            "emp",
            "cn",
            "hc",
            "theta_no_schooling",
            "theta_primary",
            "theta_secondary",
            "theta_tertiary",
        ]
    ).copy()
    for column in ["rgdpo", "emp", "cn", "hc"]:
        merged = merged[merged[column] > 0].copy()

    if US_CODE not in set(merged["countrycode"]):
        raise RuntimeError("The United States is missing from the unified merged sample.")

    return merged, unmatched_barro, unmatched_pwt


def write_unified_base_data(df: pd.DataFrame, output_dir: Path) -> Path:
    output_path = output_dir / "p6_p4_unified_base_data.csv"
    ordered_columns = [
        "countrycode",
        "country",
        "country_norm",
        "country_barro_lee",
        "year",
        "rgdpo",
        "emp",
        "cn",
        "hc",
        "no_schooling_raw_pct",
        "primary_total_raw_pct",
        "secondary_total_raw_pct",
        "tertiary_total_raw_pct",
        "theta_no_schooling",
        "theta_primary",
        "theta_secondary",
        "theta_tertiary",
        "theta_sum",
        "theta_sum_before_norm",
    ]
    df[ordered_columns].sort_values("countrycode").to_csv(output_path, index=False)
    return output_path


def _write_markdown_table(df: pd.DataFrame, output_path: Path) -> None:
    lines = [
        "| column | max_abs_diff | passed |",
        "|---|---:|---:|",
    ]
    for row in df.itertuples(index=False):
        max_abs_diff_str = "nan" if pd.isna(row.max_abs_diff) else f"{row.max_abs_diff:.12g}"
        lines.append(f"| {row.column} | {max_abs_diff_str} | {row.passed} |")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def compare_unified_data_to_benchmark(unified_df: pd.DataFrame, benchmark_path: Path, output_dir: Path) -> pd.DataFrame:
    ensure_input_file_exists(benchmark_path)
    benchmark_df = pd.read_csv(benchmark_path)

    unified_countrycodes = set(unified_df["countrycode"])
    benchmark_countrycodes = set(benchmark_df["countrycode"])
    if unified_countrycodes != benchmark_countrycodes:
        missing_in_unified = sorted(benchmark_countrycodes - unified_countrycodes)
        missing_in_benchmark = sorted(unified_countrycodes - benchmark_countrycodes)
        raise AssertionError(
            "Unified base data and benchmark country samples differ. "
            f"Missing in unified: {missing_in_unified}; missing in benchmark: {missing_in_benchmark}"
        )

    merged = unified_df.merge(
        benchmark_df,
        on="countrycode",
        how="inner",
        suffixes=("_unified", "_benchmark"),
    )

    rows = []
    numeric_columns = [
        "theta_no_schooling",
        "theta_primary",
        "theta_secondary",
        "theta_tertiary",
        "theta_sum",
    ]
    for column in numeric_columns:
        max_abs_diff = float(
            np.max(np.abs(merged[f"{column}_unified"].to_numpy() - merged[f"{column}_benchmark"].to_numpy()))
        )
        rows.append(
            {
                "column": column,
                "max_abs_diff": max_abs_diff,
                "passed": max_abs_diff <= NUMERIC_TOLERANCE,
            }
        )

    derived_checks = {
        "y_observed_from_base": merged["rgdpo"] / merged["emp"],
        "K_over_Y_from_base": merged["cn"] / merged["rgdpo"],
        "h_from_base": merged["hc"],
    }
    benchmark_columns = {
        "y_observed_from_base": "y_observed",
        "K_over_Y_from_base": "K_over_Y",
        "h_from_base": "h",
    }
    for label, derived_values in derived_checks.items():
        benchmark_column = benchmark_columns[label]
        if benchmark_column not in merged.columns:
            continue
        max_abs_diff = float(
            np.max(np.abs(derived_values.to_numpy() - merged[benchmark_column].to_numpy()))
        )
        rows.append(
            {
                "column": label,
                "max_abs_diff": max_abs_diff,
                "passed": max_abs_diff <= NUMERIC_TOLERANCE,
            }
        )

    benchmark_check_df = pd.DataFrame(rows)
    benchmark_check_csv = output_dir / "p6_p4_unified_data_benchmark_check.csv"
    benchmark_check_md = output_dir / "p6_p4_unified_data_benchmark_check.md"
    benchmark_check_df.to_csv(benchmark_check_csv, index=False)
    _write_markdown_table(benchmark_check_df, benchmark_check_md)

    failed_rows = benchmark_check_df.loc[~benchmark_check_df["passed"]]
    if not failed_rows.empty:
        failed_descriptions = ", ".join(
            f"{row.column} (max_abs_diff={row.max_abs_diff:.3e})"
            for row in failed_rows.itertuples(index=False)
        )
        raise AssertionError(f"Unified data benchmark check failed: {failed_descriptions}")

    return benchmark_check_df


def run() -> None:
    repo_root = find_repo_root()
    pwt_path = repo_root / "data" / "pwt1001.xlsx"
    barro_path = repo_root / "data" / "Barro_Lee.xls"
    benchmark_path = repo_root / "solved" / "p6" / "code" / "output" / "p6_p4_item_a_country_level.csv"
    output_dir = repo_root / "solved" / "p6" / "code" / "output" / "unified"
    output_dir.mkdir(parents=True, exist_ok=True)

    ensure_input_file_exists(pwt_path)
    ensure_input_file_exists(barro_path)

    pwt_df = load_pwt_base(pwt_path, YEAR)
    bl_df = load_barro_lee_base(barro_path, YEAR)
    bl_df = build_theta(bl_df)
    unified_df, unmatched_barro, unmatched_pwt = merge_base_data(pwt_df, bl_df, output_dir)
    unified_base_path = write_unified_base_data(unified_df, output_dir)
    benchmark_check_df = compare_unified_data_to_benchmark(unified_df, benchmark_path, output_dir)

    summary_lines = [
        f"Year used: {YEAR}",
        f"PWT countries loaded: {pwt_df['country'].nunique()}",
        f"Barro-Lee countries loaded: {bl_df['country'].nunique()}",
        f"Unified merged sample size: {len(unified_df)}",
        f"United States present: {US_CODE in set(unified_df['countrycode'])}",
        f"Unified base data: {unified_base_path}",
        f"Unmatched Barro-Lee diagnostics: {output_dir / 'p6_p4_unmatched_barro_lee.csv'}",
        f"Unmatched PWT diagnostics: {output_dir / 'p6_p4_unmatched_pwt.csv'}",
        f"Unified data benchmark check CSV: {output_dir / 'p6_p4_unified_data_benchmark_check.csv'}",
        f"Unified data benchmark check MD: {output_dir / 'p6_p4_unified_data_benchmark_check.md'}",
        f"Maximum benchmark difference: {benchmark_check_df['max_abs_diff'].max():.3e}",
        f"Benchmark checks passed: {benchmark_check_df['passed'].all()}",
        f"Remaining unmatched Barro-Lee countries: {len(unmatched_barro)}",
        f"Remaining unmatched PWT countries: {len(unmatched_pwt)}",
    ]
    summary_path = output_dir / "p6_p4_unified_data_summary.txt"
    summary_path.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

    print("\n".join(summary_lines))


if __name__ == "__main__":
    run()
