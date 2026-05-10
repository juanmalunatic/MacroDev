# Misallocation, Establishment Size, and Productivity

Bento & Restuccia

American Economic Journal: Macroeconomics, 2017

---

## Motivation

Widely studied question: what accounts for TFP differences across countries?

$\Rightarrow$ Misallocation of resources among heterogeneous production units or establishments that differs across countries

(Restuccia & Rogerson 2008; Hsieh & Klenow 2009)

Motivation: substantial cross-country differences in establishment-level productivity and investment in intangible capital

Policy distortions not only misallocate resources across heterogeneous establishments . . .

. . . but also affect the productivity distribution

$\Rightarrow$ Thus generating larger effects on aggregate productivity

---

## Data

Goal: internationally comparable measure of average establishment size for a large sample of countries representative of the world income distribution

Include all establishments regardless of whether they are registered or not, and whether they have paid employees or not

134 countries, from 2000 to 2012

---

## Findings

- Positive correlation; elasticity of establishment size w.r.t. GDP per capita is 0.29; even stronger excluding small countries with populations $<500,000$; elasticity 0.35

- Not systematically related to population

### Imagen / gráficas

La diapositiva muestra dos scatter plots en escala logarítmica.

### Gráfico izquierdo

Título visible bajo la figura:

**Figure 1. Establishment Size and GDP Per Capita**

El eje horizontal es **GDP per capita (log scale)**, con valores desde aproximadamente 500 hasta 50,000. El eje vertical es **Establishment size (log scale)**, con valores desde cerca de 1 hasta 50.

Cada punto representa un país, identificado con códigos de tres letras. Hay una nube ascendente: países con menor PIB per cápita tienden a tener establecimientos más pequeños; países con mayor PIB per cápita tienden a tener establecimientos más grandes. Hay una línea de ajuste positiva.

**Interpretación contextual:** esta figura documenta el hecho empírico central: en países más ricos, el establecimiento promedio es más grande. Esto motiva un modelo donde las distorsiones reducen el tamaño de los establecimientos y, al hacerlo, también afectan productividad agregada.

### Gráfico derecho

Título visible bajo la figura:

**Figure 2. Establishment Size and GDP Per Capita, Large Countries**

El gráfico repite la relación entre tamaño de establecimiento y PIB per cápita, pero excluyendo países pequeños. La pendiente positiva se ve incluso más clara. La nube de puntos sigue mostrando que los países de mayor ingreso tienen establecimientos promedio más grandes.

**Interpretación contextual:** al excluir países con poblaciones menores a 500,000, la relación no desaparece sino que se fortalece. Esto sugiere que el patrón no se explica solamente por casos pequeños o atípicos.

---

## Environment I

The representative final-good firm produces output using a variety of inputs from intermediate-good firms:

$$
Y =
\left(
\int_0^N y_i^{\frac{\sigma-1}{\sigma}}\,di
\right)^{\frac{\sigma}{\sigma-1}}
$$

$N$: number of intermediate-good firms

$y_i$: demand for input $i$

$\sigma > 1$: constant elasticity of substitution between varieties

Each intermediate-good firm has access to:

$$
y = sz\ell
$$

where $sz$ is productivity and $\ell$ is labor

---

## Environment II

An entrant’s realized $z$ is drawn from a known exogenous distribution; $s$ is determined endogenously

After paying entry cost $c_eY$, but before realizing $z$, an entrant chooses initial productivity $s_0$ at cost $c_SYs_0^\theta$, $c_S>0$, $\theta>1$

Each period, incumbents increase productivity by factor $(1+g)$ at cost

$$
c_g(1+g)^\phi \Omega(s_{-1},z),
\qquad
c_g>0,
\qquad
\phi>1,
$$

where

$$
\Omega(s_{-1},z)
=
\frac{Y_{-1}}{N_{-1}}
\cdot
\frac{
(s_{-1}z)^{\sigma(1-\gamma)-1}
}{
\frac{1}{N_{-1}}
\int_0^{N_{-1}}
(s_{-1,i}z_i)^{\sigma(1-\gamma)-1}\,di
}
$$

### Note

The cost of per-period productivity investment is increasing in the relative profitability of a firm. This ensures that Gibrat’s Law holds: firm growth is independent of initial size.

---

## The Role of the Normalization in $\Omega$

Why the cross-sectional mean in the denominator? To enforce Gibrat’s Law.

Benefit of raising productivity by $(1+g)$ for firm $i$:

