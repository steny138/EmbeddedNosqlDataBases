# -*- coding: utf-8 -*-
import logging
import logging.config
import datetime
import json
import leveldb
from grs import Stock,TWSENo

logging.config.fileConfig("../logging.conf", disable_existing_loggers=False, defaults={'logfilename': datetime.datetime.now().strftime("%Y%m%d")})
logger = logging.getLogger("unqlite")

class Leveldb(object):
    def test(self):
        try:
            db = leveldb.LevelDB('./db/level')
            # db.Put("1", "111")

            print (db.Get("1"))
        except Exception, e:
            logger.warning(e)
        finally:
            pass
        
    def __init__(self):
        super(Leveldb, self).__init__()


if __name__ == "__main__":
    Leveldb().test()