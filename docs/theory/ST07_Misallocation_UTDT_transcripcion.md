# ST07 - Misallocation_UTDT

# Asignación Ineficiente de Recursos

Distorsiones y Productividad Agregada

Hugo Hopenhayn

Desarrollo Económico — UTDT

2026

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 1 / 39

---

# Roadmap

Economía Base  
Asignación óptima

Distorsiones  
Tipos y efectos

Impacto en PTF  
Cuantificación

Pregunta central: ¿Por qué la productividad agregada varía tanto entre países?

▷ Las distorsiones impiden que los recursos fluyan a sus usos más productivos  
▷ Que efectos puede tener esto sobre la productividad total de los factores?

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 2 / 39

---

# Economía Base: Asignación Eficiente

Configuración:

▷ \(M\) empresas heterogéneas, productividad
\[
z_i \sim F(z)
\]

▷ Producción: \(y_i = z_i n_i^\alpha\), empleo total fijo \(N\)

Asignación óptima:
\[
\max \sum_i z_i n_i^\alpha \quad \text{s.a.} \quad \sum_i n_i = N
\]

CPO:
\[
\alpha z_i n_i^{\alpha-1} = \lambda \quad \forall i
\quad \Rightarrow \quad
n_i^*(z) \propto z^{\frac{1}{1-\alpha}}
\]

Tres propiedades clave:

1. Monotonicidad: \(z_i > z_j \Rightarrow n_i^* > n_j^*\)
2. Equidad horizontal: \(z_i = z_j \Rightarrow n_i^* = n_j^*\)
3. Eficiencia: \(PMgL\) igualado entre todas las empresas

Producto agregado eficiente

\[
y^{eff} =
\left( \int z^{\frac{1}{1-\alpha}} dF \right)^{1-\alpha}
M^{1-\alpha}N^\alpha
\]

Cualquier desviación de esta asignación reduce el producto agregado, incluso si redirige recursos hacia empresas más productivas.

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 3 / 39

---

# Roadmap

Economía Base | Distorsiones | Impacto en PTF  
Asignación óptima | Tipos y efectos | Cuantificación

Pregunta Central: ¿Por qué la productividad agregada varía tanto entre países?

▷ La mala asignación de recursos explica gran parte de las diferencias de PTF  
▷ Las distorsiones impiden que los recursos fluyan a sus usos más productivos  
▷ Entender estos mecanismos es crucial para políticas de desarrollo

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 4 / 39

---

# Tipos de Distorsiones

▷ No correlacionadas: independientes de \(z\)  
▷ Correlacionadas

**Descripción de imagen importante:** la diapositiva muestra un gráfico esquemático con eje horizontal \(\ln z\) y eje vertical \(\ln n\). Hay una línea recta sólida creciente que representa la asignación eficiente/óptima de empleo como función de productividad. También aparece una nube de puntos y una línea punteada más plana, ilustrando que las distorsiones hacen que el empleo observado se aparte de la relación eficiente entre productividad y tamaño.

Ambos tipos destruyen valor: \(PMgL_i \neq PMgL_j \Rightarrow\) Ineficiencia

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 5 / 39

---

# Ejemplo 1: Distorsión No Correlacionada

Configuración:

▷ Todas las empresas tienen \(z\) idéntico  
▷ Empleo distorsionado: \(n_i \sim F(n)\)  
▷ Media preservada: \(\bar n = N/M\)

Comparación:

\[
y^{eff} = zM\bar n^\alpha
\]

\[
y^{dist} = zM \int n^\alpha dF(n)
\]

Por Jensen: \(y^{dist} < y^{eff}\)

**Descripción de imagen importante:** gráfico de la función concava \(n^\alpha\) contra empleo \(n\). El eje horizontal dice “Empleo \((n)\)” y el vertical “Producción \((n^\alpha)\)”. Se ilustran dos puntos/escenarios: “Disperso” y “Óptimo”. La idea visual es Jensen: con la misma media de empleo, dispersar empleo entre firmas idénticas reduce el producto agregado cuando \(0<\alpha<1\).

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 6 / 39

---

# Distorsiones y Productividad

Ejercicio

