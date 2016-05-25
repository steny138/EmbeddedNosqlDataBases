# -*- coding: utf-8 -*-

from practice_unqlite import Unqlite
from unqlite import UnQLite

def main():
    print('start...')
    try:
       uqlite = Unqlite(UnQLite('./db/ubqlite.db'))
       uqlite.fetchdata()
    except Exception, e:
        print(e)
    finally:
        pass

    print('end...')

if __name__ == '__main__':
    main()
else : 
    print(__name__)
