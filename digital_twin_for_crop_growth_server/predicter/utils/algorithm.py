from .data_preset import change_data_to_ml_data, change_data_to_dl_data
from joblib import load
from . import config
import pandas as pd
import numpy as np
import os
import torch
from .dl_models import *

def ml_predict(data, modelName, cropType):
    model_path = 'predicter/utils/models/'
    pca_path = None
    pca_columns = None
    scaler_path = None
    res = []
    if cropType ==  1:
        model_path = model_path + 'wheat/'
        pca_path = model_path + 'wheat_pca.joblib'
        pca_columns = ['A1', 'A2', 'A3', 'A4', 'A5']
        scaler_path = model_path + 'wheat_scaler.joblib'
    elif cropType == 2:
        model_path = model_path + 'maize/'
        pca_path = model_path + 'maize_pca.joblib'
        pca_columns = ['A1', 'A2', 'A3', 'A4']
        scaler_path = model_path + 'maize_scaler.joblib'
    df = change_data_to_ml_data(data)
    # print(df)
    # 对数据进行归一化
    scaler_model = load(os.path.abspath(scaler_path))
    df_scaled = pd.DataFrame(scaler_model.transform(df), columns=config.ml_columns)
    # 构造ml的输入矩阵
    rows1 = df_scaled[:len(df_scaled)-6].reset_index(drop=True)
    rows2 = df_scaled[1:len(df_scaled)-5].reset_index(drop=True)
    rows3 = df_scaled[2:len(df_scaled)-4].reset_index(drop=True)
    rows4 = df_scaled[3:len(df_scaled)-3].reset_index(drop=True)
    rows5 = df_scaled[4:len(df_scaled)-2].reset_index(drop=True)
    rows6 = df_scaled[5:len(df_scaled)-1].reset_index(drop=True)
    rows7 = df_scaled[6:].reset_index(drop=True)
    # 将rows7的其他target删去
    rows7 = rows7.drop(['dvs', 'wlv', 'wst', 'wso', 'tagp', 'lai'], axis=1)
    # 进行拼接
    df_input = pd.concat([rows1, rows2, rows3, rows4, rows5, rows6, rows7], axis=1, ignore_index=True)
    print(df_input)

    # 使用pca
    pca_loaded = load(os.path.abspath(pca_path))

    df_pca = pca_loaded.transform(df_input)

    df_pca = pd.DataFrame(df_pca, columns=pca_columns) 

    print(df_pca)

    if modelName == 'mlr':
        dvs_model = load(os.path.abspath(model_path + 'dvs/dvs_mlr.joblib'))
        lai_model = load(os.path.abspath(model_path + 'lai/lai_mlr.joblib'))
        tagp_model = load(os.path.abspath(model_path + 'tagp/tagp_mlr.joblib'))
        wlv_model = load(os.path.abspath(model_path + 'wlv/wlv_mlr.joblib'))
        wst_model = load(os.path.abspath(model_path + 'wst/wst_mlr.joblib'))
        wso_model = load(os.path.abspath(model_path + 'wso/wso_mlr.joblib'))
        dvs_prediction = dvs_model.predict(df_pca)[0]
        lai_prediction = lai_model.predict(df_pca)[0]
        tagp_prediction = tagp_model.predict(df_pca)[0]
        wlv_prediction = wlv_model.predict(df_pca)[0]
        wst_prediction = wst_model.predict(df_pca)[0]
        wso_prediction = wso_model.predict(df_pca)[0]
        res.append(dvs_prediction)
        res.append(wlv_prediction)
        res.append(wst_prediction)
        res.append(wso_prediction)
        res.append(tagp_prediction)
        res.append(lai_prediction)
    elif modelName == 'svr':
        dvs_model = load(model_path + 'dvs/dvs_svr.joblib')
        lai_model = load(model_path + 'lai/lai_svr.joblib')
        tagp_model = load(model_path + 'tagp/tagp_svr.joblib')
        wlv_model = load(model_path + 'wlv/wlv_svr.joblib')
        wst_model = load(model_path + 'wst/wst_svr.joblib')
        wso_model = load(model_path + 'wso/wso_svr.joblib')
        dvs_prediction = dvs_model.predict(df_pca)[0]
        lai_prediction = lai_model.predict(df_pca)[0]
        tagp_prediction = tagp_model.predict(df_pca)[0]
        wlv_prediction = wlv_model.predict(df_pca)[0]
        wst_prediction = wst_model.predict(df_pca)[0]
        wso_prediction = wso_model.predict(df_pca)[0]
        res.append(dvs_prediction)
        res.append(wlv_prediction)
        res.append(wst_prediction)
        res.append(wso_prediction)
        res.append(tagp_prediction)
        res.append(lai_prediction)
    elif modelName == 'rfr':
        dvs_model = load(model_path + 'dvs/dvs_rfr.joblib')
        lai_model = load(model_path + 'lai/lai_rfr.joblib')
        tagp_model = load(model_path + 'tagp/tagp_rfr.joblib')
        wlv_model = load(model_path + 'wlv/wlv_rfr.joblib')
        wst_model = load(model_path + 'wst/wst_rfr.joblib')
        wso_model = load(model_path + 'wso/wso_rfr.joblib')
        dvs_prediction = dvs_model.predict(df_input)[0]
        lai_prediction = lai_model.predict(df_input)[0]
        tagp_prediction = tagp_model.predict(df_input)[0]
        wlv_prediction = wlv_model.predict(df_input)[0]
        wst_prediction = wst_model.predict(df_input)[0]
        wso_prediction = wso_model.predict(df_input)[0]
        res.append(dvs_prediction)
        res.append(wlv_prediction)
        res.append(wst_prediction)
        res.append(wso_prediction)
        res.append(tagp_prediction)
        res.append(lai_prediction)
    res_df = pd.DataFrame([res], columns=config.res_columns)

    return res_df 

