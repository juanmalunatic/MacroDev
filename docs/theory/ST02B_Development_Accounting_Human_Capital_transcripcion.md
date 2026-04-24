# ST02B - Development Accounting - Human capital

> Transcripción en Markdown del PDF **ST02B - Development Accounting - Human capital.pdf**.  
> Ecuaciones transcritas en LaTeX.  
> Se incluyen descripciones de gráficos, figuras y anotaciones visibles cuando son relevantes.

---

## Página 1 / 36

# La Contabilidad del Desarrollo - El Capital Humano

Hugo Hopenhayn

UTDT

Desarrollo Económico

2026

---

## Página 2 / 36

# Mayor rol al capital humano

- La educación puede ser más productiva en crear capital humano si la economía es más eficiente.
  - La eficiencia de la educación
  - La calidad de las instalaciones (bienes complementarios - e.g. computers)
  - El capital humano de los profesores

- Diferencias en la salud
- Diferencias en la experiencia laboral y los retornos a la experiencia
- La distancia a la frontera tecnológica puede depender del capital humano

**Anotación visible:** “Si hay tech más productiva para K, por que no lo mismo para h?”

---

## Página 3 / 36

# La Productividad de la Educación I

- Tomemos un modelo simple:

\[
h_c = \hat{A}_c^{\gamma} g(S_c)
\tag{1}
\]

- Usando la función de producción

\[
\frac{Y_c}{L_c}
= \hat{A}_c
\left(\frac{K_c}{Y_c}\right)^{\frac{\alpha}{1-\alpha}}
\underbrace{\hat{A}_c^{\gamma}g(S_c)}_{h_c}
\tag{2}
\]

- Si comparamos con la ecuación usada antes:

\[
\frac{Y_c}{L_c}
= A_c
\left(\frac{K_c}{Y_c}\right)^{\frac{\alpha}{1-\alpha}}
g(S_c)
\tag{3}
\]

  - Las diferencias de PTF se amplifican: \(A = \hat{A}^{1+\gamma}\)

**Anotación visual:** hay un recuadro rojo alrededor de “Las diferencias de PTF se amplifican: \(A = \hat{A}^{1+\gamma}\)”. A la derecha aparece la anotación “entender”.

---

## Página 4 / 36

# La Productividad de la Educación II

- Función de producción de capital humano

\[
h_c = \kappa_c^{\gamma} g(s_c)
\tag{4}
\]

donde \(\kappa_c\) son bienes de capital destinados a educación

- \(\kappa_c\) posiblemente correlacionada positivamente con \(S_c\) (mayor retorno)
- Impacto sobre contabilidad del desarrollo:

\[
\frac{Y_c}{L_c}
= \hat{A}_c \kappa_c
\left(\frac{K_c}{Y_c}\right)^{\frac{\alpha}{1-\alpha}}
g(S_c)
\tag{5}
\]

  - \(A_c = \hat{A}_c \kappa_c\)

- Impacto similar de diferencias en la calidad de los ”profesores”

---

## Página 5 / 36

# Productividad e Inversión en Capital Humano

Ilustrar mecanismos que pueden ayudar a explicar grandes diferencias de capital humano

- ¿Por qué las personas en algunos países invierten mucho más?
- Modelo de referencia que no genera diferencias
- Tres mecanismos que sí generan diferencias

Modelización cuantitativa como instrumento de medición

- Los modelos pueden calibrarse o estimarse usando datos entre países, de corte transversal u otros.
- Pregunta: ¿qué tan importantes son los mecanismos y el capital humano?

---

## Página 6 / 36

# Capital Humano y Salarios

**Anotación visible:** “Versión muy simplificada del paper de Seshadri”

Firma(s): Igual que antes - operan la tecnología agregada:

\[
Y_c = A_c K_c^{\alpha} H_c^{1-\alpha}
\]

Se mantienen los mismos dos supuestos clave que en el caso base:

1. Sustitución perfecta entre tipos de trabajo (unidades de eficiencia)
2. Mercados laborales competitivos (trabajadores remunerados a su producto marginal)

Lo que produce la expresión simple para salarios:

\[
w_{i,c} = (1-\alpha) z_c h_i
\]

**Anotación visible:** “Lo que hicimos antes, pero quizá acá Z es distinto porque no sé si Y está labor-augmenting”

