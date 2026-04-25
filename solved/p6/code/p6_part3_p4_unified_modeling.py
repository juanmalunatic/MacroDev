from __future__ import annotations

from pathlib import Path
import os

UNIFIED_OUTPUT_DIR = Path(__file__).resolve().parent / "output" / "unified"
UNIFIED_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MPLCONFIGDIR = UNIFIED_OUTPUT_DIR / "mplconfig"
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
NUMERIC_TOLERANCE = 1e-10

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
Z_BY_GROUP = {group: np.exp(value) for group, value in Z_LOG_BY_GROUP.items()}

VARIANCE_COMPONENT_LABELS_ES = {
    "firm_productivity": "Productividad de firmas",
    "capital_factor": "Factor capital",
    "worker_human_capital": "Capital humano trabajadores",
    "residual": "Residuo",
    "total": "Total",
}
EDUCATION_CONCEPT_LABELS_ES = {
    "firm_productivity_education_channel": "Canal productividad de firmas",
    "worker_human_capital_channel": "Canal capital humano trabajadores",
    "total_education_contribution": "Contribución total de educación",
    "human_capital_only": "Capital humano solamente",
    "added_contribution_from_firm_productivity": "Contribución adicional del canal firmas",
    "ratio_total_to_human_capital_only": "Ratio total / capital humano",
}
BASE_REQUIRED_COLUMNS = [
    "countrycode",
    "country",
    "country_norm",
    "country_barro_lee",
    "year",
    "rgdpo",
    "emp",
    "cn",
    "hc",
    "theta_no_schooling",
    "theta_primary",
    "theta_secondary",
    "theta_tertiary",
    "theta_sum",
    "theta_sum_before_norm",
]


def find_repo_root() -> Path:
    current = Path(__file__).resolve()
    for candidate in [current.parent, *current.parents]:
        if (candidate / "data").exists() and (candidate / "docs").exists() and (candidate / "solved").exists():
            return candidate
    raise FileNotFoundError("Could not infer the repository root from __file__.")


