# Distorsiones en el Tamaño de las Firmas y la Distribución de Productividad: Evidencia de Francia

Garricano, Lelarge y Van Reenen, AER 2016

Desarrollo Economico, 2026

---

## La Política y la Distorsión

En Francia, cuando las firmas emplean 50 o mas trabajadores:

- Deben crear un comité de empresa, establecer un comité de salud y seguridad, reportar información detallada al Ministerio de Trabajo, designar un representante sindical, etc.

### Imagen / gráfica

La diapositiva muestra un gráfico de barras titulado:

**Figure 2. Number of Firms by Employment Size in France**

El eje horizontal enumera tamaños de firma exactos entre aproximadamente 31 y 69 empleados. El eje vertical muestra el número de firmas, con escala hasta alrededor de 500.

La distribución tiene muchas firmas entre 31 y 49 empleados, con barras que oscilan aproximadamente entre 320 y 500 firmas. Al llegar al umbral regulatorio de 50 empleados se observa una caída muy marcada: las barras de 50 empleados en adelante bajan a alrededor de 90-160 firmas. Visualmente, el gráfico muestra una discontinuidad clara justo cuando empieza la regulación para firmas con 50 o más empleados.

Texto visible bajo la figura:

**Notes:** This is the population of French firms with between 31 and 69 employees in manufacturing. This plots the number of firms in each exact size category (i.e., raw data, no binning) for the year 2000. There is a clear drop when regulations begin for firms with 50 or more employees.

**Source:** FICUS

**Interpretación contextual:** la imagen ilustra el patrón empírico central del paper: muchas firmas parecen concentrarse justo por debajo del umbral de 50 trabajadores, y hay una caída abrupta en la masa de firmas a partir del punto en el que se activan obligaciones regulatorias. Esto sugiere que el umbral genera una distorsión en la elección de tamaño.

---

## Modelo

Modelo de Span of Control de Lucas

- La firma requiere un gerente y trabajadores

- Función de producción de la firma $zf(n)$ donde $z$ es la productividad del gerente (talento) con función de densidad $\phi(z)$.

- Consumidor representativo

- Política del mercado laboral:

  - costo laboral total $\tau w$ y costo fijo $F$ por cumplimiento regulatorio

  - Se aplica solo si $n > N$

---

## Equilibrio

- Decisión de empleo de un gerente de talento $z$:

$$
\pi(z) = \max_n
\begin{cases}
zf(n) - wn & \text{si } n \leq N \\
zf(n) - w\tau n - F & \text{si } n > N
\end{cases}
$$

- Dos umbrales en equilibrio $z_{min} \leq z_c \leq z_r$

  - por debajo de $z_{min}$ es trabajador; por debajo de $z_c$ elige $m < N$; hasta $z_r$, $n = N$; por encima de $z_r$ elige $n > N$.

- Equilibrio $\{w, z_{min}, n(z)\}$ tal que:

  - $n(z)$ maximiza beneficios

  - $\pi(z_{min}) = w$

  - $\int_{z_{min}} n(z)\phi(z)\,dz = \Phi(z_{min})$

---

## Selección

- Dos distorsiones: 1) elección de $n$; 2) umbral de empresarialidad $z_{min}$

### Suposición

*(el talento es escaso)* $z\phi(z)$ es decreciente en $z$

### Proposición

*La introducción del impuesto $\tau$ (i) reduce $w$; (ii) reduce $z_{min}$ (más empresarios); (iii) aumenta el tamaño de las firmas por debajo de $z_c$; y (iv) reduce el tamaño de las firmas gravadas.*

- El supuesto es necesario para la parte (iv)

### Ejercicio

Resolver el caso Pareto con $z_0 = 1$ y donde $f(n) = n^{2/3}$ donde $\tau$ representa un $20\%$ del salario de equilibrio sin distorsiones.

- Un resultado similar se obtiene para aumentos en $F$, excepto que todos los tamaños de firma aumentan, salvo aquellos para los cuales $N$ es vinculante.

---

## Modelo Empírico

- Función de producción $f(n) = n^\theta$

- Distribución del talento $\phi(z) = cz^{-\beta}$ (Pareto)

- Caso base (sin impuestos): Pareto con parámetro $\beta(1-\theta)$

### Imagen / gráfica

La diapositiva incluye una figura teórica de distribución de tamaños de firmas. El eje horizontal es **Employment (log scale)**, con marcas visibles en aproximadamente $1$, $20$, $50$, $80$ y $300$. El eje vertical es **Share of firms (log scale)**, con valores alrededor de $0.01$ y $0.0001$.

La figura muestra tres curvas:

- Una línea gruesa sólida, etiquetada como $n^*(\sigma = 0)$.
- Una línea discontinua, etiquetada como $\tilde{n}, \sigma = 0.15$.
- Una línea sólida delgada, etiquetada como $\tilde{n}, \sigma = 0.5$.

