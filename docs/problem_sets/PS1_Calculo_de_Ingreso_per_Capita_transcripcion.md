# Práctica: Análisis de Desigualdad Internacional usando la Penn World Table

Hugo Hopenhayn  
UTDT  
Desarrollo Económico  
2026

## 1. Objetivo

Calcular y comparar las ratios de desigualdad internacional utilizando diferentes medidas de ingreso y denominadores, empleando datos de la Penn World Table (PWT).

## 2. Recursos necesarios

### 2.1. Base de datos

Penn World Table 10.01: <https://www.rug.nl/ggdc/productivity/pwt/>

Descarga directa: <https://dataverse.nl/dataset.xhtml?persistentId=doi:10.34894/QT5BCC>

### 2.2. Variables clave de la PWT

`rgdpe`: PIB real ajustado por PPA (gasto)  
`rgdpna`: PIB real a precios nacionales  
`pop`: Población total  
`emp`: Empleo total

## 3. Instrucciones

### 3.1. Parte 1: Preparación de los datos

1. Descarga la Penn World Table en formato Excel o CSV (o algún otro que elijan) desde el enlace proporcionado
2. Selecciona el año más reciente disponible (probablemente 2019 o 2020)
3. Filtra los países que tengan datos completos para todas las variables necesarias

---

### 3.2. Parte 2: Cálculo de medidas de ingreso

#### 3.2.1. A. Ingreso per cápita ajustado por PPA

$$
\text{ingreso ppa pc} = \frac{\text{rgdpe}}{\text{pop}}
\tag{1}
$$

#### 3.2.2. B. Ingreso per cápita a tipos de cambio corrientes

$$
\text{ingreso tc pc} = \frac{\text{rgdpna}}{\text{pop}}
\tag{2}
$$

#### 3.2.3. C. Ingreso por trabajador ajustado por PPA

$$
\text{ingreso ppa trab} = \frac{\text{rgdpe}}{\text{emp}}
\tag{3}
$$

#### 3.2.4. D. Ingreso por trabajador a tipos de cambio corrientes

$$
\text{ingreso tc trab} = \frac{\text{rgdpna}}{\text{emp}}
\tag{4}
$$

### 3.3. Parte 3: Identificación de percentiles

1. Para cada una de las 4 medidas calculadas:
   - Ordena los países de mayor a menor ingreso
   - Identifica el top 10 % (los países más ricos)
   - Identifica el bottom 10 % (los países más pobres)
2. Cálculo de promedios:
   - Calcula el promedio del ingreso del top 10 %
   - Calcula el promedio del ingreso del bottom 10 %

### 3.4. Parte 4: Cálculo de ratios

Para cada medida, calcula la ratio:

$$
\text{Ratio} =
\frac{\text{Promedio del top 10 \%}}{\text{Promedio del bottom 10 \%}}
\tag{5}
$$

### 3.5. Parte 5: Análisis y presentación de resultados

#### 3.5.1. Tabla de resultados esperada

| Medida | Top 10 % (promedio) | Bottom 10 % (promedio) | Ratio |
|---|---:|---:|---:|
| PIB pc (PPA) |  |  |  |
| PIB pc (TC) |  |  |  |
| PIB por trabajador (PPA) |  |  |  |
| PIB por trabajador (TC) |  |  |  |

Cuadro 1: Resultados del análisis de desigualdad internacional

#### 3.5.2. Preguntas de análisis

1. ¿Qué ratio es mayor: la basada en PPA o la basada en tipos de cambio? ¿Por qué?
2. ¿Cómo se comparan las ratios usando población versus empleo como denominador?
3. ¿Qué países aparecen consistentemente en el top 10 % y bottom 10 %?
4. ¿Qué medida consideras más apropiada para medir la desigualdad internacional y por qué?

## 4. Entregables

1. Hoja de cálculo o equivalente con todos los cálculos realizados
2. Tabla resumen con las 4 ratios calculadas
3. Análisis escrito (500-750 palabras) respondiendo a las preguntas planteadas
4. Lista de países que conforman el top 10 % y bottom 10 % para cada medida

## 5. Recursos adicionales

Manual de la PWT: <https://www.rug.nl/ggdc/docs/pwt_100_user_guide.pdf>

Documentación de variables: Consulta la pestaña “Variable definitions” en el archivo de la PWT

Fecha de entrega: [Completar con fecha específica]

Formato de entrega: Archivo Excel/CSV + documento PDF con análisis

---

## Notas sobre imágenes / elementos visuales importantes

No hay imágenes, diagramas ni gráficos sustantivos en el documento. El único elemento visual importante es el **Cuadro 1**, transcrito arriba como tabla Markdown.
