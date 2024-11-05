from statsmodels.graphics.tsaplots import plot_acf

plt.figure(figsize=(8, 4))
plot_acf(data["dec10"])
plt.title('ACF of CRSP Lower 10% Monthly Returns')
plt.show()