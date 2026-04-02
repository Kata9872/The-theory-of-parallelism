import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_v1 = pd.read_csv('result_1.csv')
df_v2 = pd.read_csv('result_2.csv')

df_v1['Ep'] = df_v1['Sp'] / df_v1['p']
df_v2['Ep'] = df_v2['Sp'] / df_v2['p']
df_v1['Metric'] = df_v1['Sp'] * df_v1['Ep']
df_v2['Metric'] = df_v2['Sp'] * df_v2['Ep']

threads = [1, 2, 4, 7, 8, 16, 20, 40]

fig, axes = plt.subplots(1, 4, figsize=(22, 5))

axes[0].plot(df_v1['p'], df_v1['t'], 'o-', linewidth=2, label='Вариант 1 (отдельные секции)', markersize=6)
axes[0].plot(df_v2['p'], df_v2['t'], 's-', linewidth=2, label='Вариант 2 (одна секция)', markersize=6)
axes[0].set_xlabel('Число потоков (p)', fontsize=11)
axes[0].set_ylabel('Время (сек)', fontsize=11)
axes[0].set_title('Время выполнения от числа потоков', fontsize=12)
axes[0].set_xticks(threads)
axes[0].grid(True, alpha=0.3, linestyle=':')
axes[0].legend()

axes[1].plot(df_v1['p'], df_v1['Sp'], 'o-', linewidth=2, label='Вариант 1', markersize=6)
axes[1].plot(df_v2['p'], df_v2['Sp'], 's-', linewidth=2, label='Вариант 2', markersize=6)
axes[1].plot(threads, threads, '--', color='gray', linewidth=2, label='Линейное (идеал)')
axes[1].set_xlabel('Число потоков (p)', fontsize=11)
axes[1].set_ylabel('Ускорение (Sp)', fontsize=11)
axes[1].set_title('Ускорение от числа потоков', fontsize=12)
axes[1].set_xticks(threads)
axes[1].grid(True, alpha=0.3, linestyle=':')
axes[1].legend()

axes[2].plot(df_v1['p'], df_v1['Ep'], 'o-', linewidth=2, label='Вариант 1', markersize=6)
axes[2].plot(df_v2['p'], df_v2['Ep'], 's-', linewidth=2, label='Вариант 2', markersize=6)
axes[2].axhline(y=1.0, color='gray', linestyle='--', linewidth=2, label='Идеал (E=1)')
axes[2].set_xlabel('Число потоков (p)', fontsize=11)
axes[2].set_ylabel('Эффективность (Ep)', fontsize=11)
axes[2].set_title('Эффективность от числа потоков', fontsize=12)
axes[2].set_xticks(threads)
axes[2].grid(True, alpha=0.3, linestyle=':')
axes[2].legend()

opt_p_v1 = df_v1.loc[df_v1['Metric'].idxmax(), 'p']
opt_p_v2 = df_v2.loc[df_v2['Metric'].idxmax(), 'p']
max_v1 = df_v1['Metric'].max()
max_v2 = df_v2['Metric'].max()

axes[3].plot(df_v1['p'], df_v1['Metric'], 'o-', linewidth=2, label='Вариант 1', markersize=6)
axes[3].plot(df_v2['p'], df_v2['Metric'], 's-', linewidth=2, label='Вариант 2', markersize=6)
axes[3].axvline(x=opt_p_v1, color='blue', linestyle='--', alpha=0.5, label=f'Оптимум V1: p={int(opt_p_v1)}')
axes[3].axvline(x=opt_p_v2, color='orange', linestyle='--', alpha=0.5, label=f'Оптимум V2: p={int(opt_p_v2)}')
axes[3].plot(opt_p_v1, max_v1, 'o', color='blue', markersize=8, zorder=5)
axes[3].plot(opt_p_v2, max_v2, 's', color='orange', markersize=8, zorder=5)
axes[3].set_xlabel('Число потоков (p)', fontsize=11)
axes[3].set_ylabel('Sp × Ep', fontsize=11)
axes[3].set_title('Комбинированная метрика (оптимум = максимум)', fontsize=12)
axes[3].set_xticks(threads)
axes[3].grid(True, alpha=0.3, linestyle=':')
axes[3].legend()

plt.tight_layout()
plt.savefig('comparison_task3.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"\n💡 Оптимальное количество потоков:")
print(f"   Вариант 1: p = {int(opt_p_v1)} (Sp×Ep = {max_v1:.2f})")
print(f"   Вариант 2: p = {int(opt_p_v2)} (Sp×Ep = {max_v2:.2f})")

for i, p in enumerate(threads):
    t1 = df_v1.iloc[i]['t']
    t2 = df_v2.iloc[i]['t']
    diff = ((t1 - t2) / t1) * 100
    print(f"p={p:2d}: Вариант 1 = {t1:.4f} сек, Вариант 2 = {t2:.4f} сек, разница = {diff:+.2f}%")

avg_diff = ((df_v1['t'] - df_v2['t']) / df_v1['t']).mean() * 100

with open('task3_stats.txt', 'w', encoding='utf-8') as f:
    f.write("Статистика сравнения — Задание 3\n")
    f.write("="*60 + "\n\n")
    f.write("Вариант 1 (отдельные параллельные секции):\n")
    f.write(df_v1[['p', 't', 'Sp', 'Ep', 'Metric']].to_string(index=False) + "\n\n")
    f.write("Вариант 2 (одна параллельная секция):\n")
    f.write(df_v2[['p', 't', 'Sp', 'Ep', 'Metric']].to_string(index=False) + "\n\n")
    f.write(f"Оптимальное количество потоков:\n")
    f.write(f"  Вариант 1: p = {int(opt_p_v1)} (Sp×Ep = {max_v1:.2f})\n")
    f.write(f"  Вариант 2: p = {int(opt_p_v2)} (Sp×Ep = {max_v2:.2f})\n\n")
    f.write(f"Среднее улучшение Варианта 2: {avg_diff:+.2f}%\n")