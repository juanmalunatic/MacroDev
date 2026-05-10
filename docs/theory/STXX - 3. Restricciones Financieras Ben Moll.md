# Productivity Losses from Financial Frictions: Can Self-Financing Undo Capital Misallocation?

Benjamin Moll

AER, octubre 2014

---

## Motivación: ¿Por qué importan las finanzas?

Pregunta fundamental: ¿Qué explica la dispersión de PTF en el mundo?

En esta lección: Diferencias en el desarrollo financiero

- En países ricos, emprendedores talentosos pueden pedir préstamos para iniciar negocios

- En países pobres, solo personas con riqueza pueden iniciar negocios

- Esto significa que el capital no fluye hacia las mejores ideas

Objetivo de hoy: Construir un modelo simple para entender:

1. Cómo las restricciones crediticias afectan qué empresas operan (selección)

2. Cómo afectan la asignación de recursos entre las empresas

3. Cómo afecta la distribución de la riqueza a la PTF y la producción agregada

4. Cuánto puede impulsar el desarrollo financiero a la economía

---

## Desarrollo Financiero y PTF

### Imagen / gráfica

La diapositiva muestra un scatter plot que relaciona desarrollo financiero y productividad total de los factores.

El eje horizontal está etiquetado como **Domestic Credit to Private Sector (% of GDP, log scale)**. Tiene escala logarítmica y valores visibles aproximadamente desde 5 hasta 200.

El eje vertical está etiquetado como **Total Factor Productivity (USA = 1.00, log scale)**. También está en escala logarítmica y muestra valores aproximadamente entre 0.2 y 1.0.

Los puntos representan países, coloreados en varios grupos. Hay una línea punteada azul etiquetada como **Fitted Line (Log-Log Regression)**.

Visualmente, la nube de puntos tiene pendiente positiva: países con menor crédito doméstico al sector privado como porcentaje del PIB tienden a tener menor PTF relativa a Estados Unidos, mientras que países con mayor crédito privado tienden a ubicarse cerca de PTF más alta, alrededor de 0.8 a 1.0. Hay dispersión importante: algunos países con crédito relativamente alto tienen PTF menor, pero la tendencia general es ascendente.

**Interpretación contextual:** la figura motiva el modelo: el desarrollo financiero aparece asociado positivamente con la PTF agregada. La hipótesis del resto de las diapositivas es que, cuando hay fricciones financieras, el capital no necesariamente llega a los productores con mayor productividad, generando mala asignación y menor productividad agregada.

---

## Modelo

- Masa unitaria de empresarios que difieren en $(z,a)$ con medida $G(z,a)$.

- Tecnología de producción con rendimientos constantes:

$$
(zk)^\alpha l^{1-\alpha}
$$

- Masa $L$ de trabajadores ofrecen trabajo de manera inelástica

- Capital total

$$
K = \int a\,dG(z,a)
$$

- Restricción de endeudamiento $k(z,a) \leq \lambda a$ donde $\lambda \geq 1$.

---

## Optimización de la Firma: Beneficios y Demanda de Trabajo

El empresario $(z,a)$ resuelve:

$$
\max_{k \leq \lambda a,\, l} (zk)^\alpha l^{1-\alpha} - wl - rk
$$

**Paso 1: Demanda de trabajo.** CPO respecto a $l$:

$$
(1-\alpha)(zk)^\alpha l^{-\alpha} = w
\Longrightarrow
l^*(z,k) =
\left(\frac{1-\alpha}{w}\right)^{1/\alpha} zk
\equiv \theta(w)\cdot zk
$$

**Paso 2: Sustituir $l^*$.** Beneficios operativos como función de $k$:

$$
\Pi(z,k)
=
(zk)^\alpha [\theta(w)zk]^{1-\alpha}
- w\theta(w)zk - rk
$$

$$
=
\alpha \theta(w)^{1-\alpha}zk - rk
$$

$$
=
\pi(w)zk - rk
$$

