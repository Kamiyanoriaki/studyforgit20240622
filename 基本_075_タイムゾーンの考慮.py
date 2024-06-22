import time
import datetime
from datetime import datetime as dt
from datetime import timezone
from zoneinfo import ZoneInfo

today_naive = datetime.datetime.now()

print("naive な datetime オブジェクト")
print(today_naive, "    naive_ローカル時間")

print("")
print("aware な datetime オブジェクト")
today_UTC_aware_1 = datetime.datetime.now(timezone.utc)
print(today_UTC_aware_1, "aware_UTC時間")

today_UTC_aware_2 = today_naive.astimezone(ZoneInfo("UTC"))
print(today_UTC_aware_2, "aware_UTC時間")

today_tokyo = today_UTC_aware_2.astimezone(ZoneInfo("Asia/Tokyo"))
print(today_tokyo, "aware_JST時間")

today_tokyo_2 = today_UTC_aware_2 + datetime.timedelta(hours=9)
print(today_tokyo_2, "aware_JST時間")

print("")
print("aware な datetime オブジェクト ISO表記")
iso_time_utc = today_UTC_aware_2.isoformat()
print(iso_time_utc, "iso_time_utc")

iso_time_tokyo = today_tokyo.isoformat()
print(iso_time_tokyo, "iso_time_tokyo")

print("")
print("Excelに貼り付ける為の書式")
excel_time = dt.strftime(today_naive, ("%y/%m/%d" "  " "%H:%M:%S"))
print(excel_time, "        Excelに張り付けるための書式")
