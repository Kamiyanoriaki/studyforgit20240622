import datetime

day_1 = datetime.datetime.now()

dict_day_of_week = {
    "Mon": "月曜日",
    "Tue": "火曜日",
    "Wed": "水曜日",
    "Thu": "木曜日",
    "Fri": "金曜日",
    "Sat": "土曜日",
    "Sun": "日曜日",
}
day_of_week_list_en = []
day_of_week_iist_jp = []

i = 0
for i in range(7):
    day_2 = day_1 + datetime.timedelta(days=i)
    day_of_week = day_2.strftime("%a")

    day_of_week_list_en.append(day_of_week)
    day_of_week_iist_jp.append(dict_day_of_week[day_of_week])

print(day_of_week_list_en)
print(day_of_week_iist_jp)