donde

$$
\pi(w) \equiv \alpha\theta(w)^{1-\alpha}
=
\alpha
\left(\frac{1-\alpha}{w}\right)^{(1-\alpha)/\alpha}.
$$

---

## Equilibrio

- $(k(z,a), l(z,a), r, w)$ tal que:

  - $\int k(z,a)\,dG = K$ y $\int l(z,a)\,dG = L$

  - Maximización de beneficios: con rendimientos constantes, implica beneficios nulos o firma restringida por activos.

- El $z$ más bajo que es activo: $\Pi(z,k) = 0$ para todo $k$, por tanto

$$
\underline{z} = \frac{r}{\pi(w)}
$$

- La restricción de endeudamiento es vinculante para todos los demás $z$ activos.

- Usando la condicion de equilibrio del mercado:

$$
\lambda \int_{\underline{z}} a\,dG(z,a) = K
$$

determina $\underline{z}$ como función de $\lambda$ y la distribución de riqueza.

- 

$$
(1-\alpha)z^\alpha k^\alpha n^{-\alpha} = w
\Longrightarrow
n(z,a) = zk\theta(w) = \lambda az\theta(w)
$$

- 

$$
\lambda\theta(w)\int_{\underline{z}} az\,dG(z,a) = L
$$

---

## Productividad Agregada

- 

$$
\theta(w) =
\left(
\lambda \int_{\underline{z}} az\,dG(z,a)
\right)^{-1}L
$$

- Producto de la firma $(a,z)$:

$$
=
(z\lambda a)^\alpha n(z,a)^{1-\alpha}
=
\lambda za\theta(w)^{1-\alpha}
$$

- Producto agregado:

$$
Y
=
\left(
\lambda \int_{\underline{z}} az\,dG
\right)
\left[
\left(
\lambda \int_{\underline{z}} az\,dG(z,a)
\right)^{-1}L
\right]^{1-\alpha}
$$

$$
=
\left(
\frac{\lambda\int_{\underline{z}} az\,dG}{K}
\right)^\alpha
K^\alpha L^{1-\alpha}
$$

$$
=
\left(
\frac{\int_{\underline{z}} az\,dG}{A(\underline{z})}
\right)^\alpha
K^\alpha L^{1-\alpha}
$$

$$
A(\underline{z}) = \int_{\underline{z}} a\,dG(z,a)
= \text{riqueza de los productores activos.}
$$

- La Productividad Agregada es un promedio ponderado por riqueza de la productividad individual.

---

## Estática Comparativa

- Para un nivel fijo de activos, una mayor correlación con $z$:

  - Aumenta la demanda de trabajo

  - Eleva el salario de equilibrio

  - Eleva el umbral de productividad

  - Eleva la productividad agregada

---

## Dinámica – Decisión de Inversión

- Decisión de acumulación dinámica:

$$
v_t(z,a;\{w_t\},\{r_t\})
=
u(c) + \beta E v(z',a'|z)
$$

sujeto a:

$$
c + a' = \pi(z,a,w_t,r_t) + r_ta
$$

- La decisión de acumulación depende de la persistencia de la productividad

- Dos casos polares: persistencia total, donde $z_{it+1}=z_{it}$, e i.i.d.

---

## Ejemplo

- Utilidad lineal, persistencia total, sin endeudamiento

- Los beneficios son $zk\pi(w) - rk$ (tomamos $r=0$ para simplificar)

- Retorno marginal: $\beta z\pi(w_{t+1})$.

- Ahorra todos los activos si $\beta z\pi(w_{t+1}) > 1$. De lo contrario, ninguno.

- En el período $t$ hay un umbral $z(t)$ que depende de $w_{t+1}$

- Con el tiempo, la demanda de trabajo aumenta, por lo que $w_t$ sube y $z(t)$ decrece

- En el límite, solo la firma con el $z$ más alto produce.

- La TFP crece hasta ese punto.

---

