# Práctica: Capital Humano y Tecnología

Hugo Hopenhayn  
UTDT  
Desarrollo Económico  
2026

Hemos visto en clase dos razones por las cuales las diferencias de capital humano pueden no estar bien contabilizadas. La primera es que la calidad de la educación puede estar afectada por la productividad de la economía. La otra es que la educación puede afectar la adopción de las tecnologías de frontera. A su vez, también vimos que el nivel de TFP puede estar afectado por las tecnologías en uso y que los países mas pobres usan tecnologías mas viejas. Los ejercicios dados en este práctico ilustran ambos canales.

## 1. Medición del Capital Humano y Desarrollo

Considere la función de producción de capital humano presentada en clase (modelo de Manuelli-Seshadri):

$$
h = s^{\eta} e^{\gamma}
$$

donde $s$ son los años de escolaridad y $e$ bienes. Suponga que los valores de la Penn World Table $h_{pwt} = s^{\eta}(1 - s)$ (o sea suponen $\gamma = 0$.) Usando distintos valores de $\gamma$, recalcule el capital humano (usando las condiciones de primer orden) y el nivel de $A$ respectivo de cada país. Luego recalcule la descomposición de varianza del ingreso per capita para cada caso. Explique sus resultados. (Ayuda: Utilice la expresión para el salario $w_c = (1 - \alpha)z_c$, donde $z_c = A(K/Y)^{\frac{\alpha}{1-\alpha}}$ y considere que el agente representativo maximiza el ingreso, neto de gastos en educación).

## 2. Frontera Tecnológica y Capital Humano

Tomar como base el modelo discutido en clase, donde la frontera tecnológica del país $A_c$ (la que calcularon en el Problema 1) depende del capital humano del país $(h_c)$ y la frontera tecnológica de Estados Unidos $(A_{us})$ según:

$$
A_c = \hat{A}_c \left(\frac{h_c}{h_{us}}\right)^{\gamma} A_{us}
$$

El objetivo de este trabajo es: Calcular el valor de $\hat{A}_c$ para cada país y luego hacer una nueva descomposición de varianza de las diferencias de ingreso por trabajador. Los pasos a seguir son:

1. Usar los datos suministrados para estimar los parámetros $\hat{A}_c$ de cada país

2. Expresar el output por trabajador del país $c$ relativo al de Estados Unidos $y_c/y_{us}$ como función de: $\hat{A}_c$, los factores de capital relativos (país $c$ dividido US) y los niveles de capital humano relativos.

3. Hacer una descomposición de varianza de $y_c/y_{us}$ en las covarianzas respectivas con $\hat{A}_c$, los factores de capital relativos y los niveles de capital humano relativos y calcular la fracción del total explicada por $\hat{A}_c$.

4. Comparar los resultados con la descomposición de varianza original obtenida en el Problema 1.

## 3. Tecnologías en uso y TFP

1. Supongamos que $A_t/A_{t-1} = 1{,}02$ lo que es consistente con una tasa general de crecimiento del ingreso per capita de $2\%$ anual. Cuánto mas viejas debieran ser las tecnologías utilizadas por el percentil 10 vs. el 90?

2. Supongamos que que $A_t/A_{t-1} = 1{,}02$, que la relacion $K/Y$ de un país se mantiene fija y la tasa de depreciación del capital es $5\%$ anual (es la media utilizada en las Penn world tables). Calcule la TFP de esta economía relativa a la tecnología de frontera.

## Imágenes / figuras importantes

No hay gráficos, imágenes sustantivas ni diagramas en este documento. El contenido visual relevante son ecuaciones integradas en el texto, transcritas arriba en LaTeX.
