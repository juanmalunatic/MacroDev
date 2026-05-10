# Big Push in Distorted Economies

Paco Buera$^1$ Hugo Hopenhayn$^2$ Yongs Shin$^{1,3}$ Nico Trachter$^4$

$^1$Washington University in St. Louis

$^2$University of California–Los Angeles

$^3$Federal Reserve Bank of St. Louis

$^4$Federal Reserve Bank of Richmond

October 2024

The views expressed herein are those of the authors and do not necessarily represent the views of the Federal Reserve Banks of Richmond and St. Louis or the Federal Reserve System.

---

## Motivation

- Large income per capita differences across countries

- “Explained” by productivity differences

- Large differences in the size of establishments/firms

  (Hsieh/Klenow, Bento/Restuccia)

- Two views

  1. Barriers to technology adoption, distortions $\Longrightarrow$ Requires large distortions

     (Parente/Prescott, Restuccia/Rogerson, Hsieh/Klenow)

  2. Complementarities, coordination failures

     (Rosenstein-Rodan, Hirschman, Murphy/Shleifer/Vishny)

- In this paper, we integrate these views

We study how complementarities amplify distortions $\Longrightarrow$ small distortions can have large effects $\Longrightarrow$ **BIG PUSH**

---

## Road Map

1. Model of firm entry, technology adoption, input-output linkage, idiosyncratic distortions

   - Standard model of firm entry and technology adoption

   - Elements of Murphy et al. (1989), Matsuyama (1995), Ciccone (2002), Jones (2011), Guner, Bhattacharya, Ventura (2013), Bento and Restuccia (2017).

2. Quantitative exploration

   - Guided by aggregate and microdata from the US and India

3. Can there be large effects of distortions and policies? **YES**, in Big Push region, without multiple equilibria

4. Can development be a story of multiple equilibria? **NO**, but possible in highly distorted economies

---

## Model Economy: Summary

- Ex-ante heterogeneous potential entrants, $z \sim F(z)$

- Monopolistically competitive, differentiated goods

- Idiosyncratic correlated distortions, $\tau(z) = 1 - \tau z^{-\xi}$

- Labor cost of entry, labor and goods cost of adoption

- Produce using labor and intermediate inputs

---

## Intermediate Aggregate/Final Good Producers

- CRS technology using differentiated intermediates $j \in [0,1]$

$$
X =
\left[
\int y(j)^{\frac{\eta-1}{\eta}}\,dj
\right]^{\frac{\eta}{\eta-1}}
$$

- Used for final consumption, intermediate inputs, and for adoption investment

$$
C + \int x(j)\,dj + \# \text{ of adopters} \times \kappa_a = X
$$

---

## Intermediate Good Producers

CRS technologies $i \in \{t,m\}$

$$
y = f_i(z,x,l)
=
z
\underbrace{
\frac{A_i}{\nu_i^{\nu_i}(1-\nu_i)^{1-\nu_i}}
}_{\bar{A}_i}
x^{\nu_i}
l^{1-\nu_i},
\qquad
\bar{A}_t < \bar{A}_m,\quad \nu_t \leq \nu_m
$$

- $z$: heterogeneous productivity

- $x$: intermediate input

- $l$: labor input

- $m$: Modern, $A_m$, labor entry costs $\kappa_e$, goods costs of adoption $\kappa_a$

- $t$: Traditional, $A_t$, only labor entry cost $\kappa_e$

---

## Distortions

- Tax on revenues

- Net revenues:

$$
\tau(z;\xi)^{-1}p_iq_i
$$

- Correlation increasing with $\xi$

- Special case: $\tau z^\xi$

---

## Intermediate Good Producers’ Problem

Monopolistically Competitive Producers

$$
\pi_i^o(z)
=
\max_{p,x,l}
\underbrace{
\tau(z;\xi)^{-1}
p
\left(
\frac{P}{p}
\right)^\eta
X
}_{q}
-
Px
-
wl
$$

s.t.

$$
f_i(z,x,l) \geq q.
$$

---

## Equilibrium: $P$, $w$, $z_e$ and $z_a$ such that

The marginal entrant $z_e$

$$
\pi_t^o(z_e) = w\kappa_e;
$$

The marginal adopter $z_a$

$$
\pi_m^o(z_a) - \pi_t^o(z_a) = P\kappa_a;
$$