Hay líneas verticales alrededor de los umbrales $50$ y $80$. La curva base decrece como una ley de potencia, pero con la restricción regulatoria aparece acumulación de firmas alrededor del umbral y un valle/discontinuidad posterior. La presencia de error de medición suaviza visualmente la discontinuidad.

Texto visible bajo la figura:

**Figure 5. Theoretical Firm Size Distribution when Employment Is Measured with Error**

**Notes:** The thickest solid (blue) line shows the theoretical firm size distribution (broken power law), $n^*$. The dashed line shows the new firm size distribution when we extend the model, to allow employment size to be measured with error with $\sigma = 0.15$. The solid dark line increases the measurement error to $\sigma = 0.5$. Parameters: $\beta_a = 1.6$, $\theta = 0.5$, $\beta = 1.3$, but $\tau = 1.02$ and $F/w = 2.9$ such that $n_r = 80$.

**Interpretación contextual:** la figura muestra cómo el modelo genera una distribución de tamaños con una ruptura alrededor del umbral regulatorio. Sin error de medición, la distorsión se ve más nítida; con error de medición, el patrón se suaviza, pero la acumulación antes del umbral y la caída después todavía son visibles.

---

## Ajuste del Modelo a los Datos

Distribución de tamaños empírica vs. teórica

### Imagen / gráfica

La diapositiva compara dos figuras.

A la izquierda aparece el gráfico empírico de barras de Francia, con tamaños de firma entre 31 y 69 empleados. Muestra una fuerte concentración de firmas por debajo de 50 empleados y una caída marcada a partir del umbral regulatorio.

A la derecha aparece una figura teórica titulada:

**Panel A. Theoretical firm size distribution with regulatory constraint**

El eje vertical mide **Share of firms** y el eje horizontal muestra tamaños de empleo entre aproximadamente 5 y 80. La distribución teórica concentra mucha masa en tamaños pequeños, cae rápidamente, presenta un pico/acumulación justo antes del umbral regulatorio cercano a 50, luego un valle o caída posterior, y después una pequeña masa para tamaños más grandes.

**Interpretación contextual:** la comparación visual muestra que el modelo reproduce dos rasgos clave de los datos: la acumulación de firmas antes del umbral y la caída después del umbral. La parte empírica muestra el fenómeno en datos franceses; la parte teórica muestra que el mecanismo de costos regulatorios por tamaño puede generar un patrón similar.

---

## Error de Medición

- Se supone que el empleo observado satisface $\ln \tilde{n}(z) = \ln n(z) + \varepsilon$, donde $\varepsilon \sim N(0,\sigma)$

### Imagen / gráfica

La diapositiva repite la figura teórica de distribución de tamaños con error de medición.

El eje horizontal es **Employment (log scale)**, con marcas visibles cerca de $1$, $20$, $50$, $80$ y $300$. El eje vertical es **Share of firms (log scale)**.

La ley de potencia base cae suavemente, pero el modelo con restricción regulatoria genera una discontinuidad alrededor del umbral. Las curvas con error de medición suavizan la discontinuidad y transforman una masa puntual/acumulación en una zona más difusa.

Texto visible bajo la figura:

**Figure 5. Theoretical Firm Size Distribution when Employment Is Measured with Error**

**Notes:** The thickest solid (blue) line shows the theoretical firm size distribution (broken power law), $n^*$. The dashed line shows the new firm size distribution when we extend the model, to allow employment size to be measured with error with $\sigma = 0.15$. The solid dark line increases the measurement error to $\sigma = 0.5$. Parameters: $\beta_a = 1.6$, $\theta = 0.5$, $\beta = 1.3$, but $\tau = 1.02$ and $F/w = 2.9$ such that $n_r = 80$.

**Interpretación contextual:** el error de medición ayuda a conectar el modelo teórico con datos reales, porque en los datos observados el empleo puede no medirse exactamente. En vez de una ruptura perfecta, la distribución observada puede mostrar una acumulación y caída más suavizadas.

---

## Identificación

- Parámetros a estimar: $(\sigma, c, \beta, \theta, \tau, F)$

- Los parámetros del impuesto regulatorio se recuperan a partir de tres características de la distribución:

  - El desplazamiento hacia abajo de la densidad a partir de los 49 empleados.

  - La acumulación de firmas justo antes del umbral regulatorio de 50 empleados.

  - El ancho del valle en la distribución entre 49 empleados y el punto $n_r$ donde la densidad se recupera.

- Un impuesto variable $\tau$ sin costo fijo produce un desplazamiento paralelo de la densidad.

- Si solo existiera un costo fijo $F$, se observaría únicamente acumulación y valle, pero no desplazamiento de la densidad después de $n_r$.

