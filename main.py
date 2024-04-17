import os
from datetime import date
import calendar

year = date.today().year
month = date.today().month
_, last_day = calendar.monthrange(year, month)

for i in range(1, last_day+1):
    if not os.path.isdir(f'{i}.{month}'):
        os.mkdir(f'{i}.{month}')
