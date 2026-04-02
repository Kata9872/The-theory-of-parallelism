import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('result.csv')

df['Ep'] = df['Sp'] / df['p']
df['Metric'] = df['Sp'] * df['Ep']  # = Sp² / p

threads = [1, 2, 4, 7, 8, 16, 20, 40]

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

df_20k = df[df['N'] == 20000]
df_40k = df[df['N'] == 40000]

axes[0].plot(df_20k['p'], df_20k['Sp'], 'o-', linewidth=2, label='N = 20 000', markersize=6)
axes[0].plot(df_40k['p'], df_40k['Sp'], 's-', linewidth=2, label='N = 40 000', markersize=6)
axes[0].plot(threads, threads, '--', color='gray', linewidth=2, label='Линейное (идеал)')
axes[0].set_xlabel('Число потоков (p)', fontsize=11)
axes[0].set_ylabel('Ускорение (Sp)', fontsize=11)
axes[0].set_title('Ускорение от числа потоков', fontsize=12)
axes[0].set_xticks(threads)
axes[0].grid(True, alpha=0.3, linestyle=':')
axes[0].legend()

axes[1].plot(df_20k['p'], df_20k['Ep'], 'o-', linewidth=2, label='N = 20 000', markersize=6)
axes[1].plot(df_40k['p'], df_40k['Ep'], 's-', linewidth=2, label='N = 40 000', markersize=6)
axes[1].axhline(y=1.0, color='gray', linestyle='--', linewidth=2, label='Идеал (E=1)')
axes[1].set_xlabel('Число потоков (p)', fontsize=11)
axes[1].set_ylabel('Эффективность (Ep)', fontsize=11)
axes[1].set_title('Эффективность от числа потоков', fontsize=12)
axes[1].set_xticks(threads)
axes[1].grid(True, alpha=0.3, linestyle=':')
axes[1].legend()

axes[2].plot(df_20k['p'], df_20k['Metric'], 'o-', linewidth=2, label='N = 20 000', markersize=6)
axes[2].plot(df_40k['p'], df_40k['Metric'], 's-', linewidth=2, label='N = 40 000', markersize=6)

opt_p_20k = df_20k.loc[df_20k['Metric'].idxmax(), 'p']
opt_p_40k = df_40k.loc[df_40k['Metric'].idxmax(), 'p']
max_20k = df_20k['Metric'].max()
max_40k = df_40k['Metric'].max()

axes[2].axvline(x=opt_p_20k, color='blue', linestyle='--', alpha=0.5, label=f'Оптимум 20k: p={int(opt_p_20k)}')
axes[2].axvline(x=opt_p_40k, color='orange', linestyle='--', alpha=0.5, label=f'Оптимум 40k: p={int(opt_p_40k)}')
axes[2].plot(opt_p_20k, max_20k, 'o', color='blue', markersize=10, zorder=5)
axes[2].plot(opt_p_40k, max_40k, 's', color='orange', markersize=10, zorder=5)

axes[2].set_xlabel('Число потоков (p)', fontsize=11)
axes[2].set_ylabel('Sp × Ep', fontsize=11)
axes[2].set_title('Комбинированная метрика (оптимум = максимум)', fontsize=12)
axes[2].set_xticks(threads)
axes[2].grid(True, alpha=0.3, linestyle=':')
axes[2].legend()

plt.tight_layout()
plt.savefig('speedup(10)_task1.png', dpi=300, bbox_inches='tight')
plt.show()

with open('task1_stats.txt', 'w', encoding='utf-8') as f:
    f.write("Статистика — Задание 1 (умножение матрицы на вектор)\n")
    f.write("="*70 + "\n\n")
    for N, df_n, opt_p, max_metric in [(20000, df_20k, opt_p_20k, max_20k), 
                                        (40000, df_40k, opt_p_40k, max_40k)]:
        f.write(f"Размер матрицы: {N}×{N}\n")
        f.write(df_n[['p', 't', 'Sp', 'Ep', 'Metric']].to_string(index=False) + "\n")
        f.write(f"Оптимальное количество потоков: {int(opt_p)} (Sp×Ep = {max_metric:.2f})\n\n")
