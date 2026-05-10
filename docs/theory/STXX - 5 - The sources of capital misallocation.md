# The Sources of Capital Misallocation

Joel M. David

Venky Venkateswaran

AER

2019

---

## Introduction

Dispersion in firm-level ARPK $\equiv \frac{PY}{K} \to$ capital ‘misallocation’

- Adjustment costs? information? heterogeneity? ‘distortions’...?

- How to disentangle...?

This paper: Identification strategy using data on revenues and inputs

- Using $PY$, $K$: adjustment/information frictions vs. other factors

- Single factor models yield biased inferences if data reflect more than one

Apply to Chinese manufacturing and US publicly traded firms

- Adjustment/information frictions do not generate significant $\sigma^2_{arpk}$

- Most of $\sigma^2_{arpk}$ stems from other factors – size-dependent and permanent

- Markup/technology heterogeneity modest in China, sizable in the US

---

## Simplified model

Competitive firms, only capital, no aggregate risk

- Production:

$$
Y_{it} = A_{it}K_{it}^{\alpha},
\qquad
a_{it} = a_{it-1} + \mu_{it},
\qquad
\mu_{it} \sim N(0,\sigma^2_{\mu})
$$

Investment:

1. Quadratic adjustment costs:

$$
\Phi(I_{it},K_{it})
=
\frac{\xi}{2}
\left(
\frac{I_{it}}{K_{it}}
\right)^2
K_{it}
$$

2. Imperfect information:

$$
a_{it+1}\mid I_{it}
\sim
N(E_{it}[a_{it+1}],V),
\qquad
V \in [0,\sigma^2_{\mu}]
$$

3. Other factors: implicit tax/subsidy:

$$
\tau_{it+1}
=
\gamma a_{it+1}
+
\varepsilon_{it+1}
$$

- $\gamma \to$ size-dependent; $\varepsilon_{it+1} \overset{iid}{\sim} N(0,\sigma^2_{\varepsilon}) \to$ uncorrelated

$$
\Rightarrow
k_{it+1}
\approx
\psi_1 k_{it}
+
\psi_2(1+\gamma)E_{it}[a_{it+1}]
+
\psi_3\varepsilon_{it+1}
$$

‘Misallocation’ and aggregate TFP

$$
\sigma^2_{arpk}
\equiv
\operatorname{var}(y_{it}-k_{it})
$$

increasing in $\xi$, $V$, $|\gamma|$, $\sigma^2_{\varepsilon}$

$$
a
=
a^*
-
\frac{1}{2}
\frac{\alpha}{1-\alpha}
\sigma^2_{arpk}
$$

decreasing in $\sigma^2_{arpk}$

---

## Identification

The challenge: data moments are functions of all four factors

$\to$ Cannot ID one without controlling for others

Solution: use multiple moments from covariance matrix of $k_{it}$ and $a_{it}$

### Proposition

The parameters $\xi$, $\gamma$, $V$ and $\sigma^2_{\varepsilon}$ are uniquely identified by moments

1. $\operatorname{var}(\Delta k_{it})$

2. $\operatorname{corr}(\Delta k_{it},\Delta k_{it-1})$

3. $\operatorname{corr}(\Delta k_{it},\Delta a_{it-1})$

4. $\operatorname{corr}(\Delta arpk_{it},\Delta a_{it})$.

---

## Identification – intuition

