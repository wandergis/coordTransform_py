#坐标转换python版本
之前提供了[js版本的坐标转换工具](https://github.com/wandergis/coordTransform)，现在提供一下python版本的给有需要的人,希望能对大家有用
#使用方法
1. 由于代码里面使用了**requests**来请求百度geocode接口，因此需要这个功能的童鞋请务必先安装requests模块，可以借助pip或者easy_install来安装
```
pip install requests
```
or
```
easy_install requests
```
2. 仅仅安装requests模块是不够的，童鞋还需要将代码内的
```
key = 'your key here'  # 这里填写你的百度开放平台的key
```
中的key替换成你自己百度地图开放平台的key，不清楚的童鞋可移步[百度地图开放平台](http://developer.baidu.com/map/index.php?title=首页)去申请一个key

#示例
```
	lng = 128.543
    lat = 37.065
    result1 = gcj02tobd09(lng, lat)
    result2 = bd09togcj02(lng, lat)
    result3 = wgs84togcj02(lng, lat)
    result4 = gcj02towgs84(lng, lat)
    result5 = geocode('北京市朝阳区朝阳公园')
    print result1, result2, result3, result4, result5
```

#sometips
代码最后写了一些示例代码，不需要的同学可以删掉，完全可以作为一个坐标转换模块引用到大家的项目中
