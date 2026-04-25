from __future__ import annotations

from pathlib import Path
import os

SCRIPT_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = SCRIPT_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MPLCONFIGDIR = OUTPUT_DIR / "mplconfig"
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
TOL = 1e-10

EDUCATION_GROUPS = ["no_schooling", "primary", "secondary", "tertiary"]
Z_LOG = {
    "no_schooling": 0.28,
    "primary": 0.60,
    "secondary": 0.93,
    "tertiary": 1.20,
}
PLOT_LABEL_CODES = {"USA", "ARG", "AUS", "CHN", "IND", "DEU", "BRA", "MEX"}
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

    labels_df = df[df["countrycode"].isin(PLOT_LABEL_CODES)].copy()
    for row in labels_df.itertuples(index=False):
        ax.annotate(
            row.countrycode,
            (getattr(row, x_col), getattr(row, y_col)),
            xytext=(4, 4),
            textcoords="offset points",
            fontsize=8,
        )

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
    base_data_path = SCRIPT_DIR / "p6_p4_unified_base_data.csv"
    output_dir = SCRIPT_DIR / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    if not base_data_path.exists():
        raise FileNotFoundError("Missing p6_p4_unified_base_data.csv in the same folder as the script.")

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
        raise KeyError(f"Missing columns in p6_p4_unified_base_data.csv: {missing_columns}")

    if set(df["year"]) != {YEAR}:
        raise AssertionError(f"The script expects only year {YEAR}.")
    if US_CODE not in set(df["countrycode"]):
        raise AssertionError("The data must contain the United States.")

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
        raise AssertionError("The input CSV has missing values in key columns.")

    theta_sum_check = df[[f"theta_{group}" for group in EDUCATION_GROUPS]].sum(axis=1)
    if not np.allclose(theta_sum_check.to_numpy(), 1.0, atol=TOL, rtol=0.0):
        raise AssertionError("Education shares must sum to one.")

    for group in EDUCATION_GROUPS:
        df[f"Z_{group}"] = np.exp(Z_LOG[group])

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

    us_columns = [
        "ln_y_rel_us",
        "ln_tilde_A_rel_us",
        "ln_K_over_Y_rel_us",
        "ln_capital_factor_rel_us",
        "ln_h_rel_us",
        "ln_yhat_with_A_rel_us",
        "ln_yhat_without_A_rel_us",
    ]
    for column in us_columns:
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
            "share": "participacion",
            "covariance_with_ln_y": "covarianza_con_ln_y",
            "variance_ln_y": "varianza_ln_y",
        }
    )
    save_markdown_table(
        variance_md,
        item_b_md,
        float_columns=["participacion", "covarianza_con_ln_y", "varianza_ln_y"],
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
        raise AssertionError("Item (c) human capital identity failed.")
    if not np.isclose(
        added_contribution_from_firm_productivity,
        firm_productivity_education_channel,
        atol=TOL,
        rtol=0.0,
    ):
        raise AssertionError("Item (c) firm productivity contribution identity failed.")
    if not np.isclose(
        ratio_total_to_human_capital_only,
        total_education_contribution / human_capital_only,
        atol=TOL,
        rtol=0.0,
    ):
        raise AssertionError("Item (c) ratio identity failed.")

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

    summary_path = output_dir / "p6_p4_student_summary.txt"
    summary_lines = [
        "Input CSV: p6_p4_unified_base_data.csv",
        "Output folder: output/",
        "Country-level CSV: output/p6_p4_student_country_level.csv",
        "Item (a) with A PDF: output/p6_p4_student_item_a_with_A_relative.pdf",
        "Item (a) without A PDF: output/p6_p4_student_item_a_without_A_relative.pdf",
        "Item (b) CSV: output/p6_p4_student_item_b_variance_decomposition.csv",
        "Item (b) MD: output/p6_p4_student_item_b_variance_decomposition.md",
        "Item (c) CSV: output/p6_p4_student_item_c_education_contribution.csv",
        "Item (c) MD: output/p6_p4_student_item_c_education_contribution.md",
        f"Sample size: {len(df)}",
        f"Item (b) share sum: {share_sum:.12f}",
    ]
    summary_path.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

    print("\n".join(summary_lines))


if __name__ == "__main__":
    main()
