# 每日降水总量
tp_file = 'daily_tp.csv'
# 每日辐射总量
ssr_file = 'daily_accumulated_ssr.csv'
# 每日平均气温
temperature_file = 'daily_temp.csv'
# 每日风速与方向
wind_file = 'daily_wind_speed_and_direct.csv'

# 夏玉米数据
summer_maize_file = '2019-2023_summer_maize.csv'
# 冬小麦数据
winter_wheat_file = '2019-2023_winter_wheat.csv'

# 该日期之后的天数
forward_days = 16
# 该日期之前的天数
backward_days = 0
# 总天数为"1+forward_days+backward_days"

# 数据集划分，每个数组有两个元素，第一个元素为出苗日期，第二个元素为完熟日期
maize_train_span = [['2019-06-14', '2019-09-14'], ['2020-06-11','2020-09-17'], ['2021-06-14', '2021-09-16'], ['2022-06-14', '2022-09-17']]
maize_test_span = [['2023-06-14', '2023-09-10']]
wheat_train_span = [['2019-10-26', '2020-06-12'], ['2020-10-26', '2021-06-13'], ['2021-11-04', '2022-06-16']]
wheat_test_span = [['2022-11-08', '2023-06-16']]