Labor market clearing

$$
\int_{z_e}^{z_a} l_t(z)\,dF(z)
+
\int_{z_a}^{\infty} l_m(z)\,dF(z)
=
L - (1-F(z_e))\kappa_e
$$

The price of the intermediate aggregate

$$
P =
\left[
\int_{z_e}^{z_a} p_t(z)^{1-\eta}\,dF(z)
+
\int_{z_a}^{\infty} p_m(z)^{1-\eta}\,dF(z)
\right]^{\frac{1}{1-\eta}}
$$

---

## Distortions and Amplification

### Imagen / diagrama

La diapositiva muestra un diagrama de bloques con fondo blanco y cajas celestes.

Hay cuatro bloques principales:

1. Arriba al centro: **Distortions (higher $\xi$)**.
2. En el centro: **Aggregate Productivity Lower**.
3. Abajo al centro: **Adoption (a) Lower**.
4. A la derecha: **Consumption Lower**.

Las flechas principales indican:

- **Distortions (higher $\xi$)** $\downarrow$ **Aggregate Productivity Lower**.
- **Aggregate Productivity Lower** $\downarrow$ **Adoption (a) Lower**.
- **Aggregate Productivity Lower** $\dashrightarrow$ **Consumption Lower**.
- Hay una flecha curva punteada desde **Adoption (a) Lower** hacia **Aggregate Productivity Lower**, etiquetada como **Amplification**.
- También aparece una gran flecha curva punteada del lado izquierdo, sugiriendo retroalimentación general entre distorsiones, adopción y productividad.

**Interpretación contextual:** el diagrama resume el mecanismo central del paper. Una mayor distorsión reduce la productividad agregada; al caer la productividad, se reducen los incentivos o la capacidad de adoptar tecnología moderna; al caer la adopción, la productividad agregada cae aún más. Ese feedback amplifica el efecto inicial de las distorsiones.

---

## Productivity, Output and Prices

How do distortions and adoption affect Productivity, Output and Prices

- Average distortions:

$$
\bar{\tau}
=
\int \tau(z;\xi)\omega(z)\,dz
$$

$$
\to \text{ Aggregate markup: }
\mathcal{M}
=
\left(
\frac{\eta}{\eta-1}
\right)\bar{\tau}
$$

- Productivity:

$$
Z
\equiv
\left\{
\int
\left[
\frac{\bar{\tau}}{\tau(z;\xi)}
\right]^\eta
[A(z)z]^{\eta-1}
f(z)\,dz
\right\}^{\frac{1}{\eta-1}}
$$

- Aggregate Price:

$$
P
=
\mathcal{M}^{\frac{1}{1-\nu}}
Z^{-\frac{1}{1-\nu}}
$$

- Output:

$$
\mathcal{M}^{-\frac{\nu}{1-\nu}}
Z^{\frac{1}{1-\nu}}
(1-\nu)^{-1}L
$$

---

## Distortions and Productivity

### Imagen / diagrama

La diapositiva enfoca el vínculo entre distorsiones y productividad. Mantiene el diagrama de cajas, pero atenúa visualmente los bloques de adopción y consumo.

El bloque superior dice:

**Distortions (higher $\xi$)**

y apunta hacia:

**Aggregate Productivity Lower**

A la derecha aparece una fórmula:

$$
\frac{d\ln Z}{d\xi}\bigg|_a
=
\eta
\int
[1-\tau(z;\xi)/\bar{\tau}]
\omega(z)\ln(z)f(z)\,dz
$$

Junto a la fórmula aparecen dos bullets:

- **Positive**
- **Increasing in $\xi$**

**Interpretación contextual:** la diapositiva separa el efecto directo de las distorsiones sobre la productividad, manteniendo fija la adopción. Si las distorsiones están correlacionadas con productividad, las firmas más productivas enfrentan más fricción, lo que reduce $Z$. El efecto es positivo en magnitud y aumenta con $\xi$.

---

## Productivity and Consumption

### Imagen / diagrama

La diapositiva mantiene el mismo esquema, pero ahora destaca la relación entre **Aggregate Productivity Lower** y **Consumption Lower**.

El bloque de distorsiones está atenuado arriba. El bloque central **Aggregate Productivity Lower** está resaltado, y de él sale una flecha punteada hacia la derecha, hacia **Consumption Lower**.

