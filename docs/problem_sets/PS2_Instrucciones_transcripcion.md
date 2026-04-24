# Práctica: Problemas de Contabilidad del Desarrollo usando la Penn World Table

Hugo Hopenhayn  
UTDT  
Desarrollo Económico  
2026

## 1. Introducción

La contabilidad del desarrollo busca entender las fuentes de las diferencias de ingreso entre países descomponiendo el producto por trabajador en contribuciones del capital físico, capital humano y productividad total de factores (PTF). Este conjunto de problemas utiliza datos de Penn World Table (PWT) para realizar este análisis bajo diferentes supuestos sobre la participación del capital y la producción de capital humano.

## 2. Requerimientos de Datos

Se utilizarán las siguientes variables de Penn World Table (versión más reciente) y datos de nivel de escolaridad media de :

- `rgdpo`: PIB real a precios nacionales constantes de 2017 ajustado por PPA (en millones de USD 2017)
- `emp`: Número de personas empleadas (en millones)
- `cn`: Stock de Capital a precios nacionales constantes de 2017 ajustada por PPA (en millones de USD 2017)
- `hc`: Índice de capital humano (basado en años de escolaridad y retornos a la educación)
- `pop`: Población (en millones)

## 3. Marco Teórico

Considere la función de producción agregada:

$$
Y = K^\alpha \times (Ah \times L)^{1-\alpha}
\tag{1}
$$

Donde:

- $Y$ = producto
- $A$ = productividad total de factores (PTF)
- $K$ = stock de capital físico
- $h$ = capital humano por trabajador
- $L$ = número de trabajadores
- $\alpha$ = parámetro de participación del capital

El producto por trabajador puede escribirse como:

$$
y = \frac{Y}{L} = A \times \left(\frac{K}{Y}\right)^{\frac{\alpha}{1-\alpha}} \times h
\tag{2}
$$

Tomando logaritmos:

$$
\ln(y) = \ln(A) + \frac{\alpha}{1-\alpha} \times \ln\left(\frac{K}{Y}\right) + \ln(h)
\tag{3}
$$

## 4. Problema 1: Contabilidad del Desarrollo Estándar ($\alpha = 1/3$)

### 4.1. Parte A: Preparación de Datos y Cálculo de Importancia de PTF

1. Utilize los datos suministrados en la hoja de calculo `data.xls`
2. Calcule el producto por trabajador: $y = \text{rgdpo}/\text{emp}$
3. Calcule la razón capital-producto: $K/Y = \text{cn}/\text{rgdpo}$
4. Transforme la razón capital-producto: $\text{factor capital} = (K/Y)^{\alpha/(1-\alpha)}$ donde $\alpha = 1/3$
5. Calcule la PTF usando la identidad contable:

$$
A = \frac{y}{\text{factor capital} \times h}
\tag{4}
$$

   o en logaritmos: $\ln(A) = \ln(y) - \ln(\text{factor capital}) - \ln(h)$

6. Calcule la contribución de la PTF en cada país según la metodología explicada en clase y haga un plot de esta variable con respecto al producto por trabajador relativo al de Estados Unidos.

### 4.2. Parte B: Descomposición de Varianza

1. Calcule la varianza del logaritmo del producto por trabajador: $\operatorname{var}(\ln(y))$
2. Calcule las covarianzas:

$$
\operatorname{cov}(\ln(y), \ln(\text{factor capital}))
$$

$$
\operatorname{cov}(\ln(y), \ln(h))
$$

$$
\operatorname{cov}(\ln(y), \ln(A))
$$

3. Verifique la identidad contable:

$$
\operatorname{var}(\ln(y)) = \operatorname{cov}(\ln(y), \ln(\text{factor capital})) + \operatorname{cov}(\ln(y), \ln(h)) + \operatorname{cov}(\ln(y), \ln(A))
\tag{5}
$$

4. Calcule la contribución de cada factor como porcentaje de la varianza total:

$$
\text{Contribución del capital físico: } \frac{\operatorname{cov}(\ln(y), \ln(\text{factor capital}))}{\operatorname{var}(\ln(y))} \times 100\%
$$

$$
\text{Contribución del capital humano: } \frac{\operatorname{cov}(\ln(y), \ln(h))}{\operatorname{var}(\ln(y))} \times 100\%
$$

$$
\text{Contribución de la PTF: } \frac{\operatorname{cov}(\ln(y), \ln(A))}{\operatorname{var}(\ln(y))} \times 100\%
$$

### 4.3. Parte C: Preguntas de Análisis

1. ¿Qué factor contribuye más a las diferencias de ingreso entre países?
2. ¿Cómo se comparan sus resultados con los reportados en clase?

## 5. Problema 2: Sensibilidad a la Participación del Capital ($\alpha$ Variable)

### 5.1. Parte A: Marco Teórico

Considere cómo cambia la descomposición cuando permitimos que la participación del capital $\alpha$ varíe entre países o tome diferentes valores. Examinará $\alpha \in \{1/4, 1/2, 3/4\}$.

### 5.2. Parte B: Recalcular la Contabilidad del Desarrollo

Para cada valor de $\alpha$:

1. Recalcule el factor capital: $\text{factor capital} = (K/Y)^{\alpha/(1-\alpha)}$
2. Recalcule la PTF: $A = y/(\text{factor capital} \times h)$
3. Realice la descomposición de varianza como en el Problema 1, Parte B.
4. Cree una tabla mostrando cómo cambian las contribuciones:

| Valor de $\alpha$ | Capital Físico (%) | Capital Humano (%) | PTF (%) |
|---:|---:|---:|---:|
| $1/4$ |  |  |  |
| $1/2$ |  |  |  |
| $3/4$ |  |  |  |

**Cuadro 1:** Descomposición de varianza para diferentes valores de $\alpha$

### 5.3. Parte C: Preguntas de Análisis

1. ¿Cómo afecta el incremento de $\alpha$ la importancia relativa del capital físico versus la PTF?
2. Discuta las implicaciones para la política de desarrollo bajo diferentes supuestos sobre $\alpha$.

## Imágenes / figuras importantes

No hay gráficos, imágenes sustantivas ni diagramas en este documento. El contenido visual relevante es una tabla esperada de resultados en la sección 5.2, transcrita arriba en formato Markdown.
