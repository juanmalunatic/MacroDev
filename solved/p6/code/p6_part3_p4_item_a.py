from __future__ import annotations

from pathlib import Path
import os
import re
import unicodedata

MPLCONFIGDIR = Path(__file__).resolve().parent / "output" / "mplconfig"
MPLCONFIGDIR.mkdir(parents=True, exist_ok=True)
os.environ["MPLCONFIGDIR"] = str(MPLCONFIGDIR)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
Z_BY_GROUP = {group: np.exp(z_value) for group, z_value in Z_LOG_BY_GROUP.items()}

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
Z_COLUMNS = [
    "Z_no_schooling",
    "Z_primary",
    "Z_secondary",
    "Z_tertiary",
]


def find_repo_root() -> Path:
    current = Path(__file__).resolve()
    for candidate in [current.parent, *current.parents]:
        if (candidate / "data").exists() and (candidate / "docs").exists() and (candidate / "solved").exists():
            return candidate
    raise FileNotFoundError("Could not infer the repository root from __file__.")


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


def _assert_close(value: float, expected: float, label: str, atol: float = 1e-2) -> None:
    if not np.isclose(value, expected, atol=atol, rtol=0.0):
        raise AssertionError(f"{label} expected {expected:.4f}, found {value:.4f}.")


def validate_reference_values() -> None:
    expected_z_levels = {
        "no_schooling": 1.32,
        "primary": 1.83,
        "secondary": 2.53,
        "tertiary": 3.32,
    }
    for group, expected_value in expected_z_levels.items():
        _assert_close(Z_BY_GROUP[group], expected_value, f"Z_{group}", atol=0.02)

    expected_h_levels = {
        "no_schooling": 1.00,
        "primary": 1.62,
        "secondary": 2.61,
        "tertiary": 3.90,
    }
    for group, years in SCHOOLING_YEARS.items():
        schooling_h = float(np.exp(BAR_R * years))
        _assert_close(schooling_h, expected_h_levels[group], f"h_{group}", atol=0.03)


