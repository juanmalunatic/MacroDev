from __future__ import annotations

from pathlib import Path
import os

STUDENT_OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output" / "student"
STUDENT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MPLCONFIGDIR = STUDENT_OUTPUT_DIR / "mplconfig"
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
TOL = 1e-10

EDUCATION_GROUPS = ["no_schooling", "primary", "secondary", "tertiary"]
SCHOOLING_YEARS = {
    "no_schooling": 0,
    "primary": 6,
    "secondary": 12,
    "tertiary": 17,
}
Z_LOG = {
    "no_schooling": 0.28,
    "primary": 0.60,
    "secondary": 0.93,
    "tertiary": 1.20,
}
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


def find_repo_root() -> Path:
    current = Path(__file__).resolve()
    for candidate in [current.parent, *current.parents]:
        if (candidate / "data").exists() and (candidate / "docs").exists() and (candidate / "solved").exists():
            return candidate
    raise FileNotFoundError("Could not infer the repository root from __file__.")


def relpath(path: Path, repo_root: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def save_markdown_table(df: pd.DataFrame, path: Path, float_columns: list[str]) -> None:
    lines = [
        "| " + " | ".join(df.columns) + " |",
        "|" + "|".join("---:" if column in float_columns else "---" for column in df.columns) + "|",
    ]
    for row in df.to_dict(orient="records"):
        values = []
        for column in df.columns:
            value = row[column]
            if column in float_columns:
                values.append(f"{float(value):.12f}")
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def make_scatter(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    output_path: Path,
    title: str,
    subtitle: str,
    limits: tuple[float, float],
) -> None:
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df[x_col], df[y_col], alpha=0.7, edgecolor="white", linewidth=0.4)
    ax.plot(limits, limits, linestyle="--", color="black", linewidth=1.0, label="Línea de 45°")
    ax.set_xlim(limits)
    ax.set_ylim(limits)
    ax.set_xlabel("Ingreso explicado relativo a EE.UU. (log)")
    ax.set_ylabel("Ingreso observado relativo a EE.UU. (log)")
    ax.set_title(f"{title}\n{subtitle}\nAño 2010")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False, loc="upper left")
    fig.tight_layout()
    fig.savefig(output_path, format="pdf")
    plt.close(fig)


