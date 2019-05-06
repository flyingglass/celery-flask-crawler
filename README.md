分布式爬虫基础框架

`本项目主要用于爬虫开发，集成Flask + Celery + Scrapy组件，用于分布式爬虫管理，项目环境python3.7.2，管理套件为pipenv，ide采用pycharm，最终采用gunicorn + supervisor + celery的方式部署`

##### Quick-Start

```bash
# 主要以win/mac作为开发环境
# 1. 安装>=python3.7版本，配置好环境变量
$> python --version
Python 3.7.x
# 2. 安装pipenv包管理器
$> python -m pip install pipenv
# 3. pycharm配置pipenv环境
# 4. 等待pipenv安装包完毕，或者通过命令pipenv sync
# 5. 配置app/config.py中的redis或mysql的url
# 6. 运行main.py启动项目，启动主控程序
# 7. win为例启动celery worker，在pycharm中Terminal输入start启动新的cmd（非必须）
$>celery worker -A celery_worker.celery -l INFO --pool=solo
# 8. win为例启动celery beat，会自动调度task任务，同celery worker输入命令（非必须）
$>celery beat -A celery_worker.celery -l INFO
# 9. 启动任务监控页面，同celery worker输入命令（非必须）
$>celery flower -A celery_worker.celery --address=0.0.0.0 --port=555
```

##### 常见问题

```markdown
1. - FileNotFoundError: [Errno 2] No such file or directory: 'C:\\var\\log\\celery-flask-crawler\\celery-flask-crawler.error.log' 
- 查看app/logging.yml中配置的日志路径，修改路径或者在对应的目录创建好目录
```

##### 编码规范

- [Python 代码规范](https://www.jianshu.com/p/8b6c425b65a6)
- [PEP 8-Python编码规范整理](https://www.jianshu.com/p/e132bea1d2c9)

