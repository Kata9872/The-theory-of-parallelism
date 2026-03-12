import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('result.csv')

plt.figure(figsize=(10, 6))

plt.plot(df['p'], df['Sp'], 'o-', linewidth=2, label='nsteps = 40 000 000', markersize=6)

p_vals = [1, 2, 4, 7, 8, 16, 20, 40]
plt.plot(p_vals, p_vals, '--', color='gray', linewidth=2, label='Linear (ideal)')

plt.xlabel('Number of threads (p)', fontsize=12)
plt.ylabel('Speedup (Sp)', fontsize=12)
plt.title('Parallel Integration: Speedup vs Threads', fontsize=14)
plt.xticks([1, 2, 4, 7, 8, 16, 20, 40])
plt.yticks(range(0, 41, 5))
plt.grid(True, alpha=0.3, linestyle=':')
plt.legend()
plt.tight_layout()

plt.savefig('speedup.png', dpi=300, bbox_inches='tight')
plt.show()
