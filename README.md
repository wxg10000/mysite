# mysite

1.创建项目
```
django-admin startproject mysite
```



2.Django规定，如果要使用模型，必须要创建一个app
```
cd mysite
django-admin startapp app01
```


3.自动创建表结构
```
python3 manage.py migrate #创建表结构
python3 manage.py makemigrations app01 # 让 Django 知道我们在我们的模型有一些变更
python3 manage.py migrate app01 # 创建表结构
```

4.创建超级用户
```
python3 manage.py createsuperuser
```
5.安装captcha
```
pip3 install django-simple-captcha
```


参考资料：https://www.jianshu.com/p/4f84d0e0c8c9    