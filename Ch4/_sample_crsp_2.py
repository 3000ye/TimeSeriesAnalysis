plt.figure(figsize=(8, 4))
plt.plot(data["ewrtn"], label='Equal Weighted Return', color="green")
plt.title('CRSP Equal Weighted Index Monthly Return')
plt.ylabel('Equal Weighted')
plt.legend()
plt.show()