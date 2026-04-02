import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('result.csv')

df['Ep'] = df['Sp'] / df['p']
df['Metric'] = df['Sp'] * df['Ep']

threads = [1, 2, 4, 7, 8, 16, 20, 40]

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

axes[0].plot(df['p'], df['Sp'], 'o-', linewidth=2, label='nsteps = 40 000 000', markersize=6)
axes[0].plot(threads, threads, '--', color='gray', linewidth=2, label='Линейное (идеал)')
axes[0].set_xlabel('Число потоков (p)', fontsize=11)
axes[0].set_ylabel('Ускорение (Sp)', fontsize=11)
axes[0].set_title('Ускорение от числа потоков', fontsize=12)
axes[0].set_xticks(threads)
axes[0].grid(True, alpha=0.3, linestyle=':')
axes[0].legend()

axes[1].plot(df['p'], df['Ep'], 'o-', linewidth=2, label='nsteps = 40 000 000', markersize=6)
axes[1].axhline(y=1.0, color='gray', linestyle='--', linewidth=2, label='Идеал (E=1)')
axes[1].set_xlabel('Число потоков (p)', fontsize=11)
axes[1].set_ylabel('Эффективность (Ep)', fontsize=11)
axes[1].set_title('Эффективность от числа потоков', fontsize=12)
axes[1].set_xticks(threads)
axes[1].grid(True, alpha=0.3, linestyle=':')
axes[1].legend()

opt_p = df.loc[df['Metric'].idxmax(), 'p']
max_metric = df['Metric'].max()

axes[2].plot(df['p'], df['Metric'], 'o-', linewidth=2, label='nsteps = 40 000 000', markersize=6)
axes[2].axvline(x=opt_p, color='blue', linestyle='--', alpha=0.5, label=f'Оптимум: p={int(opt_p)}')
axes[2].plot(opt_p, max_metric, 'o', color='blue', markersize=10, zorder=5)
axes[2].set_xlabel('Число потоков (p)', fontsize=11)
axes[2].set_ylabel('Sp × Ep', fontsize=11)
axes[2].set_title('Комбинированная метрика (оптимум = максимум)', fontsize=12)
axes[2].set_xticks(threads)
axes[2].grid(True, alpha=0.3, linestyle=':')
axes[2].legend()

plt.tight_layout()
plt.savefig('speedup_task2.png', dpi=300, bbox_inches='tight')
plt.show()

with open('task2_stats.txt', 'w', encoding='utf-8') as f:
    f.write("Статистика — Задание 2 (численное интегрирование)\n")
    f.write("="*60 + "\n\n")
    f.write(f"Число точек интегрирования: {df['N'].iloc[0]:,}\n\n")
    f.write(df[['p', 't', 'Sp', 'Ep', 'Metric']].to_string(index=False) + "\n\n")
    f.write(f"Оптимальное количество потоков: {int(opt_p)} (Sp×Ep = {max_metric:.2f})\n")