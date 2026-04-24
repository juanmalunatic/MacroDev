# ST03 - Difusión tecnológica y contabilidad del desarrollo

Source: `ST03 - Difusión tecnológica y contabilidad del desarrollo.pdf`

Transcription notes:

- Text is transcribed to Markdown to the best of my ability from the PDF text layer and visible rendered slide images.
- Equations are transcribed in LaTeX.
- Important figures/charts are described so they can be referenced later.
- The PDF is a Beamer deck with incremental reveal overlays. Where several consecutive PDF pages show the same logical slide with more content revealed, I consolidate them into one logical slide and transcribe the fully revealed version once, while noting the PDF page range.

---

## Page 1 / 23 - Slide 1 / 11

# DIFUSIÓN TECNOLÓGICA Y CONTABILIDAD DEL DESARROLLO

HUGO HOPENHAYN

UTDT

DESARROLLO ECONÓMICO

2026

---

## Page 2 / 23 - Slide 2 / 11

# TFP Y ATRASO TECNOLÓGICO

- Evidencia de atraso tecnológico en economías pobres
- Agregación de distintas generaciones tecnológicas de capital
- Argumentos en contra

---

## Page 3 / 23 - Slide 3 / 11

# COMIN ET AL.: REZAGOS EN LA ADOPCIÓN TECNOLÓGICA

Referencias: (Caselli (2005), Comin and Hobijn (2008), Comin and Hobijn (2010), Comin and Hobijn (2004), Comin and Mestieri (2018))

**Hechos Estilizados Clave:**

1. Las tecnologías se difunden lentamente entre países
2. Los países pobres adoptan nuevas tecnologías 45+ años después
3. Incluso tecnologías antiguas (ferrocarriles, teléfonos) muestran brechas persistentes

**Implicación:** Explican 75% del aumento del gap de ingresos entre las economías occidentales y el resto en los últimos 200 años (factor 3.9) según Comin and Mestieri (2018)

### Descripción visual importante

La diapositiva incluye un gráfico titulado **"Log of Telephone Lines over Real GDP"**. El eje horizontal muestra años aproximadamente desde 1850 hasta 2000. El eje vertical muestra una medida logarítmica de líneas telefónicas relativa al PIB real. La leyenda compara varias economías: USA, Malawi, Pakistan, Burkina Faso, Colombia, Australia y Japan. La línea de USA despega antes y alcanza niveles altos mucho antes; Japón y Australia también convergen a niveles altos pero con rezagos; países como Colombia, Pakistan, Malawi y Burkina Faso aparecen con trayectorias más tardías y/o más bajas. La figura ilustra rezagos persistentes de adopción tecnológica entre países.

---

## Pages 4-8 / 23 - Slide 4 / 11

# AGREGACIÓN

- Supongamos que un país tiene un vector de capitales $(K_1, K_2, \ldots, K_T)$ que representa capitales de generaciones distintas.

- Función de producción:

$$
Y = \left(\sum_g A_g K_g\right)^\alpha (hL)^{1-\alpha}
$$

- Si definimos

$$
K = \sum_g K_g
$$

and

$$
A = \left(\sum_g s_g A_g\right)^{\frac{\alpha}{1-\alpha}},
\qquad \text{donde } s_g = \frac{K_g}{K},
$$

entonces:

$$
Y = K^\alpha (AhL)^{1-\alpha}
$$

- Las participaciones $s_g$ afectan el valor de PTF.

- Ejemplo: 2 generaciones, $A_2 = 4A_1$. Caso 1: $K_1 = K, K_2 = 0$. Caso 2: $K_1 = 0, K_2 = K$ y $\alpha = 1/3$

$$
\mathrm{TFP}_2 = 4^{1/2} = 2, \qquad \mathrm{TFP}_1 = 1
$$

---

## Pages 9-11 / 23 - Slide 5 / 11

# PROBLEMA CON ESTA FORMULACIÓN?

Si los países pobres usan tecnología más antigua, ¿no debería esto ya estar reflejado en los precios del capital?

