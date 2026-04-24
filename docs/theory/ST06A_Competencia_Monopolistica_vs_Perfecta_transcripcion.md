# ST06A - Competencia Monopolística vs Perfecta

## Transcripción a Markdown

**Fuente:** `ST06A - Competencia Monopolística vs Perfecta.pdf`

**Nota sobre imágenes:** No se observan gráficos, diagramas o imágenes sustantivas en estas diapositivas. El material relevante está compuesto por texto, ecuaciones y tablas comparativas, transcritas abajo.

---

## Página 1 / 11

# Distribución del Tamaño de Firmas

## Competencia Perfecta vs. Competencia Monopolística

1 / 11

---

## Página 2 / 11

# Índice

1. Naturaleza del bien y estructura de mercado
2. Derivación: Función de Producción Agregada
3. Comparación

2 / 11

---

## Página 3 / 11

# Naturaleza del bien y estructura de mercado

## Competencia perfecta (Lucas, 1978)

Bien homogéneo: el producto de todas las firmas es idéntico

Producto agregado es la suma simple:

$$
Y = \sum_i y_i
$$

La producción es lineal en el número de firmas: duplicar $M$ duplica $Y$

Tecnología con rendimientos decrecientes:

$$
y_i = e_i n_i^{\eta}, \quad \eta < 1
$$

## Competencia monopolística (Dixit-Stiglitz, 1977)

Bienes diferenciados: cada firma produce una variedad única

Producto agregado es una cesta CES:

$$
Y = \left( \int y_i^{\frac{\sigma - 1}{\sigma}} \, di \right)^{\frac{\sigma}{\sigma - 1}}
$$

Con $M$ firmas simétricas produciendo $\bar{y}$:

$$
Y = M^{1/(\sigma - 1)} \bar{y}
$$

Amor por la variedad: $Y$ aumenta con $M$ aunque $\bar{y}$ no cambie

Tecnología lineal:

$$
y_i = e_i n_i
$$

3 / 11

---

## Página 4 / 11

# Competencia Monopolística: Configuración e Ingreso como Función del Trabajo

Demanda (con $P = 1$): $y_i = Y p_i^{-\sigma}$. Invirtiendo: $p_i = Y^{1/\sigma} y_i^{-1/\sigma}$.

Ingreso como función del trabajo. Con $y_i = e_i n_i$ y $\eta \equiv (\sigma - 1)/\sigma$:

$$
R_i(n_i) = p_i y_i = Y^{1/\sigma} (e_i n_i)^\eta
= \underbrace{Y^{1/\sigma} e_i^\eta}_{\text{product. efectiva}} n_i^\eta
$$

## Paralelismo con el modelo competitivo

|  | Product. efectiva $A_i$ | Ingreso $R_i$ |
|---|---:|---:|
| Comp. perfecta | $e_i$ | $e_i n_i^\eta$ |
| Comp. monopolística | $Y^{1/\sigma} e_i^\eta$ | $Y^{1/\sigma} e_i^\eta n_i^\eta$ |

En ambos casos rendimientos decrecientes en trabajo con el mismo exponente $\eta$.

4 / 11

---

## Página 5 / 11

# Optimización de la Firma

Maximización de beneficios. Usando $R_i = Y^{1/\sigma} e_i^\eta n_i^\eta$:

$$
\max_{n_i} \left\{ Y^{1/\sigma} e_i^\eta n_i^\eta - w n_i \right\}
$$

Condición de primer orden (misma estructura que el modelo competitivo):

$$
\eta \frac{R_i}{n_i} = w \implies \eta p_i e_i = w \implies p_i = \frac{w}{\eta e_i}
$$

Las firmas más productivas cobran precios más bajos con un margen constante $1/\eta$.

Cantidades a nivel de firma. Sustituyendo $p_i$:

$$
y_i \propto e_i^{1/(1-\eta)}, \quad
n_i = \frac{y_i}{e_i} \propto e_i^{\eta/(1-\eta)}, \quad
p_i y_i = \frac{w}{\eta} n_i \propto e_i^{\eta/(1-\eta)}
$$

## Ingreso por trabajador igualado

$n_i$ y $p_i y_i$ tienen el mismo exponente $\eta/(1 - \eta)$: el ingreso por trabajador $p_i y_i/n_i = w/\eta$ es igual para todas las firmas.

## Producto escala más rápido

$y_i \propto e_i^{1/(1-\eta)}$ vs. $n_i \propto e_i^{\eta/(1-\eta)}$. Las firmas más productivas son desproporcionadamente grandes en producto.

5 / 11

---

## Página 6 / 11

# Derivación de la Función de Producción Agregada (I)

Índice de precios. Con $M$ firmas y $P = 1$:

$$
1 = M E\left[p_i^{1-\sigma}\right]
= M \left( \frac{w}{\eta} \right)^{1-\sigma} E\left[e_i^{\sigma-1}\right]
$$

Despejando el salario:

$$
\frac{w}{\eta} = \left( M E\left[e_i^{\sigma-1}\right] \right)^{1/(\sigma-1)}
\tag{1}
$$

Vaciamiento del mercado laboral. El empleo total debe igualar $N$:

$$
N = M E[n_i] = M E\left[\frac{y_i}{e_i}\right]
= M \cdot Y \left( \frac{\eta}{w} \right)^\sigma E\left[e_i^{\sigma-1}\right]
$$

Sustituyendo (1):

$$
N = M \cdot Y \cdot \frac{E\left[e_i^{\sigma-1}\right]}{\left( M E\left[e_i^{\sigma-1}\right] \right)^{\sigma/(\sigma-1)}}
= Y \left( M E\left[e_i^{\sigma-1}\right] \right)^{-1/(\sigma-1)}
$$