- El error de medición $\sigma$ se identifica a partir de las desviaciones aleatorias de la distribución respecto a la densidad implicada.

- $\beta$ y $\theta$ no son identificables por separado. Se calibra $\theta = 0,8$

---

## Evidencia Descriptiva: Distribución de Tamaños

### Imagen / gráfica

La diapositiva muestra seis paneles organizados en tres filas y dos columnas.

Encima de la columna izquierda dice **Bar plot** y encima de la columna derecha dice **log-log plot**.

### Panel A

**Panel A. FICUS: Arithmetic average of quarterly head-counts**

- Izquierda: gráfico de barras del número de firmas por tamaño. Muestra muchas firmas por debajo de 50 empleados y una caída clara después del umbral.
- Derecha: gráfico log-log de **Share of firms (log scale)** contra **Employment (log scale)**. La nube cae aproximadamente de manera lineal en escala log-log, pero hay una ruptura visible alrededor de 50 empleados.

### Panel B

**Panel B. DADS: Cross-sectional head-count of all workers on Dec. 31**

- Izquierda: gráfico de barras con patrón decreciente; también muestra una caída alrededor del umbral de 50.
- Derecha: gráfico log-log con una línea vertical en 50. La distribución cae de forma aproximadamente lineal, pero con discontinuidad o cambio de densidad en el umbral.

### Panel C

**Panel C. DADS 2002: Full-time equivalent (FTE) workers as computed by the French statistical institute**

- Izquierda: gráfico de barras usando trabajadores equivalentes a tiempo completo. La distribución cae gradualmente, pero mantiene el patrón de menor densidad después del umbral.
- Derecha: gráfico log-log con el mismo patrón de caída y ruptura alrededor de 50.

Texto visible bajo la figura:

**Figure 6. The Effect on the Measured Firm Size Distribution Using Alternative Datasets (FICUS and DADS) and Definitions of Employment**

**Interpretación contextual:** la diapositiva muestra que el patrón no depende de una única definición de empleo. Con distintas bases y mediciones —head-count trimestral, head-count al 31 de diciembre y trabajadores equivalentes a tiempo completo— sigue apareciendo una discontinuidad alrededor del umbral regulatorio de 50 trabajadores.

---

## Productividad Total de los Factores (PTF)

### Imagen / gráfica

La diapositiva muestra una gráfica titulada por el caption:

**Figure 7. TFP Distribution Around the Regulatory Threshold of 50 Employees**

El eje horizontal es **Size**, con valores visibles alrededor de 20, 50, 100 y 200. El eje vertical es **Average TFP, LP estimates**, con valores aproximadamente entre 35 y 80.

Hay una línea vertical en el umbral de 50 empleados. La serie de PTF promedio crece con el tamaño de la firma. Cerca del umbral de 50 se observan puntos/líneas más oscuros y una zona con comportamiento irregular. Para tamaños mayores, la PTF promedio sigue aumentando, con mayor dispersión y picos especialmente cerca de tamaños grandes, alrededor de 150-200.

Texto visible bajo la figura:

**Notes:** This figures plots the mean level of TFP by firm employment size using the Levinsohn-Petrin (LP) method (see online Appendix B). TFP estimated using an unbalanced panel between 1995 and 2007 of firms having 10 to 1,000 workers. A fourth-order polynomial is displayed using only data from the undistorted points (potentially distorted points are shown in black). Manufacturing firms only.

**Interpretación contextual:** la figura conecta la distorsión de tamaño con productividad. El hecho de que la PTF promedio aumente con el tamaño sugiere que las firmas más grandes tienden a ser más productivas. La zona alrededor de 50 empleados es especialmente relevante porque ahí la regulación puede alterar la distribución observada de tamaños y, por tanto, la asignación de trabajadores entre firmas.

---

## Resultados

**Table 1—Parameter Estimates (Calibrating Returns to Scale $\theta$)**

