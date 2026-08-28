import datetime

now=datetime.datetime.now()

# #format #123->5자리 빈공백 0으로 채워서 출력.
# print("{:05d}".format(123))

# #월 을 출력하는데, 1,2,3,...9월 01,02,03../ 10,11,12..
# print(now.month)
# print("{:02d} 월".format(now.month))
# print("{:02d} 분".format(now.minute))
# print("{:02d} 초".format(now.second))
# print("{:02d} 시 {:02d} 분 {:02d} 초".format(now.hour,now.minute,now.second))

# f_date=now.strftime("%Y월%m일%d일 %H시%M분%S초")
# print(f_date)
