webcrawler
==========

A commandline webcrawler created with scrapy. It will index websites and collect meta information about these.

Prerequisites
==========
The tool is written in __python__ and supports 2.7 syntax, so first install python2.7 if needed.

The following packages are installed with __pip__, so if pip isn't installed, do
this.

+ scrapy - http://scrapy.org/ ( scrape tool )
+ Flask-SQLAlchemy - http://pythonhosted.org/Flask-SQLAlchemy/ (database tool - convenient abstraction of SQLAlchemy)
+ Alembic - http://alembic.readthedocs.org/en/latest/ (database migration tool - only needed if you want to alter the database and keep revision)

This tool wants to log it's work in the database so get a database-server on your
machine. The supported databases are listed [here] (http://docs.sqlalchemy.org/en/rel_0_8/core/engines.html#database-urls)
+ Mysql / Postgres / Orocle / SQLite

Usage
=========
Get urls first, the first spider will start with webdesigner.startpagina.nl and crawls recursively until the end of the internet.
###startpagina crawler
scrapy crawl startpagina-crawly


### wordpress crawler
scrapy crawl wp-crawly



