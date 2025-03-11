
```
创建虚拟环境
py -m venv .venv
python3 -m venv webvenv
激活虚拟环境
windows
.\venv\Scripts\activate
linex
source webvenv/bin/activate
退出虚拟环境
deactivate
安装需要的包
pip install requests
```



生成依赖项
pip install pipreqs
`pipreqs . --force --encoding utf-8`

```
gunicorn -w 4 -b 0.0.0.0:5000 app:app
gunicorn -w 4 -b 0.0.0.0:8080 --access-logfile access.log --error-logfile error.log app:app -D
持久化运行
nohup python -m gunicorn -w 5 -b 0.0.0.0:6000 -t 120 main:app > app.log 2>&1 &

```

```
查看所有安装的包
pip freeze
pip freeze > requirements.txt
pip list 
pip list -r requirements.txt

```