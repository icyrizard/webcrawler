from models import db, Domain, SearchDomain, Template, WPTheme
from sqlalchemy.exc import IntegrityError

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class CrawlyPipeline(object):
    """"Store information about websites in wordpress table"""
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if 'WPPipeline' not in getattr(spider, "pipelines"):
            return item

        if item['template']:
            dmain = db.session.query(Domain).filter_by(url_domain=item['url_domain']).first()
            if dmain:
                site_template = Template(domain=dmain, template=item['template'])
                db.session.add(site_template)
                if item['theme_name']:
                    site_theme = WPTheme(domain=dmain, theme=item['theme_name'])
                    db.session.add(site_theme)
                db.session.commit()
        return item

class URLPipeline(object):
    """store information about source urls to be processed by other spiders"""
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if 'URLPipeline' not in getattr(spider, "pipelines"):
            return item
        try:
            dmain = Domain(url_domain=item['url'],
                        search_domain=item['source'],
                        status_code=item['status'])
            db.session.add(dmain)
            db.session.commit()
        except IntegrityError:
            print 'fail'
            db.session.rollback()
        return item