## Dos tipos $z_L < z_H$

- $z \in \{z_L,z_H\}$, $z_L < z_H$, masas iguales $\mu$.

- Activos iniciales: $a_0(z_L) = a_0(z_H) = a_0$ (iguales)

---

## Fase 1: Ambos Tipos Acumulan

Supongamos que en $t=0$ el salario inicial $w_0$ es suficientemente bajo para que ambos tipos encuentren rentable ahorrar:

$$
\beta z_L \pi(w_0) > 1
$$

Entonces ambos tipos ahorran todo y los activos evolucionan según:

$$
a_{t+1}(z_i) = \beta z_i \pi(w_t)\cdot a_t(z_i)
$$

Como $z_H > z_L$, el tipo $H$ acumula más rápido. Después de $t$ períodos:

$$
\frac{a_t(z_H)}{a_t(z_L)}
=
\left(\frac{z_H}{z_L}\right)^t \cdot const
\longrightarrow \infty
$$

Equilibrio del mercado de trabajo en cada período:

$$
\theta(w_t)\cdot\mu
\left[
a_t(z_L)\cdot z_L + a_t(z_H)\cdot z_H
\right]
=
L
$$

la demanda de trabajo sube $\Rightarrow w_t$ sube con el tiempo.

---

## Disparador de Salida para el Tipo L

- Existe un período umbral $T$, el menor tal que:

$$
\beta z_L\pi(w_T) < 1
$$

- Para $t<T$: ambos tipos ahorran todo

- Para $t\geq T$: $\beta z_L\pi(w_t) < 1 \Rightarrow$ el tipo $L$ consume todos sus activos, sale permanentemente

- Una brecha mayor $z_H/z_L \Rightarrow$ desplazamiento más rápido de la riqueza hacia $H \Rightarrow$ salarios suben más rápido $\Rightarrow$ menor $T$.

---

## Fase 2: Solo el Tipo H Permanece

Para $t \geq T$, solo el tipo $H$ produce. La condicion de equilibrio del mercado de trabajo se simplifica a:

$$
\theta(w_t)\cdot\mu\cdot a_t(z_H)\cdot z_H = L
$$

Los activos del tipo $H$ continúan creciendo:

$$
a_{t+1}(z_H) = \beta z_H\pi(w_t)\cdot a_t(z_H)
$$

Este proceso continúa hasta que los salarios suben a $w^*$ que satisface:

$$
\beta z_H\pi(w^*) = 1
\Longleftrightarrow
\pi(w^*) = \frac{1}{\beta z_H}
$$

En ese punto el tipo $H$ también se vuelve indiferente y la economía alcanza el estado estacionario con:

$$
w^* = (1-\alpha)z_H
\left(\frac{K}{L}\right)^\alpha,
\qquad
K = \mu a^*(z_H)
$$

---

## TFP: Tres Fases

TFP agregada

$$
=
\left(
\frac{\int_{\underline{z}} az\,dG}{A(\underline{z})}
\right)^\alpha
\qquad
\text{donde }
A(\underline{z}) = \int_{\underline{z}} a\,dG.
$$

**Fase 1** $(t<T$, ambos tipos activos):

$$
TFP_t =
\left(
\frac{a_t(z_L)z_L + a_t(z_H)z_H}
{a_t(z_L)+a_t(z_H)}
\right)^\alpha
$$

Es un promedio ponderado por riqueza de $z_L$ y $z_H$, creciente con el tiempo a medida que el tipo $H$ gana peso.

**En $t=T$** (tipo $L$ sale): la TFP salta a

$$
TFP_T = z_H^\alpha
$$

Efecto selección puro: la riqueza de baja productividad se destruye.

**Fase 2** $(t>T)$: $TFP = z_H^\alpha$ — constante. Solo el stock de capital y los salarios se ajustan.

---

## TFP a lo Largo del Tiempo: Ilustración

### Imagen / gráfica

La diapositiva muestra un diagrama conceptual de la evolución de la TFP en el tiempo.

