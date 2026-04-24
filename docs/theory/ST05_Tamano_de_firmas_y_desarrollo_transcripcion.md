# Tamaño de firmas y Desarrollo

Hopenhayn (2016)

Hugo A. Hopenhayn  
ECONOMÍA, 2016

1 / 20

---

# Índice

1. Motivación
2. Modelo
3. Agregación
4. Entrada, Salida y el Problema del Planificador
5. Distribución de Pareto
6. Resultados Cuantitativos
7. Conclusiones

2 / 20

---

# Firmas y Desarrollo

**Hecho estilizado**  
El tamaño promedio de las firmas aumenta fuertemente con el PIB per cápita.

**Evidencia:**

- Bento & Restuccia (2015): base de datos de 134 países $\Rightarrow$ elasticidad ingreso del tamaño de establecimientos $\approx 0.29$
- Muestra de América Latina: elasticidad $\approx 0.53$
- El país latinoamericano promedio tiene aproximadamente la mitad del tamaño medio de firmas de EE.UU.
- 8 de 12 países latinoamericanos están por debajo de este umbral

**Pregunta de investigación**  
¿Qué explica esta correlación? ¿Y qué implica para las diferencias en PIB?

3 / 20

---

# Distribución del Tamaño: América Latina vs. EE.UU.

**Distribución del tamaño en manufactura (%)**

| Estrato | Am. Lat. | EE.UU. |
|---|---:|---:|
| 10–19 empleados | 38.5 | 31.9 |
| 20–49 | 28.3 | 32.4 |
| 50–99 | 14.3 | 16.2 |
| 100–249 | 11.3 | 12.8 |
| 250+ | 7.6 | 6.8 |

**Firmas con <10 empleados**

| País | firmas (%) | Empleo (%) |
|---|---:|---:|
| Argentina | 84.0 | 22.0 |
| Bolivia | 91.7 | 43.6 |
| El Salvador | 82.0 | 17.7 |
| México | 90.5 | 22.7 |
| EE.UU. | 54.5 | 4.2 |

Contraste clave: la participación del empleo en microfirmas es $>5\times$ mayor en América Latina que en EE.UU.

4 / 20

---

# Tres Explicaciones Alternativas

1. **Entrada excesiva / salida insuficiente**  
   Demasiadas firmas pequeñas y de baja productividad sobreviven $\Rightarrow$ menor tamaño promedio y menor PIB

2. **Diferencias en la distribución de productividades**  
   Peores realizaciones de productividad ($\uparrow \zeta$ en Pareto) $\Rightarrow$ menor tamaño promedio y menor PIB

3. **Diferencias en retornos a escala**  
   Menor $\alpha$ (p.ej., por restricciones de crédito) $\Rightarrow$ firmas más pequeñas y menor PIB

**Resultado principal**  
Los tres canales generan grandes variaciones en el tamaño de firmas, pero variaciones mucho menores en el PIB — las elasticidades implícitas son 5–10$\times$ mayores que en los datos.

5 / 20

---

# Estructura del Modelo

**Entorno**

- Un período, población de tamaño $N$, bien homogéneo
- Función de producción: $y = z n^{\alpha}$, $\alpha \in (0,1)$
- Costo fijo: $f \geq 0$ unidades de trabajo por empresa activa
- Costo de entrada: $c$ unidades de trabajo

**Secuencia temporal (tres etapas):**

1. Decisión de entrada
2. Realización $z \sim G$; Quedarse/Salir
3. Producción

**Dos casos especiales:**

- Modelo span-of-control de Lucas (1978): $c = 0$, $f = 1$, $M_0 = N$
- Modelo de entrada y salida de Hopenhayn (1992): $c > 0$, $M_0$ endógeno

6 / 20

---

# Equilibrio

**Problema de la firma:** dado $w$, maximizar $\pi(z,w) = z n^{\alpha} - w(n+f)$

Beneficios crecientes en $z \Rightarrow$ **selección:** la empresa opera si y solo si $z \geq z^*$, donde

$$
\pi(z^*,w) = wf
$$

**Condiciones de equilibrio:**

1. **Umbral de salida:** $\pi(z^*,w) = wf$

2. **Libre entrada (Hopenhayn):**

$$
\int_{z^*} [\pi(z,w) - wf] \, dG(z) = wc,
$$

o bien $M_0 = N$ si $c = 0$

3. **Equilibrio del mercado laboral:**

$$
\underbrace{M_0[c + (1 - G(z^*))f]}_{\text{entrada + costos fijos}}
+
\underbrace{M_0 \int_{z^*} n(z,w)\,dG(z)}_{\text{trabajo productivo}}
= N
$$

