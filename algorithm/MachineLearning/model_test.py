from joblib import load
import pandas as pd
import numpy as np

scaler_loaded = load('maize/maize_scaler.joblib')

train = pd.read_csv('maize.csv', index_col=0)

train = train.rename({'tp':'precipitation'})

print(train)

train_scaled = pd.DataFrame(scaler_loaded.transform(train), columns=train.columns)

# print(train_scaled)

# train_wlv = train_scaled.drop(['dvs', 'wst', 'wso', 'tagp', 'lai'], axis=1)
rows1 = train_scaled[:len(train_scaled)-6].reset_index(drop=True)
rows2 = train_scaled[1:len(train_scaled)-5].reset_index(drop=True)
rows3 = train_scaled[2:len(train_scaled)-4].reset_index(drop=True)
rows4 = train_scaled[3:len(train_scaled)-3].reset_index(drop=True)
rows5 = train_scaled[4:len(train_scaled)-2].reset_index(drop=True)
rows6 = train_scaled[5:len(train_scaled)-1].reset_index(drop=True)
rows7 = train_scaled[6:].reset_index(drop=True)
# 将rows7的其他target删去
rows7 = rows7.drop(['dvs', 'wlv', 'wst', 'wso', 'tagp', 'lai'], axis=1)
# 进行拼接
train_input = pd.concat([rows1, rows2, rows3, rows4, rows5, rows6, rows7], axis=1, ignore_index=True)
# print(train_input)

pca_loaded = load('maize/maize_pca.joblib')

train_pca = pca_loaded.transform(train_input)

train_pca = pd.DataFrame(train_pca, columns=['A1', 'A2', 'A3', 'A4'])
# 打印累计解释方差
# print("Explained variance ratio:", pca_loaded.explained_variance_ratio_)

train_target = train['wlv'][6:].reset_index(drop=True)
print(train_target)

model = load('maize/maize_wlv/wlv_rfr.joblib')

# 预测
predictions = model.predict(train_input)

print(type(predictions[0]))

# 计算R平方
# r_squared = model.score(train_pca, train_target)
# print(f'R-squared: {r_squared}')

# 计算MAE MSE
from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(train_target, predictions)

mse = mean_squared_error(train_target, predictions)

print(f"MAE: {mae}")
print(f"MSE: {mse}")

# 可视化
import matplotlib.pyplot as plt
plt.scatter(train_target, predictions)
plt.xlabel('Actual values')
plt.ylabel('Predicted values')
plt.title('Actual vs. Predicted Values')
plt.show() 