El eje horizontal es $t$ y el eje vertical es **TFP**. Hay tres niveles horizontales marcados con líneas punteadas:

- $z_L^\alpha$, el nivel bajo asociado al tipo de baja productividad.
- $\bar{z}_0^\alpha$, el nivel inicial intermedio.
- $z_H^\alpha$, el nivel alto asociado al tipo de alta productividad.

La curva azul empieza cerca de $\bar{z}_0^\alpha$ y crece suavemente durante la **Fase 1**. Esta parte está marcada con una flecha naranja llamada **reasignación**, indicando que la TFP sube porque la riqueza se va desplazando hacia los tipos de $z$ alto.

En el tiempo $T$, indicado con una línea vertical punteada, la curva da un salto discreto hacia el nivel $z_H^\alpha$. Ese salto está marcado en rojo como **selección**. Después de $T$, en la **Fase 2**, la curva azul queda plana en $z_H^\alpha$.

Texto de la diapositiva:

Las ganancias de TFP provienen de dos márgenes: (1) **reasignación** — la riqueza se desplaza hacia los tipos de $z$ alto durante la Fase 1; (2) **selección** — los tipos de $z$ bajo salen en $T$.

**Interpretación contextual:** la figura separa dos canales de mejora de productividad. Primero, sin que nadie salga, la riqueza se reasigna gradualmente hacia productores más productivos. Luego, cuando los productores de baja productividad dejan de operar, hay un salto adicional de selección. Después de eso la TFP queda constante, aunque el capital y los salarios todavía puedan ajustarse.

---

## Descomposición de la Ganancia de TFP

Ganancia total de TFP de $t=0$ al estado estacionario:

$$
\frac{TFP_{SS}}{TFP_0}
=
\frac{z_H^\alpha}{\bar{z}_0^\alpha}
\qquad
\text{donde }
\bar{z}_0 = \frac{z_L + z_H}{2}
$$

**Descomposición:**

$$
\underbrace{
\frac{z_H^\alpha}{\bar{z}_0^\alpha}
}_{\text{ganancia total}}
=
\underbrace{
\frac{\tilde{z}_T^\alpha}{\bar{z}_0^\alpha}
}_{\text{reasignación Fase 1}}
\times
\underbrace{
\frac{z_H^\alpha}{\tilde{z}_T^\alpha}
}_{\text{salto en } T \text{ (selección)}}
$$

donde $\tilde{z}_T$ es el promedio ponderado por riqueza justo antes de la salida.

**Estática comparada:**

- Mayor $z_H/z_L \Rightarrow$ mayor ganancia total de TFP, salida más temprana, mayor salto de selección

- Mayor $\lambda > 1 \Rightarrow$ reasignación más rápida, menor $T$, misma TFP de largo plazo

- Con Pareto $\psi(z)$: un continuo de eventos de selección reemplaza el salto único en $T$

---

## Conexión con los Resultados Generales

### Idea clave

El modelo de dos tipos explicita lo que Moll (2014) establece en general: las **pérdidas de TFP por fricciones financieras** surgen porque la riqueza está mal asignada, alejándose de los productores de $z$ alto.

**Los dos mecanismos se corresponden directamente con el modelo general:**

|  | Modelo de dos tipos | Moll general |
|---|---|---|
| Fase 1 | Riqueza $\rightarrow z_H$ | $\int az\,dG/A(\bar{z})$ creciente |
| Salida en $T$ | Salto de selección discreto | Selección gradual (Pareto) |
| Fase 2 | TFP constante, $K$ crece | Acumulación estándar |
| Persistencia | Total ($z$ fijo) | Determina velocidad Fase 1 |

**Con shocks i.i.d.:** no hay vínculo sistemático entre $z$ y $a \Rightarrow$ no hay reasignación en la Fase 1 $\Rightarrow$ la TFP permanece plana en su bajo nivel inicial.

---

## Dinámica y Estado Estacionario