| Method: | $\theta$ calibrated: Basu and Fernald (1997) (1) | $\theta$ calibrated: Atkeson and Kehoe (2005) (2) | $\theta$ calibrated: Hsieh and Klenow (2009) (3) | $\theta$ calibrated at 0.9 (4) | TFP/size relationship (5) | Using production function estimates (6) |
|---|---:|---:|---:|---:|---:|---:|
| $\theta$, scale parameter | 0.80 | 0.85 | 0.50 | 0.90 | 0.793<br>(0.024) | 0.860<br>(0.012) |
| $\beta$, power law | 1.800<br>(0.054) | 1.800<br>(0.054) | 1.800<br>(0.054) | 1.813<br>(0.051) | 1.800<br>(0.058) | 1.801<br>(0.057) |
| $n_r$, upper emp. threshold | 59.271<br>(2.051) | 59.265<br>(2.026) | 59.271<br>(2.052) | 52.985<br>(0.317) | 59.271<br>(2.262) | 59.200<br>(1.715) |
| $\sigma$, measurement error | 0.121<br>(0.033) | 0.121<br>(0.032) | 0.121<br>(0.033) | 0.041<br>(0.003) | 0.121<br>(0.041) | 0.120<br>(0.027) |
| $\tau - 1$, implicit tax, variable cost | 0.023<br>(0.008) | 0.017<br>(0.006) | 0.059<br>(0.021) | 0.007<br>(0.001) | 0.024<br>(0.008) | 0.016<br>(0.005) |
| $F/w$, implicit tax, fixed cost | -0.941<br>(0.338) | -0.704<br>(0.252) | -2.375<br>(0.865) | -0.321<br>(0.057) | -0.974<br>(0.345) | -0.655<br>(0.201) |
| Mean (median) # of employees | 55.8 (24) | 55.8 (24) | 55.8 (24) | 55.8 (24) | 55.8 (24) | 55.8 (24) |
| Firms | 41,067 | 41,067 | 41,067 | 41,067 | 41,067 | 41,067 |
| ln likelihood | -184,128.7 | -184,128.7 | -184,128.7 | -184,196 |  |  |

**Notes:** Parameters estimated by ML with standard errors below in parentheses (clustered at the four-digit level). Estimation is on population of French manufacturing firms with 10 to 1,000 employees, in the year 2000. These estimates of the implicit tax are based on different estimates of $\theta$; the methods are indicated in the different columns. In columns 5 and 6, standard deviations are computed using bootstrap (100 replications). In column 5, the underlying TFP estimates are 0.109 (0.006) for capital and 0.751 (0.014) for labor.

---

## Ajuste del Modelo

### Imagen / gráfica

La diapositiva muestra dos paneles.

### Panel A. Estimated costs of regulation

El eje horizontal es **Employment (log scale)**, con líneas verticales marcando aproximadamente 50 y 59 empleados. El eje vertical es **Tax amount paid (as a share of wages, %)**.

Hay dos curvas:

- Una línea sólida: **Estimated specification with fixed and variable costs (fixed cost = -94%)**.
- Una línea discontinua: **Larger $\bar{n}$ (fixed cost = 0%)**.

La línea sólida está cerca de cero antes de 50 empleados. En el umbral salta a un nivel cercano a 20% y luego aumenta gradualmente con el tamaño. La línea discontinua representa una especificación alternativa sin costo fijo, con una carga más alta después del umbral.

### Panel B. Data and fit of model

El eje horizontal es **Employment (log scale)** y el eje vertical es **Share of firms (log scale)**. Hay líneas verticales en 49 y 59 empleados. Se observa una nube de puntos en forma de cruces, que representa los datos observados. La distribución cae casi linealmente en escala log-log, pero cerca del umbral de 50 aparece una acumulación y una caída posterior. El modelo ajustado reproduce esa ruptura.

La leyenda distingue:

- $n^*$
- $n$
- $\hat{n}$, actual

Texto visible bajo la figura:

**Figure 8. Implications of Model Estimates for Cost of Regulation and Firm Size Distribution**

**Notes:** Panel A plots the estimated tax schedule as a function of firm size. For the solid blue line, the estimates correspond to the baseline specification reported in column 1 of Table 1. The dashed red line corresponds to setting the (estimated negative) fixed costs to zero. Panel B shows the difference between the fit of the model (dashed red line, $n$) which allows for measurement error with the actual data. Estimates correspond to the baseline specification reported in column 1 of Table 1. We also include the pure theoretical predictions (in dark blue solid line, $n^*$). Actual data ($\hat{n}$) are in crosses.

**Interpretación contextual:** el panel A traduce el umbral regulatorio en una carga impositiva implícita sobre firmas de cierto tamaño. El panel B muestra que el modelo estimado puede replicar la forma empírica de la distribución: acumulación antes del umbral, caída después, y recuperación posterior de la densidad.

---

## Implicaciones Agregadas

Pérdidas de producto:

- Caso base: 0.02 % !

- Con salarios rígidos a la baja: entre 2 y 3 %

Carga fiscal: 1.3 %

Pérdidas totales (si los impuestos son absorbidos por costos de cumplimiento): entre 1.32 % y 4 %

Resultados similares utilizando el modelo de dinámica de firmas de Roys y Gourio.

---

## Empleo informal

Hopenhayn y Neumeyer, cálculo de orden de magnitud sobre cumplimiento

Impuesto laboral del 30 %

Incumplimiento por parte de un subconjunto de empresas que representa el 50 % del empleo

- Nivel de impuestos y cumplimiento del orden de magnitud correcto en América Latina y el Caribe

Gran desplazamiento del empleo hacia empresas más pequeñas, pero caída moderada de la PTF de 2.4 %

Políticas con efectos muy notorios pero impacto no tan grande sobre la PTF