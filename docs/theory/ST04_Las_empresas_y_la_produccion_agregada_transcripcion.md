# LAS EMPRESAS Y LA PRODUCCIÓN AGREGADA

HUGO HOPENHAYN

UTDT

DESARROLLO ECONÓMICO

2026

1 / 26

---

# INTRODUCCIÓN

Como se determina la productividad agregada?

Cual es el rol de las empresas?

Cual es la importancia del numero de empresas?

Que determina el tamaño de las empresas?

Que determina el numero de empresas?

2 / 26

---

# EMPRESAS: CASO HOMOGÉNEO

Empresas $i = 1, \ldots, M$. Producto Homogéneo. Empleo total $N$.

Producción

$$
y_i = z f(n)
$$

donde $n$ es el total de empleo.

$f'(n) > 0$ y decreciente - rendimiento decrecientes

Caso particular: $f(n) = n^\alpha$

3 / 26

---

# PRODUCCIÓN

Dados precios $p$ y $w$,

$$
\max_n p z f(n) - w n
$$

▷ Condición de primer orden:

$$
p z f'(n) = w
$$

Si todas las empresas son idénticas: $n = N/M$

▷ Equilibrio requiere $p z f'(N/M) = w$

▷ Producción total $y = M z f(N/M)$

4 / 26

---

# EJEMPLO

$$
y_i = z n_i^\alpha
$$

Ejercicio

Derivar una expresión para la producción total como función de $z$, $M$ y $N$.

5 / 26

---

# DETERMINACIÓN DE M

▷ Necesitamos considerar la entrada/creación de empresas

▷ Supongamos que crear una empresa (emprendimiento) cuesta $c_e$ unidades de trabajo

▷ Asignación de trabajo:

▷ $M c_e$ dedicados a emprendimientos

▷ $N - M c_e$ a trabajar en empresas

▷ Libre entrada: Se crean empresas hasta el punto que

$$
\pi\left(z, (N - M c_e)/M\right) = w c_e \tag{1}
$$

6 / 26

---

# DETERMINACIÓN DE M: OPTIMO SOCIAL

▷ Objetivo: Maximizar el output total

$$
y = z M^{1-\alpha}(N - M c_e)^\alpha
$$

Ejercicio.

Resolver este problema de maximización y encontrar los resultados dados en la pagina siguiente.

7 / 26

---

# EMPRESAS, EMPLEO Y POBLACIÓN

▷ Resultado

$$
M c_e = (1 - \alpha) N
$$

$$
N - M c_e = \alpha N
$$

▷ El numero de empresas crece proporcionalmente a la Población Activa

▷ Mayores costos de entrada $\to$ menos empresas.

Ejercicio.

Encuentre el valor de $w$ tal que esta asignación satisface la condición de equilibrio (1). Explique intuitivamente cómo cambia $w$ con el costo de entrada.

8 / 26

---

# Firms vs Working-Age Population across US states

[Descripción de imagen: gráfico de dispersión en escala log-log. El eje horizontal es "Working-Age Population" con marcas aproximadas en 300,000, 1,000,000, 3,000,000 y 10,000,000. El eje vertical es "Number of Firms" con marcas aproximadas en 10,000, 30,000, 100,000 y 300,000. Los puntos representan estados de EE.UU. y se alinean fuertemente alrededor de una recta azul creciente, indicando que el número de firmas crece casi proporcionalmente con la población en edad de trabajar.]

9 / 26

---

# EMPRESAS HETEROGÉNEAS

▷ Productividad $z_1, z_2, \ldots, z_M$. Producción $y_i = z_i n_i^\alpha$.

▷ Condiciones de primer orden:

$$
\alpha z_i n_i^{\alpha-1} = w
$$

Notese:

$$
\ln(\alpha) + \ln z_i = (1 - \alpha) \ln n_i + \ln w
$$

$$
\varepsilon_{nz} = d \ln n / d \ln z = \frac{1}{1 - \alpha}
$$

Ejercicio

Encontrar expresiones para $n(z), y(z)$ y los beneficios $\pi(z)$.Que relación hay entre $w n(z)$ e $y(z)$?

10 / 26

---

# DISTRIBUCIÓN POR TAMAÑO DE LAS EMPRESAS

$$
\ln n(z) = \ln(\alpha/w) + \frac{1}{1 - \alpha} \ln z
$$

▷ La distribución de empleo esta determinada por la distribución de $z$.

▷ Caso particular: la distribucion de $z$ es Pareto,

$$
1 - F(z) = \left(\frac{z}{z_0}\right)^{-\zeta}
$$

▷ La de empleo también sera una distribución de Pareto con coeficiente $\zeta(1 - \alpha)$

$$
P(n(z) > n) = \left(\frac{n}{n_0}\right)^{-\zeta(1 - \alpha)}
$$

donde $n_0$ depende del total de empleo $N$.

11 / 26

---

# DISTRIBUCIÓN POR TAMAÑOS