def ensure_input_file_exists(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Required input file not found: {path}")


def load_pwt(pwt_path: Path, year: int) -> pd.DataFrame:
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


def load_barro_lee(barro_path: Path, year: int) -> pd.DataFrame:
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
        (10, 6): "completed",
        (9, 7): "secondary",
        (10, 7): "total",
        (10, 8): "completed",
        (9, 9): "tertiary",
        (10, 9): "total",
        (10, 10): "completed",
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

    raw_share_columns = {
        "theta_no_schooling_raw": "no_schooling",
        "theta_primary_raw": "primary_total",
        "theta_secondary_raw": "secondary_total",
        "theta_tertiary_raw": "tertiary_total",
    }
    for raw_theta_column, source_column in raw_share_columns.items():
        df[raw_theta_column] = pd.to_numeric(df[source_column], errors="coerce") / 100.0

    raw_theta_cols = list(raw_share_columns.keys())
    if df[raw_theta_cols].isna().any().any():
        raise ValueError("Barro-Lee contains missing education shares for the selected year.")
    if (df[raw_theta_cols] < 0).any().any():
        raise AssertionError("Education shares must be nonnegative.")

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
    if not np.allclose(df["theta_sum"].to_numpy(), 1.0, atol=1e-10):
        raise AssertionError("Normalized education shares must sum to one.")

    return df


def compute_tilde_A(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    for group in EDUCATION_GROUPS:
        result[f"Z_{group}"] = Z_BY_GROUP[group]

    result["tilde_A"] = np.sqrt(
        result["theta_no_schooling"] * result["Z_no_schooling"] ** 2
        + result["theta_primary"] * result["Z_primary"] ** 2
        + result["theta_secondary"] * result["Z_secondary"] ** 2
        + result["theta_tertiary"] * result["Z_tertiary"] ** 2
    )

    if not (result["tilde_A"] > 0).all():
        raise AssertionError("tilde_A must be strictly positive for every country.")
    return result


def merge_data(pwt_df: pd.DataFrame, bl_df: pd.DataFrame, output_dir: Path) -> pd.DataFrame:
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

    return merged


def add_model_terms(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()

    required_positive_columns = [
        "rgdpo",
        "emp",
        "cn",
        "hc",
        "theta_no_schooling",
        "theta_primary",
        "theta_secondary",
        "theta_tertiary",
        "tilde_A",
    ]
    result = result.dropna(subset=required_positive_columns).copy()
    for column in ["rgdpo", "emp", "cn", "hc", "tilde_A"]:
        result = result[result[column] > 0].copy()

    result["y_observed"] = result["rgdpo"] / result["emp"]
    result["K_over_Y"] = result["cn"] / result["rgdpo"]
    result["h"] = result["hc"]

    if not (result["y_observed"] > 0).all():
        raise AssertionError("y_observed must be strictly positive.")
    if not (result["K_over_Y"] > 0).all():
        raise AssertionError("K_over_Y must be strictly positive.")
    if not (result["h"] > 0).all():
        raise AssertionError("h must be strictly positive.")

    if US_CODE not in set(result["countrycode"]):
        raise RuntimeError("The United States is missing from the final sample.")

    us_row = result.loc[result["countrycode"] == US_CODE].iloc[0]
    result["ln_y_rel_us"] = np.log(result["y_observed"]) - np.log(us_row["y_observed"])
    result["ln_tilde_A_rel_us"] = np.log(result["tilde_A"]) - np.log(us_row["tilde_A"])
    result["ln_K_over_Y_rel_us"] = np.log(result["K_over_Y"]) - np.log(us_row["K_over_Y"])
    result["ln_h_rel_us"] = np.log(result["h"]) - np.log(us_row["h"])
    result["ln_yhat_with_A_rel_us"] = (
        result["ln_tilde_A_rel_us"]
        + CAPITAL_EXPONENT * result["ln_K_over_Y_rel_us"]
        + result["ln_h_rel_us"]
    )
    result["ln_yhat_without_A_rel_us"] = CAPITAL_EXPONENT * result["ln_K_over_Y_rel_us"] + result["ln_h_rel_us"]

    us_final = result.loc[result["countrycode"] == US_CODE].iloc[0]
    us_checks = {
        "ln_y_rel_us": us_final["ln_y_rel_us"],
        "ln_tilde_A_rel_us": us_final["ln_tilde_A_rel_us"],
        "ln_K_over_Y_rel_us": us_final["ln_K_over_Y_rel_us"],
        "ln_h_rel_us": us_final["ln_h_rel_us"],
        "ln_yhat_with_A_rel_us": us_final["ln_yhat_with_A_rel_us"],
        "ln_yhat_without_A_rel_us": us_final["ln_yhat_without_A_rel_us"],
    }
    for label, value in us_checks.items():
        if not np.isclose(value, 0.0, atol=1e-10, rtol=0.0):
            raise AssertionError(f"{label} for the United States must be numerically zero; found {value}.")

    return result


def make_scatter_plot(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    output_path: Path,
    title: str,
    x_label: str,
    y_label: str,
    limits: tuple[float, float],
) -> None:
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df[x_col], df[y_col], alpha=0.7, edgecolor="white", linewidth=0.4)
    ax.plot(limits, limits, linestyle="--", color="black", linewidth=1.0, label="45-degree line")
    ax.set_xlim(limits)
    ax.set_ylim(limits)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(f"{title}\nYear {YEAR}")
    ax.grid(alpha=0.2)
    ax.legend()

    for country_code in ["USA", "ARG", "AUS", "CHN", "IND", "DEU", "BRA", "MEX"]:
        matching_rows = df.loc[df["countrycode"] == country_code]
        if matching_rows.empty:
            continue
        row = matching_rows.iloc[0]
        ax.annotate(
            country_code,
            (row[x_col], row[y_col]),
            textcoords="offset points",
            xytext=(4, 4),
            fontsize=8,
        )

    fig.tight_layout()
    fig.savefig(output_path, dpi=200)
    plt.close(fig)


def build_run_summary(
    repo_root: Path,
    output_dir: Path,
    pwt_df: pd.DataFrame,
    bl_df: pd.DataFrame,
    matched_df: pd.DataFrame,
    final_df: pd.DataFrame,
    theta_warning_df: pd.DataFrame,
    dropped_due_to_missing: pd.DataFrame,
) -> str:
    output_paths = [
        output_dir / "p6_p4_item_a_country_level.csv",
        output_dir / "p6_p4_item_a_with_A.png",
        output_dir / "p6_p4_item_a_without_A.png",
        output_dir / "p6_p4_unmatched_barro_lee.csv",
        output_dir / "p6_p4_unmatched_pwt.csv",
    ]

    lines = [
        f"Year used: {YEAR}",
        f"PWT countries loaded: {pwt_df['country'].nunique()}",
        f"Barro-Lee countries loaded: {bl_df['country'].nunique()}",
        f"Matched countries: {len(matched_df)}",
        f"Final countries after missing/non-positive PWT filters: {len(final_df)}",
        "Output paths created:",
    ]
    lines.extend(f"- {path.relative_to(repo_root)}" for path in output_paths)

    if theta_warning_df.empty:
        lines.append("Education-share normalization warnings: none.")
    else:
        lines.append(
            "Education-share normalization warnings: "
            + ", ".join(theta_warning_df["country"].tolist())
            + "."
        )

    unresolved = []
    unmatched_barro_path = output_dir / "p6_p4_unmatched_barro_lee.csv"
    unmatched_barro_count = len(pd.read_csv(unmatched_barro_path))
    if unmatched_barro_count:
        unresolved.append(f"{unmatched_barro_count} Barro-Lee countries remain unmatched by name.")
    if not dropped_due_to_missing.empty:
        unresolved.append(
            "Some matched countries were dropped for missing/non-positive PWT variables: "
            + ", ".join(dropped_due_to_missing["country"].tolist())
            + "."
        )

    if unresolved:
        lines.append("Unresolved issues:")
        lines.extend(f"- {issue}" for issue in unresolved)
    else:
        lines.append("Unresolved issues: none.")

    return "\n".join(lines) + "\n"


def run() -> None:
    validate_reference_values()

    repo_root = find_repo_root()
    pwt_path = repo_root / "data" / "pwt1001.xlsx"
    barro_path = repo_root / "data" / "Barro_Lee.xls"
    output_dir = repo_root / "solved" / "p6" / "code" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    ensure_input_file_exists(pwt_path)
    ensure_input_file_exists(barro_path)

    pwt_df = load_pwt(pwt_path, YEAR)
    bl_df = load_barro_lee(barro_path, YEAR)
    bl_df = build_theta(bl_df)

    theta_warning_df = bl_df.loc[(bl_df["theta_sum_before_norm"] - 1.0).abs() > 0.01, ["country", "theta_sum_before_norm"]]

    matched_df = merge_data(pwt_df, bl_df, output_dir)
    matched_df = compute_tilde_A(matched_df)

    dropped_due_to_missing = matched_df.loc[
        matched_df[["rgdpo", "emp", "cn", "hc"]].isna().any(axis=1)
        | (matched_df[["rgdpo", "emp", "cn", "hc"]] <= 0).any(axis=1),
        ["countrycode", "country"],
    ].drop_duplicates()

    final_df = add_model_terms(matched_df)

    keep_columns = [
        "countrycode",
        "country",
        "year",
        "theta_no_schooling",
        "theta_primary",
        "theta_secondary",
        "theta_tertiary",
        "theta_sum",
        "Z_no_schooling",
        "Z_primary",
        "Z_secondary",
        "Z_tertiary",
        "tilde_A",
        "y_observed",
        "K_over_Y",
        "h",
        "ln_y_rel_us",
        "ln_tilde_A_rel_us",
        "ln_K_over_Y_rel_us",
        "ln_h_rel_us",
        "ln_yhat_with_A_rel_us",
        "ln_yhat_without_A_rel_us",
    ]
    country_level_path = output_dir / "p6_p4_item_a_country_level.csv"
    final_df[keep_columns].sort_values(["countrycode"]).to_csv(country_level_path, index=False)

    plotted_values = np.concatenate(
        [
            final_df["ln_y_rel_us"].to_numpy(),
            final_df["ln_yhat_with_A_rel_us"].to_numpy(),
            final_df["ln_yhat_without_A_rel_us"].to_numpy(),
        ]
    )
    span_min = float(np.nanmin(plotted_values))
    span_max = float(np.nanmax(plotted_values))
    padding = max(0.1, 0.05 * (span_max - span_min))
    limits = (span_min - padding, span_max + padding)

    with_a_path = output_dir / "p6_p4_item_a_with_A.png"
    without_a_path = output_dir / "p6_p4_item_a_without_A.png"

    make_scatter_plot(
        final_df,
        x_col="ln_yhat_with_A_rel_us",
        y_col="ln_y_rel_us",
        output_path=with_a_path,
        title="Observed vs model-implied log output per worker (with aggregate firm productivity)",
        x_label="Predicted ln(y_c / y_US) with firm productivity",
        y_label="Observed ln(y_c / y_US)",
        limits=limits,
    )
    make_scatter_plot(
        final_df,
        x_col="ln_yhat_without_A_rel_us",
        y_col="ln_y_rel_us",
        output_path=without_a_path,
        title="Observed vs model-implied log output per worker (without aggregate firm productivity)",
        x_label="Predicted ln(y_c / y_US) without firm productivity",
        y_label="Observed ln(y_c / y_US)",
        limits=limits,
    )

    if not with_a_path.exists() or not without_a_path.exists():
        raise FileNotFoundError("Expected figure outputs were not created.")

    summary_text = build_run_summary(
        repo_root=repo_root,
        output_dir=output_dir,
        pwt_df=pwt_df,
        bl_df=bl_df,
        matched_df=matched_df,
        final_df=final_df,
        theta_warning_df=theta_warning_df,
        dropped_due_to_missing=dropped_due_to_missing,
    )
    summary_path = output_dir / "p6_p4_item_a_summary.txt"
    summary_path.write_text(summary_text, encoding="utf-8")

    print(summary_text.rstrip())


if __name__ == "__main__":
    run()