Supongamos que \(n\) sigue una distribución log-normal con media \(\bar n\). Mostrar que:

\[
\ln y = \ln(zM\bar n^\alpha) - \frac{\sigma^2}{2}\alpha(1-\alpha)
\]

Como \(0 < \alpha < 1\) el producto cae con la varianza del empleo

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 7 / 39

---

# Distorsión correlacionada

Configuración: Volviendo al caso original \(z \sim F(z)\)

¿Qué pasa si asignamos a las empresas el mismo empleo \(n = N/M\)?

\[
y = M\left( \int z \left( \frac{N}{M} \right)^\alpha dF(z) \right)
=
\left( \int z dF \right) M^{1-\alpha}N^\alpha
\]

Comparando con el eficiente:

\[
\frac{y}{y^{eff}} =
\frac{\int z dF}
{\left(\int z^{\frac{1}{1-\alpha}} dF\right)^{1-\alpha}}
\]

Ejercicio

1. Demostrar que \(\frac{y}{y^{eff}} < 1\).
2. Considere el caso en que \(F(z) = 1 - z^{-\zeta}\) y \(\alpha = 2/3\). Demuestre que \(y/y^{eff} = 1/3\)

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 8 / 39

---

# Parte I

Restuccia y Rogerson (2008)

Policy Distortions and Aggregate Productivity with Heterogeneous Establishments

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 9 / 39

---

# Consumidores

Hogar representativo:

\[
\sum_{t=0}^{\infty}\beta^t u(C_t), \quad 0<\beta<1
\]

▷ Dotaciones: una unidad de tiempo productivo cada período, \(K_0>0\) unidades del stock de capital, y share de todos los establecimientos

▷ Restricción presupuestaria:

\[
\sum_{t=0}^{\infty} p_t\left(C_t + K_{t+1} - (1-\delta)K_t\right)
=
\sum_{t=0}^{\infty} p_t\left(r_tK_t + w_tN_t + \pi_t - T_t\right)
\]

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 10 / 39

---

# Distorsiones de Política

▷ Foco en políticas que crean distorsiones idiosincrásicas sobre las decisiones a nivel de establecimiento

▷ Cada establecimiento enfrenta su propio impuesto/subsidio al producto \(\tau \in (-1,1)\)

▷ Los establecimientos entrantes obtienen realizaciones de \(s\) y \(\tau\) (se asume número finito de posibles \(s\) y \(\tau\))

▷ Dada la función de distribución acumulada \(H(s)\), las distorsiones de política inducen una distribución conjunta acumulada \(G(s,\tau)\) (densidad \(g\))

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 11 / 39

---

# Problema del Establecimiento Incumbente

Función de beneficio por período:

\[
\pi(s,\tau) = \max_{n,k}\left\{(1-\tau)sk^\alpha n^\gamma - wn - rk - c_f\right\}
\]

▷ \(\bar k(s,\tau)\), \(\bar n(s,\tau)\): decisiones óptimas

▷ Con \((s,\tau)\) constantes, el valor presente del establecimiento incumbente:

\[
W(s,\tau)=\frac{\pi(s,\tau)}{1-\rho},
\quad
\rho=\frac{1-\lambda}{1+R}
\]

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 12 / 39

---

# Problema del Establecimiento Entrante

Valor esperado de un potencial entrante:

\[
W_e = \sum_{(s,\tau)} \max[W(s,\tau),0]g(s,\tau)-c_e
\]

▷ \(\bar x(s,\tau) \in \{0,1\}\): decisión óptima de operación

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 13 / 39

---

# Distribución Invariante de Establecimientos

▷ Sea \(\mu(s,\tau)\) la distribución de establecimientos productores en el período actual y \(E\) la masa de entrantes

▷ Distribución del período siguiente:

\[
\mu'(s,\tau)=(1-\lambda)\mu(s,\tau)+\bar x(s,\tau)g(s,\tau)E
\]

▷ Distribución invariante:

\[
\mu'(s,\tau)=\mu(s,\tau)=\frac{E\bar x(s,\tau)}{\lambda}g(s,\tau)
\]

▷ Sea \(\hat \mu\) la distribución invariante asociada a \(E=1\):

