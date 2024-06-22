import datetime

from datetime import datetime as dt
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

# YYYMMDD を datetime型に変換
input_date_1 = "20230611"  # YYYMMDD
additional_time_1 = dt.strptime(input_date_1, "%Y%m%d")

print(input_date_1)
print(additional_time_1)

# 今月の月初日を求める
first_day_of_the_month = additional_time_1.replace(day=1)

# 来月の月初日を求める
first_day_of_the_next_month = first_day_of_the_month + relativedelta(month=1)

# 月の月松井津を求める（来月の月初日の一日前）
last_day_of_the_month = first_day_of_the_next_month + relativedelta(days=-1)

print(dt.strftime(additional_time_1, "%y%m%d"))
print(dt.strftime(first_day_of_the_month, "%y%m%d"))
print(dt.strftime(first_day_of_the_next_month, "%y%m%d"))
print(dt.strftime(last_day_of_the_month, "%y%m%d"))
