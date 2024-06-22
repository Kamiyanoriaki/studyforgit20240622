import datetime
from datetime import datetime as dt

# YYYMMDD を YYY/MM/DD に変換
print("YYYMMDD を YYY/MM/DD に変換")
input_date_1 = "20230611"  # YYYMMDD
additional_time_1 = dt.strptime(input_date_1, "%Y%m%d")
additional_time_2 = additional_time_1.strftime("%Y/%m/%d")

print(input_date_1)
print(additional_time_1)
print(additional_time_2)

# YYY/MM/DD を YYYMMDD に変換
print("YYY/MM/DD を YYYMMDD に変換")
input_date_2 = "2023/06/11"  # YYY/MM/DD
additional_time_3 = dt.strptime(input_date_2, "%Y/%m/%d")
additional_time_4 = additional_time_3.strftime("%Y%m%d")

print(input_date_2)
print(additional_time_3)
print(additional_time_4)
