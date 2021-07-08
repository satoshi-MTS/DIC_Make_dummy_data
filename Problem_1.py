# モジュールのインポート
import numpy as np

# 平均値及び共分散の設定
mean = (-3, 0)
cov = np.array([[1.0, 0.8], [0.8, 1.0]])

# seedを固定し乱数を作成
np.random.seed(0)
data = np.random.multivariate_normal(mean, cov, size=500)

# 値の確認
print(data.shape)
print(np.mean(data, axis=0))
print(np.cov(data, rowvar=False))
