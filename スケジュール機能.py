import schedule
import time
import sys
import datetime

x = 0
now_1 = datetime.datetime.now()
print(x, now_1, "実行中です。")


def job():
    # xをグローバル宣言
    global x
    x = x + 1
    now_1 = datetime.datetime.now()
    print(x, now_1, "実行中です。")
    match x == 5:
        case True:
            schedule.clear()
            sys.exit()


schedule.every(3).seconds.do(job)
# schedule.every().minute.at(":23").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
