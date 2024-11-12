from statsmodels.stats.diagnostic import acorr_ljungbox


# 执行 Ljung-Box 白噪声检验
lb_test_12 = acorr_ljungbox(data["dec10"], lags=[12], return_df=True)
print(lb_test_12)

lb_test_24 = acorr_ljungbox(data["dec10"], lags=[24], return_df=True)
print(lb_test_24)