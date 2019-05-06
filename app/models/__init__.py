from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

from ..database import db


class User(db.Model):
    """
    MYSQL test_user Table
    """
    __tablename__ = "user"

    id = Column(INTEGER(unsigned=True), primary_key=True)
    username = Column(VARCHAR(255), nullable=False, comment="用户名")
    password = Column(VARCHAR(255), comment="密码")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<TestUser %r>" % self.username