$$
\Delta \pi_i
\propto
(s_{-1}z)^{\sigma(1-\gamma)-1}
\cdot
\left[
(1+g)^{\sigma(1-\gamma)-1}
-
1
\right]
$$

More productive firms gain more in absolute terms from the same $g$ — because their profits scale more steeply with productivity.

Cost

$$
=
c_g(1+g)^\phi\Omega(s_{-1},z),
$$

and since

$$
\Omega(s_{-1},z)
\propto
\frac{
(s_{-1}z)^{\sigma(1-\gamma)-1}
}{
(\overline{sz})^{\sigma(1-\gamma)-1}
}
$$

cost also scales with the same power of $(s_{-1}z)^{\sigma(1-\gamma)-1}$.

FOC for $g$: dividing benefit by cost, the term $(s_{-1}z)^{\sigma(1-\gamma)-1}$ cancels exactly $\Rightarrow$ all incumbents choose the same $g^* \Rightarrow$ Gibrat’s Law holds.

### Economic interpretation of each component

Numerator $(s_{-1}z)^{\sigma(1-\gamma)-1}$: firm $i$’s own profits

Denominator $(\overline{sz})^{\sigma(1-\gamma)-1}$: industry average profits $\Rightarrow$ ratio = relative profitability

Prefactor $Y_{-1}/N_{-1}$: average output per firm, keeping costs in revenue units and ensuring a balanced growth path

---

## Environment III

At the end of each period, each intermediate producer faces an exogenous exit probability $\lambda$

Output distortions: each firm retains fraction $(1-\tau_i)$ of its output:

$$
(1-\tau_i) = (s_i z_i)^{-\gamma}
$$

$\gamma$ is the elasticity of a firm’s distortion w.r.t. its productivity

Given these assumptions: all entrants choose the same $s_0$; all incumbents choose the same $g$ each period; the cross-sectional productivity distribution is stationary

Exogenous interest rate $R$

---

## Equilibrium — Firm Demands

Final-good firm $\Rightarrow$ inverted demand for each input $i$:

$$
P_i = Y^{1/\sigma}y_i^{-1/\sigma}
$$

Operating profits for an incumbent:

$$
\pi_i
=
(1-\tau_i)Y^{1/\sigma}y_i^{(\sigma-1)/\sigma}
-
w\ell_i,
\qquad
y_i = s_i z_i \ell_i
$$

Firms choose labor to maximize operating profits $\Rightarrow$:

$$
\ell_i
=
\frac{
(1-\tau_i)^\sigma Y(s_i z_i)^{\sigma-1}
}{
w^\sigma
}
\left(
\frac{\sigma-1}{\sigma}
\right)^\sigma
$$

$$
y_i
=
\frac{
(1-\tau_i)^\sigma Y(s_i z_i)^\sigma
}{
w^\sigma
}
\left(
\frac{\sigma-1}{\sigma}
\right)^\sigma
$$

---

## Equilibrium — Aggregate Output

Per-period operating profits:

$$
\pi_i
=
\frac{
(1-\tau_i)^\sigma Y(s_i z_i)^{\sigma-1}
(\sigma-1)^{\sigma-1}w^{\sigma-1}
}{
\sigma^\sigma
}
$$

Combining with the final-good production function and labor-market clearing:

$$
Y
=
\left[
\int_0^N
(s_i z_i)^{\sigma-1}
\left(
\frac{1-\tau_i}{1-\bar{\tau}}
\right)^{\sigma-1}
di
\right]^{1/(\sigma-1)}
$$

$$
w
=
(1-\bar{\tau})
\frac{\sigma-1}{\sigma}
Y
$$

where $(1-\bar{\tau})$ is the output-weighted average of $(1-\tau_i)$:

$$
(1-\bar{\tau})
=
\int_0^N
\frac{P_i y_i}{Y}
(1-\tau_i)\,di
$$

---

## Equilibrium — Distortions and Productivity

Output can be rewritten as:

$$
Y
=
\left[
\int_0^N
\left(
s_i z_i
\frac{MRPL}{MRPL_i}
\right)^{\sigma-1}
di
\right]^{1/(\sigma-1)}
$$

where (following Hsieh & Klenow 2009):

$$
MRPL_i
=
\frac{P_i y_i}{\ell_i}
\propto
\frac{1}{1-\tau_i}
$$

### Imagen / diagrama

La diapositiva incluye un diagrama conceptual con eje horizontal:

$$
\ln(sz)
$$

y eje vertical:

$$
\ln\left(\frac{1}{1-\tau_i}\right)
$$

También aparece una línea horizontal de referencia:

$$
\ln\left(\frac{1}{1-\bar{\tau}}\right)
$$

Hay dos rectas ascendentes que representan la relación entre productividad y distorsión:

- **Low $\gamma$**: una pendiente más baja.
- **High $\gamma$**: una pendiente más alta.

Título visible:

**Figure 4. Firm-Level Distortions and Productivity**

**Interpretación contextual:** el gráfico muestra qué significa una distorsión correlacionada con productividad. Si $\gamma$ es alto, las firmas más productivas enfrentan una cuña mayor: retienen una fracción menor de su producto, o equivalentemente enfrentan un mayor $MRPL_i$. Esto desalienta que las firmas más productivas se expandan e inviertan, generando mala asignación y una distribución de productividad más comprimida.

---

## Value of an Incumbent Firm

$$
V(s_{-1},z)
=
\pi_{-1}(1+g)^{\sigma(1-\gamma)-1}
\cdot \Psi
-
c_g(1+g)^\phi \Omega(s_{-1},z)
$$

$$
-
c_g(1+g')^\phi \Omega(s_{-1},z)
\cdot
\frac{
(1-\lambda)(1+g)^{\sigma(1-\gamma)-1}
}{
1+R
}
\cdot \Psi
$$

where

$$
\Psi
\equiv
\sum_{t=0}^{\infty}
\left[
\frac{
(1-\lambda)(1+g')^{\sigma(1-\gamma)-1}
}{
1+R
}
\right]^t
=
\frac{
1+R
}{
1+R-(1-\lambda)(1+g')^{\sigma(1-\gamma)-1}
}
$$

First term: PDV of current and future operating profits

Second term: current cost of productivity investment $g$

Third term: PDV of all future investment costs at rate $g'$

---

## Maximization Problem

Maximizing $V$ w.r.t. $(1+g)$ and imposing $g=g'$ in steady state:

$$
c_g(1+g)^\phi
=
\frac{
[\sigma(1-\gamma)-1](1+g)^{\sigma(1-\gamma)-1}
}{
(1-\bar{\tau})^\sigma
}
\cdot
\Theta
$$

where

$$
\Theta
\equiv
\frac{
1+R
}{
\phi(1+R)
-
[\phi+1-(\sigma(1-\gamma)-1)](1-\lambda)(1+g)^{\sigma(1-\gamma)-1}
}
$$

---

## Stationary Equilibrium

$$
s_0
=
\left[
\frac{
c_e[\sigma(1-\gamma)-1]
}{
c_S[\theta+1-(\sigma(1-\gamma)-1)]
}
\right]^{1/\theta}
\qquad
\text{(entrant productivity)}
$$

$$
(1+g)^{\phi+1-(\sigma(1-\gamma)-1)}
=
\frac{
[\sigma(1-\gamma)-1](1-\bar{\tau})^\sigma
}{
c_g
}
\cdot
\Theta
\qquad
\text{(life-cycle growth)}
$$

$$
N
=
\frac{
[\theta+1-(\sigma(1-\gamma)-1)](1-\bar{\tau})^\sigma\phi
}{
[1-(1-\lambda)(1+g)^{\sigma(1-\gamma)-1}]\lambda c_e\theta
}
\cdot
\Theta
\qquad
\text{(number of firms)}
$$

Aggregate investment in productivity:

$$
\lambda N c_S s_0^\theta
+
(1-\lambda)c_g(1+g)^\phi
=
\frac{
[\sigma(1-\gamma)-1](1-\bar{\tau})^\sigma
}{}
\cdot
\Theta
\cdot
\left[
\frac{\phi\xi}{\theta}
+
(1-\lambda)(1+g)^{\sigma(1-\gamma)-1}
\right]
$$

where

$$
\xi
=
1-(1-\lambda)(1+g)^{\sigma(1-\gamma)-1}.
$$

---

## Comparative Statics

Examine equilibrium response to changes in the productivity elasticity of distortions $\gamma$:

Higher $\gamma$ decreases $[\sigma(1-\gamma)-1]$, lowering effective returns to productivity

Entrant productivity $s_0$: $\downarrow$

Life-cycle growth $g$: $\downarrow$

Number of firms $N$: $\uparrow$ (smaller, less productive entrants $\Rightarrow$ more entry)

Average establishment size $1/N$: $\downarrow$

Investment share: non-monotone in general; $s_0$ and $g$ consistently decline

---

## Decomposition of Aggregate Output and Firm Size

Accounting for exogenous life-cycle productivity growth reduces the impact of correlated distortions relative to the static factor misallocation channel

Allowing for endogenous firm-level productivity growth can increase the impact of correlated distortions, but this is offset by compression of the productivity distribution and increases in the number of firms

Extending the model to allow for endogenous entrant productivity has the potential to greatly amplify the impact of correlated distortions

---

## Calibration — US Manufacturing Data

Effect through the investment channel depends on five key parameters:

$\theta$: elasticity of entrant investment w.r.t. initial productivity

$\phi$: elasticity of life-cycle investment w.r.t. productivity growth

$c_g$: level parameter in cost of life-cycle investment

$\gamma$: elasticity of distortions w.r.t. productivity

$\sigma$: elasticity of substitution between varieties

Effect through the factor misallocation channel: + cross-sectional distribution of productivity in the benchmark economy

Simple mapping between productivity $sz$ and employment:

$$
\frac{\ell_i}{\ell_j}
=
\left(
\frac{s_i z_i}{s_j z_j}
\right)^{\sigma(1-\gamma)-1}
$$

Back out distribution of $sz$ from US Census employment data given $(\sigma,\gamma_{US})$

---

## Model Results across Correlated Distortions $\gamma$

Table: Table 2 — Model Results across Correlated Distortions $\gamma$

| $\gamma$ | Establishment size $(1/N)$ | Entrant productivity | Life-cycle growth (%) | Investment share (%) | Relative output |
|---:|---:|---:|---:|---:|---:|
| 0.09 $(\gamma_{US})$ | 22 | 1 | 5.0 | 13.5 | 1 |
| 0.15 | 12 | 0.88 | 4.6 | 13.3 | 0.97 |
| 0.20 | 8.4 | 0.80 | 4.3 | 12.7 | 0.93 |
| 0.30 | 5.3 | 0.66 | 3.7 | 10.8 | 0.83 |
| 0.40 | 3.8 | 0.54 | 3.0 | 8.3 | 0.66 |
| 0.50 $(\gamma_{India})$ | 3.0 | 0.42 | 2.1 | 5.4 | 0.47 |
| 0.60 | 2.4 | 0.28 | 0.5 | 2.3 | 0.26 |

Notes: Columns 2 and 5 relative to benchmark US economy.

---

## Decomposition — $\gamma$ and Aggregate Output

Table: Table 3 — Decomposition: $\gamma$ and Aggregate Output

| $\gamma$ | Factor misallocation | + Exogenous life-cycle | + Endogenous life-cycle | + Entry productivity |
|---:|---:|---:|---:|---:|
| 0.09 $(\gamma_{US})$ | 1 | 1 | 1 | 1 |
| 0.15 | 0.98 | 1.10 | 0.99 | 0.97 |
| 0.20 | 0.94 | 1.13 | 0.97 | 0.93 |
| 0.30 | 0.86 | 1.13 | 0.93 | 0.83 |
| 0.40 | 0.74 | 1.02 | 0.82 | 0.66 |
| 0.50 $(\gamma_{India})$ | 0.63 | 0.91 | 0.70 | 0.47 |
| 0.60 | 0.52 | 0.77 | 0.54 | 0.26 |

---

## Decomposition — $\gamma$ and Average Establishment Size

$\gamma$ from 0.09 to 0.5 results in a substantial drop in average establishment size even with exogenous life-cycle productivity growth

Allowing for life-cycle investment amplifies this effect moderately

Extending the model to include investment at entry substantially increases the impact of $\gamma$ on average size

Combined effect: decrease in establishment size by a factor of seven

Table: Table 4 — Decomposition: $\gamma$ and Establishment Size

| $\gamma$ | Factor misallocation | + Exogenous life-cycle | + Endogenous life-cycle | + Entry productivity |
|---:|---:|---:|---:|---:|
| 0.09 $(\gamma_{US})$ | 22 | 22 | 22 | 22 |
| 0.15 | 22 | 17 | 14 | 12 |
| 0.20 | 22 | 15 | 12 | 8.4 |
| 0.30 | 22 | 13 | 9.4 | 5.3 |
| 0.40 | 22 | 11 | 8.2 | 3.8 |
| 0.50 $(\gamma_{India})$ | 22 | 11 | 7.5 | 3.0 |
| 0.60 | 22 | 9.9 | 7.1 | 2.4 |

---

## Correlated Distortions

How GDP per capita and average establishment size are related to the productivity elasticity of distortions $\gamma$ in 63 countries

### Imagen / gráficas

La diapositiva muestra dos scatter plots.

### Gráfico izquierdo

Título visible bajo la figura:

**Figure 5. GDP per Capita and Correlated Distortions**

El eje horizontal es **Productivity elasticity of distortions**, con valores aproximadamente entre 0 y 0.8. El eje vertical es **GDP per capita (log scale)**, con valores desde alrededor de 500 hasta 50,000.

Los puntos representan países. La curva punteada tiene pendiente negativa: países con menor $\gamma$ tienden a tener mayor PIB per cápita; países con mayor $\gamma$ tienden a tener menor PIB per cápita. Estados Unidos aparece hacia la izquierda con bajo $\gamma$ y alto PIB per cápita. Varios países de menor ingreso se ubican hacia valores más altos de $\gamma$.

**Interpretación contextual:** la figura sugiere que en países pobres las distorsiones están más correlacionadas con productividad. Es decir, las firmas más productivas enfrentan mayores cuñas, lo cual reduce el incentivo a expandirse e invertir.

### Gráfico derecho

Título visible bajo la figura:

**Figure 6. Establishment Size and Correlated Distortions**

El eje horizontal nuevamente es **Productivity elasticity of distortions**. El eje vertical es **Establishment size (log scale)**, con valores aproximadamente entre 1 y 50.

La curva punteada cae con $\gamma$: a menor elasticidad de distorsiones, el establecimiento promedio es mayor; a mayor $\gamma$, el establecimiento promedio es menor. Estados Unidos aparece con bajo $\gamma$ y tamaño alto. La mayoría de países se agrupa en valores de $\gamma$ entre aproximadamente 0.4 y 0.65, con tamaños de establecimiento más bajos.

**Interpretación contextual:** la figura conecta directamente el mecanismo del paper con el dato inicial: si las distorsiones castigan más a las firmas productivas, esas firmas crecen menos, invierten menos y el tamaño promedio de establecimiento cae.

---

## Mechanism: Disincentive to Invest in Productivity

The share of output invested in productivity should be lower in economies with high $\gamma$

### Imagen / gráficas

La diapositiva muestra dos scatter plots.

### Gráfico izquierdo

Título visible bajo la figura:

**Figure 7. Establishment Size and R&D Intensity**

El eje horizontal es **R&D intensity (percent, log scale)**. El eje vertical es **Establishment size (log scale)**.

La nube de puntos muestra una relación positiva: países con mayor intensidad de R&D tienden a tener establecimientos más grandes. Hay bastante dispersión, pero los países con baja intensidad de R&D suelen ubicarse con tamaños menores, mientras que los de mayor intensidad de R&D tienden a aparecer con establecimientos más grandes.

**Interpretación contextual:** esta figura apoya el canal de inversión en productividad: economías donde las firmas invierten más en productividad intangible tienden a tener establecimientos más grandes.

### Gráfico derecho

Título visible bajo la figura:

**Figure 8. R&D Intensity and Correlated Distortions**

El eje horizontal es **Productivity elasticity of distortions**. El eje vertical es **R&D intensity (percent, log scale)**.

La curva punteada es decreciente: a mayor $\gamma$, menor intensidad de R&D. Países con baja elasticidad de distorsiones muestran mayor inversión en R&D, mientras que economías con alta $\gamma$ concentran valores más bajos de R&D.

**Interpretación contextual:** el gráfico ilustra el mecanismo del modelo: cuando las firmas más productivas enfrentan distorsiones más altas, el retorno a invertir en productividad cae. Como resultado, la economía invierte menos en productividad, lo que reduce tanto el tamaño de los establecimientos como la productividad agregada.

---

## Conclusion

In a reasonably calibrated version of the model, cross-country variation in the degree of correlation between establishment distortions and productivity generates substantial differences in establishment size consistent with the data and aggregate productivity

Decompose the effects of correlated distortion through:

Entry

Entrant investment

Life-cycle investment

Factor misallocation

Accounting for life-cycle investment rationalizes the relationship between correlated distortions and lower life-cycle productivity investment, but does not amplify misallocation effects relative to a setting without life-cycle growth

Accounting for entrant investment substantially increases the estimated impact of correlated distortions