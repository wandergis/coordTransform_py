# 坐标转换模块

此模块用于百度坐标系(bd-09)、火星坐标系(国测局坐标系、gcj02)、WGS84坐标系的相互转换，并提供中文地址到坐标的转换功能，仅使用Python标准模块，无其他依赖。

中文地址到坐标转换使用高德地图API，需要[申请](http://lbs.amap.com/)API KEY。

需要js版本可以移步[coordtransform](https://github.com/wandergis/coordtransform)

## 使用说明

### 方法说明

```bash
# 方法说明
gcj02_to_bd09(lng, lat) # 火星坐标系->百度坐标系
bd09_to_gcj02(lng, lat) # 百度坐标系->火星坐标系
wgs84_to_gcj02(lng, lat) # WGS84坐标系->火星坐标系
gcj02_to_wgs84(lng, lat) # 火星坐标系->WGS84坐标系
bd09_to_wgs84(lng, lat) # 百度坐标系->WGS84坐标系
wgs84_to_bd09(lng, lat) # WGS84坐标系->百度坐标系

# 中文地址到火星坐标系, 需要高德地图API Key
g = Geocoding('API_KEY')  # 这里填写你的高德Api_Key
g.geocode('北京市朝阳区朝阳公园')
```

### 测试

```bash
# 测试
$ python coordTransform_utils.py
[128.54944656269413, 37.07113427883019] [128.5365893261212, 37.058754503281534] [128.54820547949757, 37.065651049489816] [128.53779452050244, 37.06434895051018] [128.53136876750008, 37.0580926428705] [128.55468192918485, 37.07168344938498] None
```

## 批量转换csv文件(coord_converter.py)

使用方法：

```bash
$ python coord_converter.py -h

Usage: coord_converter.py -i <input> -o <output> -t <type>

where <type> is one of:
    g2b, b2g, w2g, g2w, b2w, w2b

Example: coord_converter.py -i /path/to/input_file.csv -o /path/to/output_file.csv -t b2g
```
