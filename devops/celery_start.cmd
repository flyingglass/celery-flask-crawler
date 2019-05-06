REM WIN10测试环境使用

REM 启动celery worker
celery worker -A celery_worker.celery -l INFO --pool=solo

REM 启动celery beat调度器
celery beat -A celery_worker.celery -l INFO

REM 启动celery flower监控页面
celery flower -A celery_worker.celery --address=0.0.0.0 --port=5555