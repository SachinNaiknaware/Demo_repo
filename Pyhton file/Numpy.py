import numpy as np
from scipy import stats

# data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

# mean = np.mean(data)
# median = np.median(data)
# mode = stats.mode(data)

# print(mean, median, mode)  # 3.666..., 4.0, 5
# from sklearn.linear_model import LinearRegression

# X = [[1], [2], [3], [4]]
# y = [2, 4, 6, 8]

# model = LinearRegression().fit(X, y)
# print(model.coef_, model.intercept_)  # slope=2.0, intercept=0.0
from scipy.stats import f_oneway

group1 = [20, 21, 22]
group2 = [30, 29, 31]
group3 = [40, 39, 41]

print(f_oneway(group1, group2, group3))