**Nota:** El equilibrio competitivo = solución al problema del planificador (maximizar PIB per cápita sujeto a la restricción de recursos).

7 / 20

---

# Agregación

Sea $M =$ masa de firmas productoras, $F =$ distribución de productividades (condicional en $z \geq z^*$), $L =$ trabajo productivo.

**Empleo óptimo:** $n(z) \propto z^{1/(1-\alpha)} \Rightarrow$ producto agregado:

**Función de producción agregada**

$$
y = \underbrace{\left(E_F\left[z^{\frac{1}{1-\alpha}}\right]^{1-\alpha}\right)}_{\equiv \bar z} M^{1-\alpha} L^{\alpha}
$$

donde

$$
\bar z = \left(E_F\left[z^{1/(1-\alpha)}\right]\right)^{1-\alpha}
$$

es la **media geométrica de productividades**.

**Implicaciones clave:**

- Cobb-Douglas en $M$ (número de firmas) y $L$ (trabajo) con el mismo $\alpha$
- **Las firmas son insumos** — igual que el trabajo
- Participación del trabajo: $wL = \alpha y$
- $\bar z$ determinada únicamente por la distribución de productividades $F$

8 / 20

---

# Distribución del Tamaño de firmas

**Tamaño de la empresa más pequeña** (de la condición de salida $\pi(z^*,w) = wf$):

$$
n(z^*) = \frac{\alpha}{1-\alpha} f
$$

- Independiente del costo de entrada $c$ y de la distribución de productividades
- Depende únicamente de $\alpha$ y del costo fijo $f$

**Tamaño promedio de empresa** (excluyendo costo fijo):

$$
\bar n
= \frac{\alpha}{1-\alpha}
\cdot
\frac{1}{1-G(z^*)}
\int_{z^*}
\left(\frac{z}{z^*}\right)^{\alpha/(1-\alpha)}
\, dG(z)
$$

**Observación**  
El tamaño promedio es **creciente** en $\alpha$ (retornos a escala) y en $f$ (costo fijo), y depende de $G$ solo a través de la cola derecha por encima de $z^*$.

9 / 20

---

# Problema del Planificador (Modelo de Hopenhayn)

El planificador elige $(z^*, L, M_0 \leq N)$ para maximizar:

$$
\max \quad y =
\left( \int_{z^*} z^{\frac{1}{1-\alpha}} \, dG(z) \right)^{1-\alpha}
M_0^{1-\alpha} L^{\alpha}
$$

sujeto a:

$$
M_0[c + (1 - G(z^*))f] + L \leq N
$$

**Condiciones de primer orden:**

$$
\text{(Trabajo)} \qquad \alpha y/L = \lambda
$$

$$
\text{(Entrada)} \qquad (1-\alpha)y/M_0 = \lambda [c + (1 - G(z^*))f]
$$

$$
\text{(Umbral)} \qquad (z^*)^{\frac{\alpha}{1-\alpha}} \cdot M_0 f g(z^*) = \lambda \cdot (\text{valor marginal de } z^*)
$$

De las CPO de $L$ y $M_0$:

$$
L = \alpha N, \qquad
M_0 = \frac{(1-\alpha)N}{c + (1 - G(z^*))f}
$$

10 / 20

---

# Umbral Óptimo $z^*$

Sustituyendo $L$ y $M_0$, el problema se reduce a:

$$
\max_{z^*}
\frac{\int_{z^*} z^{\frac{1}{1-\alpha}} \, dG(z)}{c + (1 - G(z^*))f}
$$

**CPO para $z^*$:**

$$
(z^*)^{\frac{1}{1-\alpha}} \cdot [c + (1 - G(z^*))f]
= f \int_{z^*} z^{\frac{1}{1-\alpha}} \, dG(z)
$$

**Resultado**

$$
\frac{\int_{z^*} z^{\frac{1}{1-\alpha}} \, dG(z)}{(z^*)^{\frac{1}{1-\alpha}}}
=
\frac{c + f(1 - G(z^*))}{f}
$$

Izq.: productividad relativa esperada de las empresas activas  
Der.: razón de costos normalizada

11 / 20

---

# Umbral Óptimo $z^*$: Análisis Gráfico

Dividir la CPO por $z^{*\frac{1}{1-\alpha}}$, restar $f(1 - G(z^*))$, dividir por $f$:

$$
\underbrace{\int_{z^*}^{\infty}
\left[\left(\frac{z}{z^*}\right)^{\frac{1}{1-\alpha}} - 1\right] dG(z)}_{\Phi(z^*) : \text{ estrictamente decreciente}}
=
\underbrace{\frac{c}{f}}_{\text{constante}}
$$

