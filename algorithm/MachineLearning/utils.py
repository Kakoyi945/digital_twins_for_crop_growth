import pandas as pd
import config

def cal_min_max(crop_type: int):
    """
    function: 获取气象数据和农作物数据的最大最小值
    @param: crop_type: 作物类型，其中1为小麦，2为玉米，3为水稻
    @return: 两个二维列表，分别为气象数据和农作物的最大最小值，每个列表的形式为：[[tp, ssr, temp, wind_speed, wind_direct], [dvs, wlv, wst, wso, tagp, lai]]
    """
    tp = pd.read_csv(config.tp_file)
    ssr = pd.read_csv(config.ssr_file)
    temp = pd.read_csv(config.temperature_file)
    wind = pd.read_csv(config.wind_file)
    crop = pd.DataFrame()
    train_span = []

    # corp_type中，1为小麦，2为玉米，3为水稻
    if crop_type == 1:
        crop = pd.read_csv(config.winter_wheat_file)
        train_span = config.wheat_train_span
    elif crop_type == 2:
        crop = pd.read_csv(config.summer_maize_file)
        train_span = config.maize_train_span
    
    tp_train = pd.DataFrame(columns=tp.columns)
    ssr_train = pd.DataFrame(columns=ssr.columns)
    temp_train = pd.DataFrame(columns=temp.columns)
    wind_train = pd.DataFrame(columns=wind.columns)
    crop_train = pd.DataFrame(columns=crop.columns)
    for span in train_span:
        filtered_tp = tp.loc[(tp['time_val'] >= span[0]) & (tp['time_val'] <= span[1])]
        tp_train = pd.concat([tp_train, filtered_tp], ignore_index=True)
        filtered_ssr = ssr.loc[(ssr['time_val'] >= span[0]) & (ssr['time_val'] <= span[1])] 
        ssr_train = pd.concat([ssr_train, filtered_ssr], ignore_index=True)
        filtered_temp = temp.loc[(temp['time_val'] >= span[0]) & (temp['time_val'] <= span[1])]
        temp_train = pd.concat([temp_train, filtered_temp], ignore_index=True)
        filtered_wind = wind.loc[(wind['time_val'] >= span[0]) & (wind['time_val'] <= span[1])]
        wind_train = pd.concat([wind_train, filtered_wind], ignore_index=True)
        filtered_crop = crop.loc[(crop['time_val'] >= span[0]) & (crop['time_val'] <= span[1])]
        crop_train = pd.concat([crop_train, filtered_crop], ignore_index=True)

    max_weather_values = []
    min_weather_values = []

    max_weather_values.append(tp_train['tp'].max(axis=0))
    max_weather_values.append(ssr_train['ssr'].max(axis=0))
    max_weather_values.append(temp_train['temperature_k'].max(axis=0))
    max_weather_values.append(wind_train['wind_speed'].max(axis=0))
    max_weather_values.append(wind_train['wind_direction'].max(axis=0))

    min_weather_values.append(tp_train['tp'].min(axis=0))
    min_weather_values.append(ssr_train['ssr'].min(axis=0))
    min_weather_values.append(temp_train['temperature_k'].min(axis=0))
    min_weather_values.append(wind_train['wind_speed'].min(axis=0))
    min_weather_values.append(wind_train['wind_direction'].min(axis=0))

    selected_columns = ['dvs','wlv','wst','wso','tagp','lai']
    max_crop_values = list(crop_train[selected_columns].max(axis=0))
    min_crop_values = list(crop_train[selected_columns].min(axis=0))

    return [max_weather_values, max_crop_values], [min_weather_values, min_crop_values]

res = cal_min_max(2)
print(res)
    