# -*- coding: utf-8 -*-
import logging
import logging.config

import json
from unqlite import UnQLite
from grs import Stock,TWSENo
import datetime
logging.config.fileConfig("../logging.conf", disable_existing_loggers=False, defaults={'logfilename': datetime.datetime.now().strftime("%Y%m%d")})
logger = logging.getLogger("unqlite")


class Unqlite(object):
    def test(self):
        try:
            db = UnQLite('./db/stocks.db')
            # stock = Stock('2618', 12)
            twse_no = TWSENo()
            users = db.collection('users')
            if not users.exists():
                print("user collection created.")
                users.create()
                users.store(twse_no.all_stock)
            tw_stock = users.fetch(0)
            stock_num = "0050"
            if users.exists() : 
                if stock_num in tw_stock:
                    print(tw_stock[stock_num])
                else:
                    print("no %s" % stock_num)
                
            else:
                print("false")
        except Exception, e:
            logger.warning(e)
        finally:
            pass
    def __init__(self):
        super(Unqlite, self).__init__()

if __name__ == "__main__":
    Unqlite().test()