- $z^*$ **creciente en** $f$ (mayor costo fijo $\Rightarrow$ selección más estricta)
- $z^*$ **creciente en** $\alpha$ (mayor complementariedad $\Rightarrow$ la calidad importa más)
- $z^*$ **decreciente en** $c$ (mayor costo de entrada $\Rightarrow$ menor $M_0$, menor $z^*$)

> **Descripción de figura (slide 12):** gráfico de $\Phi(z^*)$ contra $z^*$ con una curva roja decreciente y una línea horizontal azul que representa $c/f$. El punto negro marca el equilibrio base $z_0^*$. Una suba de $c$ desplaza hacia arriba la línea horizontal $c/f$ y mueve el umbral a la izquierda, marcado como $z_{\uparrow c}^*$. Una suba de $f$ baja $c/f$ y mueve el umbral a la derecha, marcado como $z_{\uparrow f}^*$. Una suba de $\alpha$ desplaza hacia arriba la curva $\Phi$ y también mueve el umbral a la derecha, marcado como $z_{\uparrow \alpha}^*$. La figura resume visualmente los signos comparativos: $z^*$ aumenta con $f$ y $\alpha$, y cae con $c$.

12 / 20

---

# Distribución de Pareto

Suponemos $1 - G(z) = z^{-\zeta}$ (Pareto con parámetro $\zeta$, mínimo $z_{\min}=1$).

**Resultados analíticos para el modelo de Hopenhayn:**

$$
L = \alpha N, \qquad
M_0 = \frac{N}{c} \cdot \zeta^{-1}, \qquad
z^* = \left[\frac{f}{c(\zeta(1-\alpha)-1)}\right]^{1/\zeta}
$$

$$
\bar n = \frac{\alpha}{1-\alpha}
\left[\frac{\zeta}{\zeta(1-\alpha)-1} - 1\right] + f
$$

**Proposición 4**

- $\uparrow \zeta \Rightarrow \downarrow \bar n, \downarrow$ PIB  
  Peor distribución $\Rightarrow$ firmas más pequeñas, menor producto
- $\uparrow \alpha \Rightarrow \uparrow \bar n, \uparrow$ PIB  
  Mayores retornos a escala $\Rightarrow$ firmas más grandes, mayor producto

**Tamaño medio y costo de entrada**  
Con distribución Pareto, **el costo de entrada $c$ no afecta el tamaño promedio.**

Un mayor $c$ reduce $M_0$ pero también reduce $z^*$, compensándose exactamente.

13 / 20

---

# Estrategia Cuantitativa

**Calibración de referencia:**

- Dos valores de $\alpha$: 0.65 (Hsieh-Klenow) y 0.85 (literatura macro)
- Costo fijo $f=1$, costo de entrada $c=1$
- $\zeta$ elegido para replicar tamaño promedio = 20 (manufactura EE.UU.)
  - $\alpha = 0.65 \Rightarrow \zeta = 3.14$
  - $\alpha = 0.85 \Rightarrow \zeta = 9.15$

**Tres experimentos:**

1. Aumentar el número de firmas (entrada excesiva / salida insuficiente)
2. Aumentar $\zeta$ (peor distribución de productividades)
3. Reducir $\alpha$ (menores retornos a escala)

En cada caso: ¿Cuánto cae el PIB cuando cae el tamaño promedio?

14 / 20

---

# Experimento 1: Entrada Excesiva

| Tam. prom. | PIB ($\alpha=0.65$) | PIB ($\alpha=0.85$) |
|---:|---:|---:|
| 20 | 1.00 | 1.00 |
| 10 | 0.98 | 0.99 |
| 5 | 0.91 | 0.94 |
| 2.5 | 0.74 | 0.80 |
| 2 | 0.64 | 0.73 |

**Mecanismo:** demasiadas firmas $\Rightarrow$ menor $z^*$ $\Rightarrow$ menor calidad y menos trabajadores productivos

**Resultado**  
Caída del 50% en el tamaño $\Rightarrow$ solo <2% de caída en el PIB.

Elasticidad implícita tamaño/PIB: 6.5–8.5 (vs. 0.3–0.5 en los datos)

¿Por qué? Las desviaciones de la entrada óptima son de segundo orden para el PIB pero de primer orden para el tamaño.

15 / 20

---

# Experimento 2: Peor Distribución de Productividades ($\uparrow \zeta$)

