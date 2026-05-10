import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import statsmodels.api as sm

# PUNTO (A)

excel_file_path = '../../../data/firms_misallocation_10000.xlsx'
df = pd.read_excel(excel_file_path, sheet_name="Sheet 1")
# quitar ultima linea que es un total
df = df.iloc[:-1]

alpha = 2/3
df = df.rename(columns={'Empleo': 'n', 'Output': 'y'})
df['z']    = df['y'] / (df['n']**alpha)
df['TFPR'] = df['y'] / df['n']

df['log_z']    = np.log(df['z'])
df['log_TFPR'] = np.log(df['TFPR'])

# histogramas
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# ln(z)
plt.figure(figsize=(10, 6))
plt.hist(df['log_z'].dropna(), bins=50, edgecolor='black', alpha=0.7, color='salmon')
plt.title('Distribución de ln(TFPi)', fontsize=16)
plt.xlabel('log(z)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'log_TFP_histogram.pdf'), format='pdf', bbox_inches='tight')
plt.close()

# ln(TPFR)
plt.figure(figsize=(10, 6))
plt.hist(df['log_TFPR'].dropna(), bins=50, edgecolor='black', alpha=0.7)
plt.title('Distrbución de ln(TFPRi)', fontsize=16)
plt.xlabel('log(TFPR)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'log_TFPR_histogram.pdf'), format='pdf', bbox_inches='tight')
plt.close()

# superpuesto
plt.figure(figsize=(12, 7))

min_val = min(df['log_z'].min(), df['log_TFPR'].min())
max_val = max(df['log_z'].max(), df['log_TFPR'].max())
bins = np.linspace(min_val, max_val, 70)

plt.hist(df['log_TFPR'].dropna(), bins=bins, edgecolor='black', alpha=0.5, label='log(TFPR)', color='skyblue')
plt.hist(df['log_z'].dropna(), bins=bins, edgecolor='black', alpha=0.5, label='log(TFP)', color='salmon')

plt.title('Distribución conjunta de log(TFPi) y log(TFPRi)', fontsize=16)
plt.xlabel('Log Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(fontsize=10)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'joint_log_histograms.pdf'), format='pdf', bbox_inches='tight')
plt.close()

print(f"PDF figures saved to '{output_dir}' directory.")

# estadisticos
mean_log_tfpr = df['log_TFPR'].mean()
variance_log_tfpr = df['log_TFPR'].var()

print(f"\nMean of log(TFPR): {mean_log_tfpr:.4f}")
print(f"Variance of log(TFPR): {variance_log_tfpr:.4f}")

# INCISO (C)

Ydist = df['y'].sum()
M = len(df)
N = df['n'].sum()

TFPdist = Ydist / (M**(1 - alpha) * N**alpha)

print(f"\nTotal Output (Ydist): {Ydist:.4f}")
print(f"Number of Firms (M): {M}")
print(f"Total Employment (N): {N:.4f}")
print(f"Aggregate Productivity, distorted (TFPdist): {TFPdist:.4f}")

Zden = (df['z']**(1/(1-alpha))).sum()

df['n_opt'] = N * (df['z']**(1/(1-alpha))) / Zden

print(f"\nZden: {Zden:.4f}")
print("\nDataFrame with n_opt column:")
print(df.head())

Yopt = (df['z'] * (df['n_opt']**alpha)).sum()
TFPopt = Yopt / (M**(1 - alpha) * N**alpha)

print(f"\nTotal Optimal Output (Yopt): {Yopt:.4f}")
print(f"Aggregate Productivity, optimal (TFPopt): {TFPopt:.4f}")

PoGa = ((TFPopt - TFPdist) / TFPdist) * 100
print(f"\nPotential Gains (PoGa): {PoGa:.3f}%")

# la constante C
C = N / Zden
ln_C = np.log(C)

df['log_n'] = np.log(df['n'])

# plot holder
plt.figure(figsize=(10, 6))

# plot (1): scatter
plt.scatter(df['log_z'], df['log_n'], alpha=0.6, label='Asignación distorsionada', s=20)

# plot (2): linea

# puntos para la linea
# ln(n) = ln(C) + (1/(1-alpha)) * ln(z)
# alpha = 2/3, 1/(1-alpha) = 1/(1/3) = 3
# => ln(n) = ln(C) + 3 * ln(z)
log_z_min = df['log_z'].min()
log_z_max = df['log_z'].max()
log_z_range = np.linspace(log_z_min, log_z_max, 100)
log_n_optimal_line = ln_C + (1/(1-alpha)) * log_z_range
plt.plot(log_z_range, log_n_optimal_line, color='red', linestyle='--', linewidth=2, label='Asignación óptima')

# mostrar plot
plt.title('Asignación de Empleo vs Productividad', fontsize=16)
plt.xlabel('ln(z)', fontsize=12)
plt.ylabel('ln(n)', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'n_vs_z_allocation.pdf'), format='pdf', bbox_inches='tight')
plt.close()

print(f"Allocation plot saved to '{output_dir}/n_vs_z_allocation.pdf'")

# regresion para probar
df_reg = df[['log_n', 'log_z']].dropna()

X = df_reg['log_z']
y = df_reg['log_n']

X = sm.add_constant(X)
model = sm.OLS(y, X)
results = model.fit()

print("\n--- Regression Results: observed log(n) = a + b * log(z) + u ---")
print(results.summary())

theoretical_b = 1 / (1 - alpha)
print(f"\nTheoretical optimal value for 'b' (1/(1-alpha)): {theoretical_b:.4f}")
print(f"Estimated observed value for 'b': {results.params['log_z']:.4f}")
print(f"Difference: {results.params['log_z'] - theoretical_b:.4f}")

# LO ULTIMO
correlation_log_tfpr_log_z = df['log_TFPR'].corr(df['log_z'])
print(f"\nCorrelation between log(TFPR) and log(z): {correlation_log_tfpr_log_z:.4f}")