\[
\hat \mu(s,\tau)=\frac{\bar x(s,\tau)}{\lambda}g(s,\tau)
\]

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 14 / 39

---

# Equilibrio del Mercado Laboral

Demanda agregada de trabajo:

\[
N(r,w)=E\sum_{(s,\tau)}\bar n(s,\tau)\hat\mu(s,\tau)
\]

▷ La oferta laboral es inelástica e igual a uno; la masa de entrantes \(E\) satisface:

\[
E = \frac{1}{\sum_{(s,\tau)}\bar n(s,\tau)\hat\mu(s,\tau)}
\]

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 15 / 39

---

# Definición de Equilibrio

Un equilibrio estacionario esta dado por:

\[
w, r, T, \mu(s,\tau), E, W(s,\tau), \pi(s,\tau), W_e, \bar x(s,\tau),
\bar k(s,\tau), \bar n(s,\tau), C \text{ y } K
\]

tales que:

▷ Optimización del consumidor: \(r = 1/\beta - (1-\delta)\)  
▷ Optimización de los establecimientos  
▷ Libre entrada: \(W_e=0\)  
▷ Equilibrio de mercados: trabajo, capital, producto  
▷ Equilibrio presupuestario del gobierno:

\[
T+\sum_{s,\tau}\tau f(s,\bar k,\bar n)\mu(s,\tau)=0
\]

▷ Distribución invariante:

\[
\mu(s,\tau)=E\frac{\bar x(s,\tau)}{\lambda}g(s,\tau)
\]

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 16 / 39

---

# Calibración

Calibración de la economía de referencia sin distorsiones con datos de EE. UU. Período del modelo: un año.

| Parámetro | Valor | Objetivo |
|---|---:|---|
| \(\alpha\) | 0.283 | Participación del capital en el ingreso |
| \(\gamma\) | 0.567 | Participación del trabajo en el ingreso |
| \(\beta\) | 0.96 | Tasa de retorno real |
| \(\delta\) | 0.08 | Razón inversión a producto |
| \(c_e\) | 1.0 | Normalización |
| \(c_f\) | 0.0 | Caso de referencia |
| \(\lambda\) | 0.1 | Tasa de salida anual |

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 17 / 39

---

# Calibración (cont.)

▷ Elementos clave: rango de \(s\) y \(H(s)\)

▷ Uso del mapeo de \(s\) a \(n\) y de \(H(s)\) a \(\mu(s)\) implícito en el modelo:

\[
\frac{\bar n_i}{\bar n_j}
=
\left(\frac{s_i}{s_j}\right)^{\frac{1}{1-\gamma-\alpha}},
\quad
\mu(s)=\frac{\bar x(s)}{\lambda}h(s)
\]

▷ El número de trabajadores por establecimiento en los datos de EE. UU. implica \(s \in [1,3.98]\)

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 18 / 39

---

# Establecimientos por Tamaño de Empleo

**Descripción de imagen importante:** gráfico de la distribución acumulada de establecimientos por número de empleados. El eje horizontal es “Number of Employees (log scale)” con marcas aproximadas en 1, 10, 100, 1,000 y 10,000; el eje vertical es “Cumulative Distribution of Establishments” de 0 a 1. La línea azul del modelo y los círculos verdes de datos están muy cerca, especialmente desde alrededor de 10 empleados hacia arriba, mostrando que la calibración replica bien la distribución de tamaños de establecimientos.

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 19 / 39

---

# Estadísticas de la Distribución: Economía de Referencia

Tamaño del establecimiento (N.o de empleados)

|  | < 5 | 5 a 49 | ≥ 50 |
|---|---:|---:|---:|
| Participación en establecimientos | 0.56 | 0.39 | 0.05 |
| Participación en el producto | 0.08 | 0.34 | 0.58 |
| Participación en el trabajo | 0.08 | 0.34 | 0.58 |
| Participación en el capital | 0.08 | 0.34 | 0.58 |
| Empleo promedio | 2.4 | 15.5 | 183.0 |

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 20 / 39

---

# Distorsiones Idiosincráticas: Políticas de Impuesto/Subsidio