def main() -> None:
    repo_root = find_repo_root()

    base_data_path = repo_root / "solved" / "p6" / "code" / "output" / "unified" / "p6_p4_unified_base_data.csv"
    benchmark_country_path = repo_root / "solved" / "p6" / "code" / "output" / "unified" / "p6_p4_unified_country_level.csv"
    benchmark_item_b_path = (
        repo_root / "solved" / "p6" / "code" / "output" / "unified" / "p6_p4_unified_item_b_variance_decomposition.csv"
    )
    benchmark_item_c_path = (
        repo_root / "solved" / "p6" / "code" / "output" / "unified" / "p6_p4_unified_item_c_education_contribution.csv"
    )
    output_dir = repo_root / "solved" / "p6" / "code" / "output" / "student"
    output_dir.mkdir(parents=True, exist_ok=True)

    if not base_data_path.exists():
        raise FileNotFoundError(
            "Missing unified base data. Run `py solved/p6/code/p6_part3_p4_unified_data.py` first."
        )
    for benchmark_path in [benchmark_country_path, benchmark_item_b_path, benchmark_item_c_path]:
        if not benchmark_path.exists():
            raise FileNotFoundError(
                "Missing accepted unified outputs. Run `py solved/p6/code/p6_part3_p4_unified_modeling.py` first."
            )

    df = pd.read_csv(base_data_path)
    required_columns = [
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
    missing_columns = [column for column in required_columns if column not in df.columns]
    if missing_columns:
        raise KeyError(f"Unified base data is missing required columns: {missing_columns}")

    if set(df["year"]) != {YEAR}:
        raise AssertionError(f"The student script expects only year {YEAR}.")
    if US_CODE not in set(df["countrycode"]):
        raise AssertionError("The unified base data must contain the United States.")

    key_columns = [
        "rgdpo",
        "emp",
        "cn",
        "hc",
        "theta_no_schooling",
        "theta_primary",
        "theta_secondary",
        "theta_tertiary",
    ]
    if df[key_columns].isna().any().any():
        raise AssertionError("The student script found missing values in key columns.")

    theta_sum_check = df[[f"theta_{group}" for group in EDUCATION_GROUPS]].sum(axis=1)
    if not np.allclose(theta_sum_check.to_numpy(), 1.0, atol=TOL, rtol=0.0):
        raise AssertionError("Education shares must sum to one.")

    z_values = {group: np.exp(Z_LOG[group]) for group in EDUCATION_GROUPS}
    for group in EDUCATION_GROUPS:
        df[f"Z_{group}"] = z_values[group]

    df["tilde_A"] = np.sqrt(
        df["theta_no_schooling"] * df["Z_no_schooling"] ** 2
        + df["theta_primary"] * df["Z_primary"] ** 2
        + df["theta_secondary"] * df["Z_secondary"] ** 2
        + df["theta_tertiary"] * df["Z_tertiary"] ** 2
    )
    df["y_observed"] = df["rgdpo"] / df["emp"]
    df["K_over_Y"] = df["cn"] / df["rgdpo"]
    df["h"] = df["hc"]

    for column in ["tilde_A", "y_observed", "K_over_Y", "h"]:
        if not (df[column] > 0).all():
            raise AssertionError(f"{column} must be strictly positive.")

    us_row = df.loc[df["countrycode"] == US_CODE].iloc[0]
    df["ln_y_rel_us"] = np.log(df["y_observed"]) - np.log(us_row["y_observed"])
    df["ln_tilde_A_rel_us"] = np.log(df["tilde_A"]) - np.log(us_row["tilde_A"])
    df["ln_K_over_Y_rel_us"] = np.log(df["K_over_Y"]) - np.log(us_row["K_over_Y"])
    df["ln_capital_factor_rel_us"] = CAPITAL_EXPONENT * df["ln_K_over_Y_rel_us"]
    df["ln_h_rel_us"] = np.log(df["h"]) - np.log(us_row["h"])
    df["ln_yhat_with_A_rel_us"] = df["ln_tilde_A_rel_us"] + df["ln_capital_factor_rel_us"] + df["ln_h_rel_us"]
    df["ln_yhat_without_A_rel_us"] = df["ln_capital_factor_rel_us"] + df["ln_h_rel_us"]
    df["residual"] = (
        df["ln_y_rel_us"] - df["ln_tilde_A_rel_us"] - df["ln_capital_factor_rel_us"] - df["ln_h_rel_us"]
    )

    us_checks = [
        "ln_y_rel_us",
        "ln_tilde_A_rel_us",
        "ln_K_over_Y_rel_us",
        "ln_capital_factor_rel_us",
        "ln_h_rel_us",
        "ln_yhat_with_A_rel_us",
        "ln_yhat_without_A_rel_us",
    ]
    for column in us_checks:
        value = float(df.loc[df["countrycode"] == US_CODE, column].iloc[0])
        if not np.isclose(value, 0.0, atol=TOL, rtol=0.0):
            raise AssertionError(f"{column} for the United States must be zero.")

    country_level_path = output_dir / "p6_p4_student_country_level.csv"
    df.sort_values("countrycode").to_csv(country_level_path, index=False)

    variance_rows = []
    variance_ln_y = float(df["ln_y_rel_us"].var())
    components = {
        "firm_productivity": "ln_tilde_A_rel_us",
        "capital_factor": "ln_capital_factor_rel_us",
        "worker_human_capital": "ln_h_rel_us",
        "residual": "residual",
    }
    for component, column in components.items():
        covariance_with_ln_y = float(df[column].cov(df["ln_y_rel_us"]))
        share = covariance_with_ln_y / variance_ln_y
        variance_rows.append(
            {
                "component": component,
                "share": share,
                "covariance_with_ln_y": covariance_with_ln_y,
                "variance_ln_y": variance_ln_y,
            }
        )
    variance_df = pd.DataFrame(variance_rows)
    share_sum = float(variance_df["share"].sum())
    if not np.isclose(share_sum, 1.0, atol=TOL, rtol=0.0):
        raise AssertionError(f"Variance shares must sum to one; found {share_sum:.12f}.")
    variance_df = pd.concat(
        [
            variance_df,
            pd.DataFrame(
                [
                    {
                        "component": "total",
                        "share": share_sum,
                        "covariance_with_ln_y": float(variance_df["covariance_with_ln_y"].sum()),
                        "variance_ln_y": variance_ln_y,
                    }
                ]
            ),
        ],
        ignore_index=True,
    )

    item_b_csv = output_dir / "p6_p4_student_item_b_variance_decomposition.csv"
    item_b_md = output_dir / "p6_p4_student_item_b_variance_decomposition.md"
    variance_df.to_csv(item_b_csv, index=False)
    variance_md = variance_df.copy()
    variance_md["componente"] = variance_md["component"].map(VARIANCE_COMPONENT_LABELS_ES)
    variance_md = variance_md[["componente", "share", "covariance_with_ln_y", "variance_ln_y"]].rename(
        columns={
            "share": "participación",
            "covariance_with_ln_y": "covarianza_con_ln_y",
            "variance_ln_y": "varianza_ln_y",
        }
    )
    save_markdown_table(
        variance_md,
        item_b_md,
        float_columns=["participación", "covarianza_con_ln_y", "varianza_ln_y"],
    )

    firm_productivity_education_channel = float(
        variance_df.loc[variance_df["component"] == "firm_productivity", "share"].iloc[0]
    )
    worker_human_capital_channel = float(
        variance_df.loc[variance_df["component"] == "worker_human_capital", "share"].iloc[0]
    )
    total_education_contribution = firm_productivity_education_channel + worker_human_capital_channel
    human_capital_only = worker_human_capital_channel
    added_contribution_from_firm_productivity = firm_productivity_education_channel
    ratio_total_to_human_capital_only = total_education_contribution / human_capital_only

    if not np.isclose(
        total_education_contribution,
        firm_productivity_education_channel + worker_human_capital_channel,
        atol=TOL,
        rtol=0.0,
    ):
        raise AssertionError("Item (c) total education contribution identity failed.")
    if not np.isclose(human_capital_only, worker_human_capital_channel, atol=TOL, rtol=0.0):
        raise AssertionError("Item (c) human capital only identity failed.")
    if not np.isclose(
        added_contribution_from_firm_productivity,
        firm_productivity_education_channel,
        atol=TOL,
        rtol=0.0,
    ):
        raise AssertionError("Item (c) added contribution identity failed.")

    education_df = pd.DataFrame(
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

    item_c_csv = output_dir / "p6_p4_student_item_c_education_contribution.csv"
    item_c_md = output_dir / "p6_p4_student_item_c_education_contribution.md"
    education_df.to_csv(item_c_csv, index=False)
    education_md = education_df.copy()
    education_md["concepto"] = education_md["concept"].map(EDUCATION_CONCEPT_LABELS_ES)
    education_md = education_md[["concepto", "value"]].rename(columns={"value": "valor"})
    save_markdown_table(education_md, item_c_md, float_columns=["valor"])

    all_relative_values = np.concatenate(
        [
            df["ln_y_rel_us"].to_numpy(),
            df["ln_yhat_with_A_rel_us"].to_numpy(),
            df["ln_yhat_without_A_rel_us"].to_numpy(),
        ]
    )
    min_value = float(np.nanmin(all_relative_values))
    max_value = float(np.nanmax(all_relative_values))
    margin = max(0.1, 0.05 * (max_value - min_value))
    relative_limits = (min_value - margin, max_value + margin)

    with_a_pdf = output_dir / "p6_p4_student_item_a_with_A_relative.pdf"
    without_a_pdf = output_dir / "p6_p4_student_item_a_without_A_relative.pdf"
    make_scatter(
        df,
        x_col="ln_yhat_with_A_rel_us",
        y_col="ln_y_rel_us",
        output_path=with_a_pdf,
        title="Ingreso observado vs. ingreso explicado",
        subtitle="Modelo con productividad agregada de firmas",
        limits=relative_limits,
    )
    make_scatter(
        df,
        x_col="ln_yhat_without_A_rel_us",
        y_col="ln_y_rel_us",
        output_path=without_a_pdf,
        title="Ingreso observado vs. ingreso explicado",
        subtitle="Modelo sin productividad agregada de firmas",
        limits=relative_limits,
    )

    benchmark_rows = []

    benchmark_country = pd.read_csv(benchmark_country_path)
    if set(df["countrycode"]) != set(benchmark_country["countrycode"]):
        raise AssertionError("Student country sample does not match the accepted unified sample.")
    merged_country = df.merge(benchmark_country, on="countrycode", suffixes=("_student", "_benchmark"))
    country_columns_to_check = [
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
    for column in country_columns_to_check:
        max_abs_diff = float(
            np.max(np.abs(merged_country[f"{column}_student"].to_numpy() - merged_country[f"{column}_benchmark"].to_numpy()))
        )
        benchmark_rows.append(
            {
                "check": f"country_level::{column}",
                "max_abs_diff": max_abs_diff,
                "passed": max_abs_diff <= TOL,
            }
        )

    benchmark_item_b = pd.read_csv(benchmark_item_b_path)
    merged_item_b = variance_df.merge(benchmark_item_b, on="component", suffixes=("_student", "_benchmark"))
    for component in merged_item_b["component"]:
        component_row = merged_item_b.loc[merged_item_b["component"] == component].iloc[0]
        for column in ["share", "covariance_with_ln_y", "variance_ln_y"]:
            max_abs_diff = abs(float(component_row[f"{column}_student"]) - float(component_row[f"{column}_benchmark"]))
            benchmark_rows.append(
                {
                    "check": f"item_b::{component}::{column}",
                    "max_abs_diff": max_abs_diff,
                    "passed": max_abs_diff <= TOL,
                }
            )

    benchmark_item_c = pd.read_csv(benchmark_item_c_path)
    merged_item_c = education_df.merge(benchmark_item_c, on="concept", suffixes=("_student", "_benchmark"))
    for concept in merged_item_c["concept"]:
        concept_row = merged_item_c.loc[merged_item_c["concept"] == concept].iloc[0]
        max_abs_diff = abs(float(concept_row["value_student"]) - float(concept_row["value_benchmark"]))
        benchmark_rows.append(
            {
                "check": f"item_c::{concept}::value",
                "max_abs_diff": max_abs_diff,
                "passed": max_abs_diff <= TOL,
            }
        )

    benchmark_df = pd.DataFrame(benchmark_rows)
    benchmark_csv = output_dir / "p6_p4_student_benchmark_check.csv"
    benchmark_md = output_dir / "p6_p4_student_benchmark_check.md"
    benchmark_df.to_csv(benchmark_csv, index=False)
    save_markdown_table(benchmark_df, benchmark_md, float_columns=["max_abs_diff"])

    failed_rows = benchmark_df.loc[~benchmark_df["passed"]]
    if not failed_rows.empty:
        failed_checks = ", ".join(
            f"{row.check} (max_abs_diff={row.max_abs_diff:.3e})"
            for row in failed_rows.itertuples(index=False)
        )
        raise AssertionError(f"Student benchmark check failed: {failed_checks}")

    summary_path = output_dir / "p6_p4_student_summary.txt"
    summary_lines = [
        f"Unified base data input: {relpath(base_data_path, repo_root)}",
        f"Student country-level output: {relpath(country_level_path, repo_root)}",
        f"Student item (a) with A PDF: {relpath(with_a_pdf, repo_root)}",
        f"Student item (a) without A PDF: {relpath(without_a_pdf, repo_root)}",
        f"Student item (b) CSV: {relpath(item_b_csv, repo_root)}",
        f"Student item (b) MD: {relpath(item_b_md, repo_root)}",
        f"Student item (c) CSV: {relpath(item_c_csv, repo_root)}",
        f"Student item (c) MD: {relpath(item_c_md, repo_root)}",
        f"Student benchmark CSV: {relpath(benchmark_csv, repo_root)}",
        f"Student benchmark MD: {relpath(benchmark_md, repo_root)}",
        f"Sample size: {len(df)}",
        f"Item (b) share sum: {share_sum:.12f}",
        f"Benchmark checks passed: {benchmark_df['passed'].all()}",
        f"Maximum benchmark difference: {benchmark_df['max_abs_diff'].max():.3e}",
    ]
    summary_path.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

    print("\n".join(summary_lines))


if __name__ == "__main__":
    main()
