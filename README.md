# pyautoreload
一个可以动态加载重载的模块，可以是对象或者是模块的字符串形式.

TO DO List:

1.  加入目录监控

2.  加入inotify被动扫描

3.  加入信号模式

###安装:

pypi安装
```
pip install pyautoreload
```
源码安装
```
git clone https://github.com/rfyiamcool/pyautoreload.git
cd pyautoreload
python setup.py install
```


###使用方法:

* 重新加载指定模块

    pyautoreload.reload_module(m)

* 加入模块

    pyautoreload.import_str('a.b.c.d')
    
    路径: /a/b/c
    
    函数: d

* 删除模块

    delete_str(m)

* 重新加载所有模块

    reload_all()

* 重新加载模块,支持类及函数路径模式

    reload_str()