▷ Se asume que una fracción de establecimientos paga impuestos y el resto recibe subsidios

▷ Combinaciones de impuesto/subsidio al producto:

• Niveles de impuesto: 0.1, 0.2, 0.3, 0.4, con subsidios de modo que el efecto neto sobre la acumulación de capital en estado estacionario sea cero  
• Redistribución a los consumidores para equilibrar el presupuesto del gobierno

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 21 / 39

---

# Distorsiones Idiosincráticas No Correlacionadas

| Variable | \(\tau_t = 0.1\) | \(\tau_t = 0.2\) | \(\tau_t = 0.3\) | \(\tau_t = 0.4\) |
|---|---:|---:|---:|---:|
| \(Y\) relativo | 0.98 | 0.96 | 0.93 | 0.92 |
| PTF relativa | 0.98 | 0.96 | 0.93 | 0.92 |
| \(E\) relativo | 1.00 | 1.00 | 1.00 | 1.00 |
| \(Y_s/Y\) | 0.72 | 0.85 | 0.93 | 0.97 |
| \(S/Y\) | 0.05 | 0.08 | 0.09 | 0.10 |
| \(\tau_s\) | 0.06 | 0.09 | 0.10 | 0.11 |

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 22 / 39

---

# Distorsiones Idiosincráticas Correlacionadas

| Variable | \(\tau_t = 0.1\) | \(\tau_t = 0.2\) | \(\tau_t = 0.3\) | \(\tau_t = 0.4\) |
|---|---:|---:|---:|---:|
| \(Y\) relativo | 0.90 | 0.80 | 0.73 | 0.69 |
| PTF relativa | 0.90 | 0.80 | 0.73 | 0.69 |
| \(E\) relativo | 1.00 | 1.00 | 1.00 | 1.00 |
| \(Y_s/Y\) | 0.42 | 0.67 | 0.83 | 0.92 |
| \(S/Y\) | 0.17 | 0.32 | 0.43 | 0.49 |
| \(\tau_s\) | 0.40 | 0.48 | 0.52 | 0.53 |

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 23 / 39

---

# Distorsiones Correlacionadas: Fracción Gravada

| Gravados (%) | \(\tau_t = 0.1\) | \(\tau_t = 0.2\) | \(\tau_t = 0.3\) | \(\tau_t = 0.4\) |
|---:|---:|---:|---:|---:|
| 90 | 0.81 | 0.66 | 0.56 | 0.51 |
| 80 | 0.84 | 0.70 | 0.62 | 0.57 |
| 60 | 0.88 | 0.77 | 0.69 | 0.65 |
| 50 | 0.90 | 0.80 | 0.73 | 0.69 |
| 40 | 0.92 | 0.82 | 0.76 | 0.72 |
| 20 | 0.95 | 0.89 | 0.84 | 0.81 |
| 10 | 0.97 | 0.92 | 0.88 | 0.86 |

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 24 / 39

---

# El Costo de la Mala Asignación

▷ Foco en mala asignación: sin selección (costo fijo = 0), igual distribucion de tecnologias \(H(s)\) (Restuccia y Rogerson, 2008)

▷ Considerar distorsiones de política idiosincráticas en la forma de impuestos/subsidios efectivos al producto \(\tau_i\):

\[
(1-\tau_i)=\frac{1}{A_i^\theta}\varepsilon_i
\]

donde \(\theta\) controla la elasticidad de las distorsiones respecto a la productividad (distorsiones correlacionadas) y \(\varepsilon_i\) refleja distorsiones aleatorias idiosincráticas (distorsiones no correlacionadas)

▷ Se supone que \(\varepsilon_i\) sigue una distribución log-normal con media cero y desviación estándar \(\sigma_\varepsilon\)

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 25 / 39

---

# El Costo de la Mala Asignación (cont.)

▷ Se calibra la economía de referencia sin distorsiones (\(\theta=0\), \(\sigma_\varepsilon=0\)) con datos de EE. UU.: los momentos clave son los de la distribución de productividad \(A_i\) (para replicar la distribución de establecimientos por tamaño de empleo o los momentos directos de la distribución de PTF a nivel de establecimiento)