Sobre la flecha aparece:

$$
\frac{1}{1-\nu}
$$

**Interpretación contextual:** una caída de productividad agregada reduce el consumo. El factor $\frac{1}{1-\nu}$ indica que, por la presencia de bienes intermedios, una caída de productividad puede tener un efecto amplificado sobre el consumo/output agregado: cuanto mayor sea la participación de intermediarios $\nu$, mayor el multiplicador.

---

## Productivity and Adoption

When Productivity increases:

1. Price index falls ($\downarrow P$)

2. Demand for its output increases

3. Intermediate input becomes cheaper

4. Adoption cost falls

If $2+3+4$ stronger than $1$, gains from adoption increase

Necessary and sufficient condition:

$$
(\eta-1)(1-\nu) < 1
$$

- Differentiated goods less substitutable (small $\eta$)

- Higher share of intermediates (large $\nu$)

- Higher intermediate input intensity of the modern technology $(\nu_m > \nu_t)$

---

## Incentives for Adoption

Net gains from adoption:

$$
D(z,\theta)
\equiv
\pi_m^o(z;\theta)
-
\pi_t^o(z;\theta)
-
P(\theta)\kappa_a
$$

where $\theta \in \{Z,\xi,a\}$ where $a$: fraction of adopters

- Adoption threshold $z_a$ where $D(z_a,\theta)=0$

- Equivalently:

$$
\Delta\pi(z_a,\theta)
\equiv
\frac{
\pi_m^o(z;\theta)-\pi_t^o(z;\theta)
}{
P(\theta)\kappa_a
}
=
1
$$

Fraction of adopters

$$
a = 1-F(z_a)
$$

---

## Determinants of Adoption

Equilibrium “best response” mapping

$$
T(a)
=
\{a' \mid a' = (1-F(z_a)) \text{ and } D(z_a;a)=0\}
$$

Impact of changes in adoption incentives:

