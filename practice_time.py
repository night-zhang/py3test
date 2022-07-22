import time

# 时间戳
ticks = time.time()
print("当前时间戳为:", ticks)

# 时间元组
localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

# =======================================
from datetime import *

now = datetime.now()

print(datetime.now())
print(datetime.now().date())
print(datetime.now().time())
print(datetime.now().weekday())  # [0, 6], 0表示星期一
print(datetime.now().isoweekday())  # [1, 7], 1表示星期一

# 用 striptime 方法将字符串转换为 datetime 数据类型
print(datetime.strptime('2018-02-21 Kobe 01#:02:20', '%Y-%m-%d Kobe %H#:%M:%S'))
print(datetime.strptime('2018-02-21', '%Y-%m-%d'))
print(type(datetime.strptime('2018-02-21', '%Y-%m-%d')))
# 用 strftime 方法将 datetime 数据类型转换为字符串
print(datetime.now().time().strftime('%a %m %d %H:%M:%S'))
# 用 timedelta 方法加减日期时间
print(datetime.now() + timedelta(days=1))
print(datetime.now() + timedelta(days=-1))
print(datetime.now() + timedelta(days=1) - datetime.now())
print(now < datetime.now() + timedelta(days=1))

# =======================================
from get_holiday_cn.client import getHoliday

client = getHoliday()
# 获取今日数据
print(client.assemble_holiday_data())
# 指定日期获取数据
print(client.assemble_holiday_data(today='2022-04-23'))
print(client.assemble_holiday_data(today='2022-04-24'))
print(client.assemble_holiday_data(today='2022-04-29'))
print(client.assemble_holiday_data(today='2022-04-30'))
print(client.assemble_holiday_data(today='2022-05-01'))
print(client.assemble_holiday_data(today='2022-05-07'))
print(client.assemble_holiday_data(today='2022-05-08'))


def get_monday_friday(day=datetime.now()):
    weekday = day.isoweekday()
    monday = day - timedelta(days=weekday - 1)
    friday = day + timedelta(days=5 - weekday)
    return "{}_{}".format(monday.date(), friday.date())

print(get_monday_friday())