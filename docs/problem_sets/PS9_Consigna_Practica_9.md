# Trabajo Practico 9

1. De la base de datos [Financial Development](https://www.worldbank.org/en/publication/gfdr/data/global-financial-development-database) del Banco Mundial, seleccione para el año 2019 para cada pais la variable DI.14 Domestic credit to private sector (% of GDP). Combinar usando el codigo de pais con las medidas de producto por trabajador y PTF calculado en practicos anteriores. Hacer graficos comparando el producto por trabajador y la PTF (relativos a USA) vs Domestic credit to private sector (% of GDP). Hacer las regresiones respectivas.

Para las siguientes preguntas, usaran esta version simplificada del modelo de Moll. Hay una distribucion $F(z)$ de la productividad de los emprendedores. En esta economia hay un solo insumo, capital, de modo que la funcion de produccion es $y(z,k) = zk$. El stock agregado de capital es $K$. Los activos del empresario son $a(z)$,de modo que $\int a(z)dF(z) = K$. Para simplificar los calculos, normalizamos el total de capital $K = 1$ y la masa total de empresarios igual a $1$. La restriccion financiera de un emprendedor es $k(z) \leq \lambda a(z)$.

2 Considere el modelo simplificado de Ben Moll. Suponga que la distribucion de productividades es uniforme entre 0 y 1. Considere tres casos. En el primero todos los empresarios tienen los mismos activos $a(z) = 1$. En el segundo caso Los activos correspondientes de cada empresa son $a(z) = 2z$ y en tercero $a(z) = 3z^2$. Calcule la fraccion de emprendedores y el ingreso total para $\lambda = 1$ y $\lambda = 2$ en cada caso. Interprete los resultados.

3 Tomar el modelo simple dado en clase: distribucion uniforme de $z$ entre 0 y 1, activos iniciales iguales para todos los emprendedores y $\lambda = 2$.

   (a) Calcule el equilibrio inicial.

   (b) Ahora suponga que cada emprendedor ahorra todo su beneficio (producto despues de pagar su deuda por el capital ajeno utilizado). Sumando este ahorro a los activos iniciales, esto define los activos finales.

   (c) Ahora calcule nuevamente el equilibrio pero con los niveles de activos nuevos. Calcule la fraccion de emprendedores activos, el precio del capital y el output total.

   (d) Vuelva al paso (b) y continue iterando, generando una secuencia con los resultados de cada periodo (emprendedores activos, el precio del capital y el output total).

   (e) Que conclusiones saca de este ejercicio?

4 Suponga ahora que la distribucion de productividad es Pareto con $z_0 = 1$ y coeficiente $\zeta$, o sea que $1 - F(z) = z^{-\zeta}$. Suponga que $a(z) = 1$. Derive una expresion para el output total como funcion de $\lambda$. Derive una expresion para el grado de desarrollo financiero. Es creciente en $\lambda$?