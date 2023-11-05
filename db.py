import string
from collections import namedtuple


Data = namedtuple('Data', ['time', 'photo', 'action', 'status', 'font'])

font = '⁰¹²³⁴⁵⁶⁷⁸⁹'

profile = Data(time=False, photo=False, action=False,
               status=False, font=str.maketrans(string.digits, font))
