# SimpleMark

这是我和[Gotcha](https://github.com/heyGotcha)一起做的一个简单的文本数据标注网站，使用django1.11。
python版本是3.6（别的版本没试过，不过应该也能用）

## 使用方法（生产环境）

### 一、安装Django及相关依赖
根目录下存放有requirements.txt
使用如下命令即可安装（建议在python虚拟环境中安装）
```
pip install -r requirements.txt
```
然后将项目放在/root/中即可（如果不是需要修改uwsgi.ini文件）

### 二、配置静态文件
修改根目录下SimpleMark目录中的settings.py

将`DEBUG = True`改为：`DEBUG = False`

修改静态文件目录配置，将
```python
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# STATIC_ROOT = os.path.join(BASE_DIR, "static")
```
改成（交换注释）
```python
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )

STATIC_ROOT = os.path.join(BASE_DIR, "static")
```
然后运行collectstatic命令
```
python managy.py collectstatic
```

### 三、添加数据
运行import.py，这个脚本会将根目录下results.txt中的数据逐行注入
```
python import.py
```

### 四、部署上线
详见http://www.jianshu.com/p/75fa0f111a6d

uwsgi --ini uwsgi.ini --daemonize /home/ubuntu/uwsgi.log