[Descripción de imagen: gráfico titulado "Distribution of Establishments and Enterprises Sizes in 2000". El eje horizontal es "employment (log scale)", con valores de 1 a 1,000,000. El eje vertical es $\ln(P(\text{employment} > x))$, aproximadamente de 0 a -18. Hay tres series: "Establishments" en negro, "Enterprises" en rojo y "Pareto w.c. 1" en verde. Las curvas tienen pendiente negativa casi lineal en escala log, consistente con colas tipo Pareto; las empresas siguen una cola más larga que los establecimientos, y la línea verde sirve como referencia Pareto.]

12 / 26

---

# CONCENTRACIÓN

Una medida standard de concentración es ver qué porcentaje del empleo tiene el $k\%$ superior de firmas.

▷ Para el caso de Pareto:

$$
\left(\frac{k}{100}\right)^{1 - \frac{1}{(1 - \alpha)\zeta}}
$$

▷ Mayor concentración del empleo a menor $\zeta$ y mayor $\alpha$.

▷ Ejemplo: En USA $(1 - \alpha)\zeta \approx 1.2$

Ejercicio

Que porcentaje del empleo tiene el $1\%$ superior de firmas? El $5\%$ superior?

13 / 26

---

# Ejercicio

Suponga que $z$ tiene una distribución de Pareto con coeficiente $\zeta$:

$$
P(z' > z) = 1 - F(z) = \left(\frac{z}{z_0}\right)^{-\zeta}.
$$

1. Demuestre que $n(z)$ tiene una distribución de Pareto con coeficiente $\zeta(1 - \alpha)$

2. Una medida standard de concentración es ver qué porcentaje del empleo tiene el $1\%$, $5\%$, o alguna fracción de las firmas. Demostrar que el porcentaje de empleo del $k\%$ superior de firmas está dado por:

$$
\left(\frac{k}{100}\right)^{1 - \frac{1}{(1 - \alpha)\zeta}}
$$

14 / 26

---

# REPRESENTACIÓN GRÁFICA

▷ Una distribución de Pareto se puede representar muy fácil gráficamente:

$$
\ln(1 - F(z)) = \zeta \ln z_0 - \zeta \ln z
$$

▷ En el caso de empleo

$$
\ln(1 - P(n)) = \zeta(1 - \alpha) \ln n_0 - \zeta(1 - \alpha) \ln n
$$

▷ Si suponemos que $n_0 = 1, \ln(1 - P(n)) = -\zeta(1 - \alpha) \ln n$

15 / 26

---

# EQUILIBRIO Y FUNCIÓN DE PRODUCCIÓN AGREGADA

$$
n(z) = \left(\frac{\alpha z}{w}\right)^{\frac{1}{1 - \alpha}}
$$

Usando el equilibrio en el mercado de trabajo:

$$
N = \sum_i n(z_i) = \left(\frac{\alpha}{w}\right)^{\frac{1}{1 - \alpha}} \sum_i z_i^{\frac{1}{1 - \alpha}}
$$

o sea

$$
w = \alpha N^{\alpha - 1} \left(\sum_i z_i^{\frac{1}{1 - \alpha}}\right)^{1 - \alpha}
$$

Usando $wN = \alpha y$ (de donde sale esto?)

$$
y = \frac{wN}{\alpha} = N^\alpha \left(\sum_i z_i^{\frac{1}{1 - \alpha}}\right)^{1 - \alpha}
$$

16 / 26

---

# FUNCIÓN DE PRODUCCIÓN AGREGADA

$$
y = \left(\sum_i z_i^{\frac{1}{1 - \alpha}}\right)^{1 - \alpha} N^\alpha
$$

Si el numero de empresas es $M$, podemos reescribir

$$
y = \underbrace{\left(\frac{1}{M}\sum_i z_i^{\frac{1}{1 - \alpha}}\right)^{1 - \alpha}}_{Z} M^{1 - \alpha} N^\alpha
$$

El primer termino es el promedio de $z^{\frac{1}{1 - \alpha}}$.

17 / 26

---

# FUNCIÓN DE PRODUCCIÓN AGREGADA

$$
y = \left(\sum_i z_i^{\frac{1}{1 - \alpha}}\right)^{1 - \alpha} N^\alpha
$$

Si el numero de empresas es $M$, podemos reescribir

$$
y = \underbrace{\left(\frac{1}{M}\sum_i z_i^{\frac{1}{1 - \alpha}}\right)^{1 - \alpha}}_{Z} M^{1 - \alpha} N^\alpha
$$

El primer termino es el promedio de $z^{\frac{1}{1 - \alpha}}$.

En general, si la distribución de $z$ es $F(z)$, podemos escribir

$$
y = \left(\int z^{\frac{1}{1 - \alpha}} dF(z)\right)^{1 - \alpha} M^{1 - \alpha} N^\alpha
$$

17 / 26

---

# Ejercicio.

Suponga que la función de producción de las firmas es

$$
y_i = z \left(k_i^\theta n_i^{1 - \theta}\right)^\alpha
$$

y que

$$
K = \sum_i k_i \quad \text{y} \quad N = \sum_i n_i.
$$

Derivar la función de producción agregada de esta economía.

18 / 26

---

# CASO ESPECIAL: DISTRIBUCIÓN DE PARETO

$$
\left(\int z^{\frac{1}{1 - \alpha}} dF(z)\right)^{1 - \alpha}
=
\left(\frac{\zeta(1 - \alpha)}{\zeta(1 - \alpha) - 1}\right)^{1 - \alpha}
$$

▷ Decreciente en $\zeta$. Limite inferior 1. Limite superior $\infty$

▷ Condición necesaria $\zeta(1 - \alpha) > 1$. Interpretación?

Ejercicio.

1. Derivar esta expresión.

19 / 26

---

# PRODUCTIVIDAD AGREGADA

Usando la distribución de Pareto

$$
Z \equiv \left(\int z^{\frac{1}{1 - \alpha}} dF(z)\right)^{1 - \alpha}
= \left(\frac{\zeta(1 - \alpha)}{\zeta(1 - \alpha) - 1}\right)^{1 - \alpha}
$$

▷ La productividad aumenta con $\alpha$ y decrece con $\zeta$. Por que?

▷ Usando los datos de USA, considerando $\alpha = 2/3$,nos da $Z_{usa} = 1.82$

Ejercicio.

India tiene un ingreso per capita que es la décima parte de USA y un tamaño medio de firmas que es la cuarta parte del de USA. Suponiendo que $\alpha$ es el mismo en India, cual debiera ser su valor de $\zeta$?

20 / 26

---

# ENTRADA DE FIRMAS

▷ Supongamos igual tecnología de entrada con un costo de $c_e$ empleados.

▷ Después de que la firma entra, el valor de $z$ es aleatorio con distribución $F(z)$.

▷ Si el total de firmas es $M$,

$$
y = \underbrace{\left(\int z^{\frac{1}{1 - \alpha}} dF(z)\right)^{1 - \alpha}}_{Z} M^{1 - \alpha} (N - M c_e)^\alpha
$$

El problema del planificador es el mismo de antes, donde $y = ZM^{1 - \alpha}(N - M c_e)^\alpha$

▷ El resultado es idéntico al obtenido antes, ya que la solución vimos era independiente de $z$.

21 / 26

---

# INGRESO POR TRABAJADOR

Usando los resultados

$$
M c_e = (1 - \alpha) N
$$

$$
N - M c_e = \alpha N
$$

Ejercicio

Derivar el Ingreso por trabajador $y/N$ en esta economía. Como cambia con la población? Como cambia con el costo de entrada?

22 / 26

---

# COSTOS DE ENTRADA Y PTF

▷ Regresión entre paises (Moscoso-Boedo y Mukoyama, 2010)

▷ Calcular los costos regulatorios de crear un negocio medidos en unidades de trabajo anual $\kappa$

▷ El mas bajo EE.UU. $\kappa = 0.3$, el mas alto Liberia $\kappa = 616.8$, 29 paises con $\kappa < 1$ y 31 con $\kappa > 10$.

23 / 26

---

▷ La linea de regresion $d \ln y / d \ln \kappa = -2$ sugiere un efecto muy grande

[Descripción de imagen: gráfico de dispersión titulado "Entry Cost". El eje horizontal es "GNI per capita relative to US" en escala log, con marcas alrededor de 0.01, 0.1 y 1. El eje vertical es "Total Entry Cost $\kappa$" en escala log, aproximadamente desde $10^{-1}$ hasta $10^3$. Hay muchos puntos azules y una recta verde con pendiente negativa. La relación visual muestra que países con menor ingreso relativo a EE.UU. tienden a tener mayores costos regulatorios de entrada, aunque hay bastante dispersión.]

24 / 26

---

# COSTOS DE ENTRADA E Y/N

$$
d \ln y / dc_e = -(1 - \alpha)
$$

▷ Los efectos de las distorsiones depende del nivel de rendimientos decrecientes $\alpha$

▷ Con $\alpha = 2/3$,la elasticidad $d \ln y / dc_e = -1/3$

▪ Usualmente, los investigadores toman $\alpha = 0.85$, entonces $d \ln y / d \ln \kappa = -0.15$

▷ Valores muy bajos comparados con la elasticidad «empirica». Por que?

▷ Usando variables instrumentales la elasticidad «empirica» estimada baja a 0.30

▷ Explica aproximadamente un 1/5 de la brecha del Y/N entre los paises en el 20 superior y el 20 % inferior.

25 / 26

---

# COSTOS DE ENTRADA EN BIENES

Costo de Entrada en Bienes

Suponga que el costo de entrada es $c_e$ unidades de consumo (bienes) en vez de empleo. Como cambia el numero de empresas y el ingreso per capita con la productividad agregada $Z$? Como cambian con la poblacion?

26 / 26