---

## Página 7 / 36

# Modelo de Referencia: Elección Escolar Simple

Los consumidores viven una unidad de tiempo. Maximizan la utilidad:

\[
\int_0^1 \ln c(t)\,dt
\]

Dividen su unidad de tiempo entre escuela y trabajo:

- Asisten a la escuela durante un período de duración \(s\)
- La escolaridad genera capital humano \(h(s)\)
- Trabajan con \(h(s)\) durante los \((1-s)\) períodos restantes

Restricción presupuestaria:

\[
\int_0^1 c(t)\,dt = I = (1-\alpha)z_c h(s)(1-s)
\]

**Anotaciones visibles:**

- “1 unidad de tiempo por periodo”
- “con \(h'(s) > 0\)”
- “puede suavizar perfectamente, entonces C = I = ingreso_hora * horas_trab (check)”

---

## Página 8 / 36

# Resultados del Modelo de Referencia

Los trabajadores suavizan el consumo a lo largo del período:

\[
c(t) = c = I
\]

La elección escolar óptima maximiza el ingreso. CPO:

\[
\underbrace{(1-\alpha)z_c(1-s)h'(s)}_{\text{beneficio marginal de }s\text{ adicional}}
=
\underbrace{(1-\alpha)z_ch(s)}_{\text{costo marginal de }s\text{ adicional}}
\]

Simplificando, se encuentra que la elección escolar óptima es independiente de \(z_c\) (neutralidad de Becker):

\[
h'(s)(1-s)=h(s)
\]

**Anotaciones visibles:**

- “derivando wrt s”
- “el nivel de s es independiente de z = A (K/N) blablabla”
- “es decir que la productividad no afecta el nivel de educación elegido”
- “mayor prod: probablemente aumenta beneficio marginal”
- “probablemente aumenta costo de oportunidad, entonces se cancelan”
- “Becker lo encontró antes. Empirically, doesn't hold más rico más s”

---

## Página 9 / 36

# Mecanismo 1: Restricciones de Endeudamiento

El modelo supone que el trabajador consume mientras estudia, antes de recibir ingresos:

- \(sI\) unidades de consumo, en total
- Posiblemente también costos directos de educación

Limitaciones en la capacidad de los niños y las familias de financiar esta inversión (Becker y Tomes, 1986):

1. Los mercados de crédito son imperfectos
2. Los niños no pueden firmar contratos vinculantes
3. El altruismo puede no ser perfecto
4. Los padres no pueden traspasar deuda a sus hijos

Las variaciones en los mecanismos para abordar estas limitaciones pueden ayudar a explicar la inversión en capital humano.

**Anotaciones visibles:**

- “¿Por qué empirically no funciona?”
- “te puedes endeudar en ricos”
- “cuidar a los viejos de viejos”
- “no los mandan a estudiar los viejos”
- “i.e. extendamos el modelo y cambiemoslo. hasta acá llegamos”

---

## Página 10 / 36

# Mecanismo 2: Bienes en la Producción de Capital Humano

Se utilizan tiempo y bienes para invertir en capital humano (Manuelli y Seshadri, 2014). Nueva restricción presupuestaria:

\[
\int_0^1 c(t)\,dt + e = I = (1-\alpha)z_c h(s,e)(1-s)
\]

Especializando a la función de producción de capital humano potencial:

\[
h(s,e)=a s^{\eta} e^{\gamma}
\]

Elección óptima:

\[
\max_{s,e} (1-\alpha)a z_c s^{\eta}e^{\gamma}(1-s)-e
\]

- La elección de \(s\) es independiente de \(z_c\), \(a\) y \(e\)
- La elección de \(e\) sí depende de \(z\):

\[
\varepsilon_{e,z}=\frac{1}{1-\gamma}
\]

- \[
\varepsilon_{h,z}=\frac{\gamma}{1-\gamma}
\]

**Anotación visual:** la frase “tiempo y bienes” aparece resaltada en amarillo dentro del texto inicial.

---

## Página 11 / 36

# Hacer que la Escolaridad Dependa de z

Fuente: Erosa, Koreshkova & Restuccia (2010)

Costo laboral adicional de escolaridad: \(\bar{l}s\)

\[
\max_{s,e} (1-\alpha)z_c a s^{\eta}e^{\gamma}(1-s)-e-
\underbrace{(1-\alpha)z_c}_{w}\bar{l}s
\]

Condiciones de primer orden:

\[
a e^{\gamma}\left(\eta s^{\eta-1}-(\eta+1)s^{\eta}\right)=\bar{l}
\]

\[
(1-\alpha)z_c a s^{\eta}(1-s)\gamma e^{\gamma-1}=1
\]

- \(s\) es creciente en \(e\), que a su vez crece con \(z\). También crece con \(a\).

Simplificando al eliminar el costo de oportunidad del tiempo de escolaridad:

\[
a e^{\gamma}\eta s^{\eta-1}=\bar{l}, \qquad
(1-\alpha)a z_c s^{\eta}\gamma e^{\gamma-1}=1
\]

\[
\varepsilon_{s,z}=\frac{\gamma}{1-(\gamma+\eta)}, \qquad
\varepsilon_{e,z}=\frac{1-\eta}{1-(\gamma+\eta)}, \qquad
\varepsilon_{s,a}=\varepsilon_{e,a}=\frac{1}{1-(\gamma+\eta)}
\]

---

## Página 12 / 36

# Implicancias Cuantitativas

- Manuelli Seshadri:
  - Diferencias de TFP relativamente modestas —de no más del 27%— son suficientes para explicar las grandes diferencias observadas en producto por trabajador entre países.
  - El quintil más pobre tiene una TFP equivalente al 73% de la de EE.UU., mientras que Hall y Jones la estimaban en apenas un 20%.
  - La interpretación es que ignorar las diferencias en calidad educativa amplifica artificialmente las diferencias de TFP.

- Erosa et al
  - Acumulación de capital humano amplifica fuertemente las diferencias de TFP entre países
  - Estiman una elasticidad del producto por trabajador respecto a la TFP de 2.8
  - Una diferencia de 3 veces en TFP puede explicar una diferencia de 20 veces en producto por trabajador

---

## Página 13 / 36

# Capital Humano y Frontera Tecnológica

- Hay una frontera tecnológica en el mundo: \(A_{us}\)
- La frontera tecnológica de una país depende de su capital humano, relativo al de Estados Unidos:

\[
A_c = \hat{A}_c \left(\frac{h_c}{h_{us}}\right)^{\gamma} A_{us}
\tag{6}
\]

\[
\ln\left(\frac{A_c}{A_{us}}\right)
= \ln \hat{A}_c + \gamma \ln\left(\frac{h_c}{h_{us}}\right)
\tag{7}
\]

- Esto se puede estimar haciendo la regresión

\[
\ln\left(\frac{A_c}{A_{us}}\right)
= a + \gamma \ln\left(\frac{h_c}{h_{us}}\right)+\epsilon_c
\tag{8}
\]

- ....... y luego definir \(\ln(A_c)=a+\epsilon_c\)

---

## Página 14 / 36

# Evidencia Empírica: Educación, Salud,
# Experiencia

---

## Página 15 / 36

# Calidad Educativa y Salud

**Gráfico izquierdo:** “Puntajes de Matemáticas PISA 2018 y Desarrollo (OECD, 2018)”

- Eje vertical: “2018 PISA Math Score”, aproximadamente de 300 a 600.
- Eje horizontal: “GDP p.w., 2017 US$”, con marcas aproximadas en 2500, 5000, 10000, 20000, 40000, 80000.
- El gráfico muestra una relación positiva entre desarrollo/producto por trabajador y puntajes PISA de matemáticas.
- Países de altos ingresos como SGP, HKG, MAC, TWN, EST, KOR, NLD, POL, CAN, CHE, JPN y otros aparecen en la parte alta del puntaje; varios países de ingresos medios aparecen con menor puntaje.

**Gráfico derecho:** “Tasa de Supervivencia Adulta 2018 y Desarrollo (World Bank, 2020)”

- Eje vertical: “Adult Survival Rate”, aproximadamente de 0.50 a 1.00.
- Eje horizontal: “GDP p.w., 2017 US$”, con las mismas marcas aproximadas: 2500, 5000, 10000, 20000, 40000, 80000.
- El gráfico muestra una relación positiva entre desarrollo/producto por trabajador y supervivencia adulta.
- Países más pobres aparecen más dispersos y con tasas de supervivencia más bajas; países ricos se agrupan cerca de tasas altas.

---

## Página 16 / 36

# Experiencia

Experiencia potencial = años desde graduación = edad − escolaridad − 6.

**Gráfico izquierdo:** “Perfiles, Países Ricos Seleccionados”

- Eje vertical: “Percent Wage Increase”, aproximadamente de 0 a 150.
- Eje horizontal: “Potential Experience”, de 0 a 40.
- Series: Australia, Germany, USA, Canada, France.
- Las curvas muestran aumentos salariales por experiencia potencial en países ricos, con perfiles crecientes y bastante pronunciados.

**Gráfico derecho:** “Perfiles, Países Pobres Seleccionados”

- Eje vertical: “Percent Wage Increase”, aproximadamente de 0 a 150.
- Eje horizontal: “Potential Experience”, de 0 a 40.
- Series: Jamaica, India, Bangladesh, Guatemala, Vietnam.
- Las curvas muestran retornos más bajos o perfiles más planos que en los países ricos seleccionados.

Fuente indicada en la diapositiva: “(Lagakos et al., 2018b)”

---

## Página 17 / 36

# Retornos a la Experiencia, Entrenamiento y Desarrollo

**Gráfico izquierdo:** “Retornos a la Experiencia y Desarrollo (Lagakos et al., 2018b)”

- Eje vertical: “Return to 20-24 Years of Experience”, aproximadamente de 20 a 100.
- Eje horizontal: “GDP p.w., 2017 US$”, con marcas aproximadas 2500, 5000, 10000, 20000, 40000, 80000.
- Muestra una relación positiva entre desarrollo y retorno a 20-24 años de experiencia.
- Países visibles incluyen BGD, VNM, IND, IDN, JAM, GTM, PER, BRA, URY, MEX, CHL, KOR, GBR, CAN, DEU, FRA, AUS, USA.

**Gráfico derecho:** “Entrenamiento y Desarrollo (Ma et al., 2020)”

- Eje vertical: “Share with Firm Training”, aproximadamente de 0 a 80.
- Eje horizontal: “GDP p.w., 2017 US$”, con marcas aproximadas 2500, 5000, 10000, 20000, 40000, 80000.
- Muestra que la proporción con entrenamiento en firmas tiende a ser mayor en países más desarrollados.
- Hay muchos códigos de país, con países pobres agrupados cerca de niveles bajos de entrenamiento y países más ricos con participaciones mayores.

---

## Página 18 / 36

# Capital Humano Total Construido

Acumulando, un paso a la vez, métrica

\[
\frac{\operatorname{cov}(\log(h),\log(y))}{\operatorname{var}\log(y)}:
\]

- Años de escolaridad: 19%

---

## Página 19 / 36

# Capital Humano Total Construido

Acumulando, un paso a la vez, métrica

\[
\frac{\operatorname{cov}(\log(h),\log(y))}{\operatorname{var}\log(y)}:
\]

- Años de escolaridad: 19%
- Años + calidad de escolaridad: 38%

---

## Página 20 / 36

# Capital Humano Total Construido

Acumulando, un paso a la vez, métrica

\[
\frac{\operatorname{cov}(\log(h),\log(y))}{\operatorname{var}\log(y)}:
\]

- Años de escolaridad: 19%
- Años + calidad de escolaridad: 38%
- Escolaridad total + experiencia: 56%

---

## Página 21 / 36

# Capital Humano Total Construido

Acumulando, un paso a la vez, métrica

\[
\frac{\operatorname{cov}(\log(h),\log(y))}{\operatorname{var}\log(y)}:
\]

- Años de escolaridad: 19%
- Años + calidad de escolaridad: 38%
- Escolaridad total + experiencia: 56%
- Escolaridad total + experiencia + salud: 59%

---

## Página 22 / 36

# Capital Humano Total Construido

Acumulando, un paso a la vez, métrica

\[
\frac{\operatorname{cov}(\log(h),\log(y))}{\operatorname{var}\log(y)}:
\]

- Años de escolaridad: 19%
- Años + calidad de escolaridad: 38%
- Escolaridad total + experiencia: 56%
- Escolaridad total + experiencia + salud: 59%

Ver también:

- Experiencia: Lagakos et al. (2018a); Jedwab et al. (2020)
- Calidad educativa: Schoellman (2012); Hanushek and Woessmann (2012); Kaarsen (2014).
- Salud: Weil (2007)

---

## Página 23 / 36

# Resumen

El primer enfoque para las diferencias de capital humano entre países es construirlo, pieza por pieza

- Explica diferencias en stocks o (quizás) retornos
- Las estimaciones resultantes son grandes, explican quizás el 60 por ciento de las diferencias de ingreso

Algunas preocupaciones:

- Supuestos necesarios (ver e.g. Jones, 2014).
- Es difícil ser exhaustivo
- Puede estar duplicando conteos

---

## Página 24 / 36

# Enfoque Deductivo

El capital humano está, por definición, incorporado en las personas.

- Los migrantes llevan su capital humano a nuevos países
- Sus resultados nos permiten deducir la importancia del capital humano

---

## Página 25 / 36

# Enfoque Deductivo

El capital humano está, por definición, incorporado en las personas.

- Los migrantes llevan su capital humano a nuevos países
- Sus resultados nos permiten deducir la importancia del capital humano

Recordar que bajo los supuestos mantenidos, los salarios están dados por:

\[
\log(w_{i,c}) = \log([1-\alpha]z_c)+\log(h_i)
\]

---

## Página 26 / 36

# Enfoque Deductivo

El capital humano está, por definición, incorporado en las personas.

- Los migrantes llevan su capital humano a nuevos países
- Sus resultados nos permiten deducir la importancia del capital humano

Recordar que bajo los supuestos mantenidos, los salarios están dados por:

\[
\log(w_{i,c}) = \log([1-\alpha]z_c)+\log(h_i)
\]

Dos preocupaciones adicionales que necesitan ser abordadas

- Los migrantes no son elegidos aleatoriamente (selección)
- El capital humano de los migrantes puede no ser el mismo (pérdida de habilidades, discriminación)

---

## Página 27 / 36

# Ganancias Salariales en la Migración

Las ganancias salariales para un trabajador que migra de \(c\) a \(c'\) son:

\[
\log(w_{i,c'})-\log(w_{i,c})=\log(z_{c'})-\log(z_c)
\]

---

## Página 28 / 36

# Ganancias Salariales en la Migración

Las ganancias salariales para un trabajador que migra de \(c\) a \(c'\) son:

\[
\log(w_{i,c'})-\log(w_{i,c})=\log(z_{c'})-\log(z_c)
\]

El cambio en \(z_c\) es una parte del rompecabezas de contabilidad del desarrollo

\[
\log(y_c)=\log(z_c)+\log(h_c)
\]

---

## Página 29 / 36

# Ganancias Salariales en la Migración

Las ganancias salariales para un trabajador que migra de \(c\) a \(c'\) son:

\[
\log(w_{i,c'})-\log(w_{i,c})=\log(z_{c'})-\log(z_c)
\]

El cambio en \(z_c\) es una parte del rompecabezas de contabilidad del desarrollo

\[
\log(y_c)=\log(z_c)+\log(h_c)
\]

Intuición: suponga que el trabajador migra de un país pobre a uno 10× más rico

- ¿Los salarios aumentan 10×? El país (\(z_c\)) explica los salarios bajos
- ¿Los salarios no cambian? El capital humano bajo explica los salarios bajos
- ¿Selección, pérdida de habilidades?
- Alternativas: Hendricks (2002); Schoellman (2012); De Philippis and Rossi (2020)

---

## Página 30 / 36

# Implementación

Necesario: datos sobre salarios pre y post migración. Dos fuentes (Hendricks and Schoellman, 2018).

1. Encuesta de Nuevos Inmigrantes: muestra de recipientes adultos de residentes legales permanente en EE.UU., mayo–noviembre 2003
2. Proyectos de Migración: muestra de comunidades en México y América Latina con altas tasas de migración

Salarios convertidos a PPA

- Comparar ganancias salariales reales con brecha en PIB real por trabajador

Gran conjunto de covariables

- Demografía, educación, ocupación, industria, estatus de visa

---

## Página 31 / 36

# Capital Humano y Contabilidad del Desarrollo

| Grupo | Salario por Hora Pre-Mig. | Salario por Hora Post-Mig. | Ganancia Salarial | Brecha PIB | Participación \(h\) | 95% I.C. |
|---|---:|---:|---:|---:|---:|---:|
| **Panel A: Muestra NIS por categoría de PIB por trabajador** |||||||
| < 1/16 | $2.82 | $8.91 | 3.2 | 31.8 | 0.66 | (0.60, 0.73) |
| 1/16 − 1/8 | $4.19 | $11.83 | 2.8 | 11.9 | 0.58 | (0.54, 0.62) |
| 1/8 − 1/4 | $4.95 | $9.48 | 1.9 | 5.6 | 0.63 | (0.55, 0.71) |
| 1/4 − 1/2 | $5.05 | $9.11 | 1.8 | 3.0 | 0.48 | (0.34, 0.62) |
| 1/2 − 1 | $12.64 | $15.18 | 1.2 | 1.3 | 0.48 | (-0.23, 1.19) |
| **Panel B: Muestra MP por submuestra** |||||||
| América Latina MP | $4.84 | $7.05 | 1.5 | 7.0 | 0.79 | (0.71, 0.87) |
| México MP | $2.96 | $6.04 | 2.0 | 2.9 | 0.33 | (0.29, 0.37) |

Agrupando países pobres (<1/4 PIB por trabajador de EE.UU.) en NIS: 62%

---

## Página 32 / 36

# Resumen de Medición

Enfoque deductivo: fortalezas y debilidades

- Exhaustivo, pero no constructivo
- Evita el doble conteo
- Requiere supuestos adicionales sobre migrantes

Resultados cuantitativamente similares

- El capital humano explica 50–60% de las diferencias de ingreso

Aún hay espacio para explorar

- Crianza e infancia temprana (Schoellman, 2016; De Philippis and Rossi, 2020)
- Cultura (Ek, 2020)
- Habilidades específicas (Hjort et al., 2021)

---

## Página 33 / 36

# Referencias

---

## Página 34 / 36

De Philippis, M. and Rossi, F. (2020). Parents, schools and human capital differences across countries. *Journal of the European Economic Association*. forthcoming.

Ek, A. (2020). Cultural values and productivity. mimeo, Lund University.

Hanushek, E. A. and Woessmann, L. (2012). Do better schools lead to more growth? cognitive skills, economic outcomes, and causation. *Journal of Economic Growth*, 17(4):267–321.

Hendricks, L. (2002). How important is human capital for development? evidence from immigrant earnings. *American Economic Review*, 92(1):198–219.

Hendricks, L. and Schoellman, T. (2018). Human capital and development accounting: New evidence from wage gains at migration. *Quarterly Journal of Economics*, 133(2):665–700.

Hjort, J., Malmberg, H., and Schoellman, T. (2021). The missing middle managers: Labor costs, firm structure, and development. mimeo, University of Minnesota.

Jedwab, R., Romer, P., Islam, A., and Samaniego, R. (2020). Human capital accumulation at work: Estimates for the world and implications for development. mimeo, NYU Stern.

Jones, B. F. (2014). The human capital stock: A generalized approach. *American Economic Review*, 104(11):3752–3777.

---

## Página 35 / 36

Kaarsen, N. (2014). Cross-country differences in the quality of schooling. *Journal of Development Economics*, 107(2):215–224.

Lagakos, D., Moll, B., Porzio, T., Qian, N., and Schoellman, T. (2018a). Life-cycle human capital accumulation across countries: Lessons from u.s. immigrants. *Journal of Human Capital*, 12(2):184–215.

Lagakos, D., Moll, B., Porzio, T., Qian, N., and Schoellman, T. (2018b). Life-cycle wage growth across countries. *Journal of Political Economy*, 126(2):797–849.

Ma, X., Nakab, A., and Vidart, D. (2020). Human capital investment and development: The role of on-the-job training. mimeo, UC San Diego.

OECD (2018). OECD PISA 2018 Database. https://www.oecd.org/pisa/data/2018database/.

Schoellman, T. (2012). Education quality and development accounting. *Review of Economic Studies*, 79(1):388–417.

Schoellman, T. (2016). Early childhood human capital and development. *American Economic Journal: Macroeconomics*, 8(3):145–174.

---

## Página 36 / 36

Weil, D. N. (2007). Accounting for the effect of health on economic growth. *Quarterly Journal of Economics*, 122(3):1265–1306.

World Bank (2020). Human Capital Index. World Bank, Washington DC.
