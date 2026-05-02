# Trabajos Prácticos

# Asignación Ineficiente de Recursos y Productividad Agregada

Hugo Hopenhayn

UTDT

Desarrollo Económico

2026

## Introducción

Este conjunto de ejercicios acompaña las clases sobre asignación de recursos y distorsiones en la productividad agregada. Los ejercicios están diseñados para reforzar la comprensión de los conceptos teóricos y sus aplicaciones cuantitativas.

## 1. Distorsiones No Correlacionadas

### Ejercicio 1: Dispersión de Empleo con Distribución Log-Normal

Supongamos que todas las empresas tienen la misma productividad \(z\), pero el empleo \(n\) sigue una distribución log-normal con media \(\bar{n}\) y varianza \(\sigma^2\) (en logs). La función de producción es \(y_i = zn_i^\alpha\).

Se pide:

a) Demostrar que el producto agregado \(y = E[zn^\alpha]\) puede expresarse como:

\[
\ln y = \ln(zM\bar{n}^{\alpha}) - \frac{\sigma^2}{2}\alpha(1-\alpha)
\]

b) Interpretar el resultado: ¿Por qué el producto cae con la varianza del empleo?

c) Calcular numéricamente la pérdida de producto cuando \(\alpha = 2/3\) y \(\sigma = 0,5\).

## 2. Distorsiones Correlacionadas

### Ejercicio 2: Asignación Igualitaria de Empleo

Considere una economía con \(M\) empresas heterogéneas donde la productividad \(z\) sigue una distribución \(F(z)\). La función de producción de cada empresa es \(y_i = z_i n_i^\alpha\) y el empleo total es \(N\).

En lugar de la asignación óptima, suponga que todas las empresas reciben el mismo empleo: \(n_i = N/M\) para todo \(i\).

1. Demostrar que

\[
\frac{y}{y^{eff}} < 1
\]

Considere ahora el caso específico donde \(F(z) = 1 - z^{-\zeta}\) (distribución Pareto con \(z \geq 1\) y \(\zeta > 1\)), y \(\alpha = 2/3\).

2. Demostrar que con \(\zeta = 2\) y \(\alpha = 2/3\):

\[
\frac{y}{y^{eff}} = \frac{1}{3}
\]

3. Interpretar el resultado: ¿Qué significa una pérdida del \(67\%\) del producto?

## 3. Aplicación Empírica: Cálculo de TFPR

### Ejercicio 3: Análisis de Datos de Misallocation

El archivo `firms_misallocation_10000.xlsx` contiene datos de empleo y producción para 10,000 empresas.

Suponga que la función de producción es \(y_i = z_i n_i^\alpha\) donde \(\alpha = 2/3\).

Se pide:

a) Calcular TFP y TFPR de cada firma

b) Distribución de TFP y TFPR:

- Graficar el histograma de \(\log(TFP_i)\) y el de \(\log(TFPR_i)\)
- Calcular la media y la varianza de \(\log(TFPR_i)\)

c) TFPR agregado: Calcular la PTF agregada en la economía distorsionada

d) PTF óptima: Calcular la PTF si la asignación de empleo fuera la óptima.

e) Pérdida de productividad: Calcular:

\[
\text{Ganancia potencial} = \frac{TFP^{opt} - TFP^{dist}}{TFP^{dist}} \times 100\%
\]

f) Análisis gráfico:

- Graficar \(\log(n_i)\) vs \(\log(z_i)\) para la asignación distorsionada
- Superponer la asignación óptima \(\log(n^*) = \log(a_0) + 3\log(z)\)
- Comentar las diferencias observadas

g) Relación entre dispersión y pérdidas:

- Calcular la correlación entre \(\log(TFPR_i)\) y \(\log(z_i)\)
- ¿Qué tipo de distorsión predomina en estos datos (correlacionada o no correlacionada)?

## Referencias

- Restuccia, D. y Rogerson, R. (2008). "Policy Distortions and Aggregate Productivity with Heterogeneous Establishments". *Review of Economic Dynamics*, 11(4), 707-720.

- Hsieh, C.-T. y Klenow, P. J. (2009). "Misallocation and Manufacturing TFP in China and India". *Quarterly Journal of Economics*, 124(4), 1403-1448.