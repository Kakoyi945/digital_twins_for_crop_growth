import torch
import numpy as np
from torch.utils.data import DataLoader
from Datasets import MaizeDataset, WheatDataset

train_dataset = WheatDataset(type='train')
test_dataset = WheatDataset(type='test')

def calculate_mae(predictions, true_values, epsilon=1e-10):
    """
    计算向量中每个数的平均绝对误差
    :param predictions: 预测值数组
    :param true_values: 真实值数组
    :param epsilon: 用于避免除以零的小常数
    :return: 向量中每个数的平均绝对误差数组
    """
    # 确保两个数组长度相同
    if len(predictions) != len(true_values):
        raise ValueError("预测值和真实值的长度必须相同")
    
    # 计算绝对误差
    absolute_errors = np.abs(predictions - true_values)
    
    # 创建一个与absolute_errors相同形状的epsilon数组
    epsilon_array = np.full_like(absolute_errors, epsilon)
    
    # 使用np.where来选择非零误差或epsilon
    non_zero_errors = np.where(true_values != 0, absolute_errors, epsilon_array)
    
    # 计算每个元素的MAE，只考虑非零误差
    elementwise_mae = non_zero_errors / (np.abs(true_values) + epsilon)
    
    return elementwise_mae

import torch
import torch.nn as nn

class maize_gru_model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.encoder = nn.GRU(7,16,1,batch_first=True)
        self.decoder = nn.GRU(6,16,1,batch_first=True)
        self.out = nn.Sequential(
            nn.ReLU(),
            nn.Linear(16, 6)
        )

    def forward(self,inputs,inputs_):
        h0 = torch.randn(1,inputs.shape[0],16)
        _,h1 = self.encoder(inputs,h0)
        # h1 = torch.randn(2,inputs.shape[0],6)
        outputs,_ =  self.decoder(inputs_,h1)
        outputs = self.out(outputs)
        return outputs

class maize_lstm_model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.encoder = nn.LSTM(7,28,1,batch_first=True)
        self.decoder = nn.LSTM(6,28,1,batch_first=True)
        self.out = nn.Sequential(
            nn.ReLU(),
            nn.Linear(28, 6)
        )

    def forward(self,inputs, inputs_):
        h0 = torch.randn(1,inputs.shape[0],28)
        c0 = torch.randn(1,inputs.shape[0],28)
        _,(h1,c1) = self.encoder(inputs,(h0,c0))
        # outputs = self.out(hidden)
        # h1 = torch.zeros(1,inputs.shape[0],28)
        # c1 = torch.randn(1,inputs.shape[0],28)
        outputs,_ =  self.decoder(inputs_,(h1,c1))
        outputs = self.out(outputs)
        return outputs
    
class wheat_gru_model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.encoder = nn.GRU(7,8,1,batch_first=True)
        self.decoder = nn.GRU(6,8,1,batch_first=True)
        self.out = nn.Sequential(
            nn.ReLU(),
            nn.Linear(8, 6)
        )

    def forward(self,inputs,inputs_):
        h0 = torch.randn(1,inputs.shape[0],8)
        _,h1 = self.encoder(inputs,h0)
        # h1 = torch.randn(2,inputs.shape[0],6)
        outputs,_ =  self.decoder(inputs_,h1)
        outputs = self.out(outputs)
        return outputs

class wheat_lstm_model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.encoder = nn.LSTM(7,7,1,batch_first=True)
        self.decoder = nn.LSTM(6,7,1,batch_first=True)
        self.out = nn.Sequential(
            nn.ReLU(),
            nn.Linear(7, 6)
        )

    def forward(self,inputs, inputs_):
        h0 = torch.randn(1,inputs.shape[0],7)
        c0 = torch.randn(1,inputs.shape[0],7)
        _,(h1,c1) = self.encoder(inputs,(h0,c0))
        outputs,_ =  self.decoder(inputs_,(h1,c1))
        outputs = self.out(outputs)
        return outputs

import math
import tqdm
# # # 初始化 DataLoader
train_loader = DataLoader(train_dataset, batch_size=4, shuffle=False)
model = wheat_lstm_model()
optimizer = torch.optim.Adam(model.parameters(),lr=0.001)
MSE_Measure = nn.MSELoss()
MAE_Measure = nn.L1Loss(size_average=True)
# # 使用 DataLoader
best_loss = math.inf
tolearate  = 0
for epoch in range(200): 
    model.train()
    total_train_loss = 0
    for batch_data in tqdm.tqdm(train_loader):
        optimizer.zero_grad()
        inputs,targets = batch_data
        outputs = model(inputs, targets[:, :6, :])
        # print(outputs.size())
        loss = MSE_Measure(outputs[:, -1, :],targets[:, -1, :])
        loss.backward()
        optimizer.step()
        total_train_loss+=loss.detach().cpu().numpy()
    total_train_loss = total_train_loss/len(train_loader)
    print(total_train_loss)
    if total_train_loss<best_loss:
        best_loss = total_train_loss
        torch.save(model.state_dict(),'wheat_lstm_model.pth')
    else:
        tolearate +=1
        if tolearate==15:
            break
