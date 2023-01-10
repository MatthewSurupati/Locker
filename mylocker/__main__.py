from kink import di
from mylocker.ui.locker_ui import *

if __name__ == '__main__':
    di['db_file'] = r'C:\Users\Matthew\PycharmProjects\SmartLocker\mylocker\repository\Box'
    di['dbinit'] = False
    Tkinterss(LockerService()).create_Base()
    