▷ Para cada economía \((\theta, \sigma_\varepsilon)\) se reporta la razón de PTF agregada en la asignación eficiente (economía de referencia) respecto a la economía distorsionada:

| \(\sigma_\varepsilon \backslash \theta\) | 0 | 0.5 | 0.9 |
|---:|---:|---:|---:|
| 0 | 1.00 | 1.10 | 2.02 |
| 0.1 | 1.03 | 1.12 | 2.07 |
| 0.4 | 1.23 | 1.43 | 2.72 |

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 26 / 39

---

# Asignación Distorsionada (\(\theta = 0.9\), \(\sigma_\varepsilon = 0.4\))

[Gráfico: Empleo del establecimiento \(h_i\) (en logs) vs. PTF del establecimiento \(A_i\) (en logs). Los puntos azules muestran la asignación distorsionada; la línea roja muestra la asignación eficiente.]

**Descripción de imagen importante:** gráfico de dispersión con eje horizontal “Establishment TFP \(A_i\) (in logs)” y eje vertical “Establishment employment \(h_i\) (in logs)”. Una línea roja ascendente representa la asignación eficiente: más productividad debería implicar más empleo. La nube azul de puntos distorsionados está muy dispersa alrededor de esa relación y muestra mucha variación horizontal y vertical; visualmente, firmas con productividad similar tienen tamaños muy distintos y firmas poco productivas pueden recibir demasiado empleo.

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 27 / 39

---

# Mala Asignación de Tierra en Malaui

[Gráfico: Tamaño de tierra (acres por hora, en logs) vs. productividad de la explotación (en logs). Los puntos muestran los datos; la línea discontinua roja representa la asignación eficiente.]

**Descripción de imagen importante:** gráfico de dispersión de asignación de tierra agrícola en Malaui. El eje horizontal es productividad de la explotación/finca en logs; el eje vertical es tamaño de tierra en acres por hora en logs. La nube de puntos de datos es relativamente plana, mientras que la línea roja discontinua eficiente es fuertemente creciente. La visualización sugiere que la tierra no está suficientemente reasignada hacia explotaciones más productivas.

Chen, Restuccia y Santaeulàlia-Llopis (2022): La reasignación eficiente aumenta la productividad agrícola aproximadamente **2 veces**.

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 28 / 39

---

# Parte II

Hsieh y Klenow (2009)

Misallocation and Manufacturing TFP in China and India

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 29 / 39

---

# HK: Estructura del Modelo

Bien final de industria \(s\): agregador CES

\[
Y_s = \left(\sum_{i=1}^{M_s}Y_{si}^{\frac{\sigma-1}{\sigma}}\right)^{\frac{\sigma}{\sigma-1}}
\]

\(\sigma>1\): elasticidad de sustitución entre variedades.

Demanda de la variedad \(i\):

\[
P_{si}=\left(\frac{Y_s}{Y_{si}}\right)^{1/\sigma}P_s
\]

Curva de demanda con pendiente negativa \(\Rightarrow\) poder de mercado.

Producción: rendimientos constantes a escala

\[
Y_{si}=A_{si}K_{si}^{\alpha}L_{si}^{1-\alpha}
\]

▷ \(A_{si}\): productividad física (TFPQ)  
▷ \(\alpha\): participación del capital  
▷ No hay DRS en la tecnología

El tamaño limitado de cada empresa surge del poder de mercado decreciente (demanda CES), no de la tecnología.

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 30 / 39

---

# HK: Problema del Establecimiento con Distorsiones

Establecimiento \(i\) bajo competencia monopolística con dos distorsiones

\[
\max_{K_{si},L_{si}}\left\{(1-\tau^Y_{si})P_{si}Y_{si}-(1+\tau^K_{si})rK_{si}-wL_{si}\right\}
\]

**distorsion de producto \(\tau^Y_{si}\)**

Reduce los ingresos efectivos.

\(\tau^Y>0\): empresa demasiado pequeña  
\(\tau^Y<0\): empresa demasiado grande

Distorsiona el tamaño total.

**distorsion de capital \(\tau^K_{si}\)**

