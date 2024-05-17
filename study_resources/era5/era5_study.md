## 气象学知识
1. single level 和pressure level:
   single level，比如地面气压，降水量，整层水汽积分等，没有层次这一维度，（time,lat,lon）；pressure levels，比如u v q等物理量，有层次这一维度,（time,level,lat,lon）。
   对于u、v变量，pressure level越大，离地表越近

## 数据集下载网站
- [era5常用数据集（一般在这里下载就足够了）](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form)
- [era5 pressure level数据集](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-pressure-levels?tab=overview)

## netCDF
1. netCDF介绍
   [netCDF](https://zhuanlan.zhihu.com/p/600050278)

## 之前查找的一些网站
- [ERA5数据简介及下载和使用](https://renqlsysu.github.io/2021/10/13/ERA5/#:~:text=%E4%B8%8B%E9%9D%A2%E8%BF%99%E4%B8%AA%E7%BD%91%E5%9D%80%E5%8F%AF%E4%BB%A5%E5%B0%86ERA5%E7%9A%84%E9%80%90%E6%9C%88%E6%95%B0%E6%8D%AE%E4%BA%A4%E4%BA%92%E5%BC%8F%E5%8F%AF%E8%A7%86%E5%8C%96%EF%BC%88%E5%A6%82%E4%B8%8B%E5%9B%BE%EF%BC%89%EF%BC%8C%E5%B9%B6%E4%B8%94%E6%8F%90%E4%BE%9B%E4%BA%86%E7%9B%B8%E5%BA%94%E7%9A%84python%E4%BB%A3%E7%A0%81%EF%BC%9A%20https%3A%2F%2Fcds.climate.copernicus.eu%2Fapps%2Fc3s%2Fapp-era5-explorer,ERA5%E7%9A%84%E9%99%8D%E6%B0%B4%E6%95%B0%E6%8D%AE%E6%98%AF%E9%80%90%E5%B0%8F%E6%97%B6%E7%9A%84%EF%BC%8C%E5%A6%82%E6%9E%9C%E8%A6%81%E8%AE%A1%E7%AE%97%E6%97%A5%E7%B4%AF%E7%A7%AF%E9%99%8D%E6%B0%B4%EF%BC%8C%E5%B0%B1%E9%9C%80%E8%A6%81%E5%B0%8624%E5%B0%8F%E6%97%B6%E7%9A%84%E9%99%8D%E6%B0%B4%E6%95%B0%E6%8D%AE%E5%8A%A0%E8%B5%B7%E6%9D%A5%EF%BC%8C%E8%BF%99%E9%87%8C%E6%8F%90%E4%BE%9B%E4%BA%86%E4%BB%A3%E7%A0%81%EF%BC%9A%20https%3A%2F%2Fconfluence.ecmwf.int%2Fdisplay%2FCKB%2FERA5%253A%2BHow%2Bto%2Bcalculate%2Bdaily%2Btotal%2Bprecipitation)
- [ERA5: 如何利用逐小时数据计算日总降水量？](https://cloud.tencent.com/developer/article/1936041)
- [ERA5-Land 逐小时数据_累积值(如辐射数据)处理的注意事项](https://blog.csdn.net/qq_57313910/article/details/128118259)
- [ERA5风场速度提取（某区域某时间段），u/v合成风向计算，python绘图。](https://blog.csdn.net/Mluoo/article/details/130115308)