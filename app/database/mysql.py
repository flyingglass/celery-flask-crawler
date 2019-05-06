from datetime import datetime

from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import Column, DateTime


class TimestampModel(Model):
    """
    created_at: 记录生成时间戳
    updated_at: 记录更新时间戳
    """
    created_at = Column(DateTime, default=datetime.now, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")


db = SQLAlchemy(model_class=TimestampModel)
