from torch.utils.data import Dataset
import config
import pandas as pd
import numpy as np

class MaizeDataset(Dataset):
    def __init__(self, type='train') -> None:
        super().__init__()
        data = pd.read_csv(config.summer_maize_file)
        data['date'] = pd.to_datetime(data['year'].astype(str) + '-' + data['month'].astype(str) + '-' + data['day'].astype(str), format='%Y-%m-%d')
        self.input_mins = np.array(config.maize_input_mins)
        self.input_maxs = np.array(config.maize_input_maxs)
        self.target_mins = np.array(config.maize_target_mins)
        self.target_maxs = np.array(config.maize_target_maxs)
        if type == 'train':
            self.data = data[(data['date'] >= config.maize_train_span[0][0]) &
                             (data['date'] <= config.maize_train_span[-1][1])]
            self.data = self.data.drop('date', axis=1)
        elif type == 'test':
            self.data = data[(data['date'] >= config.maize_test_span[0][0]) &
                             (data['date'] <= config.maize_test_span[-1][1])]
            self.data = self.data.drop('date', axis=1)

    def __len__(self):
        return len(self.data)-6
    
    def __getitem__(self, index):
        data_slice = self.data.iloc[index: index+7]
        input_slice = data_slice[config.input_columns]
        target_slice = data_slice[config.target_columns]
        # 转换为Numpy数组
        input_array = input_slice.to_numpy()
        target_array = target_slice.to_numpy()
        # 进行最大最小值归一化
        input_array = (input_array - self.input_mins)/(self.input_maxs - self.input_mins)
        target_array = (target_array - self.target_mins)/(self.target_maxs - self.target_mins)
        input_array = input_array.astype(np.float32)
        target_array = target_array.astype(np.float32)

        return input_array, target_array


class WheatDataset(Dataset):
    def __init__(self, type='train') -> None:
        super().__init__()
        data = pd.read_csv(config.winter_wheat_file)
        data['date'] = pd.to_datetime(data['year'].astype(str) + '-' + data['month'].astype(str) + '-' + data['day'].astype(str), format='%Y-%m-%d')
        self.input_mins = np.array(config.wheat_input_mins)
        self.input_maxs = np.array(config.wheat_input_maxs)
        self.target_mins = np.array(config.wheat_target_mins)
        self.target_maxs = np.array(config.wheat_target_maxs)
        if type == 'train':
            self.data = data[(data['date'] >= config.wheat_train_span[0][0]) &
                             (data['date'] <= config.wheat_train_span[-1][1])]
            self.data = self.data.drop('date', axis=1)
        elif type == 'test':
            self.data = data[(data['date'] >= config.wheat_test_span[0][0]) &
                             (data['date'] <= config.wheat_test_span[-1][1])]
            self.data = self.data.drop('date', axis=1)
        
    def __len__(self):
        return len(self.data)-6
    
    def __getitem__(self, index):
        data_slice = self.data.iloc[index: index+7]
        input_slice = data_slice[config.input_columns]
        target_slice = data_slice[config.target_columns]
        # 转换为Numpy数组
        input_array = input_slice.to_numpy()
        target_array = target_slice.to_numpy()
        # 进行最大最小值归一化
        input_array = (input_array - self.input_mins)/(self.input_maxs - self.input_mins)
        target_array = (target_array - self.target_mins)/(self.target_maxs - self.target_mins)
        input_array = input_array.astype(np.float32)
        target_array = target_array.astype(np.float32)
        return input_array, target_array
    