def relpath(path: Path, repo_root: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def ensure_input_file_exists(path: Path, help_command: str | None = None) -> None:
    if path.exists():
        return
    message = f"Required input file not found: {path}"
    if help_command is not None:
        message += f". Run `{help_command}` first."
    raise FileNotFoundError(message)


def load_unified_base_data(path: Path) -> pd.DataFrame:
    ensure_input_file_exists(path, help_command="py solved/p6/code/p6_part3_p4_unified_data.py")
    df = pd.read_csv(path)

    missing_columns = [column for column in BASE_REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise KeyError(f"Unified base data is missing required columns: {missing_columns}")

    if set(df["year"]) != {YEAR}:
        raise AssertionError(f"Unified base data must contain only year {YEAR}.")
    if US_CODE not in set(df["countrycode"]):
        raise AssertionError("Unified base data must contain the United States.")
    if not np.allclose(df["theta_sum"].to_numpy(), 1.0, atol=NUMERIC_TOLERANCE, rtol=0.0):
        raise AssertionError("Unified base data must have theta_sum equal to one.")

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
        raise AssertionError("tilde_A must be strictly positive in the unified modeling sample.")
    return result


def add_model_terms(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["y_observed"] = result["rgdpo"] / result["emp"]
    result["K_over_Y"] = result["cn"] / result["rgdpo"]
    result["h"] = result["hc"]

    if not (result["y_observed"] > 0).all():
        raise AssertionError("y_observed must be strictly positive.")
    if not (result["K_over_Y"] > 0).all():
        raise AssertionError("K_over_Y must be strictly positive.")
    if not (result["h"] > 0).all():
        raise AssertionError("h must be strictly positive.")

    us_row = result.loc[result["countrycode"] == US_CODE]
    if us_row.empty:
        raise AssertionError("United States missing from unified modeling sample.")
    us_row = us_row.iloc[0]

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

    us_checks = {
        "ln_y_rel_us": result.loc[result["countrycode"] == US_CODE, "ln_y_rel_us"].iloc[0],
        "ln_tilde_A_rel_us": result.loc[result["countrycode"] == US_CODE, "ln_tilde_A_rel_us"].iloc[0],
        "ln_K_over_Y_rel_us": result.loc[result["countrycode"] == US_CODE, "ln_K_over_Y_rel_us"].iloc[0],
        "ln_h_rel_us": result.loc[result["countrycode"] == US_CODE, "ln_h_rel_us"].iloc[0],
        "ln_yhat_with_A_rel_us": result.loc[result["countrycode"] == US_CODE, "ln_yhat_with_A_rel_us"].iloc[0],
        "ln_yhat_without_A_rel_us": result.loc[result["countrycode"] == US_CODE, "ln_yhat_without_A_rel_us"].iloc[0],
    }
    for label, value in us_checks.items():
        if not np.isclose(value, 0.0, atol=NUMERIC_TOLERANCE, rtol=0.0):
            raise AssertionError(f"{label} for the United States must be numerically zero; found {value}.")

    return result


def add_item_b_terms(df: pd.DataFrame) -> tuple[pd.DataFrame, float]:
    result = df.copy()
    result["ln_capital_factor_rel_us"] = CAPITAL_EXPONENT * result["ln_K_over_Y_rel_us"]
    if not np.allclose(
        result["ln_capital_factor_rel_us"].to_numpy(),
        (CAPITAL_EXPONENT * result["ln_K_over_Y_rel_us"]).to_numpy(),
        atol=NUMERIC_TOLERANCE,
        rtol=0.0,
    ):
        raise AssertionError("ln_capital_factor_rel_us must equal CAPITAL_EXPONENT * ln_K_over_Y_rel_us.")

    result["residual"] = (
        result["ln_y_rel_us"]
        - result["ln_tilde_A_rel_us"]
        - result["ln_capital_factor_rel_us"]
        - result["ln_h_rel_us"]
    )
    required_columns = [
        "ln_y_rel_us",
        "ln_tilde_A_rel_us",
        "ln_capital_factor_rel_us",
        "ln_h_rel_us",
        "residual",
    ]
    if result[required_columns].isna().any().any():
        raise AssertionError("Item (b) unified sample contains missing values.")

    reconstruction = (
        result["ln_tilde_A_rel_us"]
        + result["ln_capital_factor_rel_us"]
        + result["ln_h_rel_us"]
        + result["residual"]
    )
    reconstruction_error = result["ln_y_rel_us"] - reconstruction
    max_abs_reconstruction_error = float(reconstruction_error.abs().max())
    if not np.allclose(
        result["ln_y_rel_us"].to_numpy(),
        reconstruction.to_numpy(),
        atol=NUMERIC_TOLERANCE,
        rtol=0.0,
    ):
        raise AssertionError("Residual definition does not reconstruct ln_y_rel_us.")

    return result, max_abs_reconstruction_error


def compute_variance_decomposition(df: pd.DataFrame) -> tuple[pd.DataFrame, float]:
    variance_ln_y = float(df["ln_y_rel_us"].var())
    if not np.isfinite(variance_ln_y) or variance_ln_y <= 0:
        raise AssertionError("Variance of ln_y_rel_us must be strictly positive.")

    component_map = {
        "firm_productivity": "ln_tilde_A_rel_us",
        "capital_factor": "ln_capital_factor_rel_us",
        "worker_human_capital": "ln_h_rel_us",
        "residual": "residual",
    }
    rows = []
    for component, column in component_map.items():
        covariance_with_ln_y = float(df[column].cov(df["ln_y_rel_us"]))
        share = covariance_with_ln_y / variance_ln_y
        rows.append(
            {
                "component": component,
                "share": share,
                "covariance_with_ln_y": covariance_with_ln_y,
                "variance_ln_y": variance_ln_y,
            }
        )

    decomposition_df = pd.DataFrame(rows)
    share_sum = float(decomposition_df["share"].sum())
    if not np.isclose(share_sum, 1.0, atol=NUMERIC_TOLERANCE, rtol=0.0):
        raise AssertionError(f"Variance-decomposition shares must sum to one; found {share_sum:.12f}.")

    total_row = pd.DataFrame(
        [
            {
                "component": "total",
                "share": share_sum,
                "covariance_with_ln_y": float(decomposition_df["covariance_with_ln_y"].sum()),
                "variance_ln_y": variance_ln_y,
            }
        ]
    )
    decomposition_df = pd.concat([decomposition_df, total_row], ignore_index=True)
    return decomposition_df, share_sum


def compute_education_contribution(variance_decomposition: pd.DataFrame) -> pd.DataFrame:
    decomposition = variance_decomposition.set_index("component")
    required_components = {"firm_productivity", "worker_human_capital"}
    missing_components = sorted(required_components - set(decomposition.index))
    if missing_components:
        raise AssertionError(
            f"Variance decomposition is missing required components for item (c): {missing_components}"
        )

    firm_productivity_education_channel = float(decomposition.loc["firm_productivity", "share"])
    worker_human_capital_channel = float(decomposition.loc["worker_human_capital", "share"])
    total_education_contribution = (
        firm_productivity_education_channel + worker_human_capital_channel
    )
    human_capital_only = worker_human_capital_channel
    added_contribution_from_firm_productivity = firm_productivity_education_channel
    if np.isclose(human_capital_only, 0.0, atol=NUMERIC_TOLERANCE, rtol=0.0):
        raise AssertionError("worker_human_capital_channel is numerically zero, so the ratio is undefined.")
    ratio_total_to_human_capital_only = total_education_contribution / human_capital_only

    if not np.isclose(
        total_education_contribution,
        firm_productivity_education_channel + worker_human_capital_channel,
        atol=NUMERIC_TOLERANCE,
        rtol=0.0,
    ):
        raise AssertionError("Item (c) total education contribution identity failed.")
    if not np.isclose(human_capital_only, worker_human_capital_channel, atol=NUMERIC_TOLERANCE, rtol=0.0):
        raise AssertionError("Item (c) human_capital_only identity failed.")
    if not np.isclose(
        added_contribution_from_firm_productivity,
        firm_productivity_education_channel,
        atol=NUMERIC_TOLERANCE,
        rtol=0.0,
    ):
        raise AssertionError("Item (c) added contribution identity failed.")
    if not np.isclose(
        ratio_total_to_human_capital_only,
        total_education_contribution / human_capital_only,
        atol=NUMERIC_TOLERANCE,
        rtol=0.0,
    ):
        raise AssertionError("Item (c) ratio identity failed.")

    return pd.DataFrame(
        [
            {"concept": "firm_productivity_education_channel", "value": firm_productivity_education_channel},
            {"concept": "worker_human_capital_channel", "value": worker_human_capital_channel},
            {"concept": "total_education_contribution", "value": total_education_contribution},
            {"concept": "human_capital_only", "value": human_capital_only},
            {
                "concept": "added_contribution_from_firm_productivity",
                "value": added_contribution_from_firm_productivity,
            },
            {"concept": "ratio_total_to_human_capital_only", "value": ratio_total_to_human_capital_only},
        ]
    )


def _markdown_table_from_dataframe(df: pd.DataFrame, output_path: Path, float_columns: list[str]) -> None:
    headers = df.columns.tolist()
    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join("---:" if header in float_columns else "---" for header in headers) + "|",
    ]
    for row in df.to_dict(orient="records"):
        values = []
        for header in headers:
            value = row[header]
            if header in float_columns:
                values.append(f"{float(value):.3f}")
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_latex_table(content_lines: list[str], output_path: Path) -> None:
    output_path.write_text("\n".join(content_lines) + "\n", encoding="utf-8")


def write_variance_outputs(variance_decomposition: pd.DataFrame, output_dir: Path) -> dict[str, Path]:
    csv_path = output_dir / "p6_p4_unified_item_b_variance_decomposition.csv"
    md_path = output_dir / "p6_p4_unified_item_b_variance_decomposition.md"
    tex_path = output_dir / "p6_p4_unified_item_b_variance_decomposition.tex"
    variance_decomposition.to_csv(csv_path, index=False)

    markdown_df = variance_decomposition.copy()
    markdown_df["componente"] = markdown_df["component"].map(VARIANCE_COMPONENT_LABELS_ES)
    markdown_df = markdown_df[["componente", "share", "covariance_with_ln_y", "variance_ln_y"]].rename(
        columns={
            "share": "participación",
            "covariance_with_ln_y": "covarianza_con_ln_y",
            "variance_ln_y": "varianza_ln_y",
        }
    )
    _markdown_table_from_dataframe(
        markdown_df,
        md_path,
        float_columns=["participación", "covarianza_con_ln_y", "varianza_ln_y"],
    )

    latex_lines = [
        r"\begin{table}[H]",
        r"    \centering",
        r"    \begin{tabular}{lrrr}",
        r"        \toprule",
        r"        Componente & Participaci\'on & Covarianza con $\ell^y_c$ & Varianza de $\ell^y_c$ \\",
        r"        \midrule",
    ]
    for row in variance_decomposition.itertuples(index=False):
        label = VARIANCE_COMPONENT_LABELS_ES[row.component]
        latex_lines.append(
            f"        {label} & {row.share:.3f} & {row.covariance_with_ln_y:.3f} & {row.variance_ln_y:.3f} \\\\"
        )
    latex_lines.extend(
        [
            r"        \bottomrule",
            r"    \end{tabular}",
            r"",
            r"    \caption{Descomposici\'on de varianza del ingreso relativo.}",
            r"    \label{tab:p6_p4_var_decomp}",
            r"\end{table}",
        ]
    )
    write_latex_table(latex_lines, tex_path)

    return {"csv": csv_path, "md": md_path, "tex": tex_path}


def write_education_outputs(education_contribution: pd.DataFrame, output_dir: Path) -> dict[str, Path]:
    csv_path = output_dir / "p6_p4_unified_item_c_education_contribution.csv"
    md_path = output_dir / "p6_p4_unified_item_c_education_contribution.md"
    tex_path = output_dir / "p6_p4_unified_item_c_education_contribution.tex"
    education_contribution.to_csv(csv_path, index=False)

    markdown_df = education_contribution.copy()
    markdown_df["concepto"] = markdown_df["concept"].map(EDUCATION_CONCEPT_LABELS_ES)
    markdown_df = markdown_df[["concepto", "value"]].rename(columns={"value": "valor"})
    _markdown_table_from_dataframe(markdown_df, md_path, float_columns=["valor"])

    latex_lines = [
        r"\begin{table}[H]",
        r"    \centering",
        r"    \begin{tabular}{lr}",
        r"        \toprule",
        r"        Concepto & Valor \\",
        r"        \midrule",
    ]
    for row in education_contribution.itertuples(index=False):
        label = EDUCATION_CONCEPT_LABELS_ES[row.concept]
        latex_lines.append(f"        {label} & {row.value:.3f} \\\\")
    latex_lines.extend(
        [
            r"        \bottomrule",
            r"    \end{tabular}",
            r"",
            r"    \caption{Contribuci\'on total de la educaci\'on.}",
            r"    \label{tab:p6_p4_education_contribution}",
            r"\end{table}",
        ]
    )
    write_latex_table(latex_lines, tex_path)

    return {"csv": csv_path, "md": md_path, "tex": tex_path}


def compute_axis_limits(*arrays: np.ndarray) -> tuple[float, float]:
    concatenated = np.concatenate([np.asarray(array, dtype=float) for array in arrays])
    min_value = float(np.nanmin(concatenated))
    max_value = float(np.nanmax(concatenated))
    margin = max(0.1, 0.05 * (max_value - min_value))
    return min_value - margin, max_value + margin


def make_scatter_plot_pdf(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    output_path: Path,
    title: str,
    subtitle: str,
    x_label: str,
    y_label: str,
    limits: tuple[float, float],
) -> None:
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df[x_col], df[y_col], alpha=0.7, edgecolor="white", linewidth=0.4)
    ax.plot(limits, limits, linestyle="--", color="black", linewidth=1.0, label="Línea de 45°")
    ax.set_xlim(limits)
    ax.set_ylim(limits)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(f"{title}\n{subtitle}\nAño 2010")
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
    fig.savefig(output_path, format="pdf")
    plt.close(fig)


def compare_country_level_to_benchmark(
    unified_df: pd.DataFrame, benchmark_path: Path, rows: list[dict[str, object]]
) -> None:
    ensure_input_file_exists(benchmark_path)
    benchmark_df = pd.read_csv(benchmark_path)

    unified_countrycodes = set(unified_df["countrycode"])
    benchmark_countrycodes = set(benchmark_df["countrycode"])
    if unified_countrycodes != benchmark_countrycodes:
        missing_in_unified = sorted(benchmark_countrycodes - unified_countrycodes)
        missing_in_benchmark = sorted(unified_countrycodes - benchmark_countrycodes)
        raise AssertionError(
            "Unified modeling sample and benchmark country sample differ. "
            f"Missing in unified: {missing_in_unified}; missing in benchmark: {missing_in_benchmark}"
        )

    merged = unified_df.merge(
        benchmark_df,
        on="countrycode",
        how="inner",
        suffixes=("_unified", "_benchmark"),
    )
    compare_columns = [
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
        "ln_capital_factor_rel_us",
        "residual",
    ]
    for column in compare_columns:
        max_abs_diff = float(
            np.max(np.abs(merged[f"{column}_unified"].to_numpy() - merged[f"{column}_benchmark"].to_numpy()))
        )
        rows.append(
            {
                "check": f"country_level::{column}",
                "max_abs_diff": max_abs_diff,
                "passed": max_abs_diff <= NUMERIC_TOLERANCE,
            }
        )


def compare_table_to_benchmark(
    table_df: pd.DataFrame,
    benchmark_path: Path,
    key_column: str,
    numeric_columns: list[str],
    prefix: str,
    rows: list[dict[str, object]],
) -> None:
    ensure_input_file_exists(benchmark_path)
    benchmark_df = pd.read_csv(benchmark_path)

    if set(table_df[key_column]) != set(benchmark_df[key_column]):
        raise AssertionError(
            f"{prefix} keys differ from benchmark. "
            f"Unified keys: {sorted(set(table_df[key_column]))}; "
            f"benchmark keys: {sorted(set(benchmark_df[key_column]))}"
        )

    merged = table_df.merge(
        benchmark_df,
        on=key_column,
        how="inner",
        suffixes=("_unified", "_benchmark"),
    )
    for row in merged.itertuples(index=False):
        for numeric_column in numeric_columns:
            unified_value = getattr(row, f"{numeric_column}_unified")
            benchmark_value = getattr(row, f"{numeric_column}_benchmark")
            max_abs_diff = float(abs(unified_value - benchmark_value))
            rows.append(
                {
                    "check": f"{prefix}::{getattr(row, key_column)}::{numeric_column}",
                    "max_abs_diff": max_abs_diff,
                    "passed": max_abs_diff <= NUMERIC_TOLERANCE,
                }
            )


def write_benchmark_check(rows: list[dict[str, object]], output_dir: Path) -> pd.DataFrame:
    benchmark_check_df = pd.DataFrame(rows)
    csv_path = output_dir / "p6_p4_unified_modeling_benchmark_check.csv"
    md_path = output_dir / "p6_p4_unified_modeling_benchmark_check.md"
    benchmark_check_df.to_csv(csv_path, index=False)

    lines = [
        "| check | max_abs_diff | passed |",
        "|---|---:|---:|",
    ]
    for row in benchmark_check_df.itertuples(index=False):
        lines.append(f"| {row.check} | {row.max_abs_diff:.12g} | {row.passed} |")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    failed_rows = benchmark_check_df.loc[~benchmark_check_df["passed"]]
    if not failed_rows.empty:
        failed_descriptions = ", ".join(
            f"{row.check} (max_abs_diff={row.max_abs_diff:.3e})"
            for row in failed_rows.itertuples(index=False)
        )
        raise AssertionError(f"Unified modeling benchmark check failed: {failed_descriptions}")

    return benchmark_check_df


def run() -> None:
    repo_root = find_repo_root()
    output_dir = repo_root / "solved" / "p6" / "code" / "output" / "unified"
    output_dir.mkdir(parents=True, exist_ok=True)

    unified_base_path = output_dir / "p6_p4_unified_base_data.csv"
    benchmark_country_level_path = repo_root / "solved" / "p6" / "code" / "output" / "p6_p4_item_a_country_level.csv"
    benchmark_item_b_path = repo_root / "solved" / "p6" / "code" / "output" / "p6_p4_item_b_variance_decomposition.csv"
    benchmark_item_c_path = repo_root / "solved" / "p6" / "code" / "output" / "p6_p4_item_c_education_contribution.csv"
    unmatched_barro_path = output_dir / "p6_p4_unmatched_barro_lee.csv"
    unmatched_pwt_path = output_dir / "p6_p4_unmatched_pwt.csv"

    ensure_input_file_exists(unified_base_path, help_command="py solved/p6/code/p6_part3_p4_unified_data.py")
    ensure_input_file_exists(benchmark_country_level_path)
    ensure_input_file_exists(benchmark_item_b_path)
    ensure_input_file_exists(benchmark_item_c_path)

    base_df = load_unified_base_data(unified_base_path)
    country_level_df = compute_tilde_A(base_df)
    country_level_df = add_model_terms(country_level_df)
    country_level_df, max_abs_reconstruction_error = add_item_b_terms(country_level_df)
    variance_decomposition_df, share_sum = compute_variance_decomposition(country_level_df)
    education_contribution_df = compute_education_contribution(variance_decomposition_df)

    us_row = country_level_df.loc[country_level_df["countrycode"] == US_CODE].iloc[0]
    country_level_df["ln_y_abs"] = np.log(country_level_df["y_observed"])
    country_level_df["ln_yhat_with_A_abs_us_anchor"] = np.log(us_row["y_observed"]) + country_level_df["ln_yhat_with_A_rel_us"]
    country_level_df["ln_yhat_without_A_abs_us_anchor"] = np.log(us_row["y_observed"]) + country_level_df["ln_yhat_without_A_rel_us"]

    unified_country_level_path = output_dir / "p6_p4_unified_country_level.csv"
    country_level_df.sort_values("countrycode").to_csv(unified_country_level_path, index=False)

    variance_output_paths = write_variance_outputs(variance_decomposition_df, output_dir)
    education_output_paths = write_education_outputs(education_contribution_df, output_dir)

    relative_limits = compute_axis_limits(
        country_level_df["ln_y_rel_us"].to_numpy(),
        country_level_df["ln_yhat_with_A_rel_us"].to_numpy(),
        country_level_df["ln_yhat_without_A_rel_us"].to_numpy(),
    )
    absolute_limits = compute_axis_limits(
        country_level_df["ln_y_abs"].to_numpy(),
        country_level_df["ln_yhat_with_A_abs_us_anchor"].to_numpy(),
        country_level_df["ln_yhat_without_A_abs_us_anchor"].to_numpy(),
    )

    main_with_a_pdf = output_dir / "p6_p4_unified_item_a_with_A_relative.pdf"
    main_without_a_pdf = output_dir / "p6_p4_unified_item_a_without_A_relative.pdf"
    debug_with_a_pdf = output_dir / "p6_p4_unified_item_a_with_A_absolute_debug.pdf"
    debug_without_a_pdf = output_dir / "p6_p4_unified_item_a_without_A_absolute_debug.pdf"

    make_scatter_plot_pdf(
        country_level_df,
        x_col="ln_yhat_with_A_rel_us",
        y_col="ln_y_rel_us",
        output_path=main_with_a_pdf,
        title="Ingreso observado vs. ingreso explicado",
        subtitle="Modelo con productividad agregada de firmas",
        x_label="Ingreso explicado relativo a EE.UU. (log)",
        y_label="Ingreso observado relativo a EE.UU. (log)",
        limits=relative_limits,
    )
    make_scatter_plot_pdf(
        country_level_df,
        x_col="ln_yhat_without_A_rel_us",
        y_col="ln_y_rel_us",
        output_path=main_without_a_pdf,
        title="Ingreso observado vs. ingreso explicado",
        subtitle="Modelo sin productividad agregada de firmas",
        x_label="Ingreso explicado relativo a EE.UU. (log)",
        y_label="Ingreso observado relativo a EE.UU. (log)",
        limits=relative_limits,
    )
    make_scatter_plot_pdf(
        country_level_df,
        x_col="ln_yhat_with_A_abs_us_anchor",
        y_col="ln_y_abs",
        output_path=debug_with_a_pdf,
        title="Figura de depuración: ingreso absoluto observado vs. explicado",
        subtitle="Modelo con productividad agregada de firmas, anclado en EE.UU.",
        x_label="Ingreso explicado absoluto (log, anclado en EE.UU.)",
        y_label="Ingreso observado absoluto (log)",
        limits=absolute_limits,
    )
    make_scatter_plot_pdf(
        country_level_df,
        x_col="ln_yhat_without_A_abs_us_anchor",
        y_col="ln_y_abs",
        output_path=debug_without_a_pdf,
        title="Figura de depuración: ingreso absoluto observado vs. explicado",
        subtitle="Modelo sin productividad agregada de firmas, anclado en EE.UU.",
        x_label="Ingreso explicado absoluto (log, anclado en EE.UU.)",
        y_label="Ingreso observado absoluto (log)",
        limits=absolute_limits,
    )

    required_paths = [
        unified_country_level_path,
        main_with_a_pdf,
        main_without_a_pdf,
        debug_with_a_pdf,
        debug_without_a_pdf,
        *variance_output_paths.values(),
        *education_output_paths.values(),
    ]
    missing_paths = [path for path in required_paths if not path.exists()]
    if missing_paths:
        raise FileNotFoundError(f"Missing unified modeling outputs: {missing_paths}")

    benchmark_rows: list[dict[str, object]] = []
    compare_country_level_to_benchmark(country_level_df, benchmark_country_level_path, benchmark_rows)
    compare_table_to_benchmark(
        variance_decomposition_df,
        benchmark_item_b_path,
        key_column="component",
        numeric_columns=["share", "covariance_with_ln_y", "variance_ln_y"],
        prefix="item_b",
        rows=benchmark_rows,
    )
    compare_table_to_benchmark(
        education_contribution_df,
        benchmark_item_c_path,
        key_column="concept",
        numeric_columns=["value"],
        prefix="item_c",
        rows=benchmark_rows,
    )
    benchmark_check_df = write_benchmark_check(benchmark_rows, output_dir)

    unmatched_barro_count = len(pd.read_csv(unmatched_barro_path)) if unmatched_barro_path.exists() else np.nan
    unmatched_pwt_count = len(pd.read_csv(unmatched_pwt_path)) if unmatched_pwt_path.exists() else np.nan

    summary_lines = [
        f"Unified base data input: {relpath(unified_base_path, repo_root)}",
        f"Unified modeling output: {relpath(unified_country_level_path, repo_root)}",
        f"Unified modeling sample size: {len(country_level_df)}",
        f"Item (b) share sum: {share_sum:.12f}",
        f"Item (b) max absolute reconstruction error: {max_abs_reconstruction_error:.3e}",
        f"Main relative PDF with A: {relpath(main_with_a_pdf, repo_root)}",
        f"Main relative PDF without A: {relpath(main_without_a_pdf, repo_root)}",
        f"Absolute debug PDF with A: {relpath(debug_with_a_pdf, repo_root)}",
        f"Absolute debug PDF without A: {relpath(debug_without_a_pdf, repo_root)}",
        f"Unified item (b) CSV: {relpath(variance_output_paths['csv'], repo_root)}",
        f"Unified item (b) MD: {relpath(variance_output_paths['md'], repo_root)}",
        f"Unified item (b) TEX: {relpath(variance_output_paths['tex'], repo_root)}",
        f"Unified item (c) CSV: {relpath(education_output_paths['csv'], repo_root)}",
        f"Unified item (c) MD: {relpath(education_output_paths['md'], repo_root)}",
        f"Unified item (c) TEX: {relpath(education_output_paths['tex'], repo_root)}",
        f"Unified modeling benchmark check CSV: {relpath(output_dir / 'p6_p4_unified_modeling_benchmark_check.csv', repo_root)}",
        f"Unified modeling benchmark check MD: {relpath(output_dir / 'p6_p4_unified_modeling_benchmark_check.md', repo_root)}",
        f"Maximum benchmark difference: {benchmark_check_df['max_abs_diff'].max():.3e}",
        f"Benchmark checks passed: {benchmark_check_df['passed'].all()}",
        f"Remaining unmatched Barro-Lee countries from unified data stage: {unmatched_barro_count}",
        f"Remaining unmatched PWT countries from unified data stage: {unmatched_pwt_count}",
    ]
    summary_path = output_dir / "p6_p4_unified_modeling_summary.txt"
    summary_path.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

    print("\n".join(summary_lines))


if __name__ == "__main__":
    run()
