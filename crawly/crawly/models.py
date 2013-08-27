from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Domain(Base):
    __tablename__ = 'tb_domain'
    id = Column(Integer, primary_key=True, unique=True)
    url_domain = Column(String(512), unique=True, nullable=False)
    status = Column(Boolean(), nullable=True)
    #status = Column(Integer(), nullable=True)
    remark = Column(String(128), nullable=True)
    date_created = Column(DateTime(), nullable=False)

    def __repr__(self):
        return """<tb_domain> url_domain: %s status: %s remark: %s date_created: %s """ % (self.url_domain, self.status, self.remark, self.date_created)
    # changed what?, just delete and add a new one?
    #date_changed = Column(DateTime(), nullable=False)

class SearchDomain(Base):
    __tablename__ = 'tb_searchdomain'
    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer(), ForeignKey("tb_domain.id"), nullable=False)
    domain = relationship("Domain")

    # dont know the type
    search_domain = Column(String(128), nullable=False)

    def __repr__(self):
        return """<tb_searchdomain> search_domain: %s"""% (self.search_domain)

class Template(Base):
    __tablename__ = "tb_template"
    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer(), ForeignKey("tb_domain.id"), nullable=False)
    domain = relationship("Domain")
    template = Column(String(64), nullable=False)
    version = Column(String(64), nullable=True)

    def __repr__(self):
        return \
        """<tb_searchdomain> template: %s, version: %s""" \
        % (self.template, self.version)

class WPTheme(Base):
    __tablename__ = "tb_wptheme"
    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer(), ForeignKey("tb_domain.id"), nullable=False)
    domain = relationship("Domain")
    date_searched = Column(DateTime(), nullable=False)
    theme = Column(String(64))

    def __repr__(self):
        return \
        """<tb_searchdomain> template: %s, version: %s"""\
        %  (self.date_searched, self.theme)










