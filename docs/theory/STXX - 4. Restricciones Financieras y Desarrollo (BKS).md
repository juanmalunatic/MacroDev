# Finanzas y Desarrollo: Una Historia de Dos Sectores

Buera, Kaboski y Shin (2011)

Hugo Hopenhayn

UTDT

Desarrollo Económico, 2026

---

## Contenido

1. Motivación y Hechos Empíricos

2. El Modelo

3. Análisis de Equilibrio

4. Canales hacia la PTF

5. Cuantificación

6. Conclusiones

---

## Introducción

Correlación positiva entre desarrollo financiero (préstamos al sector privado/PIB) e ingreso per cápita.

El modelo explora cómo las restricciones al crédito afectan la PTF mediante dos canales:

1. La mala selección de emprendedores.

2. La mala asignación de recursos (capital) entre emprendimientos.

Novedad: el impacto de las fricciones financieras sobre la estructura sectorial (manufactura vs. servicios).

### Referencia central

Buera, F., Kaboski, J. y Shin, Y. (2011). “Finance and Development: A Tale of Two Sectors”. American Economic Review, 101(5), 1964–2002.

---

## Tres Hechos Empíricos Clave

1. **El desarrollo financiero varía ampliamente entre países**

   - Países ricos: financiamiento externo/PIB $\approx 2,1$.

   - Países pobres: financiamiento externo/PIB $\approx 0,1$.

2. **La manufactura es menos productiva en países pobres**

   - Precios relativos de bienes manufacturados más altos.

   - PTF relativa de manufactura más baja.

3. **La manufactura tiene mayor escala**

   - EE.UU.: 47 trabajadores por establecimiento (manuf.) vs. 14 (servicios).

   - Mayor escala $\Rightarrow$ mayores necesidades de financiamiento.

---

## PTF Sectorial entre Países

| País | PTF Manuf.<br>(relativa a EE.UU.) | PTF Servicios<br>(relativa a EE.UU.) |
|---|---:|---:|
| Estados Unidos | 1,00 | 1,00 |
| Corea del Sur | 0,72 | 0,85 |
| México | 0,45 | 0,74 |
| India | 0,28 | 0,61 |

### Patrón clave

La brecha de PTF en manufactura es *desproporcionadamente* grande respecto a servicios — el sector con mayores requerimientos de capital.

---

## El Mecanismo: Por Qué Importa la Escala

### Manufactura

Costos fijos **altos** $\kappa_M$

Necesita **más** capital

Fricciones financieras: **gran impacto**

### Servicios

Costos fijos **bajos** $\kappa_S$

Necesita **menos** capital

Fricciones financieras: **impacto pequeño**

*La asimetría de escala es la razón por la que las fricciones golpean más a la manufactura que a los servicios.*

---

## Agentes y Sectores

### Agentes

Continuo de masa $N$ de individuos de vida infinita, heterogéneos en riqueza $a$ y talento empresarial $z$.

### Sectores

- Dos sectores: manufactura $M$ y servicios $S$.

- Cada sector $j \in \{S,M\}$ tiene un costo fijo $\kappa_j$ medido en unidades del propio bien, con $\kappa_M > \kappa_S$.

### Talento empresarial

- $z = (z_S,z_M)$ extraído de la distribución $\mu(z)$.

- Se remuestrea con hazard rate constante $\gamma$.

---

## Preferencias

Cada individuo maximiza la utilidad esperada descontada:

$$
U(c) = \mathbb{E}
\left[
\sum_{t=0}^{\infty} \beta^t u(c_t)
\right]
$$

con utilidad de consumo compuesto:

$$
u(c_t)
=
\frac{1}{1-\sigma}
\left(
\psi c_{S,t}^{1-1/\varepsilon}
+
(1-\psi)c_{M,t}^{1-1/\varepsilon}
\right)^{
\frac{1-\sigma}{1-1/\varepsilon}
}
$$

- $\beta$: factor de descuento.

- $\sigma$: coeficiente de aversión relativa al riesgo.

- $\varepsilon$: elasticidad de sustitución entre $S$ y $M$.

- $\psi$: parámetro de participación de servicios.

---

## Tecnología

Función de producción del empresario $i$ en sector $j$:

