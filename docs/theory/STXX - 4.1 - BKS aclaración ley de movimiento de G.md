# Distribución Conjunta y Dinámica del Talento

$G_t(a,z)$: CDF conjunta de riqueza y talento en el período $t$. $\mu(z)$: CDF marginal del talento (Pareto, parámetro $\eta$).

En cada período, el talento evoluciona de forma independiente de la riqueza:

## Retención (prob. $\gamma$)

$$
z_{t+1} = z_t
$$

El talento se conserva.

## Remuestreo (prob. $1-\gamma$)

$$
z_{t+1} \sim \mu(z), \text{ indep. de } z_t
$$

Nuevo talento i.i.d.

Implica:

Cuando el talento se remuestrea, $z_{t+1}$ es independiente de $a_{t+1}$ y de $z_t$, lo que permite que $\mu(z)$ factorice en la ley de movimiento.

---

# Ley de Movimiento de $G_t(a,z)$

## Conjunto de estados predecesores

$$
A_t(a,z)
\equiv
\{(a_t,z_t): a_{t+1}(a_t,z_t) \leq a \text{ y } z_t \leq z\}
$$

## Ley de movimiento

$$
G_{t+1}(a,z)
=
\gamma
\underbrace{
\int_{A_t(a,z)} G_t(da_t,dz_t)
}_{\text{talento retenido: } z_{t+1}=z_t\leq z}
+
(1-\gamma)\mu(z)
\underbrace{
\int_{A_t(a,\infty)} G_t(da_t,dz_t)
}_{\text{talento remuestreado: } \Pr(z_{t+1}\leq z)=\mu(z)}
$$

- Primer término: talento retenido — $z_t \leq z$ requerido, se integra sobre $A_t(a,z)$.

- Segundo término: $\mu(z)$ factoriza por independencia de $z_{t+1}$ respecto a $z_t$.

- Equilibrio estacionario: punto fijo $G_{t+1} = G_t = G$, con precios y política constantes; $A_t$ colapsa a $A$.