Eleva el costo efectivo del capital.

\(\tau^K>0\): demasiado poco capital

Distorsiona la relación \(K/L\) dentro de la empresa.

Los \(\tau\) no son impuestos explícitos: representan fricciones crediticias, regulación, corrupción o cualquier factor que altere los precios efectivos que enfrenta cada empresa.

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 31 / 39

---

# HK: CPO e Identificación de Distorsiones

\[
(1-\tau^Y_{si})\frac{\sigma-1}{\sigma}(1-\alpha)\frac{P_{si}Y_{si}}{L_{si}}=w
\quad \Rightarrow \quad
(1-\tau^Y_{si}) \propto \frac{wL_{si}}{P_{si}Y_{si}}
\]

\[
(1-\tau^Y_{si})\frac{\sigma-1}{\sigma}\alpha\frac{P_{si}Y_{si}}{K_{si}}=(1+\tau^K_{si})r
\quad \Rightarrow \quad
\frac{1+\tau^K_{si}}{1-\tau^Y_{si}}\propto \frac{rK_{si}}{P_{si}Y_{si}}
\]

Identificación desde los datos

Las distorsiones se recuperan directamente de participaciones factoriales en ingresos: no hace falta observar ni los impuestos explícitos ni los precios individuales. La asignación observada revela la magnitud de las distorsiones.

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 32 / 39

---

# HK: TFPQ, TFPR y su Relación con las Distorsiones

**TFPQ: productividad física**

\[
A_{si}=\frac{Y_{si}}{K_{si}^{\alpha}L_{si}^{1-\alpha}}
\]

Refleja tecnología real; heterogénea entre empresas.

Las empresas más productivas deberían ser más grandes.

**TFPR: productividad de ingresos**

\[
TFPR_{si}\equiv P_{si}A_{si}
=\frac{P_{si}Y_{si}}{K_{si}^{\alpha}L_{si}^{1-\alpha}}
\]

De las CPO:

\[
TFPR_{si}\propto \frac{(1+\tau^K_{si})^{\alpha}}{1-\tau^Y_{si}}
\]

Propiedad del equilibrio eficiente: Sin distorsiones, empresas más productivas cobran precios más bajos (\(P_{si}\propto 1/A_{si}\)) de modo que:

\[
TFPR_{si}=P_{si}A_{si}=TFPR_s \quad \forall i
\]

Diagnóstico

\(Var(TFPR_{si})=0\) en el eficiente. Dispersión observada \(\Rightarrow\) mala asignación.

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 33 / 39

---

# HK: Fórmula de la PTF Agregada

Combinando demanda CES, producción RCE y distorsiones:

\[
TFP_s =
\left[\sum_{i=1}^{M_s}
\left(A_{si}\frac{TFPR_s}{TFPR_{si}}\right)^{\sigma-1}
\right]^{\frac{1}{\sigma-1}}
\]

where

\[
TFPR_s \equiv
\frac{\sigma}{\sigma-1}
\left(\frac{r}{\alpha}\right)^\alpha
\left(\frac{w}{1-\alpha}\right)^{1-\alpha}
\]

es la TFPR del caso eficiente.

▷ El factor \(A_{si}\cdot (TFPR_s/TFPR_{si})\) es la contribución efectiva de la empresa  
▷ TFPR alto (gravada) \(\Rightarrow\) empresa demasiado pequeña \(\Rightarrow\) sub-contribuye  
▷ TFPR bajo (subsidiada) \(\Rightarrow\) demasiado grande \(\Rightarrow\) desplaza recursos de las productivas  
▷ Mayor \(\sigma\) \(\Rightarrow\) mayor costo de la dispersión (variedades más sustituibles)

Ganancia de eliminar distorsiones

\[
\frac{TFP_s^e}{TFP_s}
=
\frac{\left(\sum_i A_{si}^{\sigma-1}\right)^{\frac{1}{\sigma-1}}}{TFP_s}
\geq 1
\]

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 34 / 39

---

# HK: Distribuciones de TFPQ y TFPR

**TFPQ (productividad física)**

India y China desplazadas a la izquierda: más firmas con baja productividad real.