| Tam. prom. | PIB ($\alpha=0.65$) | PIB ($\alpha=0.85$) |
|---:|---:|---:|
| 20 | 1.00 | 1.00 |
| 15 | 0.83 | 0.91 |
| 10 | 0.67 | 0.78 |
| 6.7 | 0.53 | 0.65 |
| 2.9 | 0.25 | — |

**Mecanismo:** mayor $\zeta \Rightarrow$ cola derecha más delgada $\Rightarrow$ menor $\bar z \Rightarrow$ menor PTF y tamaño

**Elasticidad implícita**  
$\approx 1.5$ ($\alpha=0.85$) a $2.7$ ($\alpha=0.65$)

Elasticidad considerablemente menor que en Exp. 1, pero aún por encima de los datos.

**Nota**  
Un $\zeta$ elevado implica menor dispersión en el tamaño — contrario a los datos (India y América Latina tienen mayor dispersión que EE.UU.)

16 / 20

---

# Experimento 3: Menores Retornos a Escala ($\downarrow \alpha$)

| Tam. prom. | Lucas $\zeta=3.1$ | Lucas $\zeta=9.2$ | Hopenhayn $\zeta=3.1$ | Hopenhayn $\zeta=9.2$ |
|---:|---:|---:|---:|---:|
| 20 | 1.00 | 1.00 | 1.00 | 1.00 |
| 15 | 0.91 | 0.95 | 0.91 | 0.95 |
| 10 | 0.79 | 0.87 | 0.80 | 0.88 |
| 5 | 0.62 | 0.73 | 0.65 | 0.75 |
| 2.5 | 0.50 | 0.61 | 0.54 | 0.65 |

**Resultados**  
Elasticidad PIB/tamaño implícita: 3.3–4.20

Caída de 12–21% en PIB para reducir el tamaño a la mitad

**Mecanismo:** menor $\alpha \Rightarrow$ empresa óptima más pequeña $\Rightarrow$ más firmas $\Rightarrow$ menor tamaño promedio

**Fundamento:** restricciones de crédito impiden adoptar tecnologías con alto costo fijo y alto $\alpha$ (Banerjee & Duflo)

17 / 20

---

# Comparación entre Experimentos

| Fuente de variación | Efecto PIB | Efecto tamaño | Elast. implíc. |
|---|---|---|---:|
| 1. Entrada excesiva | Muy pequeño | Grande | 6.5–8.5 |
| 2. Peor dist. productiv. ($\uparrow \zeta$) | Moderado | Grande | 1.2–2.7 |
| 3. Menores ret. escala ($\downarrow \alpha$) | Moderado | Grande | 3.3–4.20 |
| Datos (mundo) | — | — | $\approx 0.3$ |
| Datos (Am. Lat.) | — | — | $\approx 0.5$ |

**Lección general**

- El tamaño de empresa es muy sensible a las tres fuentes de variación
- El PIB per cápita es mucho menos sensible — las brechas observadas en PIB requieren cambios enormes en el tamaño
- Los canales 2 y 3 son los más próximos a replicar la elasticidad en los datos

18 / 20

---

# Conclusiones

1. El tamaño promedio de empresa es muy elástico ante distorsiones de entrada, la distribución de productividades y los retornos a escala
2. El PIB per cápita es mucho menos elástico — las elasticidades implícitas tamaño-PIB son 3–5$\times$ mayores que en los datos
3. El modelo no puede dar cuenta de la mayor parte de la brecha de PIB, pero es muy efectivo para explicar las diferencias en tamaño
4. Mejores candidatos para reconciliar teoría y datos:
   - Distorsiones correlacionadas que reducen la inversión en productividad (Bento & Restuccia)
   - Restricciones de crédito que limitan la adopción de tecnologías con alto $\alpha$ (Banerjee & Duflo)

19 / 20

---

# Referencias

Banerjee & Duflo (2005). Growth Theory through the Lens of Development Economics. Handbook of Development Economics.

Bento & Restuccia (2015). Misallocation, Establishment Size, and Productivity. Working Paper, U. Toronto.

Caselli (2005). Accounting for Cross-Country Income Differences. Handbook of Economic Growth.

Hopenhayn (1992). Entry, Exit, and Firm Dynamics in Long-Run Equilibrium. Econometrica.

Hsieh & Klenow (2009). Misallocation and Manufacturing TFP in China and India. QJE.

Hsieh & Klenow (2014). The Life Cycle of Plants in India and Mexico. QJE.

Lucas (1978). On the Size Distribution of Business Firms. Bell Journal of Economics.

Pagés, ed. (2010). La era de la productividad. BID.

Poschke (2010). The Regulation of Entry and Aggregate Productivity. Economic Journal.

20 / 20
