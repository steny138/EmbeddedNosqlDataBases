# -*- coding: utf-8 -*-
import logging
import logging.config

import json
from unqlite import UnQLite
from grs import Stock, TWSENo
import datetime
logging.config.fileConfig("../logging.conf", disable_existing_loggers=False,
                          defaults={'logfilename': datetime.datetime.now().strftime("%Y%m%d")})
logger = logging.getLogger("unqlite")

class Unqlite(object):
    def fetchdata(self):
        try:
            # stock = Stock('2618', 12)
            # twse_no = TWSENo()
            fetch_stocks = self.__read_prepare_stocks()
            process_count = 0

            for st in fetch_stocks["stocks"]:
                dbname = 'stock_records_' + st["stockno"]
                records = self.db.collection(dbname)
                if not records.exists():
                    logger.info("records collection created.")
                    records.create()
                    
                logger.info("stockno: %s" % st["stockno"])
                
                datas = Stock(st["stockno"], mons=24).raw
                for data in datas:
                    stock_data = StockData(st["stockno"], data)
                    if not self.__hasRaw(dbname, "date", stock_data.date):
                        records.store(stock_data.__dict__)
                        process_count = process_count + 1

            if records.exists():
                logger.info("success %d " % process_count)
            else:
                print("fail to fetch data")
        except Exception, e:
            logger.warning(e)
        finally:
            pass

    def readdata(self):
        fetch_stocks = self.__read_prepare_stocks()
        for st in fetch_stocks["stocks"]:
            dbname = 'stock_records_' + st["stockno"]
            records = self.db.collection(dbname)
            rawData = Stock(st["stockno"])
            # logger.info("%s : " % st["stockno"])
            # print(rawData.MAV(10)[1])
            if records.exists():
                # print(rawData.MAV(10))
                logger.info("%s : " % st["stockno"])
                for record in records.all():
                    logger.info(record)
            else:
                print("fail to read data")

    def __read_prepare_stocks(self):
        with open("choose_stocks.json") as data_file:
            data = json.load(data_file)
        return data

    def __hasRaw(self, dbname, key, value):
        """ 是否已存在同樣資料

            :param dbname: 集合的名稱
            :param key: 須比對的key的名稱
            :param value: 須比對的值
            :rtype: boolean
        """
        return len(self.db.collection(dbname).filter(lambda obj: obj[key] == value)) > 0

    def __init__(self, db):
        super(Unqlite, self).__init__()
        self.db = db  # UnQLite('./db/ubqlite.db')
        if self.db is None:
            raise Exception("there is no unqlite database to load.")

class StockData(object):
    """docstring for StockData"""

    def __init__(self, no, data):
        super(StockData, self).__init__()
        """ fetch data row 
            0. 日期
            1. 成交股數
            2. 成交金額
            3. 開盤價
            4. 最高價（續）
            5. 最低價
            6. 收盤價
            7. 漲跌價差
            8. 成交筆數
        """
        self.no = no
        self.date = data[0]
        self.deal_num = data[1]
        self.deal_price = data[2]
        self.open_price = data[3]
        self.high_price = data[4]
        self.low_price = data[5] 
        self.last_price = data[6]
        self.deviation = data[7]
        self.deal_count = data[8]

if __name__ == "__main__":
    Unqlite(UnQLite('./db/unqlite.db')).fetchdata()