- Un Tesla Model 3 2024: \$40,000 (tecnología nueva)
- Un Honda Civic 2010: \$8,000 (tecnología antigua)

La Lógica:

1. Tecnología más antigua $\rightarrow$ Menos productiva
2. Menos productiva $\rightarrow$ Precio de mercado más bajo
3. Medimos el capital usando precios de mercado
4. ¡Entonces las diferencias tecnológicas deberían aparecer en $K$, no en PTF!

---

## Pages 12-14 / 23 - Slide 6 / 11

# EL ARGUMENTO FORMAL

- Consideremos la función de producción dada:

$$
Y = \left(\sum_g A_g K_g\right)^\alpha (hL)^{1-\alpha}
$$

- Condiciones de primer orden para el capital $K_g$

$$
\alpha \left(\sum_g A_g K_g\right)^{\alpha-1} (hL)^{1-\alpha} A_g = r_g
$$

donde $r_g$ es el precio del capital de generación $g$.

- Para que esta igualdad se cumpla para los distintas generaciones de capital, los precios $r_g$ tienen que ser proporcionales a $A_g$

---

## Pages 15-18 / 23 - Slide 7 / 11

- Podemos reescribir la función de producción

$$
\begin{aligned}
Y
&= \left(\sum_g \frac{A_g}{A_T} K_g\right)^\alpha
\left(A_T^{\frac{\alpha}{1-\alpha}} hL\right)^{1-\alpha} \\
&= \left(\sum_g \frac{r_g}{r_T} K_g\right)^\alpha
\left(A_T^{\frac{\alpha}{1-\alpha}} hL\right)^{1-\alpha} \\
&= K^\alpha \left(A_T^{\frac{\alpha}{1-\alpha}} hL\right)^{1-\alpha}
\end{aligned}
$$


definiendo

$$
K = \sum_g \frac{r_g}{r_T} K_g
$$

tomando como numerario el capital de la generación mas reciente.

- Los precios relativos del capital deprecian el capital de generaciones más antiguas en proporción a su productividad relativa.

---

## Page 19 / 23 - Slide 8 / 11

# POSIBLES ATENUANTES?

- Precios no ajustan apropiadamente por calidad
- Insumos complementarios o efectos de red bajan la calidad relativa de las tecnologías nuevas
- Complementariedad del capital humano con las tecnologías nuevas.

---

## Page 20 / 23 - Slide 9 / 11

# EJERCICIOS

1. Supongamos que $A_t/A_{t-1} = 1.02$ lo que es consistente con una tasa general de crecimiento del ingreso per capita de 2% anual. Cuánto mas viejas debieran ser las tecnologías utilizadas por el percentil 10 vs. el 90?

2. Supongamos que que $A_t/A_{t-1} = 1.02$, que la relacion $K/Y$ de un país se mantiene fija y la tasa de depreciación del capital es 5% anual (es la media utilizada en las Penn world tables). Calcule la TFP de esta economía relativa a la tecnología de frontera.

---

## Page 21 / 23 - Slide 10 / 11

# Referencias

---

## Page 22 / 23 - Slide 11 / 11

Caselli, F. (2005). Accounting for cross-country income differences. Handbook of Economic Growth, 1:679-741. Seminal review of development accounting methodology and the TFP puzzle.

Comin, D. and Hobijn, B. (2004). Cross-country technology adoption: Making the theories face the facts. Technical Report 1, Journal of Monetary Economics. CHAT database showing persistent technology gaps.

Comin, D. and Hobijn, B. (2008). Technology diffusion and postwar growth. NBER Macroeconomics Annual, 23(1):209-246.

Comin, D. and Hobijn, B. (2010). An exploration of technology diffusion. American Economic Review, 100(5):2031-2059. Documents extensive lags in technology adoption across countries.

---

## Page 23 / 23 - Slide 12 / 11

Comin, D. and Mestieri, M. (2018). The extensive margin of technology adoption. Journal of Political Economy, 126(1):52-103. Distinguishes intensive and extensive margins of technology adoption.
