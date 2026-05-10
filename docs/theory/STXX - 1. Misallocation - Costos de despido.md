# Politicas Distorsivas: Costos de Despido

Basado en Hopenhayn-Rogerson

Desarrollo Economico, 2026

---

## Mala asignación: algunos ejemplos

- Costos de despido (impuesto a la reasignación)

- Impuestos y exenciones/incumplimiento

- Límites al tamaño de las empresas (India)

- Restricciones crediticias

---

## Costos de Despido

- Los costos de despido son comunes en muchos países

- Introducen una cuña en el ajuste del empleo

- Implican que las empresas no igualan los productos marginales

- Generan pérdidas de productividad agregada

---

## Elección del nivel de empleo

$$
V(z,n)=\max_{n'} f(z,n') - wn' - \tau (n - n')_+ + \beta E v(z', n'|z)
$$

- Condiciones de primer orden para $n'$:

$$
f_2(z,n') - w + \tau + \beta E v_2(z',n'|z)
\qquad \text{si } n' < n
$$

$$
f_2(z,n') - w + \beta E v_2(z',n'|z) = 0
\qquad \text{si } n' > n
$$

$$
-\tau \leq f_2(z,n) - w + \beta E v_2(z',n|z) \leq 0
\qquad \Rightarrow \qquad n' = n
$$

- Para un $n$ dado, lo último ocurrirá para $\underline{z}(n) \leq z \leq \bar{z}(n)$ y se denomina zona de inacción

---

## Costos de Despido y Cuñas

Ejemplo hipotético con $z_1 < z_2 < z_3$

### rzglas de decisión

|      | $n_l$ | $n_h$ |
|------|------:|------:|
| $z_1$ | 5 | 9 |
| $z_2$ | 8 | 12 |
| $z_3$ | 14 | 20 |

### conjunto ergódico

|      | $n_l$ | $n_h$ |
|------|------:|------:|
| $z_1$ |  | 9 |
| $z_2$ | 9 | 12 |
| $z_3$ | 14 |  |

- empleo por encima del óptimo para $z_1$

- empleo por debajo del óptimo para $z_3$

- empleo por encima o por debajo del óptimo para $z_2$ (varianza de las cuñas)

- ¡También hay cuña correlacionada!

---

## Experimento cuantitativo

Hopenhayn y Rogerson (1993) con función de producción

$$
q_{it} = z_{it} n_{it}^{0,85}
\quad \text{con}
$$

$$
z_{it} = \bar{z}(1-\rho) + \rho z_{it-1} + \varepsilon_t
\qquad
\varepsilon_t \sim \log N(0,\sigma^2)
$$

donde

- $\rho = 0,92$ es consistente con el empleo a nivel de empresa en EE.UU. con una unidad de tiempo de 5 años

- $\sigma^2$ se calibra para reproducir la desviación estándar de $z_{it}$ en EE.UU. y China (manufactura).

- $\bar{e}$ genera un tamaño promedio de 50 trabajadores en la economía sin distorsiones, similar al nivel de EE.UU.

- Sin entrada ni salida de empresas

---

## Costos de despido: la función de política sS

**Gráfica:** `s-S policy (f=2)`

La gráfica tiene el eje vertical etiquetado como $n$, en escala logarítmica, con marcas aproximadas en $1$, $10$, $100$, $1000$ y $10000$. El eje horizontal está etiquetado como $\ln e$, con valores desde aproximadamente $1.1$ hasta $10.3$.

Aparecen tres curvas principales:

- Una curva roja escalonada, ubicada por encima de la curva central para buena parte del rango.
- Una curva azul escalonada, ubicada por debajo de la curva central.
- Una curva negra suave creciente, que funciona visualmente como referencia central.

También aparecen segmentos punteados horizontales: uno azul cerca de niveles bajos de empleo y uno rojo cerca de niveles altos de empleo.

**Interpretación contextual:** la figura ilustra una política tipo $s$-$S$ para el empleo con costos de despido. La empresa no ajusta continuamente su empleo hasta el nivel óptimo sin fricciones. En cambio, existe una banda de inacción entre umbrales: mientras el empleo esté dentro de esa zona, la firma mantiene $n$ aunque cambie la productividad. Cuando el empleo queda suficientemente lejos, ajusta. Esto genera empresas con empleo por encima o por debajo del nivel que igualaría productos marginales, produciendo cuñas y mala asignación.

---

## Costos de despido: brecha impositiva implícita

| $z$ | $N_L$ | $N$ | $N_H$ | $N_H/N_L$ | brecha impositiva |
|---:|---:|---:|---:|---:|---:|
| 1.5 | 4.5 | 6 | 20.7 | 4.6 | 25 % |
| 2.2 | 29 | 59 | 170 | 5.9 | 27 % |
| 3 | 243 | 483 | 1257 | 5.2 | 25 % |
| 4 | 1677 | 3607 | 4454 | 2.7 | 15 % |

---

## Costos de despido: TFPR y Productividad

**Gráfica:** `firing cost = 5 yearly wages`

La gráfica muestra una nube de puntos. El eje horizontal está etiquetado como $\ln e$ y va aproximadamente de $0$ a $80$. El eje vertical está etiquetado como $\ln TFPR$ y va aproximadamente de $-0.4$ a $0.5$.

Los puntos forman una nube creciente: para valores bajos de $\ln e$, la TFPR está en niveles negativos, alrededor de $-0.3$ a $-0.1$; a medida que $\ln e$ aumenta, la nube se desplaza hacia arriba y termina cerca de valores entre $0.25$ y $0.4$. También se observa dispersión dentro de la nube: para valores similares de $\ln e$, hay varios puntos con distinta $\ln TFPR$.

- TFPR positivamente correlada

- varianza dentro de niveles dados de $z$

**Interpretación contextual:** con costos de despido, la TFPR no queda igualada entre firmas. La inacción y el ajuste parcial generan dispersión de TFPR incluso para niveles dados de productividad. Además, la nube ascendente sugiere una cuña correlacionada: firmas más productivas o de mayor escala terminan enfrentando una TFPR más alta, consistente con empleo relativamente bajo respecto del óptimo, mientras que firmas menos productivas pueden quedar con empleo excesivo.

---

## Nivel de Costos de Despido y TFPR

| costo de despido | varianza | covarianza | correlación |
|---:|---:|---:|---:|
| 2 años | 0.014 | 1.01 | 0.57 |
| 5 años | 0.036 | 2.19 | 0.76 |
| 25 años | 0.114 | 5.08 | 1.00 |

---

## Costos de despido y PTF agregada

| Costo de despido (años) | Pérdida de PTF | Brecha (rango de impuestos laborales equivalentes) |
|---:|---:|---:|
| 2 años | -2.8 % | 32.9 |
| 5 años | -7.5 % | 56.0 |
| 25 años | -24.3 % | 97.6 |

---

## Políticas y Cumplimiento

- Muchos países tienen políticas que eximen a las empresas pequeñas de ciertos costos

- En otros países, las empresas pequeñas eligen no cumplir

- Tres tipos de distorsiones:

  - algunas empresas reducirán su tamaño para calificar, aumentando la TFPR

  - las empresas por debajo del umbral enfrentarán costos salariales menores al promedio, reduciendo la TFPR

  - las que están por encima del umbral enfrentarán costos salariales mayores al promedio, aumentando la TFPR

- Estas son distorsiones correlacionadas