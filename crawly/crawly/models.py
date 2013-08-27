from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class tb_domain(Base):
    __tablename__ = 'tb_domains'
    id = Column(Integer, primary_key=True)
    url_domain = Column(String)
    status =