def dl_predict(data, modelName, cropType):    
    model_path = 'predicter/utils/models/'
    model = None
    input_mins = None
    input_maxs = None
    target_mins = None
    target_maxs = None  
    if cropType == 1:
        input_mins = np.array(config.wheat_input_mins)
        input_maxs = np.array(config.wheat_input_maxs)
        target_mins = np.array(config.wheat_target_mins)
        target_maxs = np.array(config.wheat_target_maxs)
        if modelName == 'gru':
            model = wheat_gru_model()
            model.load_state_dict(torch.load(model_path+'wheat/wheat_gru_model.pth'))
            model.eval() 
        elif modelName == 'lstm':
            model = wheat_lstm_model()
            model.load_state_dict(torch.load(model_path+'wheat/wheat_lstm_model.pth'))
    elif cropType == 2:
        input_mins = np.array(config.maize_input_mins)
        input_maxs = np.array(config.maize_input_maxs)
        target_mins = np.array(config.maize_target_mins)
        target_maxs = np.array(config.maize_target_maxs)
        if modelName == 'gru':
            model = maize_gru_model()
            model.load_state_dict(torch.load(model_path+'maize/maize_gru_model.pth'))
        elif modelName == 'lstm':
            model = maize_lstm_model()
            model.load_state_dict(torch.load(model_path+'maize/maize_lstm_model.pth'))
    input, input_ = change_data_to_dl_data(data)
    # 最大最小值归一化
    input = np.array(input)
    input_ = np.array(input_)
    input = (input - input_mins)/(input_maxs-input_mins)
    input_ = (input_ - target_mins)/(target_maxs - target_mins)
    print('input and input_')
    print(input)
    print(input_)
    # 转换为张量，并增加batch维度
    input = input.reshape(1, input.shape[0], input.shape[1]).astype(np.float32)
    input = torch.from_numpy(input)
    input_ = input_.reshape(1, input_.shape[0], input_.shape[1]).astype(np.float32)
    input_ = torch.from_numpy(input_)
    # 预测
    res = model(input, input_)
    res = res.detach().cpu().numpy()[0]
    # 进行反归一化
    res = res*(target_maxs-target_mins)+target_mins
    res_df = pd.DataFrame(res, columns=config.res_columns)

    return res_df