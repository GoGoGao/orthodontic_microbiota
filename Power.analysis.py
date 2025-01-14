

from statsmodels.stats.power import TTestIndPower

# 创建功效分析对象
analysis = TTestIndPower()

# 参数设定
alpha = 0.05       # 显著性水平
nobs1 = 30         # 健康组样本量
nobs2 = 31         # 不健康组样本量
ratio = nobs2 / nobs1  # 样本比例

# 假设效应大小 (Cohen's d)
effect_size = 0.8  # 如果有实际数据，可以用 Cohen's d 计算效应大小

# 计算功效 (power)
power = analysis.power(effect_size=effect_size, nobs1=nobs1, alpha=alpha, ratio=ratio)
print(f"统计功效 (Power): {power:.4f}")

# 或者，计算在目标功效下需要的效应大小
required_effect_size = analysis.solve_power(alpha=alpha, power=0.8, nobs1=nobs1, ratio=ratio)
print(f"达到80%功效所需效应大小 (Cohen's d): {required_effect_size:.4f}")

