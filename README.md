# digital_twins_for_crop_growth
It's a project that simulates a crop(exactly wheat and maize) in Shandong Qihe, which is also my undergraduate project

# 文件树
```shell
│  .gitattributes
│  digital_twin_for_crop_growth.unitypackage # Unity package文件，导入后就可以直接使用本项目
│  README.md
│  
├─algorithm
│  ├─DeepLearning
│  │  │  config.py
│  │  │  Datasets.py
│  │  │  demo.py # 模型+训练+测试
│  │  │  demo2.py
│  │  │  gru_model.pth
│  │  │  lstm_model.pth
│  │  │  maize.csv
│  │  │  maize_gru_model.pth
│  │  │  maize_lstm_model.pth
│  │  │  maize_lstm_model2.pth
│  │  │  wheat.csv
│  │  │  wheat_gru_model.pth
│  │  │  wheat_lstm_model.pth
│  │  │  
│  │  └─__pycache__
│  │          
│  ├─MachineLearning
│  │  │  2019-2023_summer_maize.csv
│  │  │  2019-2023_winter_wheat.csv
│  │  │  config.py
│  │  │  daily_accumulated_ssr.csv
│  │  │  daily_temp.csv
│  │  │  daily_tp.csv
│  │  │  daily_wind_speed_and_direct.csv
│  │  │  maize.csv
│  │  │  maize_ml.ipynb # 玉米机器学习算法
│  │  │  model_test.py
│  │  │  utils.py
│  │  │  wheat.csv
│  │  │  wheat_ml.ipynb # 小麦机器学习算法
│  │  │  
│  │  ├─maize # 训练出来的模型
│  │  │  │  maize_pca.joblib
│  │  │  │  maize_scaler.joblib
│  │  │  │  
│  │  │  ├─maize_dvs
│  │  │  │      dvs_mlr.joblib
│  │  │  │      dvs_rfr.joblib
│  │  │  │      dvs_svr.joblib
│  │  │  │      
│  │  │  ├─maize_lai
│  │  │  │      lai_mlr.joblib
│  │  │  │      lai_rfr.joblib
│  │  │  │      lai_svr.joblib
│  │  │  │      
│  │  │  ├─maize_tagp
│  │  │  │      tagp_mlr.joblib
│  │  │  │      tagp_rfr.joblib
│  │  │  │      tagp_svr.joblib
│  │  │  │      
│  │  │  ├─maize_wlv
│  │  │  │      wlv_mlr.joblib
│  │  │  │      wlv_rfr.joblib
│  │  │  │      wlv_svr.joblib
│  │  │  │      
│  │  │  ├─maize_wso
│  │  │  │      wso_mlr.joblib
│  │  │  │      wso_rfr.joblib
│  │  │  │      wso_svr.joblib
│  │  │  │      
│  │  │  └─maize_wst
│  │  │          wst_mlr.joblib
│  │  │          wst_rfr.joblib
│  │  │          wst_svr.joblib
│  │  │          
│  │  └─wheat # 训练出来的模型
│  │      │  wheat_pca.joblib
│  │      │  wheat_scaler.joblib
│  │      │  
│  │      ├─wheat_dvs
│  │      │      dvs_mlr.joblib
│  │      │      dvs_rfr.joblib
│  │      │      dvs_svr.joblib
│  │      │      
│  │      ├─wheat_lai
│  │      │      lai_mlr.joblib
│  │      │      lai_rfr.joblib
│  │      │      lai_svr.joblib
│  │      │      
│  │      ├─wheat_tagp
│  │      │      tagp_mlr.joblib
│  │      │      tagp_rfr.joblib
│  │      │      tagp_svr.joblib
│  │      │      
│  │      ├─wheat_wlv
│  │      │      wlv_mlr.joblib
│  │      │      wlv_rfr.joblib
│  │      │      wlv_svr.joblib
│  │      │      
│  │      ├─wheat_wso
│  │      │      wso_mlr.joblib
│  │      │      wso_rfr.joblib
│  │      │      wso_svr.joblib
│  │      │      
│  │      └─wheat_wst
│  │              wst_mlr.joblib
│  │              wst_rfr.joblib
│  │              wst_svr.joblib
│  │              
│  └─__pycache__
│          
├─digital_twin_for_crop_growth_server # 项目后端文件，使用django实现
│  │  db.sqlite3
│  │  db_admin_info.cnf
│  │  manage.py
│  │  requirements.txt
│  │  
│  ├─data_server
│  │  │  admin.py
│  │  │  apps.py
│  │  │  models.py
│  │  │  serializers.py
│  │  │  tests.py
│  │  │  urls.py
│  │  │  views.py
│  │  │  __init__.py
│  │  │  
│  │  ├─migrations
│  │  │  │  0001_initial.py
│  │  │  │  0002_crop_crop_type_crop_dvs_crop_lai_crop_tagp_crop_wlv_and_more.py
│  │  │  │  0003_rename_weatehr_type_name_weather_weather_type_name.py
│  │  │  │  0004_rename_u_wind_speed_weather_wind_direction_and_more.py
│  │  │  │  0005_weather_surface_solar_radiation.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │  └─__pycache__
│  │  │          
│  │  ├─templates
│  │  │  └─data_server
│  │  │          index.html
│  │  │          
│  │  └─__pycache__
│  │          
│  ├─digital_twin_for_crop_growth_server
│  │  │  asgi.py
│  │  │  settings.py
│  │  │  urls.py
│  │  │  wsgi.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          
│  └─predicter
│      │  admin.py
│      │  apps.py
│      │  models.py
│      │  tests.py
│      │  urls.py
│      │  views.py
│      │  __init__.py
│      │  
│      ├─migrations
│      │      __init__.py
│      │      
│      ├─utils
│      │  │  algorithm.py
│      │  │  config.py
│      │  │  data_preset.py
│      │  │  dl_models.py
│      │  │  __init__.py
│      │  │  
│      │  ├─models
│      │  │  ├─maize
│      │  │  │  │  maize_gru_model.pth
│      │  │  │  │  maize_lstm_model.pth
│      │  │  │  │  maize_pca.joblib
│      │  │  │  │  maize_scaler.joblib
│      │  │  │  │  
│      │  │  │  ├─dvs
│      │  │  │  │      dvs_mlr.joblib
│      │  │  │  │      dvs_rfr.joblib
│      │  │  │  │      dvs_svr.joblib
│      │  │  │  │      
│      │  │  │  ├─lai
│      │  │  │  │      lai_mlr.joblib
│      │  │  │  │      lai_rfr.joblib
│      │  │  │  │      lai_svr.joblib
│      │  │  │  │      
│      │  │  │  ├─tagp
│      │  │  │  │      tagp_mlr.joblib
│      │  │  │  │      tagp_rfr.joblib
│      │  │  │  │      tagp_svr.joblib
│      │  │  │  │      
│      │  │  │  ├─wlv
│      │  │  │  │      wlv_mlr.joblib
│      │  │  │  │      wlv_rfr.joblib
│      │  │  │  │      wlv_svr.joblib
│      │  │  │  │      
│      │  │  │  ├─wso
│      │  │  │  │      wso_mlr.joblib
│      │  │  │  │      wso_rfr.joblib
│      │  │  │  │      wso_svr.joblib
│      │  │  │  │      
│      │  │  │  └─wst
│      │  │  │          wst_mlr.joblib
│      │  │  │          wst_rfr.joblib
│      │  │  │          wst_svr.joblib
│      │  │  │          
│      │  │  └─wheat
│      │  │      │  wheat_gru_model.pth
│      │  │      │  wheat_lstm_model.pth
│      │  │      │  wheat_pca.joblib
│      │  │      │  wheat_scaler.joblib
│      │  │      │  
│      │  │      ├─dvs
│      │  │      │      dvs_mlr.joblib
│      │  │      │      dvs_rfr.joblib
│      │  │      │      dvs_svr.joblib
│      │  │      │      
│      │  │      ├─lai
│      │  │      │      lai_mlr.joblib
│      │  │      │      lai_rfr.joblib
│      │  │      │      lai_svr.joblib
│      │  │      │      
│      │  │      ├─tagp
│      │  │      │      tagp_mlr.joblib
│      │  │      │      tagp_rfr.joblib
│      │  │      │      tagp_svr.joblib
│      │  │      │      
│      │  │      ├─wlv
│      │  │      │      wlv_mlr.joblib
│      │  │      │      wlv_rfr.joblib
│      │  │      │      wlv_svr.joblib
│      │  │      │      
│      │  │      ├─wso
│      │  │      │      wso_mlr.joblib
│      │  │      │      wso_rfr.joblib
│      │  │      │      wso_svr.joblib
│      │  │      │      
│      │  │      ├─wst
│      │  │      │      wst_mlr.joblib
│      │  │      │      wst_rfr.joblib
│      │  │      │      wst_svr.joblib
│      │  │      │      
│      │  │      └─__pycache__
│      │  │              
│      │  └─__pycache__
│      │          
│      └─__pycache__
│              
└─study_resources # 学习资料
    ├─arcgis # arcgis，需要学习arcgis的工具家族（arcmap,arcscene,cityengine）的使用
    │  │  gis_knowledge_and_arcgis_usage.md
    │  │  
    │  └─assets
    │          
    ├─era5 # 气象数据下载
    │  │  era5_study.md
    │  │  
    │  └─assets
    │
    └─unity_resources_and_skill
        │  unity_ide_usage_tips.md
        ├─assets 
        └─resources # 里面有一些Unity学习资源
            │  推荐一些不错的Unity游戏开发素材资源 - 知乎.html
            │  
            └─推荐一些不错的Unity游戏开发素材资源 - 知乎_files
                    
```