$$
y_j = z_j k^\alpha l^\theta,
\qquad
\alpha + \theta < 1
\quad
\text{(rendimientos decrecientes)}
$$

- Mismas participaciones factoriales en ambos sectores.

- La escala eficiente depende de $z_j$ y de los precios:

$$
\left(k_j^u(z_j), l_j^u(z_j)\right)
=
\arg\max_{k,l}\pi_j(k,l)
$$

- El costo fijo $\kappa_j$ implica que sólo emprendedores con suficiente talento o riqueza pueden operar.

### Beneficios del empresario

$$
\pi_j(k,l;R,w,p)
=
p_j z_j k^\alpha l^\theta
-
Rk
-
wl
-
(1+r)p_j\kappa_j
$$

---

## Timing: Elección de Sector y Ocupación

### Imagen / diagrama

La diapositiva muestra un árbol de decisión temporal titulado internamente **Model: Timing — Sector and Occupation Choice**.

A la izquierda aparece el período $t$ y el estado inicial del agente:

$$
(a,(z_S,z_M))
$$

Desde ese nodo inicial sale una bifurcación marcada como **occupational choice**.

La rama superior corresponde a elegir ser empresario:

- Texto: **entrepreneur in $j,k_j$**
- Luego aparece una etapa: **produce, consume**
- Al final de la rama, en $t+1$, el talento puede:
  - permanecer como $z$ con probabilidad $\gamma$,
  - o remuestrearse como $z' \sim \mu(z')$ con probabilidad $1-\gamma$.

La rama inferior corresponde a trabajar:

- Texto: **work in any $j$**
- Luego aparece una etapa: **produce, consume**
- Al final también hay una bifurcación:
  - $z$ con probabilidad $\gamma$,
  - $z' \sim \mu(z')$ con probabilidad $1-\gamma$.

**Interpretación contextual:** el diagrama organiza el timing básico del modelo. Primero el agente llega con activos y talento sectorial. Luego decide si ser trabajador o empresario y, si es empresario, en qué sector operar. Después produce y consume. Finalmente, su talento puede persistir o remuestrearse, lo que introduce dinámica en la distribución de habilidades.

---

## Timing + Decision de Default

### Imagen / diagrama

La diapositiva repite el árbol de timing anterior, pero agrega explícitamente la dimensión financiera.

A la izquierda aparece el estado inicial:

$$
(a,(z_S,z_M))
$$

En el nodo de elección ocupacional aparece el texto:

**occupational choice**

y debajo:

**rent capital**

**borrow**

La rama superior corresponde al empresario:

- Texto: **entrepreneur in $j,k_j$**
- Luego aparece una etapa con el texto: **produce, repay/default, consume**
- Al final, en $t+1$, el talento:
  - queda como $z$ con probabilidad $\gamma$,
  - o pasa a $z' \sim \mu(z')$ con probabilidad $1-\gamma$.

La rama inferior corresponde al trabajador:

- Texto: **work in any $j$**
- Luego aparece una etapa: **produce, consume**
- Al final se repite la misma estructura de persistencia/remuestreo del talento.

**Interpretación contextual:** esta versión enfatiza que el empresario debe financiar capital antes de producir y que, después de producir, decide si repaga o incumple. Por eso las fricciones de cumplimiento y colateral se vuelven centrales: determinan cuánto puede pedir prestado un empresario y, por tanto, si puede operar a escala eficiente.

---

## Mercados de Crédito y Capital

### Mercado de capital

Condición de cero beneficios para el arrendamiento de capital:

$$
R = r + \delta
$$

### Fricción financiera: cumplimiento imperfecto

El empresario puede retener la fracción $(1-\varphi)$ del valor neto de la empresa si incumple:

$$
(1-\varphi)\left[p_jz_jf(k,l)-wl+(1-\delta)k\right]
$$

- El castigo es perder los activos $a$, pero puede seguir operando

- $\varphi$ mide la fortaleza del cumplimiento legal; $\varphi = 1$ es cumplimiento perfecto.

### Restricción de colateral

$$
k \leq \bar{k}_j(a,z;\varphi),
\qquad
\text{creciente en } a,z \text{ y } \varphi.
$$

