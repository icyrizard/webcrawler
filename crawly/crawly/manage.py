#!/usr/bin/python
import sys, argparse, logging
from sqlalchemy import func
from models import db, Domain, Template

def syncdb():
    """syncdb with flask"""
    logging.info("start syncing db")
    db.create_all()
    logging.info("done")

def del_endswith(pattern):
    """deletes urls with patterns that ends with the given pattern"""
    all_domains = db.session.query(Domain).filter(Domain.url_domain.like("%" + pattern)).all()
    logging.info("deleting %s", len(all_domains))
    db.session.query(Domain).filter(Domain.url_domain.like("%" + pattern)).delete(synchronize_session='fetch')
    logging.info("deleting done")
    db.session.commit()

def del_startswith(pattern):
    """deletes urls with patterns that stats with the given pattern"""
    all_domains = db.session.query(Domain).filter(Domain.url_domain.like(pattern + "%")).all()
    logging.info("deleting %s", len(all_domains))
    db.session.query(Domain).filter(Domain.url_domain.like(pattern + "%")).delete(synchronize_session='fetch')
    logging.info("deleting done")
    db.session.commit()

def del_with(pattern):
    """deletes urls with patterns that has this pattern"""
    all_domains = db.session.query(Domain).filter(Domain.url_domain.like("%" + pattern + "%")).all()
    logging.info("deleting %s", len(all_domains))
    db.session.query(Domain).filter(Domain.url_domain.like("%" + pattern + "%")).delete(synchronize_session='fetch')
    logging.info("deleting done")
    db.session.commit()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--syncdb", action="store_true")
    parser.add_argument("--del_endswith", nargs="?")
    parser.add_argument("--del_startswith", nargs="?")
    parser.add_argument("--del_with", nargs="?")
    args = parser.parse_args()
    if args.syncdb:
        syncdb()
    elif args.del_startswith:
        del_startswith(args.del_startswith)
    elif args.del_endswith:
        del_endswith(args.del_endswith)
    elif args.del_with:
        del_with(args.del_with)

if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    parse_arguments()




