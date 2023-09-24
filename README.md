# qq&wb2phone

随便写的QQ和微博id查绑定手机号的小工具，数据来自于公开的api接口，不保证准确性，仅作为参考。

数据来源：https://zy.xywlapi.cc

需要安装的库：

```
pip install requests
```

参数说明：
```
-h/--help：查看帮助信息
-q/-qq：查询qq号绑定的手机号
-w/--weibo：查询weiboid对应的手机号
```

使用示例：

```
python ./qq&wb2phone.py -q [qq号] -w [微博id]
或
python ./qq&wb2phone.py --qq [qq号] --weibo [微博id]
```

示例：

![image-20230731192519419](./test.png) 

免责声明：本工具仅供研究学习使用，不得用于非法用途，使用者因本工具导致的任何违法问题与开发者本人无关。