Mayor $\kappa_j \Rightarrow$ límite de endeudamiento más bajo en $j$.

---

## Problema Dinámico del Agente

$$
v(a,z)
=
\max\{v^w(a,z), v^S(a,z), v^M(a,z)\}
$$

### Trabajador:

$$
v^w(a,z)
=
\max_{c,a'\geq 0}
u(c)
+
\beta
\left[
\gamma v(a',z)
+
(1-\gamma)Ev(a',z')
\right]
$$

s.a.

$$
pc+a' \leq w+(1+r)a
$$

### Empresario en sector $j$:

$$
v^j(a,z)
=
\max_{c,a',k,l}
u(c)
+
\beta
\left[
\gamma v(a',z)
+
(1-\gamma)Ev(a',z')
\right]
$$

s.a.

$$
pc+a'
\leq
\pi_j(z_j,k,l)+(1+r)a,
\qquad
k \leq \bar{k}_j(a,z_j;\varphi)
$$

---

## Equilibrio Estacionario

Un equilibrio estacionario es un conjunto de funciones de política

$$
\{c_j,a',o,l,k,\bar{k}_j\},
$$

precios

$$
\{w,R,r,p\}
$$

y distribución $G(a,z)$ tal que:

1. Las funciones de política resuelven el problema del agente dados precios y límites de endeudamiento.

2. Los intermediarios financieros obtienen beneficios nulos: $R = r+\delta$.

3. Los límites de endeudamiento son los más generosos compatibles con el cumplimiento.

4. Los mercados de capital, trabajo, $S$ y $M$ se vacían.

5. La distribución $G(a,z)$ es invariante:

Definiendo

$$
A(a',z') =
\{(a,z)\mid a'(a,z)\leq a;\ z\leq z'\}
$$

$$
G(a,z)
=
\gamma
\int_{A(a,z)}
G(da',dz')
+
(1-\gamma)\mu(z)
\int_{A(a,\infty)}
G(da',dz')
$$

---

## Decisiones de Emprendimiento con Crédito Perfecto

### Imagen / diagrama

La diapositiva muestra un plano con eje vertical $a$ y eje horizontal $z$. Sobre el eje horizontal aparece un umbral vertical etiquetado como $\underline{z}_T$.

En la parte superior del gráfico aparece el texto:

$$
\text{for } z_{NT} \to 0
$$

El gráfico tiene una línea vertical en $\underline{z}_T$, lo que indica que con crédito perfecto la decisión de emprendimiento depende de un umbral de talento/productividad, no de la riqueza.

**Interpretación contextual:** con crédito perfecto, la riqueza inicial $a$ no limita la escala ni la entrada. Por eso la frontera de decisión es vertical: si el talento $z$ supera el umbral, el individuo puede ser empresario aunque sea pobre; si está por debajo, trabaja aunque sea rico.

---

## Decisiones de Emprendimiento con Crédito Perfecto

### Imagen / diagrama

La diapositiva repite el plano $(a,z)$ con eje vertical $a$ y eje horizontal $z$. Se mantiene el umbral vertical $\underline{z}_T$ y el texto:

$$
\text{for } z_{NT} \to 0
$$

A la izquierda del umbral aparece la etiqueta:

**Worker**

A la derecha del umbral aparece la etiqueta:

**Entrepreneur**

**Interpretación contextual:** la versión completa del gráfico deja explícita la partición ocupacional. Con crédito perfecto, todos los agentes con $z<\underline{z}_T$ son trabajadores y todos los agentes con $z>\underline{z}_T$ son empresarios, independientemente de su riqueza $a$.

---

## Fricción de Crédito: Equilibrio Parcial

### Imagen / diagrama

La diapositiva muestra nuevamente el plano con riqueza $a$ en el eje vertical y talento/productividad $z$ en el eje horizontal. Se mantiene la línea vertical punteada en $\underline{z}_T$ y el texto:

$$
\text{for } z_{NT} \to 0
$$

A diferencia del caso de crédito perfecto, ahora aparece una curva negra decreciente que parte cerca del umbral $\underline{z}_T$ con valores altos de riqueza y cae hacia la derecha. Debajo de esa curva, a la derecha de $\underline{z}_T$, hay una región sombreada en rojo con líneas diagonales.

La diapositiva incluye el texto:

**Fewer poor, talented entrepreneurs**

con una flecha apuntando a la zona de alta productividad pero baja riqueza.

**Interpretación contextual:** en equilibrio parcial con fricciones de crédito, algunos individuos talentosos pero pobres no pueden financiar la escala necesaria para operar como empresarios. Por eso, aunque tengan $z$ alto, quedan excluidos si su riqueza $a$ es demasiado baja. Esta es una distorsión de selección: se pierden emprendedores potencialmente productivos por falta de colateral.

---

## Efectos de Equilibrio General

### Imagen / diagrama

La diapositiva mantiene el plano $(a,z)$ con eje vertical $a$ y eje horizontal $z$. El umbral $\underline{z}_T$ aparece marcado con una línea vertical punteada. También aparece una curva negra decreciente similar a la anterior.

A la derecha y debajo de la curva permanece una zona roja rayada, que representa empresarios talentosos pero pobres que no pueden operar por restricciones de crédito.

Además, a la izquierda del umbral aparece una nueva región sombreada en verde, cerca de niveles altos de riqueza y relativamente bajo talento. Una flecha apunta a esa zona con el texto:

**More rich, Low talent entrepreneurs**

**Interpretación contextual:** el equilibrio general agrega otro canal. Cuando las fricciones reducen la entrada de pobres talentosos, los precios y retornos pueden hacer rentable que individuos ricos pero menos talentosos se vuelvan empresarios. Esto genera mala selección ocupacional en dos direcciones: faltan emprendedores pobres y talentosos, y sobran emprendedores ricos de menor productividad.

---

## Importancia de las Fricciones de Crédito

### Imagen / diagrama

La diapositiva muestra el mismo plano $(a,z)$ con la frontera de emprendimiento bajo fricciones. Además de las regiones roja y verde, se agregan curvas elípticas negras que representan distribuciones conjuntas posibles de riqueza y talento.

El texto dentro del gráfico dice:

**Impact depends on joint distribution of a,z**

con una flecha apuntando a las elipses de distribución.

Las elipses se ubican principalmente en la zona izquierda-baja/media del gráfico y muestran que la masa de agentes puede estar más o menos alineada con las regiones distorsionadas. La frontera de restricción queda cerca del umbral $\underline{z}_T$, y la magnitud de la pérdida depende de cuántos agentes caigan en las zonas relevantes.

**Interpretación contextual:** la diapositiva enfatiza que no alcanza con conocer la severidad de la fricción financiera. El impacto agregado depende de la distribución conjunta de riqueza y talento. Si muchos agentes talentosos son pobres, la pérdida es grande. Si riqueza y talento están más alineados, la fricción puede ser menos costosa.

---

## Cómo las Fricciones Reducen la PTF Agregada

### Canal 1: Selección Ocupacional

Talentosos pero pobres $\to$ no pueden ser empresarios.

Menos talentosos pero ricos $\to$ se vuelven empresarios.

$\Rightarrow$ Mala asignación de talento empresarial.

### Canal 2: Ineficiencia de Escala

Los empresarios no pueden pedir prestado hasta alcanzar la escala eficiente.

La riqueza $a$, no la productividad $z$, determina la escala.

$\Rightarrow$ Mala asignación de capital y trabajo entre empresas.

### Canal 3: Reasignación Sectorial

Los recursos se desplazan de manufactura (alta escala) a servicios (baja escala).

$\Rightarrow$ La economía opera en los sectores “incorrectos”.

---

## Análisis Cuantitativo: Parámetros

### Parámetros tecnológicos

$$
\{\alpha,\theta,\kappa_S,\kappa_M,\delta\}
$$

### Distribución de talentos

Pareto con coeficiente $\eta$, independiente entre sectores. Probabilidad de remuestreo $\gamma$

### Preferencias

$$
\{\beta,\sigma,\varepsilon,\psi\}
$$

### Calibración base

EE.UU. como referencia (sin restricciones): $\varphi = 1$.

---

## Calibración

| Momento objetivo | Datos EE.UU. | Modelo | Parámetro |
|---|---:|---:|---:|
| Top 10 % empleo | 0,69 | 0,69 | $\eta = 4,84$ |
| Top 5 % ingresos | 0,30 | 0,30 | $\alpha+\theta = 0,79$ |
| Escala media servicios | 14 | 14 | $\kappa_S = 0,00$ |
| Escala media manuf. | 47 | 47 | $\kappa_M = 4,68$ |
| Tasa de salida | 0,10 | 0,10 | $\gamma = 0,89$ |
| Partic. manuf. PIB | 0,25 | 0,25 | $\psi = 0,91$ |
| Tasa de interés | 0,04 | 0,04 | $\beta = 0,92$ |

- $\delta = 0,06$ (estándar en la literatura).

- $\sigma = 1,5$; $\varepsilon = 1,0$.

- Participación del capital: $\alpha/(1/\eta+\alpha+\theta)=0,30$.

---

## Principales Resultados Cuantitativos

| Variable | Crédito perfecto<br>$(\varphi = 1)$ | Autarquía financiera<br>$(\varphi = 0)$ |
|---|---:|---:|
| Producto por trabajador | 100 % | 48 % |
| PTF agregada | 100 % | 64 % |
| PTF manufactura | 100 % | 45 % |
| PTF servicios | 100 % | 74 % |
| Razón capital/producto | 100 % | 85 % |

---

## Simulación: Metodología de Regresión

1. Resolver el modelo para distintos valores de $\varphi \in [0,1]$.

2. Calcular el PIB para cada $\varphi$.

3. Calcular el desarrollo financiero:

$$
\operatorname{df}(\varphi)
=
\int (k_i-a_i)\,di \,/\, \text{PIB}.
$$

4. Renormalizar: $\operatorname{df}(\varphi)/\operatorname{df}(1)$.

5. Regresionar el PIB relativo contra el df normalizado.

6. Comparar con la regresión en datos reales con normalización similar.

| Variable | Coef. datos | Coef. modelo | Cociente |
|---|---:|---:|---:|
| $Y/N$ | 0,34 | 0,22 | 65 % |
| PTF | 0,26 | 0,15 | 58 % |
| $K/Y$ | 0,76 | 0,25 | 33 % |
| $p_M/p_S$ | $-0,67$ | $-0,16$ | 24 % |

### Implicancias

Las fricciones financieras pueden explicar:

- $\approx 60\%$ de la relación PTF–finanzas entre países.

- $\approx 67\%$ de la diferencia de producto EE.UU.–México.

---

## Resultados Sectoriales

- PTF cae 26 % en servicios y 55 % en manufactura.

- **Margen intensivo:** distorsión en asignación de capital.

$$
DS(\ln PgMK) = 1,07\ (S)
\qquad \text{vs.} \qquad
1,23\ (M)
$$

- **Margen extensivo:** distorsión en decisiones de entrada y salida.

| Canal | Manufactura | Servicios |
|---|---:|---:|
| Efecto selección | 35 % | 18 % |
| Efecto escala | 45 % | 25 % |
| Efecto composición | 20 % | 7 % |
| **Pérdida total PTF** | **55 %** | **26 %** |

---

## Desarrollo Financiero y Crecimiento de PTF

El modelo también genera dinámicas de crecimiento:

- Mejorar mercados financieros $\Rightarrow$ crecimiento de PTF.

- La manufactura crece más rápido que servicios (cambio estructural).

- El crecimiento se concentra en establecimientos grandes.

| Episodio | Aumento $\varphi$ | Crecimiento PTF (anual)<br>Datos | Crecimiento PTF (anual)<br>Modelo |
|---|---:|---:|---:|
| Corea 1980–1995 | $0,3 \to 0,8$ | 4,2 % | 3,8 % |

### Resultado clave

La profundización financiera puede explicar una porción significativa del milagro coreano.

---

## Conclusiones

### Principales resultados

1. El desarrollo financiero es un determinante importante de la productividad agregada.

2. Los efectos son heterogéneos entre sectores: manufactura sufre el doble que servicios.

3. El vínculo finanzas–PTF opera a través de la mala asignación.

4. El modelo replica la correlación finanzas–PIB/trabajador en datos de corte transversal.

5. Las fricciones financieras explican parte del cambio estructural de manufactura a servicios.