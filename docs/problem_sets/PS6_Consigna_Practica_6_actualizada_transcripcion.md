# Trabajo Practico 6

# Competencia monopolística, Elección Ocupacional y Contabilidad del Desarrollo

## Parte I: Competencia Monopolística y Función de Producción Agregada

### Problema 1 (Número de firmas y empleo con Competencia Monopolistica). y función de producción agregada]

Derivar el numero de firmas \(M\) y el empleo \(L\) en el modelo de competencia monopolística dado en clase, suponiendo que las firmas que entran obtienen su productividad de la misma distribución y la restricción de recursos humanos

\[
M c_e + L = N
\]

## Parte II: Elección Ocupacional con Agentes Heterogéneos

Hay una masa unitaria de agentes. Cada agente extrae un par

\[
(z_1, z_2) \sim N(\mu, \Sigma), \quad
\mu =
\begin{pmatrix}
\mu_1 \\
\mu_2
\end{pmatrix}, \quad
\Sigma =
\begin{pmatrix}
\sigma_1^2 & \rho \sigma_1 \sigma_2 \\
\rho \sigma_1 \sigma_2 & \sigma_2^2
\end{pmatrix}.
\]

Tras observar \((z_1, z_2)\), cada agente elige ser trabajador o emprendedor.

**Trabajadores.** Un agente que trabaja ofrece \(h = e^{z_1}\) unidades de capital humano en un mercado competitivo al salario \(w\) por unidad, obteniendo ingreso \(V_W = w e^{z_1}\).

**Emprendedores.** Un agente que se convierte en emprendedor con realización \(z_2\) contrata \(H \geq 0\) unidades de capital humano y produce:

\[
y = e^{z_2} H^\alpha, \quad \alpha \in (0, 1).
\]

Tomando \(w\) como dado, el emprendedor maximiza el beneficio \(\pi = e^{z_2}H^\alpha - wH\) sobre \(H\).

**Equilibrio.** Un equilibrio competitivo es un salario \(w^*\) tal que cada agente elige óptimamente una ocupación y el mercado de capital humano se vacía:

\[
\underbrace{\int_{E(w)^c} e^{z_1}\, dF(z_1, z_2)}_{\text{oferta de trabajadores}}
=
\underbrace{\int_{E(w)} H^*(z_2; w)\, dF(z_1, z_2)}_{\text{demanda de emprendedores}},
\]

donde \(F\) es la función de distribución acumulada normal conjunta, \(H^*(z_2; w)\) es la demanda óptima de capital humano del emprendedor y \(E(w)\) denota el conjunto de agentes que eligen el emprendimiento.

### Problema 2 (Elección ocupacional y condición de ordenamiento).

(a) Un agente elige el emprendimiento si y solo si \(\pi(z_2; w) \geq V_W(z_1)\). Para un salario \(w\) fijo, encuentre las regiones del plano \((z_1, z_2)\) que definen la elección de emprendimiento.

(b) ¿Cómo cambian estas regiones en función del salario \(w\)?

(c) Usando el teorema de la función implícita aplicado a la condición de vaciamiento del mercado, determine el signo de \(dw^*/d\alpha\). Proporcione una interpretación económica.

### Problema 3 (Equilibrio y vaciamiento del mercado).

(a) Escriba explícitamente la condición de equilibrio del mercado como una única ecuación en \(w\). Argumente que el lado izquierdo (oferta de capital humano) es estrictamente creciente en \(w\) y el lado derecho (demanda de capital humano) es estrictamente decreciente en \(w\), estableciendo así la existencia y unicidad del equilibrio.

(b) Suponga que \(\mu_2\) aumenta (los emprendedores se vuelven en promedio más productivos). Determine el efecto sobre \(w^*\). ¿Cuál es el efecto sobre la segmentación de la población entre trabajadores y emprendedores? ¿Y sobre el producto agregado? Proporcione un argumento intuitivo para este resultado.

(c) Realice el mismo análisis para un aumento en \(\mu_1\).

(d) Usando los siguientes valores \(\mu_1 = \mu_2 = 0\), \(\sigma_1 = \sigma_2 = 1\) y \(\rho = 0.5\) resolver el modelo numericamente para distintos valores de \(\alpha\). Describir los resultados lo mas detalladamente posible y dar una intuición.

(e) Usando los mismos valores fijando \(\alpha = 2/3\), resolver para distintos valores de \(\rho\). Describir los resultados lo mas detalladamente posible y dar una intuición.

## Parte III: Educación y Desarrollo

