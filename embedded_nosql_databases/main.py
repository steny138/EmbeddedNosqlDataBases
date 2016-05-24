# -*- coding: utf-8 -*-

from practice_unqlite import Unqlite

def main():
    print('start...')
    try:
       uqlite = Unqlite()
       uqlite.test()
    except Exception, e:
        print(e)
    finally:
        pass

    print('end...')

if __name__ == '__main__':
    main()
else : 
    print(__name__)
