# 坐标转换模块
此模块用于百度坐标系(bd-09)、火星坐标系(国测局坐标系、gcj02)、WGS84坐标系的相互转换，并提供中文地址到坐标的转换功能，仅使用Python标准模块，无其他依赖。中文地址到坐标转换使用高德地图API，需要[申请](http://lbs.amap.com/)API KEY。
# 使用说明
```
    lng = 128.543
    lat = 37.065
    result1 = gcj02_to_bd09(lng, lat)#火星坐标系->百度坐标系
    result2 = bd09_to_gcj02(lng, lat)#百度坐标系->火星坐标系
    result3 = wgs84_to_gcj02(lng, lat)#WGS84坐标系->火星坐标系
    result4 = gcj02_to_wgs84(lng, lat)#火星坐标系->WGS84坐标系
    result5 = bd09_to_wgs84(lng, lat)#百度坐标系->WGS84坐标系
    result6 = wgs84_to_bd09(lng, lat)#WGS84坐标系->百度坐标系

	#中文地址到火星坐标系,需要高德地图API Key
    g = Geocoding('API_KEY')  # 这里填写你的高德Api_Key
    result7 = g.geocode('北京市朝阳区朝阳公园')
    print result1, result2, result3, result4, result5, result6, result7
```