- Supone preferencias

$$
E\sum \beta^t \ln c_t
$$

- Esto implica

  - 

$$
c(z,a) = (1-\beta)za\pi(w)
$$

  - Activos del período siguiente:

$$
\tilde{a}(z,a) = \beta za\pi(w)
$$

- Mayor $z$ hoy implica mayores activos en el futuro

- Con depreciación se obtiene

$$
c(z,a) = (1-\beta)(z\pi(w)-\delta)a
$$

---

## Derivaciones

$$
v(z,a) = \max \ln(c) + \beta E v(z', za\pi(w)-c)
$$

Propongamos que la función de valor tiene la forma $v(z) + B\ln a$ y el consumo es lineal en $a$. Verificar:

$$
v(z) + B\ln a
=
\ln(c(z)a)
+
\beta E
\left[
v(z') + B\ln(za\pi(w)) - c(z)a
\right]
$$

Esto implica que $B = 1 + \beta B$, por tanto

$$
B = \frac{1}{1-\beta}.
$$

Resolver para el consumo:

$$
\frac{1}{c_t}
=
\beta B \frac{1}{a_{t+1}}
$$

Esto implica

$$
c_t = (\beta B)^{-1}a_{t+1}
=
(\beta B)^{-1}(za\pi(w)-c_t)
$$

Por tanto

$$
c_t =
\frac{1/\beta B}{1+1/\beta B}za\pi(w)
=
(1-\beta)za\pi(w)
$$

y

$$
a_{t+1} = \beta za\pi(w).
$$

---

## Persistencia y Estado Estacionario

- Caso de persistencia total: $z_{t+1}=z_t$

- Solo $\max\{z\}$ producirá.

- Cuando $w$ alcanza el punto donde $\beta z_{max}a\pi(w)=a$, entonces $z_{max}$ mantendrá los mismos activos

- Todo $z<z_{max}$ agotará sus activos.

- En el largo plazo debe cumplirse la condición anterior (i.e. $\pi(w)=1/\beta z_{max}$) y

$$
w = (1-\alpha)z_{max}\left(\frac{K}{L}\right)^\alpha
$$

determina el nivel de activos $a=K$.

### Ejercicio

Resuelva la evolución dinámica con una distribución Pareto de shocks (¡sin estado estacionario!).

---

## Caso sin Persistencia

- Suponga que los shocks son i.i.d. y la firma invierte antes de conocer el $z$ del período siguiente

- El consumo/ahorro sigue una regla de decisión lineal similar.

- La riqueza de un agente depende de la distribución pasada de shocks $z_{it}$

- Pero el shock actual es independiente de la riqueza.

- La distribución conjunta de riqueza/shocks es

$$
G(a,z) = \omega(a)\psi(z)
$$

- 

$$
\beta z_i a_{it}\pi(w) = a_{it+1}
$$

- Condición de estado estacionario: $\beta Eza\pi(w)=a$, por tanto

$$
\pi(w)=\frac{1}{\beta Ez}
$$

determina $w$.

---

## Distribución Estacionaria de Riqueza

- La riqueza del agente individual es estocástica, pero la distribución $\omega(a)$ es estacionaria.

- $\underline{z} = z_{min}$ (todos producen porque no hay alternativa)

$$
TFP =
\left(
\frac{
\int_{\underline{z}} az\,\omega(da)\psi(dz)
}
{A(\underline{z})}
\right)^\alpha
$$

- Sin asociación entre riqueza y productividad, por tanto menor TFP

- La TFP no cambia a lo largo de la senda de ajuste.

---

## Extensiones

- Los resultados se mantienen con depreciación, función de utilidad CRRA y $\lambda > 1$

- Idea general: shocks más persistentes implican mayor TFP en el largo plazo pero una senda de ajuste más lenta

- Ha sido utilizado como motivación para las sendas de transición lentas

- Mayor $\lambda$ implica una transición más rápida y mayor asociación

---

## Distribuciones de Riqueza

### Imagen / gráfica

La diapositiva muestra cuatro paneles pequeños, organizados en una cuadrícula de 2 por 2, bajo el título **Distribuciones de Riqueza**.

Cada panel compara dos distribuciones sobre el eje horizontal $z$:

- Línea azul punteada: $\psi(z)$, la distribución de productividad.
- Línea roja sólida: $\omega(z)$, las participaciones de riqueza.

Los paneles están titulados según distintos niveles de correlación/autocorrelación:

- **(a) Corr = 0.5**
- **(b) Corr = 0.8**
- **(c) Corr = 0.95**
- **(d) Corr = 0.99**

En el panel (a), las curvas azul y roja son muy parecidas: la riqueza está distribuida de forma cercana a la distribución de productividad. En el panel (b), la curva roja empieza a desplazarse hacia la derecha, indicando más riqueza concentrada en niveles de productividad mayores. En el panel (c), la diferencia es más clara: la distribución de productividad azul está concentrada más cerca de valores bajos de $z$, mientras la riqueza roja tiene más masa hacia valores medios y altos. En el panel (d), la riqueza roja está fuertemente desplazada hacia la derecha, con mucha más masa en empresarios de productividad alta.

Texto visible bajo la figura:

**Fig. 1: Wealth Shares and Autocorrelation**

**Note:** The dashed lines are the productivity distribution $\psi(z)$ from (27). The solid lines are the wealth shares $\omega_t(z)$, i.e. the solution to (22) for the stochastic process (26). As persistence $\theta$ (equivalently autocorrelation) increases, wealth becomes more concentrated with high productivity entrepreneurs.

**Interpretación contextual:** la figura muestra que, cuando la productividad es más persistente, la riqueza se concentra más en los productores de alta productividad. Esto mejora la asignación de capital porque quienes tienen buenas oportunidades productivas también acumulan más riqueza y pueden financiar más capital. Con baja autocorrelación, riqueza y productividad se parecen menos alineadas.

---

## TFP y Autocorrelación

### Imagen / gráfica

La diapositiva muestra dos gráficos lado a lado.

### Gráfico izquierdo

El eje horizontal es $\lambda$, con valores de 1 a 10. El eje vertical es **TFP**, con valores aproximadamente entre 0.65 y 1.

Hay cuatro curvas crecientes etiquetadas por correlación:

- **Corr = 0**: curva baja que crece desde alrededor de 0.65 hasta alrededor de 0.90.
- **Corr = .5**: curva similar, algo por encima de Corr = 0 para buena parte del rango.
- **Corr = .9**: curva más alta, que crece desde alrededor de 0.72 hasta más de 0.90.
- **Corr = .99**: curva superior, que empieza cerca de 0.84 y se acerca a 0.97.

Visualmente, mayor $\lambda$ aumenta la TFP, y mayor autocorrelación también eleva el nivel de TFP.

### Gráfico derecho

El eje horizontal es **Years**, con valores de 0 a 30. El eje vertical muestra TFP. El título interno del panel es **(a) TFP**.

Hay tres curvas:

- **Corr = 0**: línea horizontal alrededor de 0.66; no hay transición visible.
- **Corr = .85**: curva verde que sube rápidamente al principio y converge cerca de 0.72.
- **Corr = .97**: curva roja que sube de forma más lenta pero alcanza un nivel mucho más alto, cerca de 0.80.

**Interpretación contextual:** los gráficos resumen la intuición dinámica de Moll. Un mayor desarrollo financiero, capturado por $\lambda$, permite reasignar capital hacia productores más productivos y eleva la TFP. Pero la persistencia de los shocks de productividad también importa: si la productividad es persistente, la riqueza se va asociando con alta productividad y la TFP de largo plazo es mayor. Al mismo tiempo, una mayor persistencia puede generar transiciones más lentas: la economía tarda más en reasignar riqueza, aunque el destino final sea mejor.