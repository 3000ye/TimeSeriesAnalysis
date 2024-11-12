from statsmodels.graphics.tsaplots import plot_acf

plt.figure(figsize=(8, 4))
ax = plt.gca()  # 获取当前的轴对象
plot_acf(data["vwrtn"], ax=ax, lags=30)
ax.set_ylim(-0.25, 0.25)
ax.set_xlabel('Lag', fontsize=16)  # 设置横轴标签
plt.title('ACF of Value Weighted Return')
plt.show()