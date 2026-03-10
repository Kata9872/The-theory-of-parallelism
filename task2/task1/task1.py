import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('result.csv')

plt.figure(figsize=(10, 6))

df_20k = df[df['N'] == 20000]
df_40k = df[df['N'] == 40000]

plt.plot(df_20k['p'], df_20k['Sp'], 'o-', linewidth=2, label='N = 20 000', markersize=6)
plt.plot(df_40k['p'], df_40k['Sp'], 's-', linewidth=2, label='N = 40 000', markersize=6)

# линия идеального ускорения
p_vals = [1, 2, 4, 7, 8, 16, 20, 40]
plt.plot(p_vals, p_vals, '--', color='gray', linewidth=2, label='Linear')

plt.xlabel('p', fontsize=12)
plt.ylabel('Sp', fontsize=12)
plt.xticks([1, 2, 4, 7, 8, 16, 20, 40])
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig('speedup.png', dpi=300, bbox_inches='tight')
plt.show()