6 / 11

---

## Página 7 / 11

# Derivación de la Función de Producción Agregada (II)

Despejando $Y$. Reordenando el vaciamiento del mercado laboral:

$$
Y = N \left( M E\left[e_i^{\sigma-1}\right] \right)^{1/(\sigma-1)}
$$

Usando $\sigma - 1 = \eta/(1 - \eta)$, es decir $1/(\sigma - 1) = (1 - \eta)/\eta$:

$$
Y = \left( E\left[e_i^{\eta/(1-\eta)}\right] \right)^{(1-\eta)/\eta} M^{(1-\eta)/\eta} N
$$

Rendimientos a escala. Los exponentes sobre $(M, N)$ suman:

$$
\frac{1 - \eta}{\eta} + 1 = \frac{1}{\eta} > 1
$$

## Rendimientos crecientes a escala

Doblar tanto $M$ como $N$ más que duplica $Y$. Los RCE surgen del agregador CES: más variedades aumentan $Y$ incluso manteniendo fijo el producto de cada firma (amor por la variedad).

7 / 11

---

## Página 8 / 11

# Transformación $Y^\eta$ y Equivalencia con el Modelo Competitivo

Elevando ambos lados a la potencia $\eta$:

$$
Y^\eta = \left( E\left[e_i^{\eta/(1-\eta)}\right] \right)^{1-\eta} M^{1-\eta} N^\eta
$$

Misma forma Cobb-Douglas que el modelo competitivo de Lucas:

$$
Y_{Lucas} = \left( E\left[e_i^{1/(1-\eta)}\right] \right)^{1-\eta} M^{1-\eta} N^\eta
$$

## Equivalencia observacional

Con la sustitución $\tilde{e} = e^{1/\eta}$, los términos de PTF son idénticos:

$$
\left( E\left[e^{\eta/(1-\eta)}\right] \right)^{1-\eta}
= \left( E\left[\tilde{e}^{1/(1-\eta)}\right] \right)^{1-\eta}.
$$

Ambos modelos son observacionalmente equivalentes a nivel agregado, salvo por esta reparametrización de la distribución de productividades.

8 / 11

---

## Página 9 / 11

# Entrada Endógena

Costo de entrada $c_e$ en unidades de trabajo.

## El numero de firmas en equilibrio

Mostrar que en el modelo de competencia monopolística $M = (1 - \eta)N/c_e$ y $L = \eta N$ en equilibrio, igual que lo que obtuvimos en competencia perfecta.

9 / 11

---

## Página 10 / 11

# Comparación (I): Naturaleza del bien y función agregada

Todos los resultados usan $\eta \equiv (\sigma - 1)/\sigma$

|  | Competencia perfecta<br>Lucas (1978) | Competencia monopolística<br>Dixit-Stiglitz / Melitz |
|---|---|---|
| **Tecnología y estructura de mercado** |  |  |
| Naturaleza del bien | Homogéneo: $Y = \sum_i y_i$, lineal en $M$ | Diferenciado: cesta CES. $Y = M^{1/(\sigma-1)} \bar{y}$ (simétrico). Amor por la variedad. |
| Ingreso en función de $n_i$ | $R_i = e_i n_i^\eta$ | $R_i = Y^{1/\sigma} e_i^\eta n_i^\eta$<br>Misma estructura; difiere la productividad efectiva. |
| **Función de producción agregada (dados $M, N$)** |  |  |
| Forma natural | $Y = \left(E\left[e^{1/(1-\eta)}\right]\right)^{1-\eta} M^{1-\eta} N^\eta$<br>RCE: exponentes suman 1 | $Y = \left(E\left[e^{\eta/(1-\eta)}\right]\right)^{(1-\eta)/\eta} M^{(1-\eta)/\eta} N$<br>RCI: exponentes suman $1/\eta > 1$ |
| Tras transf. $Y^\eta$ en competencia monopolística | Sin cambio | $Y^\eta = \left(E\left[e^{\eta/(1-\eta)}\right]\right)^{1-\eta} M^{1-\eta} N^\eta$<br>Misma Cobb-Douglas $\Rightarrow$ equivalencia |

10 / 11

---

## Página 11 / 11

# Comparación (II): Cantidades a nivel de firma e invarianza

Todos los resultados usan $\eta \equiv (\sigma - 1)/\sigma$

|  | Competencia perfecta<br>Lucas (1978) | Competencia monopolística<br>Dixit-Stiglitz / Melitz |
|---|---|---|
| **Exponentes sobre $e_i$ a nivel de firma** |  |  |
| Empleo $n_i$ | $1/(1 - \eta)$ | $\eta/(1 - \eta)$ |
| Producto $y_i$ | $1/(1 - \eta)$ | $1/(1 - \eta)$ |
| Ingreso $p_i y_i$ | $1/(1 - \eta)$ | $\eta/(1 - \eta)$ |
| Implicación | Empleo, producto e ingreso escalan igual con $e_i$ | Producto escala más rápido que empleo e ingreso. Empleo e ingreso comparten exponente $\eta/(1 - \eta)$. |
| **Ingreso por trabajador** |  |  |
| Cantidad igualada entre firmas | Producto/Ingreso por trabajador: $y_i/n_i = w/\eta = \text{cte}$ | Ingreso por trabajador: $p_i y_i/n_i = w/\eta = \text{cte}$<br>Producto por trabajador $y_i/n_i = e_i$ varía. |

11 / 11
