from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from settings import DATABASE_LIST, DATABASE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

def create_URI():
    """Builds and returns a database URI, based on the flask / SQLAlchemy
    format: dialect+driver://username:password@host:port/database
    """
    if DATABASE not in DATABASE_LIST:
        raise KeyError("db name %s not in DATABASE_LIST in settings.py" % \
                DATABASE)

    ## get database parameters
    db = DATABASE_LIST[DATABASE]
    dialect = db["DIALECT"]
    driver =  "+" + db["DRIVER"] if db["DRIVER"] else ""
    user = db["USER"]
    password = db["PASSWORD"]
    host = db["HOST"]
    port = ":" + db["PORT"] if db["PORT"] else ""
    name = db["NAME"]

    return "%s%s://%s:%s@%s%s/%s" % (dialect, driver, user, password,
            host, port, name)

# flask related initiatializations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = create_URI()
#app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app)

# models
class Domain(db.Model):
    __tablename__ = 'tb_domain'
    id = db.Column(Integer, primary_key=True, unique=True)
    url_domain = db.Column(String(512), unique=True, nullable=False, index=True)
    status_code = db.Column(Integer(), nullable=True)
    remark = db.Column(String(128), nullable=True)
    date_created = db.Column(DateTime(), nullable=False, default=datetime.now)
    start_url = db.Column(String(512), nullable=False)
    domain_ext = db.Column(String(12), nullable=True)

    date_changed = db.Column(DateTime(), nullable=True, default=datetime.now)
    def __repr__(self):
        return """<tb_domain> url_domain: %s status: %s remark: %s date_created: %s """ % (self.url_domain, self.status_code, self.remark, self.date_created)
    # changed what?, just delete and add a new one?
    #date_changed = db.Column(DateTime(), nullable=False)

class Template(db.Model):
    __tablename__ = "tb_template"
    id = db.Column(Integer, primary_key=True)
    domain_id = db.Column(Integer(), ForeignKey("tb_domain.id",
        ondelete="cascade"), nullable=False, unique=True)
    domain = relationship("Domain")
    template = db.Column(String(64), nullable=False)
    version = db.Column(String(64), nullable=True)
    theme = db.Column(String(64), nullable=True)
    date_searched = db.Column(DateTime(), nullable=False, default=datetime.now)

    def __repr__(self):
        return \
        """<tb_searchdomain> template: %s, version: %s""" \
        % (self.template, self.version)

#class WPTheme(db.Model):
#    __tablename__ = "tb_wptheme"
#    id = db.Column(Integer, primary_key=True)
#    domain_id = db.Column(Integer(), ForeignKey("tb_domain.id",
#        ondelete="cascade"), nullable=False, unique=True)
#    domain = relationship("Domain")
#    date_searched = db.Column(DateTime(), nullable=False, default=datetime.now())
#
#    def __repr__(self):
#        return \
#        """<tb_searchdomain> template: %s, version: %s"""\
#        %  (self.date_searched, self.theme)