Consider la siguiente versión simplificada del modelo de Queiro.

**Bien final.** El producto agregado es una cesta CES de un continuo de variedades intermedias:

\[
Y = \left(\int y(\omega)^{\frac{\sigma - 1}{\sigma}}\, d\omega\right)^{\frac{\sigma}{\sigma - 1}}, \quad \sigma > 1,
\]

con índice de precios normalizado a uno, \(P = 1\). Cada variedad enfrenta una demanda \(y_i = Y p_i^{-\sigma}\).

**Emprendedores y trabajadores.** Hay una medida \(M\) de emprendedores y una medida \(N\) de trabajadores, con \(M = N\) (normalización). Cada trabajador en el país \(c\) ofrece \(h_c = e^{\bar r \bar s_c}\) unidades de capital humano (\(\bar r = 0.08\)). Los emprendedores se dividen en cuatro grupos de escolaridad \(i \in \{0, 1, 2, 3\}\) — sin escolaridad, primaria (6 años), secundaria (12 años), superior (17 años) — y \(\theta_{i,c}\) es la fracción de emprendedores con escolaridad \(s_i\).

**Producción.** Un emprendedor con escolaridad \(s_i\) contrata capital \(K_i\) y capital humano \(H_i\) para producir:

\[
y_i = Z_i K_i^\gamma H_i^{1-\gamma}, \quad \gamma = \frac{1}{3}.
\]

El capital se alquila a tasa mundial exógena \(\rho\); el capital humano se contrata al salario competitivo \(w\).

**Productividad emprendedora.** Los valores \(Z_i\) se derivan de Queiró (2022). Sus estimaciones estructurales implican una log-productividad promedio en estado estacionario \(z_i = \ln Z_i\) para emprendedores con escolaridad \(s_i\):

| Grupo de escolaridad | \(s_i\) | \(z_i\) | \(Z_i = e^{z_i}\) | \(h_i = e^{0.08s_i}\) |
|---|---:|---:|---:|---:|
| Sin escolaridad | 0 | 0.28 | 1.32 | 1.00 |
| Primaria | 6 | 0.60 | 1.83 | 1.62 |
| Secundaria | 12 | 0.93 | 2.53 | 2.61 |
| Superior | 17 | 1.20 | 3.32 | 3.90 |

Se utiliza \(\sigma = 3\) en todos los ejercicios, siguiendo a Queiró (2022) y Hsieh–Klenow (2009).

Para esta sección se utilizará el modelo de la Parte I, cuya función de producción agregada es:

\[
\ln \frac{Y_c}{N_c}
= \ln A_c + \frac{\gamma}{1 - \gamma}\ln \frac{K_c}{Y_c} + \bar r \bar s_c,
\quad
A_c \propto \left(\sum_i \theta_{i,c} Z_i^2\right)^{1/2}.
\]

A efectos de este ejercicio, el termino \(\bar r\bar s_c\) es el capital humano promedio reportado en la Penn World Table.

### Problema 4 (Ejercicio empírico de contabilidad del desarrollo).

Para este ejercicio utilice los datos de Penn World Tables y los datos de logro educativo de Barro–Lee que se proporcionan. Elija el año más reciente disponible en los datos de Barro–Lee y el mismo año en PWT. Calcule las participaciones de cada componente del logro educativo:

- Sin escolaridad: fracción sin escolaridad completada.
- Primaria: primaria incompleta y completa.
- Secundaria: secundaria incompleta y completa.
- Superior: educación superior incompleta y completa.

En todo el problema suponga que el numero de firmas per capita es el mismo en todas las economias. Suponga ademas, que la distribucion de la educacion de los empresarios (i.e.. firmas) es la misma que en toda la poblacion del pais.

(a) Grafique el logaritmo del ingreso per cápita en los datos contra el explicado por el modelo. Repítalo para un valor calculado sin incluir el término de productividad agregada (incluyendo solo el capital físico y el capital humano de los trabajadores).

(b) Tomando logaritmos de todas las variables, realice la descomposición de varianza: participación de la productividad de las firmas, el factor capital, el capital humano y el residuo.

(c) ¿Cuál es la participación total de las diferencias de educación entre países en este cálculo? ¿Cómo se compara con el rol del capital humano solo, sin considerar su efecto sobre la productividad de las firmas?

---

## Notas sobre imágenes / elementos visuales

No hay imágenes, gráficos o diagramas sustantivos en el documento. Los elementos visuales relevantes son ecuaciones y una tabla de productividad emprendedora, transcritas arriba en LaTeX/Markdown.
