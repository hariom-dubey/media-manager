from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import LONGTEXT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    password = Column(String(1000), nullable=False)
    username = Column(String(100))
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    mobile = Column(String(10))
    role_id = Column(Integer, nullable=False)
    is_master = Column(Integer, nullable=False, server_default=text("'0'"))
    is_active = Column(Integer, nullable=False)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    deleted_on = Column(TIMESTAMP)


class MediaGithubWebhookLog(Base):
    __tablename__ = 'media_github_webhook_logs'

    id = Column(Integer, primary_key=True)
    code = Column(String(36), index=True)
    event = Column(String(36), index=True)
    response = Column(LONGTEXT, nullable=False)
    is_deployed = Column(TINYINT, nullable=False, server_default=text("'0'"))
    deploy_messages = Column(LONGTEXT)
    created_on = Column(TIMESTAMP, nullable=False, index=True, server_default=text("CURRENT_TIMESTAMP"))
    updated_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