**TFPR (productividad de ingresos)**

China e India: mucho más dispersa.

EE.UU.: concentrada alrededor de la media.

**Descripción de imagen importante:** la diapositiva contiene dos gráficos de densidad. A la izquierda, “The Distribution of TFPQ in 4-digit Manufacturing Industries”, compara China, India y EE.UU.; China e India aparecen más desplazadas hacia la izquierda que EE.UU., indicando más firmas con baja productividad física. A la derecha, “The Distribution of TFPR in 4-digit Manufacturing Industries”, muestra que China e India tienen distribuciones más anchas/dispersas que EE.UU.; la distribución de EE.UU. está más concentrada cerca de la media.

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 35 / 39

---

# HK: Dispersión en Números

**TFPQ (productividad física):**

| País | Año | D.E. | P90-P10 |
|---|---:|---:|---:|
| China | 1998 | 1.06 | 2.72 |
| China | 2005 | 0.95 | 2.44 |
| India | 1994 | 1.23 | 3.11 |
| EE.UU. | 1997 | 0.84 | 2.18 |

Mayor dispersión en China e India refleja selección y tecnología, no solo mala asignación.

**TFPR (productividad de ingresos):**

| País | Año | D.E. | P90-P10 |
|---|---:|---:|---:|
| China | 1998 | 0.74 | 1.87 |
| China | 2005 | 0.63 | 1.59 |
| India | 1994 | 0.67 | 1.60 |
| EE.UU. | 1997 | 0.49 | 1.19 |

Alta dispersión de TFPR = mala asignación. China mejora 1998-2005 (reformas de mercado).

La dispersión de TFPQ refleja heterogeneidad tecnológica real; la de TFPR refleja distorsiones. Ambas contribuyen a las diferencias de PTF agregada.

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 36 / 39

---

# HK: Ganancias Potenciales

Ganancia de igualar la TFPR dentro de cada industria:

| País | Año | Ganancia PTF |
|---|---:|---:|
| China | 1998 | +115% |
| China | 2001 | +96% |
| China | 2005 | +87% |
| India | 1987 | +100% |
| India | 1991 | +102% |
| India | 1994 | +128% |
| EE.UU. | 1977 | +36% |
| EE.UU. | 1987 | +31% |
| EE.UU. | 1997 | +43% |

▷ Ganancias dentro de industrias: misma distribución de \(A_{si}\), solo se redistribuye \(K\) y \(L\)  
▷ Relativo a EE.UU. (no a cero distorsión): China 1998 \(\approx +51\%\), India 1994 \(\approx +59\%\)  
▷ La mejora de China entre 1998 y 2005 refleja reformas de mercado reales

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 37 / 39

---

# HK: Interpretación y Limitaciones

**Virtudes:**

▷ No requiere identificar la fuente de las distorsiones  
▷ Comparaciones entre países y períodos con los mismos datos  
▷ Cuantifica directamente la pérdida de PTF  
▷ Identifica qué empresas están sub/sobre-dimensionadas

**Limitaciones:**

▷ Error de medición: sobreestima la dispersión real (Bils-Klenow-Ruane 2017)  
▷ Costos de ajuste: parte de la dispersión es dinámica, no distorsión  
▷ Supuesto CES: requiere estructura de demanda para separar precio y cantidad  
▷ Silencio sobre causas: ¿qué política genera las distorsiones?

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 38 / 39

---

# Ejercicio con Datos

Ejercicio

El archivo `misallocation.xls` contiene datos de empleo y output para 10.000 firmas. Suponga \(y_i=z_i n_i^\alpha\), \(\alpha=2/3\).

1. Calcule \(TFP_i = y_i/n_i^\alpha\) y \(TFPR_i = y_i/n_i\) para cada firma; Haga un plot de ambas.
2. Calcule el output agregado y el \(TFP = Y/N^\alpha\)
3. Reasigne el empleo total \(N\) en forma optima y recompute el output y la TFP. Compare con los resultados anteriores.
4. ¿Cuál es la ganancia potencial?

Hugo Hopenhayn (Desarrollo Económico — UTDT) Asignación Ineficiente de Recursos 2026 39 / 39