import config as c
import numpy as np
target_min = np.array(c.wheat_target_mins)
target_max = np.array(c.wheat_target_maxs)

model = wheat_lstm_model()
model.load_state_dict(torch.load('wheat_lstm_model.pth'))

test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)
model.eval()
total_test_loss = 0

dvs_targets = []
dvs_outputs = []
wlv_targets = []
wlv_outputs = []
wst_targets = []
wst_outputs = []
wso_targets = []
wso_outputs = []
tagp_targets = []
tagp_outputs = []
lai_targets = []
lai_outputs = []


for batch_data in tqdm.tqdm(test_loader):
       
    inputs,targets = batch_data
    outputs = model(inputs, targets[:, :6, :])
    print(outputs.size())
    targets = targets.detach().cpu().numpy()[0]
    outputs = outputs.detach().cpu().numpy()[0]
    targets = targets*(target_max-target_min)+target_min
    outputs = outputs*(target_max-target_min)+target_min
    # print(targets.shape,outputs.shape)
    dvs_targets.append(targets[-1][0])
    dvs_outputs.append(outputs[-1][0])
    wlv_targets.append(targets[-1][1])
    wlv_outputs.append(outputs[-1][1])
    wst_targets.append(targets[-1][2])
    wst_outputs.append(outputs[-1][2])
    wso_targets.append(targets[-1][3])
    wso_outputs.append(outputs[-1][3])
    tagp_targets.append(targets[-1][4])
    tagp_outputs.append(outputs[-1][4])
    lai_targets.append(targets[-1][5])
    lai_outputs.append(outputs[-1][5])

    # current_mae = np.mean(np.array(calculate_mae(outputs, targets)), axis=0)

    # total_test_loss+=current_mae

from sklearn.metrics import mean_squared_error

# total_test_loss = total_test_loss/len(test_loader)
dvs_outputs = np.array(dvs_outputs)
dvs_targets = np.array(dvs_targets)
dvs_error = np.mean(np.abs(dvs_outputs-dvs_targets))
print('dvs mae:', dvs_error)
dvs_mse = mean_squared_error(dvs_targets, dvs_outputs)
print('dvs mse:', dvs_mse)

wlv_outputs = np.array(wlv_outputs)
wlv_targets = np.array(wlv_targets)
wlv_error = np.mean(np.abs(wlv_outputs-wlv_targets))
print('wlv mae:', wlv_error)
wlv_mse = mean_squared_error(wlv_targets, wlv_outputs)
print('wlv mse:', wlv_mse)

wst_outputs = np.array(wst_outputs)
wst_targets = np.array(wst_targets)
wst_error = np.mean(np.abs(wst_outputs-wst_targets))
print('wst mae:', wst_error)
wst_mse = mean_squared_error(wst_targets, wst_outputs)
print('wst mse:', wst_mse)

wso_outputs = np.array(wso_outputs)
wso_targets = np.array(wso_targets)
wso_error = np.mean(np.abs(wso_outputs-wso_targets))
print('wso mae:', wso_error)
wso_mse = mean_squared_error(wso_targets, wso_outputs)
print('wso mse:', wso_mse)

tagp_outputs = np.array(tagp_outputs)
tagp_targets = np.array(tagp_targets)
tagp_error = np.mean(np.abs(tagp_outputs-tagp_targets))
print('tagp mae:', tagp_error)
tagp_mse = mean_squared_error(tagp_targets, tagp_outputs)
print('tagp mse:', tagp_mse)

lai_outputs = np.array(lai_outputs)
lai_targets = np.array(lai_targets)
lai_error = np.mean(np.abs(lai_outputs-lai_targets))
print('lai mae:', lai_error)
print(total_test_loss)
lai_mse = mean_squared_error(lai_targets, lai_outputs)
print('lai mse:', lai_mse)

n = len(dvs_outputs)
x = list(range(1, n+1))
# 可视化
import matplotlib.pyplot as plt
plt.plot(x, wlv_outputs, color='blue')
plt.plot(x, wlv_targets, color='red')
plt.xlabel('time')
plt.ylabel('values')
plt.show() 