For each parameter pair, examine pair of moments $(M,M')$

$\to$ Key idea: both params. move $M$ in same direction, but $M'$ in opposing ways

Example: adjustment costs $(\xi)$ vs correlated factors $(\gamma)$

$M$: Investment variability $\sigma^2_k$ decreasing in both $\xi$ and $\gamma$

$M'$: Investment autocorrelation $\rho_{k,k-1}$ increasing in $\xi$ but decreasing in $\gamma$

$\Rightarrow$ *Ceteris paribus*, unique $(\xi,\gamma)$ consistent with observed $(\sigma^2_k,\rho_{k,k-1})$

### Imagen / diagrama: ‘Isomoment’ Curves

La diapositiva muestra un diagrama con eje vertical $\xi$ y eje horizontal $\gamma$, donde $\gamma$ aparece aumentando hacia la izquierda y $0$ está a la derecha. Hay dos curvas:

- Una curva decreciente etiquetada $\rho_{k,k-1}$.
- Una curva creciente etiquetada $\sigma^2_k$.

Las curvas se cruzan en un punto. La idea visual es que una misma observación de varianza de inversión y autocorrelación de inversión identifica una combinación única de $\xi$ y $\gamma$, porque ambos parámetros pueden mover un momento en la misma dirección pero el otro en direcciones opuestas.

$$
\operatorname{var}(\Delta k)
=
\frac{
\psi_2^2(1+\gamma)^2\sigma^2_{\mu}
+
2(1-\psi_1)\psi_3^2\sigma^2_{\varepsilon}
}{
1-\psi_1^2
}
$$

$$
\rho_{\Delta k}
=
\psi_1
-
\frac{
\psi_3^2\sigma^2_{\varepsilon}
}{
\operatorname{var}(\Delta k)
}
$$

- $\xi \uparrow \Rightarrow \psi_1 \uparrow,\ \psi_3 \downarrow: \operatorname{var}(\Delta k)\downarrow,\ \rho\uparrow$

- $\gamma \downarrow \Rightarrow (1+\gamma)^2\downarrow: \operatorname{var}(\Delta k)\downarrow,\ \rho\downarrow$

- Potential bias ignoring $\gamma$: targeting $\sigma^2_k$ $(\rho_{k,k-1})$ over(under)-estimates $\xi$

---

## Identification - other cases

- Uncertainty $(V)$ vs correlated factors $(\gamma)$

  - $M_4$: $\rho_{arpk,a} \uparrow$ in $V$ and $\gamma$; $M_3$: $\rho_{k,a-1} \uparrow$ in $V$ and $\downarrow$ in $\gamma$

- Transitory $(\sigma^2_{\varepsilon})$ vs correlated factors $(\gamma)$

  - $M_2$: $\rho_{k,k-1} \downarrow$ in $\gamma$ and $\sigma^2_{\varepsilon}$; $M_4$: $\lambda_{arpk,a} \uparrow$ in $\gamma$ and ind. of $\sigma^2_{\varepsilon}$

- Uncertainty $(V)$ vs adjustment costs $(\xi)$

  - $M_3$: $\rho_{k,a-1} \uparrow$ in $\xi$ and $V$; $M_2$: $\rho_{k,k-1} \uparrow$ in $\xi$ and ind. of $V$

$\Rightarrow$ In each case, unique combination of two params. consistent w both moms.

---

## Quantitative analysis

### Extended model

- Monopolistic competition:

$$
Y_t
=
\left(
\int
\hat{A}_{it}Y_{it}^{\frac{\theta-1}{\theta}}\,di
\right)^{\frac{\theta}{\theta-1}}
$$

- Labor:

$$
Y_{it}
=
K_{it}^{\hat{\alpha}}N_{it}^{1-\hat{\alpha}}
\Rightarrow
\text{profits }
\Pi_{it}
=
GA_{it}K_{it}^{\alpha}
$$

- AR(1) process:

$$
a_{it}
=
\rho a_{it-1}
+
\mu_{it},
\qquad
\mu_{it}\sim N(0,\sigma^2_{\mu})
$$

- Permanent factor:

$$
\tau_{it+1}
=
\gamma a_{it+1}
+
\varepsilon_{it+1}
+
\chi_i,
\qquad
\chi_i\sim N(0,\sigma^2_{\chi})
$$

### Data and estimation

- Panels of Chinese manufacturing and US publicly traded firms (98-09)

- $\theta$, $\hat{\alpha}$: set to standard values

- $\rho$, $\sigma^2_{\mu}$: measure $a_{it}$ directly and estimate AR(1)

- $\xi$, $V$, $\gamma$, $\sigma^2_{\varepsilon}$, $\sigma^2_{\chi}$: follow earlier strategy (additional moment $\sigma^2_{arpk}$)

---

## The sources of ‘misallocation’

|  | Adj Costs | Uncertainty | Correlated | Transitory | Permanent |
|---|---:|---:|---:|---:|---:|
| **Parameters** | $\xi$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
| China | 0.02 | 0.10 | $-0.70$ | 0.00 | 0.41 |
| US | 0.20 | 0.03 | $-0.33$ | 0.03 | 0.29 |

|  | Adj Costs | Uncertainty | Correlated | Transitory | Permanent |
|---|---:|---:|---:|---:|---:|
| **Share of $\sigma^2_{arpk}$** |  |  |  |  |  |
| China | 1.3% | 10.3% | 47.4% | 0.0% | 44.4% |
| US | 10.8% | 7.3% | 14.4% | 6.3% | 64.7% |

|  | Adj Costs | Uncertainty | Correlated | Transitory | Permanent |
|---|---:|---:|---:|---:|---:|
| **TFP Losses** |  |  |  |  |  |
| China | 0.01 | 0.08 | 0.38 | 0.00 | 0.36 |
| US | 0.02 | 0.01 | 0.03 | 0.01 | 0.13 |

1. Adjustment costs and uncertainty do not generate much dispersion in $arpk$

2. Correlated factors substantial in China; permanent factors in both countries

3. Patterns robust to non-convexities, labor frictions, richer processes

1. Adjustment costs are essential to explain firm-level investment dynamics

2. Adjustment cost-only models can lead to significantly biased estimates

3. ’Reasonable’ adjustment costs do not generate substantial $\sigma^2_{arpk}$

---

## Why the small effects from adjustment costs?

Answer: because we match more moments/explicitly control for other factors

- Data: Investment volatility, serial correlation and inaction are all modest

Abstracting from other factors, i.e., an AC-only model targeting

- $\rho_{\iota,\iota-1} \to$ larger non-convexities, but counterfactually high $\sigma^2_{\iota}$ and inaction

- $\sigma^2_{\iota} \to$ larger convex costs, but counterfactually high $\rho_{\iota,\iota-1}$

- Both $\rho_{\iota,\iota-1}$ and $\sigma^2_{\iota} \to$ large costs, but counterfactually high inaction

Reconciling full set of moments requires additional factors

- Correlated factors reduce both $\rho_{\iota,\iota-1}$ and $\sigma^2_{\iota}$

- Uncorrelated factors also help reduce $\rho_{\iota,\iota-1}$ (and have a small effect on $\sigma^2_{\iota}$)

$\Rightarrow$ Low $\rho_{\iota,\iota-1}$ and $\sigma^2_{\iota}$ w/o large non-convexities (and resulting high inaction)

---

## Why the differences with Asker et al. (2014)?

ACD estimate an AC-only model by targeting variability, inaction and spikes

$\to$ Large convex costs but counterfactually high serial correlation

Parameter estimates and key moments:

|  | $\xi$ | $\xi_f$ | $\rho_{\Delta\iota,\Delta\iota-1}$ | $\sigma^2_{\Delta\iota}$ | $\rho_{\iota,\iota-1}$ | $\sigma^2_{\iota}$ | inact | $spk^+$ | $spk^-$ | $\sigma^2_{arpk}$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **US** |  |  |  |  |  |  |  |  |  |  |
| Data | – | – | $-0.30$ | 0.06 | 0.25 | 0.04 | 0.18 | 0.26 | 0.10 | 0.45 |
| DV | 0.25 | 0.002 | $-0.30$ | 0.05 | 0.46 | 0.05 | 0.18 | 0.31 | 0.08 | 0.45 |
| ACD | 0.65 | 0.003 | $-0.18$ | 0.03 | 0.66 | 0.05 | 0.18 | 0.30 | 0.07 | 0.11 |
| **China** |  |  |  |  |  |  |  |  |  |  |
| Data | – | – | $-0.36$ | 0.14 | 0.04 | 0.08 | 0.20 | 0.27 | 0.15 | 0.92 |
| DV | 0.07 | 0.002 | $-0.38$ | 0.11 | 0.24 | 0.08 | 0.21 | 0.35 | 0.13 | 0.92 |
| ACD | 0.80 | 0.012 | $-0.17$ | 0.05 | 0.67 | 0.07 | 0.20 | 0.34 | 0.13 | 0.28 |

---

## Heterogeneity in markups/technologies

Extended production function:

$$
Y_{it}
=
K_{it}^{\hat{\alpha}_{it}}
N_{it}^{\hat{\zeta}-\hat{\alpha}_{it}}
M_{it}^{1-\hat{\zeta}}
$$

### Markups:

- Assume static materials $\to \operatorname{var}(\log markup_{it}) = \operatorname{var}(\log materials\ share_{it})$

- 4% of $\sigma^2_{arpk}$ in China, 14% in the US

### Technologies:

$$
arpk_{it}
=
\log markup_{it}
-
\log \hat{\alpha}_{it}
+
\tau^K_{it}
$$

$$
arpn_{it}
\approx
\log markup_{it}
+
\frac{\bar{\alpha}}{\hat{\zeta}-\bar{\alpha}}
\log \hat{\alpha}_{it}
+
\tau^N_{it}
$$

- If $\hat{\alpha}_{it}\perp\tau_{it}$, then $\operatorname{cov}(arpk_{it},arpn_{it}) \to$ upper bound on $\operatorname{var}(\log \hat{\alpha}_{it})$

- 17% of $\sigma^2_{arpk}$ in China, 38% in the US

### Financial factors

- Act similarly to $\gamma$ (but difficult to disentangle using production data alone)

---

## Conclusion

### Methodological:

- Production-side data can tell us a lot about the drivers of $\sigma^2_{arpk}$

- Essential to analyze sources jointly to reach accurate inferences

### Substantive:

### Imagen / gráfica

La diapositiva muestra dos gráficos de torta, uno para **China** y otro para **US Compustat**, junto con una leyenda de colores:

- Adjustment Costs
- Information
- Markups
- Technologies
- ???

En **China**, la torta está dominada por el componente rojo **???**, con 67%. También aparece **Technologies** con 17%, **Information** con 10%, **Markups** con 5%, y una porción muy pequeña de **Adjustment Costs**.

En **US Compustat**, la distribución es más repartida: **Technologies** representa 38%, **???** representa 30%, **Markups** 14%, **Adjustment Costs** 11%, e **Information** 7%.

**Interpretación contextual:** la figura resume la conclusión sustantiva del paper: los costos de ajuste y la información explican una parte relativamente pequeña de la dispersión de ARPK. En China, una gran parte queda en componentes “unexplained/???” o factores no capturados directamente, mientras que en Estados Unidos la heterogeneidad tecnológica tiene un peso mucho más importante.

---

# Appendix / Additional Slides

---

## Value and Policy Functions

Value function:

$$
V(K_{it},I_{it})
=
\max_{K_{it+1}}
E_{it}
\left[
A_{it}K_{it}^{\alpha}
-
T^K_{it+1}K_{it+1}(1-\beta(1-\delta))
-
\Phi(I_{it},K_{it})
+
\beta V(K_{it+1},I_{it+1})
\right]
$$

Optimal investment (first order approximation):

$$
k_{it+1}
=
\psi_1 k_{it}
+
\psi_2(1+\gamma)E_{it}[a_{it+1}]
+
\psi_3\varepsilon_{it+1}
$$

- $\psi_j$’s depend only on $(\alpha,\beta,\xi)$; independent of $V$ and other factors

- $\psi_1$ $(\psi_2,\psi_3)$ increasing (decreasing) in $\xi$

- Frictionless benchmark:

$$
k_{it+1}
=
\frac{1}{1-\alpha}a_{it+1}
$$

---

## Firm Problem

$$
V(K_{it},I_{it})
=
\max_{K_{it+1}}
E_{it}
\left[
GA_{it}K_{it}^{\alpha}
-
T^K_{it+1}K_{it+1}
+
T^K_{it}(1-\delta)K_{it}
\right]
+
E_{it}
\left[
-\Phi(I_{it},K_{it})
+
\beta V(K_{it+1},I_{it+1})
\right]
$$

Define

$$
\overline{V}(K_{it},I_{it})
\equiv
V(K_{it},I_{it})
-
T^K_{it}(1-\delta)K_{it}
$$

Then,

$$
\overline{V}(K_{it},I_{it})
=
\max_{K_{it+1}}
E_{it}
\left[
GA_{it}K_{it}^{\alpha}
-
T^K_{it+1}K_{it+1}(1-\beta(1-\delta))
\right]
+
E_{it}
\left[
-\Phi(I_{it},K_{it})
+
\beta \overline{V}(K_{it+1},I_{it+1})
\right]
$$

FOC (without adjustment costs)

$$
T^K_{it+1}(1-\beta(1-\delta))
=
\beta E_{it}
\left[
\alpha A_{it+1}K_{it+1}^{\alpha-1}
\right]
$$

---

## Identification – intuition

For each parameter pair, examine pair of moments $(M,M')$

$\to$ Key idea: both params. move $M$ in same direction, but $M'$ in opposing ways

Example: adjustment costs $(\xi)$ vs correlated factors $(\gamma)$

- $M$: Investment variability $\sigma^2_k$ decreasing in both $\xi$ and $\gamma$

- $M'$: Investment autocorrelation $\rho_{k,k-1}$ increasing in $\xi$ but decreasing in $\gamma$

$\Rightarrow$ *Ceteris paribus*, unique $(\xi,\gamma)$ consistent with observed $(\sigma^2_k,\rho_{k,k-1})$

### Imagen / diagrama: ‘Isomoment’ Curves

La diapositiva repite el gráfico con eje vertical $\xi$ y eje horizontal $\gamma$, donde dos curvas de isomomentos se cruzan: una para $\rho_{k,k-1}$ y otra para $\sigma^2_k$. El cruce representa la identificación conjunta de costos de ajuste y factores correlacionados.

- Potential bias ignoring $\gamma$: targeting $\sigma^2_k$ $(\rho_{k,k-1})$ over(under)-estimates $\xi$

---

## Identification - other cases

### Uncertainty $(V)$ vs correlated factors $(\gamma)$

- $M_4$: $\lambda_{arpk,a} \uparrow$ in $V$ and $\gamma$; $M_3$: $\rho_{k,a-1} \uparrow$ in $V$ and $\downarrow$ in $\gamma$

### Transitory $(\sigma^2_{\varepsilon})$ vs correlated factors $(\gamma)$

- $M_2$: $\rho_{k,k-1} \downarrow$ in $\gamma$ and $\sigma^2_{\varepsilon}$; $M_4$: $\lambda_{arpk,a} \uparrow$ in $\gamma$ and ind. of $\sigma^2_{\varepsilon}$

### Uncertainty $(V)$ vs adjustment costs $(\xi)$

- $M_3$: $\rho_{k,a-1} \uparrow$ in $\xi$ and $V$; $M_2$: $\rho_{k,k-1} \uparrow$ in $\xi$ and ind. of $V$

$\Rightarrow$ In each case, unique combination of two params. consistent w both moms.

---

## Data and moments

### China: Annual Surveys of Industrial Producers (1998-2009)

- All industrial firms w/ sales $> 5M$ RMB, $\approx \$600K$

- Remove outliers, industry-year fixed effects

- Final sample: 797,047 firm-year observations

### US: Compustat North America (1998-2009)

- Data treated in the same manner as Chinese firms

- Final sample: 34,260 firm-year observations

### Moments

|  | $\rho$ | $\sigma^2_{\mu}$ | $\rho_{\iota,a-1}$ | $\rho_{\iota,\iota-1}$ | $\rho_{arpk,a}$ | $\sigma^2_{\iota}$ | $\sigma^2_{arpk}$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| China | 0.91 | 0.15 | 0.29 | $-0.36$ | 0.76 | 0.14 | 0.92 |
| US | 0.93 | 0.08 | 0.13 | $-0.30$ | 0.55 | 0.06 | 0.45 |

---

## Contributions to misallocation

Adjustment costs: Solved numerically

Uncertainty:

$$
\Delta\sigma^2_{arpk}
=
\left(
\frac{V}{\sigma^2_{\mu}}
\right)
\sigma^2_{\mu}
$$

Correlated dists:

$$
\Delta\sigma^2_{arpk}
=
\gamma^2\sigma^2_a
=
\gamma^2
\frac{\sigma^2_{\mu}}{1-\rho^2}
$$

Transitory dists:

$$
\Delta\sigma^2_{arpk}
=
\sigma^2_{\varepsilon}
$$

Permanent dists:

$$
\Delta\sigma^2_{arpk}
=
\sigma^2_{\chi}
$$

---

## Non-convex adjustment costs

Add fixed adj cost:

$$
\Phi(I_{it},K_{it})
=
\frac{\xi}{2}
\left(
\frac{I_{it}}{K_{it}}
\right)^2
K_{it}
+
\xi_f
I\{I_{it}\neq 0\}
\Pi(A_{it},K_{it})
$$

Additional moment: ‘inaction’:

$$
Pr\left(
\left|
\frac{I_{it}}{K_{it}}
\right|
<5\%
\right)
=
20\%\ (\text{China}),\ 18\%\ (\text{US})
$$

|  | $\xi$ | $\xi_f$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
|---|---:|---:|---:|---:|---:|---:|
| **Parameters** |  |  |  |  |  |  |
| China | 0.075 | 0.002 | 0.09 | $-0.64$ | 0.00 | 0.44 |
| US | 0.250 | 0.002 | 0.03 | $-0.30$ | 0.02 | 0.29 |

|  | $\xi$ | $\xi_f$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
|---|---:|---:|---:|---:|---:|---:|
| **Share of $\sigma^2_{arpk}$** |  |  |  |  |  |  |
| China | 6.5% | 0.8% | 10.1% | 35.6% | 0.0% | 47.7% |
| US | 13.0% | 1.1% | 7.1% | 11.5% | 4.4% | 64.4% |

Results close to baseline (linearized) model

- Both components relatively modest, generate little $arpk$ dispersion

- Robust to using other moments (e.g., spikes)

---

## Adjustment costs – three main takeaways

1. Adjustment costs are essential to explain firm-level investment dynamics

2. Adjustment cost-only models can lead to significantly biased estimates

3. ’Reasonable’ adjustment costs do not generate substantial $\sigma^2_{arpk}$

---

## Why do we find small effects from adjustment costs?

Answer: because we match more moments/explicitly control for other factors

- Data: Investment volatility, serial correlation and inaction are all modest

Abstracting from other factors, i.e., an AC-only model targeting

- $\rho_{\iota,\iota-1} \to$ larger non-convexities, but counterfactually high $\sigma^2_{\iota}$ and inaction

- $\sigma^2_{\iota} \to$ larger convex costs, but counterfactually high $\rho_{\iota,\iota-1}$

- Both $\rho_{\iota,\iota-1}$ and $\sigma^2_{\iota} \to$ large costs, but counterfactually high inaction

Reconciling full set of moments requires additional factors

- Correlated factors reduce both $\rho_{\iota,\iota-1}$ and $\sigma^2_{\iota}$

- Uncorrelated factors also help reduce $\rho_{\iota,\iota-1}$ (and have a small effect on $\sigma^2_{\iota}$)

$\Rightarrow$ Low $\rho_{\iota,\iota-1}$ and $\sigma^2_{\iota}$ w/o large non-convexities (and resulting high inaction)

---

## Why do we differ from Cooper and Haltiwanger (2006)?

CH estimate an AC-only model by targeting serial correlation and spikes

$\to$ Large non-convex costs but counterfactually high $\sigma^2_{\iota}$ and inaction

Parameter estimates and key moments:

|  | $\xi$ | $\xi_f$ | $\rho_{\Delta\iota,\Delta\iota-1}$ | $\sigma^2_{\Delta\iota}$ | $\rho_{\iota,\iota-1}$ | $\sigma^2_{\iota}$ | inact | $spk^+$ | $spk^-$ | $\sigma^2_{arpk}$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **US** |  |  |  |  |  |  |  |  |  |  |
| Data | – | – | $-0.30$ | 0.06 | 0.25 | 0.04 | 0.18 | 0.26 | 0.10 | 0.45 |
| DV | 0.25 | 0.002 | $-0.30$ | 0.05 | 0.46 | 0.05 | 0.18 | 0.31 | 0.08 | 0.45 |
| CH | 0.11 | 0.130 | $-0.42$ | 0.26 | 0.24 | 0.17 | 0.70 | 0.23 | 0.07 | 0.06 |
| KT | 0.10 | 0.120 | $-0.40$ | 0.24 | 0.27 | 0.16 | 0.34 | 0.21 | 0.06 | 0.05 |
| **China** |  |  |  |  |  |  |  |  |  |  |
| Data | – | – | $-0.36$ | 0.14 | 0.04 | 0.08 | 0.20 | 0.27 | 0.15 | 0.92 |
| DV | 0.07 | 0.002 | $-0.38$ | 0.11 | 0.24 | 0.08 | 0.21 | 0.35 | 0.13 | 0.92 |
| CH | 0.01 | 0.200 | $-0.47$ | 2.23 | 0.05 | 1.17 | 0.60 | 0.28 | 0.12 | 0.05 |
| KT | 0.01 | 0.190 | $-0.47$ | 2.28 | 0.05 | 1.19 | 0.24 | 0.27 | 0.11 | 0.04 |

---

## Why do we differ from Asker et al. (2014)?

ACD estimate an AC-only model by targeting variability, inaction and spikes

$\to$ Large convex costs but counterfactually high serial correlation

Parameter estimates and key moments:

|  | $\xi$ | $\xi_f$ | $\rho_{\Delta\iota,\Delta\iota-1}$ | $\sigma^2_{\Delta\iota}$ | $\rho_{\iota,\iota-1}$ | $\sigma^2_{\iota}$ | inact | $spk^+$ | $spk^-$ | $\sigma^2_{arpk}$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **US** |  |  |  |  |  |  |  |  |  |  |
| Data | – | – | $-0.30$ | 0.06 | 0.25 | 0.04 | 0.18 | 0.26 | 0.10 | 0.45 |
| DV | 0.25 | 0.002 | $-0.30$ | 0.05 | 0.46 | 0.05 | 0.18 | 0.31 | 0.08 | 0.45 |
| ACD | 0.65 | 0.003 | $-0.18$ | 0.03 | 0.66 | 0.05 | 0.18 | 0.30 | 0.07 | 0.11 |
| **China** |  |  |  |  |  |  |  |  |  |  |
| Data | – | – | $-0.36$ | 0.14 | 0.04 | 0.08 | 0.20 | 0.27 | 0.15 | 0.92 |
| DV | 0.07 | 0.002 | $-0.38$ | 0.11 | 0.24 | 0.08 | 0.21 | 0.35 | 0.13 | 0.92 |
| ACD | 0.80 | 0.012 | $-0.17$ | 0.05 | 0.67 | 0.07 | 0.20 | 0.34 | 0.13 | 0.28 |

---

## Frictional labor

Assume $N$ chosen under same frictions/distortions as $K$

$\to$ Same structure with higher $\alpha\left(=1-\frac{1}{\theta}\right)$

Results for China:

| Parameters | $\xi$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
|---|---:|---:|---:|---:|---:|
|  | 0.11 | 0.11 | $-0.68$ | 0.04 | 0.30 |

| Agg Effects | $\xi$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
|---|---:|---:|---:|---:|---:|
| Share of $\sigma^2_{arpk}$ | 12.8% | 11.3% | 51.2% | 4.0% | 32.2% |
| TFP Losses | 0.36 | 0.32 | 1.44 | 0.11 | 0.90 |

Parameter estimates – and contribution to $arpk$ dispersion – close to baseline

- Larger TFP losses from all factors (likely upper bound)

---

## Labor distortions

Assume labor choice subject to arbitrary firm-specific ‘taxes’ $T^N_{it}$:

$$
\Pi
=
\max_{N_{it}}
Y^{\frac{1}{\theta}}
\hat{A}_{it}
K_{it}^{\alpha_1}
N_{it}^{\alpha_2}
-
WT^N_{it}N_{it}
$$

Maximized profits:

$$
\Pi_{it}
=
GA_{it}K_{it}^{\alpha},
$$

where

$$
A_{it}
=
\left(
\frac{\hat{A}_{it}}{(T^N_{it})^{\alpha_2}}
\right)^{\frac{1}{1-\alpha_2}}
$$

$\Rightarrow$ Changes interpretation of $A_{it}$ but strategy and conclusions still valid

---

## Fixed effects in productivity

$$
a_{it}
=
\bar{a}_i
+
\hat{a}_{it},
\qquad
\bar{a}_i\sim N(0,\sigma^2_{\bar{a}})
$$

$$
\hat{a}_{it}
=
\rho \hat{a}_{it-1}
+
\mu_{it},
\qquad
\mu_{it}\sim N(0,\sigma^2_{\mu})
$$

Estimate $\sigma^2_{\bar{a}}$ by adding serial correlation of $\Delta a$

| Parameters | $\rho$ | $\sigma^2_{\mu}$ | $\sigma^2_{\bar{a}}$ | $\xi$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| China | 0.87 | 0.14 | 0.29 | 0.12 | 0.10 | $-0.71$ | 0.00 | 0.42 |
| US | 0.84 | 0.08 | 0.33 | 0.76 | 0.04 | $-0.38$ | 0.00 | 0.30 |

| Share of $\sigma^2_{arpk}$ | $\xi$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
|---|---:|---:|---:|---:|---:|
| China | 1.1% | 10.3% | 47.8% | 0.0% | 46.1% |
| US | 6.7% | 8.1% | 18.9% | 1.1% | 65.9% |

$\Rightarrow$ Sizable fixed effects, but other parameter estimates largely unchanged

---

## AR(1) process for other factors

$$
\tau_{it}
=
\gamma a_{it}
+
\hat{\tau}_{it}
+
\chi_i
$$

$$
\hat{\tau}_{it}
=
\rho_{\tau}\hat{\tau}_{it-1}
+
\varepsilon_{it}
$$

- Estimate by adding second-order serial correlation of $arpk$

- (identification proof extends in random walk case)

| Parameters | $\xi$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\rho_{\tau}$ | $\sigma^2_{\chi}$ |
|---|---:|---:|---:|---:|---:|---:|
| China | 0.24 | 0.09 | $-0.69$ | 0.00 | 0.00 | 0.40 |
| US | 1.00 | 0.03 | $-0.34$ | 0.01 | 0.00 | 0.28 |

$\Rightarrow$ $\rho_{\tau}$ essentially zero, other parameters largely unchanged

---

## Role of country-specific $\alpha$

Re-estimate on Chinese data with same $\alpha$ as US

|  | Adj Costs | Uncertainty | Correlated | Transitory | Permanent |
|---|---:|---:|---:|---:|---:|
| **Parameters** | $\xi$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
|  | 0.02 | 0.09 | $-0.63$ | 0.00 | 0.51 |

| Agg Effects | Adj Costs | Uncertainty | Correlated | Transitory | Permanent |
|---|---:|---:|---:|---:|---:|
| Share of $\sigma^2_{arpk}$ | 1.1% | 9.4% | 36.1% | 0.0% | 55.2% |
| TFP Losses | 0.00 | 0.04 | 0.14 | 0.00 | 0.22 |

$\Rightarrow$ Similar patterns and magnitudes as baseline

---

## Interactions between factors - US

|  | Adj Costs | Uncertainty | Correlated | Transitory | Permanent |
|---|---:|---:|---:|---:|---:|
| **Parameters** | $\xi$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
|  | 0.20 | 0.03 | $-0.33$ | 0.03 | 0.29 |

### In isolation

|  | Adj Costs | Uncertainty | Correlated | Transitory | Permanent |
|---|---:|---:|---:|---:|---:|
| Contr. to $\sigma^2_{arpk}$ | 0.05 | 0.03 | 0.06 | 0.03 | 0.29 |
| Share of $\sigma^2_{arpk}$ | 10.8% | 7.3% | 14.4% | 6.3% | 64.7% |

### Joint

|  | Adj Costs | Uncertainty | Correlated | Transitory | Permanent |
|---|---:|---:|---:|---:|---:|
| Contr. to $\sigma^2_{arpk}$ | 0.04 | 0.03 | 0.08 | 0.00 | 0.29 |
| Share of $\sigma^2_{arpk}$ | 8.0% | 5.7% | 17.4% | 0.3% | 64.7% |

$\Rightarrow$ Some interaction, though quantitatively modest

---

## Heterogeneous capital elasticities - details

Abstract from adjustment/information frictions, adjust $arpk$, $arpn$ for markups:

$$
arpk^g_{it}
=
\log\left(
\frac{P_{it}Y_{it}}{K_{it}}
\right)
-
\log\left(
\frac{P_{it}}{MC_{it}}
\right)
=
-\log \hat{\alpha}_{it}
+
\tau^K_{it}
$$

$$
arpn^g_{it}
=
\log\left(
\frac{P_{it}Y_{it}}{N_{it}}
\right)
-
\log\left(
\frac{P_{it}}{MC_{it}}
\right)
\approx
\frac{\bar{\alpha}}{\hat{\zeta}-\bar{\alpha}}
\log \hat{\alpha}_{it}
+
\tau^N_{it}
$$

### Proposition

If $\log \hat{\alpha}_{it}$ is uncorrelated with $\tau^K_{it}$ and $\tau^N_{it}$, then

$$
\sigma^2(\log \hat{\alpha}_{it})
\leq
\frac{
\sigma^2_{arpk^g}\sigma^2_{arpn^g}
-
\operatorname{cov}(arpk^g_{it},arpn^g_{it})^2
}{
2\frac{\bar{\alpha}}{\hat{\zeta}-\bar{\alpha}}
\operatorname{cov}(arpk^g_{it},arpn^g_{it})
+
\left(
\frac{\bar{\alpha}}{\hat{\zeta}-\bar{\alpha}}
\right)^2
\sigma^2_{arpk^g}
+
\sigma^2_{arpn^g}
}
$$

$\to$ Greater $\operatorname{cov}(arpk_{it},arpn_{it})$ implies lower potential for dispersion in $\log \hat{\alpha}_{it}$

---

## Heterogeneous materials elasticities

Production function:

$$
Y_{it}
=
K_{it}^{\hat{\alpha}_{it}}
N_{it}^{\hat{\zeta}_{it}-\hat{\alpha}_{it}}
M_{it}^{1-\hat{\zeta}_{it}}
$$

$$
arpk_{it}
=
\log markup_{it}
-
\log \hat{\alpha}_{it}
+
\tau^K_{it}
+
constant
$$

$$
arpn_{it}
\approx
\log markup_{it}
+
\frac{\bar{\alpha}}{\bar{\zeta}-\bar{\alpha}}
\log \hat{\alpha}_{it}
-
\frac{\bar{\zeta}}{\bar{\zeta}-\bar{\alpha}}
\log \hat{\zeta}_{it}
+
\tau^N_{it}
+
constant
$$

$$
arpm_{it}
\approx
\log markup_{it}
+
\frac{\bar{\zeta}}{1-\bar{\zeta}}
\log \hat{\zeta}_{it}
+
constant
$$

### Proposition

Assume

$$
markup_{it}
\perp
(\hat{\alpha}_{it},\hat{\zeta}_{it})
\perp
(\tau^K_{it},\tau^N_{it})
$$

(arbitrary correlation within each group). Then, $\sigma^2(\log \hat{\alpha}_{it})$ can be bounded and $\sigma^2(\log markup_{it})$ identified by the covariance matrix of $arpk_{it}$, $arpn_{it}$ and $arpm_{it}$.

$\to$ Results close to baseline version in both countries

---

## Size-dependent factors

Add component correlated with $K$:

$$
\tau_{it}
=
\gamma_k k_{it}
+
\gamma a_{it}
+
\varepsilon_{it}
+
\chi_i
$$

- E.g., size-related policies, financial frictions, ...

$$
k_{it+1}
=
\frac{1}{
(1+\beta)\hat{\xi}
+
1-\alpha-\gamma_k
}
\left\{
\hat{\xi}k_{it}
+
(1+\gamma)E_{it}[a_{it+1}]
+
\varepsilon_{it+1}
+
\beta\hat{\xi}E_{it}[k_{it+2}]
\right\}
$$

### Implications

- Effective curvature in policy function: $\alpha+\gamma_k$

- Dampens (amplifies) investment volatility if $\gamma_k<0$ $(>0)$

### Identification

- If only friction, isomorphic to

$$
\gamma
=
\frac{\gamma_k}{1-\alpha-\gamma_k}
$$

- More generally, cannot separately ID $\gamma$ and $\gamma_k$ with data on $(PY,K)$

$\to$ Derive results for $\alpha+\gamma_k\in[0.36,0.71]$

---

## Size vs prod-dependent factors - China

| Correlated Component | Size-Dependent<br>$\gamma_k$ | Prod.-Dependent<br>$\gamma$ | Total |
|---|---:|---:|---:|
| **$\alpha+\gamma_k=0.71$ (baseline)** |  |  |  |
| Parameters | 0.00 | $-0.70$ |  |
| Share of $\sigma^2_{arpk}$ | 0.0% | 47.4% | 47.4% |
| **$\alpha+\gamma_k=0.54$** |  |  |  |
| Parameters | $-0.18$ | $-0.51$ |  |
| Share of $\sigma^2_{arpk}$ | 14.2% | 25.4% | 39.6% |
| **$\alpha+\gamma_k=0.36$** |  |  |  |
| Parameters | $-0.36$ | $-0.33$ |  |
| Share of $\sigma^2_{arpk}$ | 29.6% | 10.2% | 39.8% |

$\Rightarrow$ Larger $\gamma_k$ reduces $\gamma \to$ total contribution largely unchanged

---

## Financial frictions

Firms face liquidity cost: $\Upsilon(K_{it+1},B_{it+1})$, $\Upsilon_1>0$, $\Upsilon_2<0$

- $B_{it+1} \equiv$ Liquid assets, rate of return $R < \frac{1}{\beta}$

- Interpretation: Firms must hold low-return assets in order to operate

Tractable functional form:

$$
\Upsilon(K_{it+1},B_{it+1})
=
\hat{\nu}
K_{it+1}^{\omega_1}
B_{it+1}^{\omega_2}
$$

- Smoothed, flexible version of $K_{it}\leq \lambda B_{it}$

Firm problem:

$$
V(K_{it},B_{it},I_{it})
=
\max_{B_{it+1},K_{it+1}}
\Pi(K_{it},A_{it})
+
RB_{it}
-
B_{it+1}
-
\hat{\nu}
K_{it+1}^{\omega_1}
B_{it+1}^{\omega_2}
-
\Phi(I_{it},K_{it})
$$

$$
-
K_{it+1}(1-\beta(1-\delta))
+
\beta E_{it}
\left[
V(K_{it+1},B_{it+1},I_{it+1})
\right]
$$

Optimality:

$$
k_{it+1}
=
\frac{1}{
(1+\beta)\hat{\xi}
+
1-\alpha-\gamma_k
}
\left\{
(1+\gamma)E_{it}[a_{it+1}]
+
\varepsilon_{it+1}
+
\beta\hat{\xi}E_{it}[k_{it+2}]
+
\hat{\xi}k_{it}
\right\}
$$

where

$$
\gamma_k
=
-\nu
\left(
\frac{\omega_1}{1+\omega_2}
-
1
\right),
\qquad
\nu>0
$$

$\Rightarrow$ Isomorphic to size-dependent factor (acts similarly to $\gamma$)

---

## Additive measurement error

$$
\hat{X}_{it}
=
X_{it}
+
e_{it}
$$

- Follow Bils, Klenow and Ruane (2017), estimate:

$$
\Delta \widehat{rev}_{it}
=
\Phi \widehat{arpk}_{it}
+
\Psi \Delta \hat{k}_{it}
-
\Psi(1-\lambda)\widehat{arpk}_{it}\cdot \Delta \hat{k}_{it}
+
D_{jt}
+
\epsilon_{it}
$$

- Under some conditions,

$$
1-\lambda
=
\frac{\sigma^2_e}{\hat{\sigma}^2_{arpk}}
$$

Findings: Modest role for additive measurement error

- $1-\lambda=0.08$ in China, $0.12$ in US

---

## Estimates for other countries/firms

| Parameters | $\xi$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
|---|---:|---:|---:|---:|---:|
| Colombia | 0.54 | 0.05 | $-0.55$ | 0.01 | 0.60 |
| Mexico | 0.13 | 0.04 | $-0.82$ | 0.00 | 0.42 |
| China Compustat | 0.15 | 0.03 | $-0.69$ | 0.00 | 0.18 |

| Share of $\sigma^2_{arpk}$ | $\xi$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
|---|---:|---:|---:|---:|---:|
| Colombia | 2.5% | 5.6% | 30.9% | 0.7% | 61.3% |
| Mexico | 0.5% | 4.9% | 44.9% | 0.0% | 52.8% |
| China Compustat | 0.8% | 6.3% | 54.0% | 0.2% | 43.7% |

| TFP Losses | $\xi$ | $V$ | $\gamma$ | $\sigma^2_{\varepsilon}$ | $\sigma^2_{\chi}$ |
|---|---:|---:|---:|---:|---:|
| Colombia | 0.01 | 0.02 | 0.13 | 0.00 | 0.26 |
| Mexico | 0.00 | 0.02 | 0.16 | 0.00 | 0.18 |
| China Compustat | 0.00 | 0.02 | 0.19 | 0.00 | 0.16 |

Similar story as Chinese manufacturing firms

- Adj costs and uncertainty: modest contribution to $\sigma^2_{arpk}$

- Important role for correlated and permanent components

---

## Results for other countries

### Imagen / gráfica

La diapositiva muestra un gráfico de barras apiladas con países en el eje horizontal:

**ARG, BRA, CHN, COL, MEX, MYS, TWN, THA, TUR, JPN, USA**

El eje vertical mide **Percent of Total Dispersion**, de 0 a 100. Cada barra está dividida en cinco componentes:

- rojo: **Adj. Costs**
- amarillo: **Information**
- celeste: **Markups**
- verde: **Technologies**
- azul: **Unexplained**

La mayor parte de cada barra se reparte entre **Technologies** y **Unexplained**. Los costos de ajuste son generalmente una fracción pequeña, con una excepción más visible en USA. La información también aparece como una fracción relativamente modesta. Los markups son más importantes en algunos países —por ejemplo Colombia, México y USA— pero no dominan la dispersión total.

Visualmente:

- Argentina y Brasil tienen grandes componentes verdes y azules.
- China muestra un componente azul importante, tecnologías relevantes y una fracción pequeña de markups/information.
- Colombia tiene una porción celeste notable de markups y una porción verde grande.
- USA muestra una composición más repartida, con partes visibles de adjustment costs, information, markups, technologies y unexplained.

Source: World Bank, *Reviving Global Productivity*, November 2018

**Interpretación contextual:** la gráfica extiende la lectura del paper a otros países: los costos de ajuste y la información rara vez explican la mayor parte de la dispersión total. La parte dominante suele venir de tecnologías, componentes permanentes/no explicados, u otros factores persistentes.

---

## Time series of moments - China

`Figures/CHNmomentsTSplot_2_venky-eps-converted-to.pdf`

$\Rightarrow$ Key moments (and therefore, drivers of misallocation) stable over the sample

### Imagen / nota visual

La diapositiva parece tener un marcador de archivo/figura no renderizado en el centro, con el texto del path `Figures/CHNmomentsTSplot_2_venky-eps-converted-to.pdf`. No se ve una gráfica completa en el PDF renderizado. La conclusión visible es que los momentos clave —y por tanto los drivers de misallocation— son estables a lo largo de la muestra para China.