$$
\text{Amplification}
=
\frac{\text{Total}}{\text{Direct}}
=
\frac{1}{1-T'(a)}
$$

### Imagen / diagrama

La diapositiva incluye un pequeño diagrama de plano cartesiano. El eje horizontal representa $a$ y el eje vertical representa $a'$. Aparece una curva creciente de best response $T(a)$ y una línea de 45 grados. La distancia inicial representa el efecto directo de un cambio de incentivos, y el movimiento a lo largo de la curva muestra el efecto total después de la retroalimentación.

**Interpretación contextual:** la fórmula muestra que, si la adopción genera feedback positivo, un shock directo se amplifica. Cuanto más cerca esté $T'(a)$ de 1, mayor es el multiplicador. Si $T'(a)$ es bajo, el efecto total se parece al efecto directo.

---

## Amplification & Multiplicity

### Direct and Total Effect

### Imagen / diagrama

La diapositiva muestra un gráfico de best response con una curva creciente y una línea de 45 grados. El gráfico ilustra cómo un cambio directo puede generar un cambio total mayor cuando hay retroalimentación positiva.

- Even without multiplicity, amplification could be strong, the steeper the slope $T'(a) \in (0,1)$

**Interpretación contextual:** la clave es que no se necesitan múltiples equilibrios para tener grandes efectos. Basta con que la curva de adopción responda fuertemente a la adopción agregada, pero sin superar la pendiente de 1.

---

## Amplification & Multiplicity

### Direct and Total Effect Multiple Equilibria

### Imagen / diagrama

La diapositiva agrega un segundo gráfico al lado derecho, etiquetado como **Multiple Equilibria**.

- En el gráfico izquierdo, la curva de best response cruza una vez la línea de 45 grados: hay un único equilibrio, pero puede haber amplificación.
- En el gráfico derecho, la curva tiene forma más empinada o en S, cruzando la línea de 45 grados más de una vez: hay múltiples equilibrios.

- Even without multiplicity, amplification could be strong, the steeper the slope $T'(a) \in (0,1)$

- Multiplicity requires $T'(a)>1$

**Interpretación contextual:** la diapositiva distingue amplificación de multiplicidad. El paper enfatiza que puede haber efectos de Big Push sin múltiples equilibrios; múltiples equilibrios requieren una pendiente aún más fuerte de la best response.

---

## Incentives and adoption

$$
\frac{dT(a,\xi)}{d\theta}
=
\underbrace{
\frac{d\ln\Delta\pi(z_a)}{d\theta}
}_{\text{Incentive Effect}}
\underbrace{
\frac{da'}{d\ln\Delta\pi(z_a)}
}_{\text{Sensitivity}}
\tag{1}
$$

- Incentive: effect of change in mass of adopters on net gains from adoption for marginal adopter

- Sensitivity: effect of change in net gains of adoption on identity of marginal adopter

  - $\uparrow \eta$: $\uparrow$ demand elast. $\Rightarrow$ higher reaction to own $z$ $\Rightarrow \downarrow T'(a)$

  - Higher feedback when distortions $\xi$ are higher

  - $\zeta$ translates the change in $z_a$ to the adoption rate

  - higher difference $\nu_m-\nu_t$

---

## Productivity and Adoption

### Imagen / diagrama

La diapositiva resalta el vínculo entre productividad y adopción dentro del diagrama de bloques.

El bloque central **Aggregate Productivity Lower** apunta hacia abajo al bloque **Adoption (a) Lower**. A la izquierda de esa flecha aparece el texto:

**Incentive + Sensitivity**

Los bloques de distorsiones y consumo aparecen atenuados, mientras que productividad y adopción están resaltados.

**Interpretación contextual:** esta diapositiva explica que la caída de productividad reduce la adopción mediante dos componentes: el cambio en incentivos netos de adoptar y la sensibilidad de la frontera de adopción ante esos incentivos.

---

## Productivity and Adoption

### Imagen / diagrama

La diapositiva repite el diagrama anterior y agrega una anotación en rojo junto a la flecha de productividad hacia adopción:

**Stronger when:**

- **When adoption uses goods.**

- **When modern technology is less labor intensive**

**Interpretación contextual:** la retroalimentación productividad-adopción es más fuerte cuando adoptar requiere bienes/intermedios y cuando la tecnología moderna usa relativamente menos trabajo. En esos casos, una caída en productividad y un aumento en el precio relativo de bienes afectan más el costo efectivo de adoptar.

---

## Distortions and Adoption: Direct Effect

### Imagen / diagrama

La diapositiva muestra el diagrama completo con foco en el efecto directo de distorsiones sobre adopción.

A la izquierda aparecen dos componentes:

### Incentive

$$
\frac{\delta \tau(z_a,\xi)}{\delta \xi}
-
\frac{\delta \ln \bar{\tau}}{\delta \xi}
$$

Nota amarilla:

**Lowers Adoption Incentives when $a$ is smaller**

### Sensitivity

$$
\{\eta[1-\xi]-1\}^{-1}\zeta a
$$

Nota amarilla:

**Feedback: stronger when $\hat{a}$ is larger smaller when $a$ is smaller**

En el centro se ven las cajas:

- **Distortions (higher $\xi$)**
- **Aggregate Productivity Lower**
- **Adoption (a) Lower**
- **Consumption Lower**

**Interpretación contextual:** la diapositiva separa el efecto directo de una mayor distorsión sobre la adopción en dos partes: cuánto cambian los incentivos del adoptante marginal y cuánto se mueve la frontera de adopción cuando cambian esos incentivos.

---

## Amplification

### Imagen / diagrama

La diapositiva muestra el diagrama completo de amplificación.

Bloques principales:

- **Distortions (higher $\xi$)** arriba.
- **Aggregate Productivity Lower** al centro.
- **Adoption (a) Lower** abajo.
- **Consumption Lower** a la derecha.

Hay una flecha curva punteada entre adopción y productividad etiquetada **Amplification**.

A la izquierda, en rojo:

**Stronger when:**

- **When adoption uses goods.**
- **When modern technology is less labor intensive**

A la derecha, en rojo, bajo el título **Direct + Reallocation**:

- **Direct Effect (negative)**
- **Reallocation: Negative when adoption is low, positive when high**
- **Total effect gets very negative as $a$ gets small**

**Interpretación contextual:** la diapositiva combina todos los canales. Las distorsiones reducen productividad y adopción; la caída de adopción retroalimenta la productividad. Además, el efecto de reasignación puede cambiar de signo según el nivel inicial de adopción, pero cuando la adopción es baja el efecto total se vuelve muy negativo.

---

## Quantitative Exploration

1. Parameterize the model with US plant/firm level data

2. Choose idiosyncratic distortions to match data from India

3. Explore how complementarities amplify distortions and policies

4. Explore set of equilibria, in the calibrations and more broadly

5. Quantify the role of coordination failures on GDP

---

## Parameterization

$$
(A_m,\eta,\nu_t,\nu_m,\zeta,A_t,\kappa_e,\kappa_a,\xi)
$$

- $A_m$ normalized to 1

- $\eta = 3$, comparison w/ Hsieh & Klenow (2009)

- $(\nu_t,\nu_m)$ jointly determine aggregate share of intermediate goods.

  - $\nu_t = 0$, traditional technology labor only

- $\xi$ assumed zero in the US

- $(\zeta,A_t,\kappa_e,\kappa_a,\xi)$ chosen to match size distribution

- Point identification with data on the size distribution of firms

- Key identification assumption: both technologies are observed in equilibrium

---

## Identification: given $\eta$, $\nu_t=\nu_m$, and $\xi=0$

Figure: Identification from the establishment size distribution

$$
\log l^t
=
\log[(\eta-1)(1-\nu)\kappa_e]
-
\frac{\zeta}{\eta-1}\log \bar{l}^t
$$

$$
\log l_m
$$

$$
-\zeta\log\frac{z_a}{z_e}
$$

$$
(\eta-1)\log\frac{A_m}{A_t}
$$

### Imagen / diagrama

La diapositiva muestra un esquema en escala log-log de la distribución acumulada de tamaños de establecimiento. El eje horizontal es $\log l$ y el eje vertical es **log fraction w/ emp. $\geq l$**.

El diagrama marca dos segmentos o colas de la distribución:

- Una parte asociada a establecimientos tradicionales.
- Una parte asociada a establecimientos modernos.

La pendiente de la cola está relacionada con $\zeta/(\eta-1)$. La distancia horizontal/vertical entre tramos se usa para identificar el umbral de adopción $z_a/z_e$ y la brecha tecnológica $A_m/A_t$.

**Interpretación contextual:** la distribución de tamaños revela información sobre la productividad subyacente, la tecnología moderna y tradicional, y los costos/umbrales de entrada y adopción. La identificación usa la forma de la cola y los cambios de pendiente/nivel en la distribución.

---

## Parameterization

- Obtain $\zeta = 2.4$ (Pareto tail) and $\nu_m = 0.7$, $A_t/A_m = 0.43$

$$
y
=
z
\frac{A_i}{\nu_i^{\nu_i}(1-\nu_i)^{1-\nu_i}}
x^{\nu_i}
l^{1-\nu_i},
\qquad
i=t,m
$$

- Average est. size: 19 employees; 50% of entrants adopt

- We use eight moments of the establishment size distribution: the average size and the size of the establishments in the 10th, 25th, 50th, 75th, 90th, 99th, and 99.9th percentiles.

### Imagen / gráfica

La diapositiva incluye una gráfica log-log de distribución de tamaños de establecimientos.

Eje horizontal: $s=\text{Employment}$, con escala logarítmica de aproximadamente 1 a 10,000.

Eje vertical: **Fraction of establishments with employment $\geq s$**, también en escala logarítmica, desde cerca de 1 hasta $10^{-5}$.

La línea azul representa **Model** y los círculos naranjas representan **U.S. BDS 2007**. La línea del modelo sigue de cerca los puntos de datos, especialmente en la cola de la distribución. La relación es aproximadamente lineal en escala log-log, consistente con una cola Pareto.

**Interpretación contextual:** el ajuste muestra que la parametrización del modelo puede reproducir la distribución de tamaños de firmas en Estados Unidos, usando la cola Pareto y la estructura de tecnologías tradicional/moderna.

---

## Impact of Idiosyncratic Distortions

### Imagen / gráfica

La diapositiva muestra una curva azul de **Normalized Consumption** contra **Distortions, $\xi$**.

Eje horizontal: $\xi$, desde 0 hasta 0.5.

Eje vertical: consumo normalizado, en escala logarítmica, desde aproximadamente 0.1 hasta 1.

La curva empieza cerca de 1 cuando $\xi=0$, cae lentamente al principio, luego tiene una caída muy pronunciada alrededor de $\xi\approx 0.18$-$0.22$, y después sigue cayendo más suavemente. Hay una línea vertical punteada etiquetada:

$$
\xi = 0.195
$$

La leyenda indica:

- **U.S. Calibration**
- $\xi = 0.195$

**Interpretación contextual:** la figura muestra una región de Big Push: cerca del valor de distorsiones asociado a India, pequeños cambios en $\xi$ pueden generar grandes cambios en consumo agregado. El efecto no es lineal.

---

## Impact of Idiosyncratic Distortions I

Starting from the US $(\xi=0)$

### Consumption

### Adoption

- Locally nonlinear effect in the benchmark (Big Push region)

- Adoption costs increase endogenously

- More entry but lower adoption rates

### Average Size

### Imagen / gráficas

La diapositiva muestra dos gráficos principales.

### Gráfico izquierdo: Consumption

Eje horizontal: **Distortions, $\xi$**.  
Eje vertical: **Normalized Consumption**.

Hay varias curvas:

- **Baseline**: curva azul con caída muy fuerte alrededor de $\xi\approx 0.2$.
- Curvas contrafactuales punteadas o de otros colores, incluyendo casos con $\nu_m=\nu_t=0.69$ y/o **no adoption**, y un caso con $\nu_m=\nu_t=0$.

Visualmente, la curva baseline es la más no lineal: muestra un desplome abrupto. Las curvas sin adopción o con tecnologías más similares caen mucho más gradualmente.

### Gráfico derecho: Adoption

Eje horizontal: **Distortions, $\xi$**.  
Eje vertical: **Fraction of Adopters**.

La curva baseline empieza cerca de 0.5, sube ligeramente al comienzo, y luego cae abruptamente hasta casi 0 cerca de $\xi\approx 0.2$. Las curvas sin adopción permanecen en cero. Otros contrafactuales muestran caídas más suaves.

**Interpretación contextual:** la caída fuerte de consumo coincide con el colapso de la adopción. Esto evidencia el mecanismo de amplificación: las distorsiones reducen la adopción, y la menor adopción reduce productividad/consumo de forma desproporcionada.

---

## Impact of Idiosyncratic Distortions II

Starting from the US $(\xi=0)$

### Consumption

### Adoption

### Imagen / gráficas

La diapositiva muestra nuevamente dos gráficos.

### Gráfico izquierdo: Consumption

Compara tres curvas:

- **Baseline**: caída abrupta alrededor de $\xi\approx 0.2$.
- Una curva con $\eta=10$.
- Una curva con $\nu_m=\nu_t=0.69$.

La curva baseline cae primero y de forma más pronunciada. La curva con mayor $\eta$ cae más suavemente al principio, pero luego también baja. La curva con igual participación de intermedios se mantiene relativamente más alta por más tiempo y luego cae.

### Gráfico derecho: Adoption

Muestra la fracción de adoptantes para las mismas configuraciones. En baseline, la adopción cae a cero más temprano. En las otras configuraciones, la adopción disminuye más gradualmente y colapsa más tarde o de manera menos abrupta.

**Interpretación contextual:** los parámetros que gobiernan sustitución y uso de intermediarios modifican la fuerza de la complementariedad. La región de Big Push depende de cuán fuerte sea el feedback entre productividad, costos de adopción y adopción agregada.

---

## Gap between the US and India

- Assume the only difference for India is idiosyncratic distortions, pinned down by the tail of est. size distribution $(\xi=0.195)$

- Adoption cost endogenously up by 30%

- Setting $\xi=0 \Rightarrow$ Aggregate consumption jumps by 144%

- Small reform can have disproportionate effects

- No multiplicity

### Imagen / gráfica

La diapositiva muestra la misma curva de **Normalized Consumption** contra **Distortions, $\xi$**. La curva tiene un tramo de caída muy pronunciado cerca de $\xi=0.195$, marcado por una línea vertical punteada.

**Interpretación contextual:** el valor calibrado para India cae justo en la región donde la curva es muy empinada. Por eso una reducción relativamente pequeña en distorsiones puede generar un aumento grande de consumo agregado, aun sin múltiples equilibrios.

---

## Understanding the Gap

| Case In Model | Relative Cons |
|---|---:|
| Benchmark | 0.41 |
| Labor innovation cost $\gamma=0$ | 0.49 |
| Same intermediate good share $\nu_t=\nu_m$ | 0.62 |
| Jones $\nu_t=\nu_m$, adopt | 0.63 |
| Bento & Restuccia $\nu=0$, $\gamma=0$ | 0.85 |
| Restuccia & Rogerson $\nu=0$, adopt | 0.86 |

(Consumption with $\xi=0.195$ over consumption with $\xi=0$)

---

## Full parameterization for India

### Imagen / gráficas

La diapositiva compara dos distribuciones de tamaño de establecimientos.

### Panel izquierdo: US

Eje horizontal: $s=\text{Employment}$ en escala log.  
Eje vertical: **Fraction of establishments with employment $\geq s$** en escala log.

La línea azul del modelo ajusta los puntos naranjas **U.S. BDS 2007**. La distribución tiene una cola larga y establecimientos relativamente grandes.

### Panel derecho: India, Economic Census

Eje horizontal y vertical iguales. La línea azul del modelo ajusta los puntos naranjas **EC 2005**. La distribución cae más rápido y muestra establecimientos mucho más pequeños que en Estados Unidos.

Texto de la diapositiva:

India parameterization:

- higher $\kappa_a$ (and $\xi$),

- lower $A_t$

**Interpretación contextual:** para ajustar India no basta con cambiar $\xi$; la parametrización completa también usa un mayor costo de adopción y una menor productividad de la tecnología tradicional. Esto genera una distribución de establecimientos más pequeña y menor adopción moderna.

---

## Understanding the Gap

| Case In Model | Relative Cons |
|---|---:|
| Full India | 0.15 |
| Benchmark | 0.41 |
| Labor innovation cost $\gamma=0$ | 0.49 |
| Same intermediate good share $\nu_t=\nu_m$ | 0.62 |
| Jones $\nu_t=\nu_m$, n/adopt | 0.63 |
| Bento & Restuccia $\nu=0$, $\gamma=0$ | 0.85 |
| Restuccia & Rogerson $\nu=0$, n/adopt | 0.86 |

---

## The Korean Economic Miracle

- Is our model able to explain a miracle where others failed?

  (Mining and Manufacturing Survey of all Korean establishments)

- Focus on 1969 to 1994

  - 1973: Heavy and Chemical Industry Drive

  - Oil shock in 1978-79 and assasination of president: HCI ends

  - Five year plan of 1982-86 (liberalization)

    (Buera and Shin, 2017)

  - Democratization and further liberalization in ealry 1990s

### Imagen / gráfica

La diapositiva muestra una trayectoria temporal en un plano con eje horizontal **Distortions, $\xi$** y eje vertical **Normalized Consumption**.

Los puntos rojos están etiquetados por año, desde 1969 hasta 1994. La trayectoria se mueve desde una zona de mayor distorsión y menor consumo hacia una zona de menor distorsión y mayor consumo. La curva azul de referencia muestra una relación decreciente entre distorsiones y consumo.

Visualmente, los años iniciales aparecen con consumo más bajo y distorsiones relativamente altas. A medida que avanza el tiempo, especialmente durante los ochenta y comienzos de los noventa, la trayectoria se desplaza hacia arriba y a la izquierda, consistente con liberalización, menor distorsión y mayor consumo.

**Interpretación contextual:** la figura usa Corea como episodio dinámico. El modelo intenta capturar cómo reformas y reducción de distorsiones pueden mover la economía a través de la región de Big Push, generando aumentos grandes de consumo/productividad.

---

## Wrapping Up

- Can there be large effects of distortions and policies?

  Yes, even without multiple equilibria

- Complementarities $\Longrightarrow$ Feedbacks, amplifying the effect of distortions/policies, with or without multiplicity

- Nonlinear effects in the Big Push region

- Can development be a story of (lack of) coordination?

  Yes, for economies with enough distortions

---

# Appendix / Additional Slides

---

## Identification: given $\eta$, $\nu_t=\nu_m$, and $\xi=0$

Figure: Identification from the establishment size distribution

$$
\log l^t
=
\log[(\eta-1)(1-\nu)\kappa_e]
-
\frac{\zeta}{\eta-1}\log \bar{l}^t
$$

$$
\log l_m
$$

$$
-\zeta\log\frac{z_a}{z_e}
$$

$$
(\eta-1)\log\frac{A_m}{A_t}
$$

### Imagen / diagrama

Esta diapositiva repite el esquema de identificación a partir de la distribución de tamaños. El eje horizontal es $\log l$ y el eje vertical es **log fraction w/ emp. $\geq l$**. La cola de la distribución y la separación entre tramos identifican parámetros de productividad, entrada y adopción.

---

## Calibrated Parameters

| Parameter | US | India |
|---|---:|---:|
| Elasticity of substitution, $\eta$ | 3 |  |
| Intermediate agg. share in adoption good production, $\gamma$ | 1 |  |
| Productivity distribution Pareto tail parameter, $\zeta$ | 2.42 |  |
| Modern technology productivity, $A_m$ | 1 |  |
| Modern technology intermediate input elasticity $\nu_m$ | 0.70 |  |
| Traditional technology intermediate input elasticity, $\nu_t$ | 0 |  |
| Entry cost, $\kappa_e$ | 0.50 | 0.50 |
| Traditional technology, $A_t$ | 0.43 | 0.23 |
| Adoption cost, $\kappa_a$ | 15.93 | 46.54 |
| $P\kappa_a$ | 9.36 | 101.4 |
| Degree of distortions, $\xi$ | 0 | 0.19 |
| Distortion scale parameter, $\tau$ | 1 | 1.61 |

---

## Aggregate Moments

|  | US | India |
|---|---:|---:|
| Fraction of active firms (out of 1) | 0.05 | 0.32 |
| Fraction of active firms that adopt $A_m$ | 0.5 | 0.001 |
| Average establishment size | 19.0 | 2.4 |
| Aggregate Consumption | 1 | 0.15 |

- India’s GDP per worker in 2005 is 6% of US (Penn World Tables)

---

## Impact on Average Size

United States

back

### Imagen / gráfica

La diapositiva muestra una curva azul de **Average Establishment Size** contra **Distortions, $\xi$**.

Eje horizontal: $\xi$, desde 0 hasta 0.5.  
Eje vertical: **Average Establishment Size**, en escala logarítmica, desde aproximadamente 1 hasta más de 100.

La curva empieza cerca de 19 trabajadores cuando $\xi=0$, cae con fuerza hasta alrededor de $\xi\approx 0.2$, y luego continúa descendiendo más lentamente. Una línea vertical punteada marca:

$$
\xi_{\text{India}} = 0.195
$$

Leyenda:

- **U.S. Calibration**
- $\xi_{\text{India}}=0.195$

**Interpretación contextual:** el gráfico muestra que el mismo mecanismo que reduce consumo también reduce el tamaño promedio de establecimiento. En la región cercana a India, pequeñas reducciones en distorsiones podrían tener efectos grandes sobre tamaño promedio.

---

## How robust is Big Push - consumption level

Fix $\kappa_a$

Fix $A_t$

$A_t$ exercise

$\kappa_a$ exercise

### Imagen / heatmaps

La diapositiva muestra dos mapas de calor lado a lado, ambos titulados internamente **Consumption**.

### Panel izquierdo: Fix $\kappa_a$

El eje horizontal es **Distortions, $\xi$**. El eje vertical varía **Traditional technology, $A_t$**. Los colores van de rojo/amarillo para consumo alto a azul oscuro para consumo bajo.

Se observa una frontera curva entre regiones de alto y bajo consumo. Para bajos niveles de $\xi$, el consumo es alto. A medida que $\xi$ aumenta, el consumo cae, especialmente cuando $A_t$ es bajo. La región azul aparece hacia la derecha e inferior/central, indicando que distorsiones altas y tecnología tradicional débil generan bajo consumo.

### Panel derecho: Fix $A_t$

El eje horizontal vuelve a ser **Distortions, $\xi$**. El eje vertical varía **Adoption cost, $\kappa_a$**. También hay una frontera marcada entre consumo alto y bajo. Con $\xi$ alto y costos de adopción altos, el consumo cae mucho. Con $\xi$ bajo, el consumo se mantiene alto incluso para costos de adopción mayores.

**Interpretación contextual:** estos mapas muestran que la región de Big Push es robusta a variaciones en tecnología tradicional y costos de adopción. Las distorsiones interactúan fuertemente con los parámetros que determinan la facilidad de adoptar tecnología moderna.